from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse,get_object_or_404,get_list_or_404
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.utils.crypto import get_random_string
from datetime import datetime
from . import models
import json
# Create your views here.
def home(request):
    title = 'Shop'
    object_list = models.Shop.objects.all()
    if object_list:
        return render(request,'shop/shop.html', locals())
    else:
        return render(request,'shop/404.html', locals())


def image(request,key):
    image = get_object_or_404(models.Shop, image__key=key)
    index = image.order
    prev = models.Shop.objects.order_by('-order')
    next = models.Shop.objects.order_by('order')

    if prev.filter(order=index):
        prev = prev.filter(order=index)[0].image.key
    else:
        prev = prev[0].image.key
    if next.filter(order=index):
        next = next.filter(order=index)[0].image.key
    else:
        next = next[0].image.key
    buyable = True
    obj = get_object_or_404(models.Shop, order=index)
    material_dict = {}
    for material in obj.materials.all():
        material_dict[str(material)] = {}
        for size in material.sizes.all():
            material_dict[str(material)][str(size)] = {
                'width' : size.width,
                'height' : size.height,
                'price' : get_object_or_404(
                    models.Combination,
                    material = material,
                    size = size
                ).price
            }
    return render(request,'shop/single_image.html', locals())

def payment(request, key):
    cropper_data = request.POST.get('cropper_data')
    size = json.loads(request.POST.get('size'))
    material = request.POST.get('material')
    shop = get_object_or_404(models.Shop, image__key=key)
    image=shop.image

    time = datetime.utcnow()
    invoice = "UTC--{}--{}".format(time,get_random_string())
    combination = get_object_or_404(
        models.Combination,
        material__material=material,
        size__width=size['width'],
        size__height=size['height']
    )
    models.Payment(invoice= invoice, image= shop, combination= combination, cropper_data= cropper_data).save()
    amount = combination.price
    item_name = image.title

    paypal_dict = {
    "business": "augustin.pro-facilitator@gmail.com",
    "amount": str(amount),
    "currency_code": "EUR",
    "no_shipping": "2",
    "item_name": item_name,
    "invoice": invoice,
    "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
    "return_url": request.build_absolute_uri(reverse('shop_after_payment')),
    "cancel_return": request.build_absolute_uri(reverse('shop_image',kwargs={"key":key})),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "shop/paiement.html", {"form":form,"image":image})

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    payment = models.Payment.objects.get(invoice=ipn_obj.invoice)
    payment.txn_id = ipn_obj.txn_id
    payment.address = address
    payment.email = ipn_obj.payer_email
    payment.save()
    content= ""
    content+="Payment status : {}\n\n".format(ipn_obj.payment_status or " ")

    content+="A payment of {amount} {currency_code} was made to {email} for {name}\n\n".format(
        amount = ipn_obj.mc_gross or " ",
        currency_code = ipn_obj.mc_currency or " ",
        email= ipn_obj.receiver_email or " ",
        name= ipn_obj.item_name or " ",
    )

    content+="Planned price for this item: {}\n".format(payment.combination.price or "")

    content+="Payment invoice : {}\n Payment Payment ID : {}\n\n".format(ipn_obj.invoice,ipn_obj.txn_id or " ")

    address = '{street} {city}, {zip}, {country}'.format(
        street = ipn_obj.address_street or " ",
        city = ipn_obj.address_city or " ",
        zip = ipn_obj.address_zip or " ",
        country = ipn_obj.address_country or " ",
    )
    content+="USER INFORMATION:\n\
        first and last name: {first} {last}\n\
        email-adress: {email}\n\
        Phone number : {phone}\n\
        adress:{street} {city}, {zip}, {country}\n".format(
            email = ipn_obj.payer_email or " ",
            first = ipn_obj.first_name or " ",
            last = ipn_obj.last_name or " ",
            address = address,
            phone = ipn_obj.contact_phone or " ",
    )

    send_mail(
        '[SERVEUR-PAYMENT]-{}'.format(ipn_obj.txn_id or " "),
        content,
        'test@hugoboulenger.com',
        # TODO: change email to hugo's
        ['augustin.pro@gmail.com'],
    )
valid_ipn_received.connect(show_me_the_money)

def after_payment(request):
    return render(request,'shop/return.html')
