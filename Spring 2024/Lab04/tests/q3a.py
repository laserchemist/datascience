test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
          {
            'code': r"""
             >>> # Need to define your name at top of sheet
             >>> # rerun top cells to make sure defined
             >>> type(name) == str
             True
             """
        },
        {
          'code': r"""
          >>> type(time1) == float
          True
          >>> type(time2) == float
          True
          """
        },
        {
            'code': r"""
            >>> # Need create Data Table using original COVID dataand where method
            >>> from datascience import *
            >>> type(Late2020) == tables.Table
            True
            """
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
   }
  ]
}
