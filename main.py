#!/usr/bin/env python3

from predict import process_image
from io import BytesIO
import PIL
import streamlit as st

from support import resize, fade, blur


MIND_XY = (620, 374)
MIND_SIZE = 550
FILE_EXT = ['jpeg', 'jpg', 'png', 'tiff']


def main():
    screen = st.image('ui/spin.gif', use_column_width=True)

    ans = st.image('ui/intro.png', use_column_width=True)
    st.image('ui/bot.png', use_column_width=True)

    st.image('ui/sho.png', use_column_width=True)
    file = st.file_uploader(f'', FILE_EXT)
    show_file = st.empty()
    st.image('ui/body.png', use_column_width=True)

    if not file:
        # show_file.info(
        #     f"Upload {', '.join(FILE_EXT)} without frames and logos")
        return

    imgpath = 'ui/quest.png'
    if isinstance(file, BytesIO):
        result = process_image(file, '.')

        value = float(result[1])
        if result[0] == 'Like':
            if value >= 99:
                imgpath = 'ui/like/perfect.png'
            elif value >= 90:
                imgpath = 'ui/like/love.png'
            elif value > 80:
                imgpath = 'ui/like/like.png'
            elif value >= 70:
                imgpath = 'ui/like/good.png'
            elif value >= 60:
                imgpath = 'ui/like/notbad.png'
            elif value >= 50:
                imgpath = 'ui/like/maybe.png'

        elif result[0] == 'Beauty':
            if value >= 90:
                imgpath = 'ui/beauty/giveart.png'
            elif value >= 80:
                imgpath = 'ui/beauty/itjoke.png'
            elif value >= 70:
                imgpath = 'ui/beauty/sosimple.png'
            elif value >= 60:
                imgpath = 'ui/beauty/sure.png'
            elif value >= 50:
                imgpath = 'ui/beauty/maybe.png'

        layer = PIL.Image.open(file).convert('RGBA')

        layer_resize = resize(layer, MIND_SIZE)

        layer_fade = fade(layer_resize)

        layer_blur = blur(layer_fade, 10)
        mind = PIL.Image.open('ui/screen.png')
        mind.paste(layer_blur, (MIND_XY[0] - layer_blur.width // 2,
                                MIND_XY[1] - layer_blur.height // 2))
        screen.image(mind, use_column_width=True)

    ans.image(imgpath, use_column_width=True)


if __name__ == '__main__':
    main()
