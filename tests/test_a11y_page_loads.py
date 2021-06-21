import markers

from components.accessibility import ApplyA11yRules as a11y

from pages.landing import LandingPage
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.project import MyProjectsPage, ProjectPage
from pages.preprints import PreprintDiscoverPage, PreprintSubmitPage
from pages.registries import RegistriesDiscoverPage, RegistrationDraftPage
from pages.registrations import MyRegistrationsPage
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


@markers.dont_run_on_prod
class TestProjectPage:

    def test_accessibility(self, driver, session, default_project, must_be_logged_in):
        """ For the Project page test we are creating a new dummy test project and then deleting it after we have finished
        """
        project_page = ProjectPage(driver, guid=default_project.id)
        project_page.goto()
        assert ProjectPage(driver, verify=True)
        # wait until file widget has fully loaded so that we can ensure that all sections of project page have fully loaded before applying a11y rules
        project_page.file_widget.loading_indicator.here_then_gone()
        a11y.run_axe(driver, session, 'project')


class TestPreprintDiscoverPage:

    def test_accessibility(self, driver, session):
        discover_page = PreprintDiscoverPage(driver)
        discover_page.goto()
        assert PreprintDiscoverPage(driver, verify=True)
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
