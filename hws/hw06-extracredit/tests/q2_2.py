OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(simulate_key_strike() is not None)\nTrue\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import string\n'
                                               '>>> print(all([simulate_key_strike() in list(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(100)]))\n'
                                               'True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numpy as np\n>>> np.random.seed(22)\n>>> print(62 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 45)\nTrue\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
