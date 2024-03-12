OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(full_data.num_rows - -562)\n1124\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(list(full_data.labels)[0] == 'Player')\nTrue\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> print(full_data.select(sorted(full_data.labels)).sort(4).take(range(3)).column(0).item(0) == 0.6)\nTrue\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
