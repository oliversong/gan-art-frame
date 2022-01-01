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

def render_pic():
    try:
        logging.info("attempting render")
        epd.display(epd.getbuffer(pic))

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
        Himage = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), pic))
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
