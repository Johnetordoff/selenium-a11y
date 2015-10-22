#!/usr/bin/env python
# encoding: utf-8

import os

from modularodm import Q
from modularodm.exceptions import ModularOdmException

from website import settings
from website.app import init_app
from website.conferences.model import Conference
from datetime import datetime

def main():
    init_app(set_backends=True, routes=False)
    populate_conferences()

MEETING_DATA = {
    'spsp2014': {
        'name': 'Society for Personality and Social Psychology 2014',
        'info_url': None,
        'logo_url': None,
        "location": "Austin, TX",
        "start_date": "Feb 13 2014",
        "end_date": "Feb 15 2014",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'asb2014': {
        'name': 'Association of Southeastern Biologists 2014',
        'info_url': 'http://www.sebiologists.org/meetings/talks_posters.html',
        'logo_url': None,
        "location": "Spartanburg, SC",
        "start_date": "Apr 2 2014",
        "end_date": "Apr 4 2014",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'aps2014': {
        'name': 'Association for Psychological Science 2014',
        'info_url': 'http://centerforopenscience.org/aps/',
        'logo_url': '/static/img/2014_Convention_banner-with-APS_700px.jpg',
        "location": "San Franscisco, CA",
        "start_date": "May 22 2014",
        "end_date": "May 25 2014",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'annopeer2014': {
        'name': '#annopeer',
        'info_url': None,
        'logo_url': None,
        "location": None,
        "start_date": None,
        "end_date": None,
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'cpa2014': {
        'name': 'Canadian Psychological Association 2014',
        'info_url': None,
        'logo_url': None,
        "location": "Vancouver, BC",
        "start_date": "Jun 05 2014",
        "end_date": "Jun 07 2014",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'filaments2014': {
        'name': 'National Radio Astronomy Observatory Filaments 2014',
        'info_url': None,
        'logo_url': 'https://science.nrao.edu/science/meetings/2014/'
                    'filamentary-structure/images/filaments2014_660x178.png',
        "location": "Charlottesville, VA",
        "start_date": "Oct 10 2014",
        "end_date": "Oct 11 2014",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'bitss2014': {
        'name': 'Berkeley Initiative for Transparency in the Social Sciences Research Transparency Forum 2014',
        'info_url': None,
        'logo_url': os.path.join(
            settings.STATIC_URL_PATH,
            'img',
            'conferences',
            'bitss.jpg',
        ),
        "location": "Berkeley, CA",
        "start_date": "Dec 11 2014",
        "end_date": "Dec 12 2104",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': False,
        'talk': True,
    },
    'spsp2015': {
        'name': 'Society for Personality and Social Psychology 2015',
        'info_url': None,
        'logo_url': None,
        "location": "Long Beach, CA",
        "start_date": "Feb 26 2015",
        "end_date": "Feb 28 2015",
        'active': False,
        'admins': [],
        'poster': True,
        'talk': True,
    },
    'aps2015': {
        'name': 'Association for Psychological Science 2015',
        'info_url': None,
        'logo_url': 'http://www.psychologicalscience.org/images/APS_2015_Banner_990x157.jpg',
        "location": "New York, NY",
        "start_date": "May 21 2015",
        "end_date": "May 24 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'icps2015': {
        'name': 'International Convention of Psychological Science 2015',
        'info_url': None,
        'logo_url': 'http://icps.psychologicalscience.org/wp-content/themes/deepblue/images/ICPS_Website-header_990px.jpg',
        "location": "Amsterdam, The Netherlands",
        "start_date": "Mar 12 2014",
        "end_date": "Mar 14 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'mpa2015': {
        'name': 'Midwestern Psychological Association 2015',
        'info_url': None,
        'logo_url': 'http://www.midwesternpsych.org/resources/Pictures/MPA%20logo.jpg',
        "location": "Chicago, IL",
        "start_date": "Apr 30 2015",
        "end_date": "May 02 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'NCCC2015': {
        'name': 'North Carolina Cognition Conference 2015',
        'info_url': None,
        'logo_url': None,
        "location": "Elon, NC",
        "start_date": "Feb 21 2015",
        "end_date": "Feb 21 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'VPRSF2015': {
        'name': 'Virginia Piedmont Regional Science Fair 2015',
        'info_url': None,
        'logo_url': 'http://vprsf.org/wp-content/themes/VPRSF/images/logo.png',
        "location": "Charlottesville, VA",
        "start_date": "Mar 17 2015",
        "end_date": "Mar 17 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'APRS2015': {
        'name': 'UVA Annual Postdoctoral Research Symposium 2015',
        'info_url': None,
        'logo_url': 'http://s1.postimg.org/50qj9u6i7/GPA_Logo.jpg',
        "location": "Charlottesville, VA",
        "start_date": None,
        "end_date": None,
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'ASB2015': {
        'name': 'Association of Southeastern Biologists 2015',
        'info_url': None,
        'logo_url': 'http://www.sebiologists.org/wp/wp-content/uploads/2014/09/banner_image_Large.png',
        "location": "Chattanooga, TN",
        "start_date": "Apr 01 2015",
        "end_date": "Apr 04 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'TeaP2015': {
        'name': 'Tagung experimentell arbeitender Psychologen 2015',
        'info_url': None,
        'logo_url': None,
        "location": "Hildesheim, Germany",
        "start_date": "Mar 08 2015",
        "end_date": "Mar 11 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'VSSEF2015': {
        'name': 'Virginia State Science and Engineering Fair 2015',
        'info_url': 'http://www.vmi.edu/conferences/vssef/vssef_home/',
        'logo_url': 'http://www.vmi.edu/uploadedImages/Images/Headers/vssef4.jpg',
        "location": "Lexington, VA",
        "start_date": "Mar 27 2015",
        "end_date": "Mar 28 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'RMPA2015': {
        'name': 'Rocky Mountain Psychological Association 2015',
        'info_url': 'http://www.rockymountainpsych.org/uploads/7/4/2/6/7426961/85th_annual_rmpa_conference_program_hr.pdf',
        'logo_url': 'http://www.rockymountainpsych.org/uploads/7/4/2/6/7426961/header_images/1397234084.jpg',
        "location": "Boise, Idaho",
        "start_date": "Apr 09 2015",
        "end_date": "Apr 11 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'ARP2015': {
        'name': 'Association for Research in Personality 2015',
        'info_url': 'http://www.personality-arp.org/conference/',
        'logo_url': 'http://www.personality-arp.org/wp-content/uploads/conference/st-louis-arp.jpg',
        "location": "St. Louis, MO",
        "start_date": "Jun 11 2015",
        "end_date": "Jun 13 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'SEP2015': {
        'name': 'Society of Experimental Psychologists Meeting 2015',
        'info_url': 'http://faculty.virginia.edu/Society_of_Experimental_Psychologists/',
        'logo_url': 'http://www.sepsych.org/nav/images/SEP-header.gif',
        "location": "Charlottesville, VA",
        "start_date": "Apr 17 2015",
        "end_date": "Apr 18 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'Reid2015': {
        'name': 'L. Starling Reid Undergraduate Psychology Conference 2015',
        'info_url': 'http://avillage.web.virginia.edu/Psych/Conference',
        "location": "Charlottesville, VA",
        "start_date": "Apr 02 2015",
        "end_date": "Apr 02 2015",
        'logo_url': None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'NEEPS2015': {
        'name': 'Northeastern Evolutionary Psychology Conference 2015',
        'info_url': 'http://neeps2015.weebly.com/',
        "location": "Boston, MA",
        "start_date": "Apr 09 2015",
        "end_date": "Apr 11 2015",
        'logo_url': None,
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'VaACS2015': {
        'name': 'Virginia Section American Chemical Society Student Poster Session 2015',
        'info_url': 'http://virginia.sites.acs.org/',
        'logo_url': 'http://virginia.sites.acs.org/Bulletin/15/UVA.jpg',
        "location": "Charlottesville, VA",
        "start_date": "Apr 17 2015",
        "end_date": "Apr 17 2015",
        'active': False,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'MADSSCi2015': {
        'name': 'Mid-Atlantic Directors and Staff of Scientific Cores & Southeastern Association of Shared Services 2015',
        'info_url': 'http://madssci.abrf.org',
        'logo_url': 'http://s24.postimg.org/qtc3baefp/2015madssci_seasr.png',
        "location": "Charlottesville, VA",
        "start_date": "Jun 03 2015",
        "end_date": "Jun 5 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'NRAO2015': {
        'name': 'National Radio Astronomy Observatory Accretion 2015',
        'info_url': 'https://science.nrao.edu/science/meetings/2015/accretion2015/posters',
        "location": "Charlottesville, VA",
        "start_date": "Oct 09 2015",
        "end_date": "Oct 10 2015",
        'logo_url': None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'ARCS2015': {
        'name': 'Advancing Research Communication and Scholarship 2015',
        'info_url': 'http://commons.pacificu.edu/arcs/',
        'logo_url': 'http://commons.pacificu.edu/assets/md5images/4dfd167454e9f4745360a9550e189323.png',
        "location": "Philadelphia, PA",
        "start_date": "Apr 26 2015",
        "end_date": "Apr 28 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'singlecasedesigns2015': {
        'name': 'Single Case Designs in Clinical Psychology: Uniting Research and Practice',
        'info_url': 'https://www.royalholloway.ac.uk/psychology/events/eventsarticles/singlecasedesignsinclinicalpsychologyunitingresearchandpractice.aspx',
        'logo_url': None,
        "location": "London, UK",
        "start_date": "Apr 17 2015",
        "end_date": "Apr 17 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'OSFM2015': {
        'name': 'OSF for Meetings 2015',
        'info_url': None,
        'logo_url': None,
        "location": "Charlottesville, VA",
        "start_date": None,
        "end_date": None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'JSSP2015': {
        'name': 'Japanese Society of Social Psychology 2015',
        'info_url': 'http://www.socialpsychology.jp/conf2015/index.html',
        'logo_url': None,
        "location": "Tokyo, Japan",
        "start_date": "Oct 31 2015",
        "end_date": "Nov 01 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    '4S2015': {
        'name': 'Society for Social Studies of Science 2015',
        'info_url': 'http://www.4sonline.org/meeting',
        'logo_url': 'http://www.4sonline.org/ee/denver-skyline.jpg',
        "location": "Denver, CO",
        "start_date": "Nov 11 2015",
        "end_date": "Nov 14 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'IARR2016': {
        'name': 'International Association for Relationship Research 2016',
        'info_url': 'http://iarr.psych.utoronto.ca/',
        'logo_url': None,
        "location": "Toronto, Canada",
        "start_date": "Jul 20 2016",
        "end_date": "Jul 24 2016",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'IA2015': {
        'name': 'Inclusive Astronomy 2015',
        'info_url': 'https://vanderbilt.irisregistration.com/Home/Site?code=InclusiveAstronomy2015',
        'logo_url': 'https://vanderbilt.blob.core.windows.net/images/Inclusive%20Astronomy.jpg',
        "location": "Nashville, TN",
        "start_date": "Jun 17 2015",
        "end_date": "Jun 19 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'PsiChiRepository': {
        'name': 'Psi Chi Repository',
        'info_url': None,
        'logo_url': None,
        "location": None,
        "start_date": None,
        "end_date": None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'R2RC': {
        'name': 'Right to Research Coalition',
        'info_url': None,
        'logo_url': None,
        "location": None,
        "start_date": None,
        "end_date": None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'OpenCon2015': {
        'name': 'OpenCon2015',
        'info_url': 'http://opencon2015.org/',
        'logo_url': 'http://s8.postimg.org/w9b30pxyd/Open_Con2015_new_logo.png',
        "location": "Brussels, Belgium",
        "start_date": "Nov 14 2015",
        "end_date": "Nov 16 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'ESIP2015': {
        'name': 'Earth Science Information Partners 2015',
        'info_url': 'http://esipfed.org/',
        'logo_url': 'http://s30.postimg.org/m2uz2g4pt/ESIP.png',
        "location": None,
        "start_date": None,
        "end_date": None,
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'SPSP2016': {
        'name': 'Society for Personality and Social Psychology 2016 ',
        'info_url': 'http://meeting.spsp.org',
        'logo_url': None,
        "location": "San Diego, CA",
        "start_date": "Jan 28 2016",
        "end_date": "Jan 30 2016",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'NACIII': {
        'name': '2015 National Astronomy Consortium (NAC) III Workshop',
        'info_url': 'https://info.nrao.edu/do/odi/meetings/2015/nac111/',
        'logo_url': None,
        "location": "Washington, DC",
        "start_date": "Aug 29 2015",
        "end_date": "Aug 30 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'CDS2015': {
        'name': 'Cognitive Development Society 2015',
        'info_url': 'http://meetings.cogdevsoc.org/',
        'logo_url': None,
        "location": "Columbus, OH",
        "start_date": "Oct 09 2015",
        "end_date": "Oct 10 2015",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
    'SEASR2016': {
        'name': 'Southeastern Association of Shared Resources 2016',
        'info_url': 'http://seasr.abrf.org',
        'logo_url': None,
        "location": "Atlanta, GA",
        "start_date": "Jun 22 2016",
        "end_date": "Jun 24 2016",
        'active': True,
        'admins': [],
        'public_projects': True,
        'poster': True,
        'talk': True,
    },
}

def clear_up_conf():
    print "Clear all the existing conferences"
    confs = Conference.find()
    for conf in confs:
        print conf.to_storage()
        conf.remove()
        conf.save()

def populate_conferences():
    clear_up_conf()
    for meeting, attrs in MEETING_DATA.iteritems():
        conf = Conference(
            endpoint=meeting, **attrs
        )
        try:
            conf.save()
        except ModularOdmException:
            print('{0} Conference already exists. Updating existing record...'.format(meeting))
            conf = Conference.find_one(Q('endpoint', 'eq', meeting))
            for key, value in attrs.items():
                setattr(conf, key, value)
            conf.save()


if __name__ == '__main__':
    main()
