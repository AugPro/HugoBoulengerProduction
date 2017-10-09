import os
import shutil
import json
from PIL import Image
from django.http import HttpResponse

def get_hd(data_cropper, photo_data):
    ld = photo_data.ld
    hd = photo_data.hd
    ratio = hd.width/ld.width
    im = Image.open(hd.path)
    im = im.crop((
        data_cropper["x"]*ratio,
        data_cropper["y"]*ratio,
        (data_cropper["x"]+data_cropper["width"])*ratio,
        (data_cropper["y"]+data_cropper["height"])*ratio
    ))
    return im

def get_resp_zip_from_payment_queryset(queryset):
    # NOTE: example from https://stackoverflow.com/questions/67454/serving-dynamically-generated-zip-archives-in-django
    folder = "temporary_cropped"
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    for payment in queryset:
        if payment.txn_id:
            photo_data = payment.image.image
            im = get_hd(json.loads(payment.cropper_data),photo_data)
            im.save(os.path.join(folder,payment.txn_id)+'.jpg',format='jpeg')
    zipped = shutil.make_archive(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cropped'),"zip",folder)
    shutil.rmtree(folder)

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(open(zipped,'rb').read(),content_type = "application/zip")
    # ..and correct content-disposition
    os.remove(zipped)
    resp['Content-Disposition'] = 'attachment; filename=cropped.zip'
    return resp
