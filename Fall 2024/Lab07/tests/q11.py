test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> changes(make_array(10, 7, 12, 9, 13, 9, 11, 2, 14, 7, 19)) == 4
          True
          """,
          'hidden': False,
          'locked': False
        }, 
          {
          'code': r"""
          >>> changes(make_array(10, 7, 12, 9, 13, 9, 11, 2, 14, 7, 19, 382, 22, 392), 5) == 3
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
