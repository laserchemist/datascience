test = {
  'name': 'q1.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your estimate is subtracting minimumdie roll of 1
          >>> modifier-7 < estimated_modifier <  modifier+7 
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
