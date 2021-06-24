import markers
import settings

from selenium.webdriver.common.keys import Keys

from components.accessibility import ApplyA11yRules as a11y

from pages.landing import LandingPage
from pages.login import LoginPage, ForgotPasswordPage
from pages.dashboard import DashboardPage
from pages.project import MyProjectsPage, ProjectPage, FilesPage
from pages.preprints import PreprintDiscoverPage, PreprintSubmitPage
from pages.registries import RegistriesDiscoverPage, RegistrationDraftPage
from pages.registrations import MyRegistrationsPage
from pages.institutions import InstitutionsLandingPage, InstitutionBrandedPage
from pages.search import SearchPage
from pages import user


class TestOSFHomePage:

    def test_accessibility(self, driver, session):
        landing_page = LandingPage(driver)
        landing_page.goto()
        assert LandingPage(driver, verify=True)
        a11y.run_axe(driver, session, 'home')


class TestCASLoginPage:

    def test_accessibility(self, driver, session):
        login_page = LoginPage(driver)
        login_page.goto()
        assert LoginPage(driver, verify=True)
        a11y.run_axe(driver, session, 'login')


class TestDashboardPage:

    def test_accessibility(self, driver, session, must_be_logged_in):
        dashboard_page = DashboardPage(driver)
        dashboard_page.goto()
        assert DashboardPage(driver, verify=True)
        a11y.run_axe(driver, session, 'dash')


class TestMyProjectsPage:

    def test_accessibility(self, driver, session, must_be_logged_in):
        my_projects_page = MyProjectsPage(driver)
        my_projects_page.goto()
        assert MyProjectsPage(driver, verify=True)
        a11y.run_axe(driver, session, 'myproj')


class TestUserProfilePage:

    def test_accessibility(self, driver, session, must_be_logged_in):
        profile_page = user.UserProfilePage(driver)
        profile_page.goto()
        assert user.UserProfilePage(driver, verify=True)
        a11y.run_axe(driver, session, 'profile')


class TestProjectPage:

    def test_accessibility(self, driver, session, default_project, must_be_logged_in):
        """ For the Project page test we are creating a new dummy test project and then deleting it after we have finished
        unless we are running in Production, then we are using a Preferred Node from the environment settings file.
        """
        project_page = ProjectPage(driver, guid=default_project.id)
        project_page.goto()
        assert ProjectPage(driver, verify=True)
        # wait until file widget has fully loaded so that we can ensure that all sections of project page have fully loaded before applying a11y rules
        project_page.file_widget.loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'project')


class TestProjectFilesPage:

    def test_accessibility(self, driver, session, project_with_file, must_be_logged_in):
        """ For the Project Files page test we are creating a new dummy test project and then deleting it after we have finished
        unless we are running in Production, then we are using a Preferred Node from the environment settings file.
        """
        files_page = FilesPage(driver, guid=project_with_file.id)
        files_page.goto()
        assert FilesPage(driver, verify=True)
        a11y.run_axe(driver, session, 'projfiles')


class TestPreprintDiscoverPage:

    def test_accessibility(self, driver, session):
        discover_page = PreprintDiscoverPage(driver)
        discover_page.goto()
        assert PreprintDiscoverPage(driver, verify=True)
        discover_page.loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'prepdisc')


class TestPreprintSubmitPage:

    def test_accessibility(self, driver, session, must_be_logged_in):
        submit_page = PreprintSubmitPage(driver)
        submit_page.goto()
        assert PreprintSubmitPage(driver, verify=True)
        a11y.run_axe(driver, session, 'prepsub')


class TestRegistriesDiscoverPage:

    def test_accessibility(self, driver, session):
        discover_page = RegistriesDiscoverPage(driver)
        discover_page.goto()
        assert RegistriesDiscoverPage(driver, verify=True)
        discover_page.loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'regdisc')


@markers.dont_run_on_prod
class TestDraftRegistrationMetadataPage:

    def test_accessibility(self, driver, session, must_be_logged_in_as_user_two):
        """ User Two already has an existing draft registration in each test environment so we will just navigate to it
        so we don't have to create a new draft every time we run, which can't be deleted.
        """
        my_registrations_page = MyRegistrationsPage(driver)
        my_registrations_page.goto()
        my_registrations_page.drafts_tab.click()
        my_registrations_page.draft_registration_title.click()
        assert RegistrationDraftPage(driver, verify=True)
        a11y.run_axe(driver, session, 'draftregmeta')


class TestBrandedInstitutionPage:

    def test_accessibility(self, driver, session):
        landing_page = InstitutionsLandingPage(driver)
        landing_page.goto()
        # In Production every institution in the list has some projects so clicking the first in the list is fine.
        # But in the test environments the first institution may not have any projects, so we need to filter for
        # COS to ensure we will have some projects loaded on the branded institution page.
        if not settings.PRODUCTION:
            landing_page.search_bar.send_keys('Center for Open Science')
        landing_page.institution_list[0].click()
        institution_page = InstitutionBrandedPage(driver, verify=True)
        # wait for projects list to load before running axe
        institution_page.projects_loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'brandinstn')


class TestSearchPage:

    def test_accessibility(self, driver, session):
        search_page = SearchPage(driver)
        search_page.goto()
        assert SearchPage(driver, verify=True)
        # Enter wildcard in search input box and press enter so that we have some search results on the page before
        # running accessibility test
        search_page.search_bar.send_keys('*')
        search_page.search_bar.send_keys(Keys.ENTER)
        search_page.loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'search')


class TestForgotPasswordPage:

    def test_accessibility(self, driver, session):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.goto()
        assert ForgotPasswordPage(driver, verify=True)
        a11y.run_axe(driver, session, 'frgtpwrd')
