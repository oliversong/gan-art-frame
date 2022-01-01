#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import time

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd5in65f
from PIL import Image,ImageDraw
import traceback

logging.basicConfig(level=logging.DEBUG)

pic = 'test.bmp'

def bitmapitize():
    # TODO: convert a normal image into a X by Y bitmap with 7 colors
    pass

def render_pic(epd):
    # TODO: pass in pic received from hook
    try:
        logging.info("attempting render")
        image = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), pic))
        epd.display(epd.getbuffer(image))

        time.sleep(3)

        logging.info("sleep")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()

def init_display():
    try:
        epd = epd5in65f.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        return epd

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()


def main():
    try:
        logging.info("hi")
        epd = epd5in65f.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        logging.info("read bmp file")
        Himage = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '3.bmp'))
        epd.display(epd.getbuffer(Himage))
        time.sleep(3)

        logging.info("sleep")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
