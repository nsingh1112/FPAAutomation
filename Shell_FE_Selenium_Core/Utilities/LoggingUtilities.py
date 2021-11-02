import inspect
import logging
import os
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class LoggingUtilities:
    logFolder = os.path.dirname(os.getcwd()) + '\\Shell_FE_Behave_Tests\\TestResults\\Logs\\'

    def logger(self, filename="logfile.log"):
        """Creates logger instance with predefined format for logs.

        Returns:
            Logger instance
        """
        logger = logging.getLogger(inspect.stack()[1][3])
        logger.setLevel("DEBUG")
        filehandler = logging.FileHandler(LoggingUtilities.logFolder + filename, "a")
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        return logger