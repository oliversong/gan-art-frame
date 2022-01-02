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

pics = ['test.bmp', '1.bmp', '2.bmp', '3.bmp', '4.bmp']

def make_bitmap(path):
    # TODO: convert a normal image into a X by Y bitmap with 7 colors
    pass

class AcepController:
    def __init__(self):
        self.epd_instance = None
        self.pic_index = 0
        self.awake = False

    def render_pic(self, bitmap_path=None):
        try:
            logging.info("attempting render")
            if not self.awake:
                logging.info("not awake, waking")
                self.epd_instance.init()

            if not bitmap_path:
                image = Image.open(
                    os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        pics[self.pic_index]
                    )
                )
                self.epd_instance.display(self.epd_instance.getbuffer(image))
                self.pic_index = (self.pic_index + 1) % len(pics)
            else:
                image = Image.open(bitmap_path)
                self.epd_instance.display(self.epd_instance.getbuffer(image))


            time.sleep(3)
            logging.info("sleep")
            self.epd_instance.sleep()
            self.awake = False

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd5in65f.epdconfig.module_exit()
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
