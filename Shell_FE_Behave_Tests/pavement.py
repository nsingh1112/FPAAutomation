import json
import platform
import threading
from paver.easy import *


def browserstack_parallel_web_test(task_id):
    if platform.system() == 'Windows':
        sh('SET TASK_ID=%s & behave --no-capture -f allure_behave.formatter:AllureFormatter -o TestResults/AllureJson/' % task_id)
    else:
        sh('export TASK_ID=%s && behave --no-capture -f allure_behave.formatter:AllureFormatter -o '
           'TestResults/AllureJson/' % task_id)


@task
@consume_nargs(0)
def browserstack_parallel_web():
    """Run parallel test using the different configurations provided in Browserstack.json file."""
    with open("browserstack.json") as config_file:
        config = json.load(config_file)
    iterations = len(config['environments'])
    jobs = []
    for i in range(int(iterations)):
        p = threading.Thread(target=browserstack_parallel_web_test, args=(i, ))
        jobs.append(p)
        p.start()

    for th in jobs:
        th.join()

