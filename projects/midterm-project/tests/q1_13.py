OK_FORMAT = True

test = {   'name': 'q1_13',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> region_counts.labels == ('region', 'count')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(region_counts.column('count')) == 25\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
