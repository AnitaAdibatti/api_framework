import pytest
from datetime import  datetime
from utils.apis import APIS
import webbrowser
import os


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     report_dir = "reports"
#     now = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
#     config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = r"C:\Users\Anita\PycharmProjects\api_framework\reports"
    now = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    report_path = os.path.join(report_dir, f"report_{now}.html")

    config.option.htmlpath = report_path
    pytest.report_path = report_path

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish():
    report_path = getattr(pytest, 'report_path', None)
    if report_path and os.path.exists(report_path):
        webbrowser.open(f"file://{report_path}")


@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("setting up test case")
    yield
    print("tear down")

@pytest.fixture(scope="session")
def apis():
    return APIS()


