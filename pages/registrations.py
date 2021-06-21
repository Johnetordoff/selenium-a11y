import settings

from selenium.webdriver.common.by import By
from base.locators import Locator, GroupLocator
from pages.base import OSFBasePage


class MyRegistrationsPage(OSFBasePage):
    url = settings.OSF_HOME + '/registries/my-registrations/'
    identity = Locator(By.CSS_SELECTOR, 'div[data-analytics-scope="Registries"]')

    drafts_tab = Locator(By.XPATH, '//a[text()="Drafts"]')
    no_drafts_message = Locator(By.CSS_SELECTOR, 'p[data-test-draft-list-no-drafts]')
    draft_registration_title = Locator(By.CSS_SELECTOR, 'a[data-analytics-name="view_registration"]')

    submissions_tab = Locator(By.XPATH, '//a[text()="Submitted"]')
    no_submissions_message = Locator(By.CSS_SELECTOR, 'p[data-test-draft-list-no-registrations]')
    public_registration_title = Locator(By.CSS_SELECTOR, 'a[data-test-node-title]')

    create_a_registration_button = GroupLocator(By.XPATH, '//button[text()="Create a registration"]')
