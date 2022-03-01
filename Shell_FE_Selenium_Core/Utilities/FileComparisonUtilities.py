import os
import time

import pandas
import numpy

from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities


class FileComparisonUtilities:
    """File Comparison Utilities contains the methods for file comparison related activities."""
    current_working_directory = os.path.dirname(os.getcwd())
    comparison_data = current_working_directory + "/Shell_FE_Behave_Tests/TestData/FileComparisons/"
    log = LoggingUtilities().logger()

    @staticmethod
    def compare_excel(expected_file_name, actual_file_name):
        """The compare_excel method compares the given two excel files and returns a Boolean values based on the results of comparison.
        The method returns True if the files are equal and returns False if the files are not equal.
        Also, if the files are not equal a new excel file would be created containing the difference at the cell level.
        """
        expected_file = pandas.read_excel(FileComparisonUtilities.comparison_data + expected_file_name)
        actual_file = pandas.read_excel(FileComparisonUtilities.comparison_data + actual_file_name)

        if expected_file.equals(actual_file) is True:
            FileComparisonUtilities.log.info(
                f"The files {expected_file_name} and {actual_file_name} has been compared and found to be equal.")
            return True
        else:
            comparison_values = expected_file.values == actual_file.values
            rows, cols = numpy.where(comparison_values == False)
            for item in zip(rows, cols):
                expected_file.iloc[item[0], item[1]] = '{} --> {}'.format(expected_file.iloc[item[0], item[1]],
                                                                          actual_file.iloc[item[0], item[1]])
            timestamp = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
            difference_excel = f"{FileComparisonUtilities.comparison_data}ExcelDifference{timestamp}.xlsx"
            expected_file.to_excel(difference_excel, index=False, header=True)
            FileComparisonUtilities.log.error(
                f"The compared files {expected_file_name} and {actual_file_name} are not equal and the differences "
                f"are captured in the file {difference_excel}.")
            return False
