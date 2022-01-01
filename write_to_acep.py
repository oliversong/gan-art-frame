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

class AcepController:
    def __init__(self, epd_instance):
        self.awake = False
        self.epd_instance = epd_instance

    def render_pic(self):
        # TODO: pass in pic received from hook
        try:
            logging.info("attempting render")
            if self.awake == False:
                logging.info("module asleep, waking")
                epd5in65f.epdconfig.module_init()
            image = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), pic))
            self.epd_instance.display(self.epd_instance.getbuffer(image))

            time.sleep(3)

            logging.info("sleep")
            self.epd_instance.sleep()

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd5in65f.epdconfig.module_exit()
            self.awake = False
            exit()

    def init_display(self):
        try:
            self.epd_instance = epd5in65f.EPD()
            logging.info("init and Clear")
            self.epd_instance.init()
            self.epd_instance.Clear()
            self.awake = True
            return self.epd_instance

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd5in65f.epdconfig.module_exit()
            exit()

def main():
    try:
        logging.info("hi")
        epd_instance = epd5in65f.EPD()
        logging.info("init and Clear")
        epd_instance.init()
        epd_instance.Clear()

        logging.info("read bmp file")
        Himage = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '3.bmp'))
        epd_instance.display(epd_instance.getbuffer(Himage))
        time.sleep(3)

        logging.info("sleep")
        epd_instance.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
