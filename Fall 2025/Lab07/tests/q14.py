test = {
  'name': 'Question 14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simulate_under_null(100) > -25 and simulate_under_null(100) < 25
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> max(samples) < 1200
          True
          >>> min(samples) > -1200
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
