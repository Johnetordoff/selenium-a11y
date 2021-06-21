import settings

import pandas as pd
from axe_selenium_python import Axe

class ApplyA11yRules:

    def run_axe(driver, session, page_name, write_files=True, terminal_errors=True):
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        if write_files:
            write_results_files(axe, results, page_name)
        if terminal_errors:
            # Assert no violations are found
            assert len(results['violations']) == 0, axe.report(results['violations'])


def write_results_files(axe, results, page_name):
    # Write results to files (separate files for passes, violations, and incomplete)
    file_name_passes = 'a11y_results/a11y_' + page_name + '_passes_' + settings.DOMAIN + '.json'
    axe.write_results(results['passes'], file_name_passes)
    # now also create .csv file
    pandaObject = pd.read_json(file_name_passes)
    file_name_passes_csv = 'a11y_results/a11y_' + page_name + '_passes_' + settings.DOMAIN + '.csv'
    pandaObject.to_csv(file_name_passes_csv)
    #csv_data = pandaObject.to_csv()
    # try uploading files to an OSF project for storage
    # if settings.TEST:
    #     #results_content = results['passes']
    #     #results_content = '{' + str(results['passes']) + '}'
    #     results_content = results
    #     #upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_passes, contents=results_content)
    #     file_name_all = 'a11y_' + page_name + '_all_' + settings.DOMAIN + '.json'
    #     upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_all, contents=results_content)
    #     results_content = csv_data
    #     upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_passes_csv, contents=results_content)
    file_name_violations = 'a11y_results/a11y_' + page_name + '_violations_' + settings.DOMAIN + '.json'
    axe.write_results(results['violations'], file_name_violations)
    # now also create .csv file
    pandaObject = pd.read_json(file_name_violations)
    file_name_violations_csv = 'a11y_results/a11y_' + page_name + '_violations_' + settings.DOMAIN + '.csv'
    pandaObject.to_csv(file_name_violations_csv)
    #csv_data = pandaObject.to_csv()
    # try uploading files to an OSF project for storage
    # if settings.TEST:
    #     #results_content = (results['violations']
    #     #upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_violations, contents=results_content)
    #     results_content = csv_data
    #     upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_violations_csv, contents=results_content)
    file_name_incomplete = 'a11y_results/a11y_' + page_name + '_incomplete_' + settings.DOMAIN + '.json'
    axe.write_results(results['incomplete'], file_name_incomplete)
    # now also create .csv file
    pandaObject = pd.read_json(file_name_incomplete)
    file_name_incomplete_csv = 'a11y_results/a11y_' + page_name + '_incomplete_' + settings.DOMAIN + '.csv'
    pandaObject.to_csv(file_name_incomplete_csv)
    #csv_data = pandaObject.to_csv()
    # try uploading files to an OSF project for storage
    # if settings.TEST:
    #     #results_content = (results['incomplete']
    #     #upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_incomplete, contents=results_content)
    #     results_content = csv_data
    #     upload_file_to_osf_project(session=session, node_id='vxb8e', name=file_name_incomplete_csv, contents=results_content)

    def upload_file_to_osf_project(session, node_id, name, contents):
        """ Upload a file to a given node/project in OSF storage using the OSF api
        """
        upload_url = '{}/v1/resources/{}/providers/{}/'.format(settings.FILE_DOMAIN, node_id, 'osfstorage')
        session.put(url=upload_url, query_parameters={'kind': 'file', 'name': name}, raw_body=contents)
