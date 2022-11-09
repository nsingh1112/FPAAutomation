import os.path
import subprocess

if __name__ == '__main__':
    s = subprocess.run('behave --no-capture -f allure_behave.formatter:AllureFormatter -o TestResults/AllureJson/ '
                       , shell=True, check=True)
