test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure density function is correctly formulated and using correct value of R
          >>> density(1,298,18.0)<=0.74
          True
          >>> density(1,298,18.0)>=0.73
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
