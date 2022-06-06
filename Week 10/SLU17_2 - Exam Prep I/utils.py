import inspect
import math
import re
import json
import sys


#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback


def generate_data():
    return [{"Year": "2013", "Total": "53,2", "Education": "80,4", "Arts and Humanities": "56,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "201", "Total": "22,2", "Education": "80,4", "Arts and Humanities": "16,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "2014", "Total": "53,5", "Education": "80,7", "Arts and Humanities": "58,0", "Social Sciences, Management and Law": "58,5", "Sciences, Maths and Computer Science": "(R) 47,5", "Engineering": "(R) 27,6", "Agriculture": "56,9", "Health and Social Security": "76,6", "Services": "(R) 41,1"},
            {"Year": "2015", "Total": "53,6", "Education": "80,7", "Arts and Humanities": "58,7", "Social Sciences, Management and Law": "58,6", "Sciences, Maths and Computer Science": "(R) 47,8", "Engineering": "(R) 27,0", "Agriculture": "56,3", "Health and Social Security": "76,7", "Services": "(R) 41,0"},
            {"Year": "2016", "Total": "53,4", "Education": "80,3", "Arts and Humanities": "58,6", "Social Sciences, Management and Law": "58,9", "Sciences, Maths and Computer Science": "(R) 45,7", "Engineering": "(R) 27,3", "Agriculture": "56,4", "Health and Social Security": "76,8", "Services": "(R) 41,7"},
            {"Year": "2017", "Total": "53,6", "Education": "79,3", "Arts and Humanities": "59,0", "Social Sciences, Management and Law": "59,5", "Sciences, Maths and Computer Science": "44,2", "Engineering": "27,5", "Agriculture": "57,3", "Health and Social Security": "77,0", "Services": "42,1"},
            {"Year": "2013", "Total": "52,2", "Education": "80,4", "Arts and Humanities": "57,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "2014", "Total": "53,5", "Education": "80,7", "Arts and Humanities": "58,0", "Social Sciences, Management and Law": "58,5", "Sciences, Maths and Computer Science": "(R) 47,5", "Engineering": "(R) 27,6", "Agriculture": "56,9", "Health and Social Security": "76,6", "Services": "(R) 41,1"},
            {"Year": "2015", "Total": "53,6", "Education": "80,7", "Arts and Humanities": "58,7", "Social Sciences, Management and Law": "58,6", "Sciences, Maths and Computer Science": "(R) 47,8", "Engineering": "(R) 27,0", "Agriculture": "56,3", "Health and Social Security": "76,7", "Services": "(R) 41,0"},
            {"Year": "2016", "Total": "53,4", "Education": "80,3", "Arts and Humanities": "58,6", "Social Sciences, Management and Law": "58,9", "Sciences, Maths and Computer Science": "(R) 45,7", "Engineering": "(R) 27,3", "Agriculture": "56,4", "Health and Social Security": "76,8", "Services": "(R) 41,7"}
            ]


def generate_data_comma():
    return [{"year": "2013", "total": "53,2", "education": "80,4", "arts_and_humanities": "56,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "201", "total": "22,2", "education": "80,4", "arts_and_humanities": "16,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "2014", "total": "53,5", "education": "80,7", "arts_and_humanities": "58,0", "social_sciences_management_and_law": "58,5", "sciences_maths_and_computer_science": "47,5", "engineering": "27,6", "Agriculture": "56,9", "health_and_social_security": "76,6", "services": "41,1"},
            {"year": "2015", "total": "53,6", "education": "80,7", "arts_and_humanities": "58,7", "social_sciences_management_and_law": "58,6", "sciences_maths_and_computer_science": "47,8", "engineering": "27,0", "Agriculture": "56,3", "health_and_social_security": "76,7", "services": "41,0"},
            {"year": "2016", "total": "53,4", "education": "80,3", "arts_and_humanities": "58,6", "social_sciences_management_and_law": "58,9", "sciences_maths_and_computer_science": "45,7", "engineering": "27,3", "Agriculture": "56,4", "health_and_social_security": "76,8", "services": "41,7"},
            {"year": "2017", "total": "53,6", "education": "79,3", "arts_and_humanities": "59,0", "social_sciences_management_and_law": "59,5", "sciences_maths_and_computer_science": "44,2", "engineering": "27,5", "Agriculture": "57,3", "health_and_social_security": "77,0", "services": "42,1"},
            {"year": "2013", "total": "52,2", "education": "80,4", "arts_and_humanities": "57,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "2014", "total": "53,5", "education": "80,7", "arts_and_humanities": "58,0", "social_sciences_management_and_law": "58,5", "sciences_maths_and_computer_science": "47,5", "engineering": "27,6", "Agriculture": "56,9", "health_and_social_security": "76,6", "services": "41,1"},
            {"year": "2015", "total": "53,6", "education": "80,7", "arts_and_humanities": "58,7", "social_sciences_management_and_law": "58,6", "sciences_maths_and_computer_science": "47,8", "engineering": "27,0", "Agriculture": "56,3", "health_and_social_security": "76,7", "services": "41,0"},
            {"year": "2016", "total": "53,4", "education": "80,3", "arts_and_humanities": "58,6", "social_sciences_management_and_law": "58,9", "sciences_maths_and_computer_science": "45,7", "engineering": "27,3", "Agriculture": "56,4", "health_and_social_security": "76,8", "services": "41,7"}
            ]


def generate_data_clean():
    return [{"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.7, "social_sciences_management_and_law": 58.6, "sciences_maths_and_computer_science": 47.8, "engineering": 27.0, "arts_and_humanities": 58.7, "year": 2015, "services": 41.0, "total": 53.6, "agriculture": 56.3},
            {"education": 80.3, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.9, "sciences_maths_and_computer_science": 45.7, "engineering": 27.3, "arts_and_humanities": 58.6, "year": 2016, "services": 41.7, "total": 53.4, "agriculture": 56.4},
            {"education": 79.3, "health_and_social_security": 77.0, "social_sciences_management_and_law": 59.5, "sciences_maths_and_computer_science": 44.2, "engineering": 27.5, "arts_and_humanities": 59.0, "year": 2017, "services": 42.1, "total": 53.6, "agriculture": 57.3},
            {"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.7, "social_sciences_management_and_law": 58.6, "sciences_maths_and_computer_science": 47.8, "engineering": 27.0, "arts_and_humanities": 58.7, "year": 2015, "services": 41.0, "total": 53.6, "agriculture": 56.3},
            {"education": 80.3, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.9, "sciences_maths_and_computer_science": 45.7, "engineering": 27.3, "arts_and_humanities": 58.6, "year": 2016, "services": 41.7, "total": 53.4, "agriculture": 56.4},
            {"education": 79.3, "health_and_social_security": 77.0, "social_sciences_management_and_law": 59.5, "sciences_maths_and_computer_science": 44.2, "engineering": 27.5, "arts_and_humanities": 59.0, "year": 2017, "services": 42.1, "total": 53.6, "agriculture": 57.3}
            ]


def generate_data_enrolled():
    return [(2013, 56.9), (2014, 58.0), (2015, 58.7), (2016, 58.6), (2017, 59.0)]
