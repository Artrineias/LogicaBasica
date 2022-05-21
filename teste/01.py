from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

browser = Firefox(executable_path=GeckoDriverManager().install()) 