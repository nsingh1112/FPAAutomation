import sys
from behave import __main__ as runner_with_options
import os

if __name__ == '__main__':
    sys.stdout.flush()

    # Activating virtual environment
    os.system("/venv/Scripts/activate")

    # Provide Feature Files
    featureFileFolder = '../Shell_FE_Behave_Tests/features'

    # Runner Option set to junit
    commonRunnerOptions = ' --no-capture -f allure_behave.formatter:AllureFormatter -o TestResults/AllureJson/  '

    # Complete command
    fullRunnerOptions = commonRunnerOptions + featureFileFolder
    var = runner_with_options.main(fullRunnerOptions)

    # Generating allure report
    os.system("allure generate TestResults/AllureJson --clean -o TestResults/Reports")

    # Opening generated allure reports
    command = "allure open TestResults/Reports"
    os.system(command)
    sys.exit()



