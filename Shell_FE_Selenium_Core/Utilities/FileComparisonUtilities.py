import os
import time

from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
import numpy as np
from PIL import Image, ImageChops
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import urllib.request
from selenium.webdriver.common.by import By



class FileComparisonUtilities:
    """FileComparisonUtilities class contains reusable methods to compare images and screenshots"""

    current_working_directory = os.path.dirname(os.getcwd())
    test_data = current_working_directory + "/Shell_FE_Behave_Tests/TestData/"
    test_img_data = current_working_directory + "\\Shell_FE_Behave_Tests\\TestData\\images\\"
    test_screenshot_data = current_working_directory + "\\Shell_FE_Behave_Tests\\TestData\\screenshots\\"
    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def download_image(image='', svg = False,):
        """
        The method is used to download the image from the image xpath provided
        :param image: image xpath
        :param svg: True or False
        :return:
        """
        img_ele = SeleniumBase.driver.find_element(*image)
        img_src= img_ele.get_attribute("src")
        FileComparisonUtilities.log.info("Image source {0}".format(img_src))
        if svg == True:
            remote_img = "{}{}".format(FileComparisonUtilities.test_img_data, "remote.svg")
        else:
            remote_img = "{}{}".format(FileComparisonUtilities.test_img_data, "remote_file.png")
        urllib.request.urlretrieve(img_src, remote_img)
        FileComparisonUtilities.log.info("Image {0} downloaded successfully .".format(image))

    @staticmethod
    def compare_image(localimage='', remoteimage = '',svg = False, comp_type= 'image'):
        """
        This method will compare the screenshots or images and return the boolean result
        :param localimage: provide the base image name
        :param remoteimage: in case of image comparison provide image xpath
        :param svg: True or False
        :param comp_type: image or screenshot
        :return: True or False
        """
        FileComparisonUtilities.log.info("Images path {}".format(remoteimage))
        if comp_type == 'image':
            img_data = FileComparisonUtilities.test_img_data
            FileComparisonUtilities.download_image(remoteimage, svg = False,)
            loc_img = "{}{}".format(FileComparisonUtilities.test_img_data, localimage)
        elif comp_type == 'screenshot':
            img_data = FileComparisonUtilities.test_screenshot_data

        if svg == True:
            remote_img = "{}{}".format(img_data, "remote.svg")

            im3 = svg2rlg(r"{}".format(remote_img))
            im4 = svg2rlg(r"{}".format(loc_img))
            renderPM.drawToFile(im3, img_data+"remote_file.png", fmt="PNG")
            renderPM.drawToFile(im4, img_data + "local_file.png", fmt="PNG")

            im1 =  Image.open(r"{}".format(img_data+"remote_file.png"))
            im2 =  Image.open(r"{}".format(img_data + "local_file.png"))
        else:
            im1 =  Image.open(r"{}".format(img_data+"remote_file.png"))
            im2 =  Image.open(r"{}".format(img_data + localimage))

        diff = ImageChops.difference(im2, im1)
        tot_diff = np.mean(np.array(diff))
        os.remove(img_data + '/' + "remote_file.png")
        FileComparisonUtilities.log.info("Images differenece is {0}" .format(tot_diff))
        if tot_diff < 1 :
            FileComparisonUtilities.log.info("Images are same")
            return True
        else:
            FileComparisonUtilities.log.info("Images are NOT same")
            return False

    @staticmethod
    def compare_screenshot(local_image = None):
        """
        This method will download the screenshot of the current page and call the compare method to compare the local
        image with the downloaded image
        :param local_image: provide the base image name
        :return: result True or False
        """
        screenshot_img = "{}{}".format(FileComparisonUtilities.test_screenshot_data, "remote_file.png")
        SeleniumBase.driver.save_screenshot(screenshot_img)
        result = FileComparisonUtilities.compare_image(localimage= local_image, remoteimage='screenshot_img',comp_type='screenshot')
        return result