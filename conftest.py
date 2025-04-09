import pytest
from datetime import  datetime
from utils.apis import APIS

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("setting up test case")
    yield
    print("tear down")

@pytest.fixture(scope="session")
def apis():
    return APIS()