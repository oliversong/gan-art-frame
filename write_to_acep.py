#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(, 'pic')

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("hi")
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("read bmp file")
    Himage = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.bmp'))
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
