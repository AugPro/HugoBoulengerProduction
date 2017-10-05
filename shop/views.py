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
    cropper_data = json.loads(request.POST['cropper_data'])
    size = json.loads(request.POST['size'])
    material = request.POST['material']
    image = get_object_or_404(models.Shop, image__key=key).image

    amount = get_object_or_404(
        models.Combination,
        material__material=material,
        size__width=size['width'],
        size__height=size['height']
    ).price
    item_name = image.title
    time = datetime.utcnow()
    paypal_dict = {
    "business": "augustin.pro-facilitator@gmail.com",
    "amount": str(amount),
    "currency_code": "EUR",
    "item_name": item_name,
    "invoice": "UTC--{}--{}".format(time,get_random_string()),
    "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
    "return_url": request.build_absolute_uri(reverse('main_home')),
    "cancel_return": request.build_absolute_uri(reverse('main_home')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "shop/paiement.html", {"form":form,"image":image})

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    content= ""
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        content+="payment status : {}\n".format(ipn_obj.payment_status)
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != "augustin.pro-facilitator@gmail.com":
            # Not a valid payment
            content += "wrong email : {}\n".format(ipn_obj.receiver_email)

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.

        # Undertake some action depending upon `ipn_obj`.
        # if ipn_obj.custom == "premium_plan":
        #     price = ...
        # else:
        #     price = ...

    #     if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
    #         ...
    # else:
    #     #...
    content+="\n\n{}".format(ipn_obj)
    send_mail(
        '[SERVEUR-CONTACT]',
        content,
        'test@hugoboulenger.com',
        # TODO: change email to hugo's
        ['augustin.junk@gmail.com','boris.ghidaglia@edu.esiee.fr'],
    )

valid_ipn_received.connect(show_me_the_money)
