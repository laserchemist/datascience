test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
            'code': r"""
             >>> # Need to define your name at top of sheet
             >>> type(name) == str
             True
             """
        },

        {
          'code': r"""
          >>> # Need to use EDS.ptrend and the 2023 Table
          >>> int(plotcheck) == int(364.0)
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
