from PIL import Image


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
    im.show()
