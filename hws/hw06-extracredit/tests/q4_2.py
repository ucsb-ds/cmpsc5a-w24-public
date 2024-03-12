OK_FORMAT = True

test = {   'name': 'q4_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(representative_sample.num_rows == 200)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(all(np.in1d(representative_sample.column('mag'), earthquakes.column('mag'))))\nTrue\n", 'hidden': False, 'locked': False},
                                   {   'code': ">>> print(representative_mean < max(representative_sample.column('mag')) and representative_mean > min(representative_sample.column('mag')))\nTrue\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
