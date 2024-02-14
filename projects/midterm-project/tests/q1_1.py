OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> ind_pop.labels == ('time', 'population_total')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> all(ind_pop.sort('time').column('time') == np.arange(1960, 2016))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
