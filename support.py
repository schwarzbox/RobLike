import PIL


def fade(image, color=(100, 100, 100, 80)):
    alpha = PIL.Image.new('RGBA', image.size, color=color)
    return PIL.Image.alpha_composite(image, alpha)


def resize(layer, limit):
    wid = layer.width
    hei = layer.height
    mod = limit / wid if wid > hei else limit / hei

    return layer.resize((int(mod * wid),
                         int(mod * hei)), PIL.Image.ANTIALIAS)


def blur(image, rad):
    # white frame
    diam = 2 * rad
    back = PIL.Image.new('RGB', (image.size[0] + diam,
                                 image.size[1] + diam), (39, 56, 81))
    back.paste(image, (rad, rad))

    # mask
    mask = PIL.Image.new('L', (image.size[0] + diam,
                               image.size[1] + diam), 255)
    blck = PIL.Image.new('L', (image.size[0] - diam,
                               image.size[1] - diam), 0)
    mask.paste(blck, (diam, diam))
    blur = back.filter(PIL.ImageFilter.GaussianBlur(rad / 2))
    back.paste(blur, mask=mask)
    # crop origin
    crop_back = back.crop((rad, rad, back.size[0] - rad, back.size[1] - rad))
    return crop_back
