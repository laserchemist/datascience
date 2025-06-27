test = {
  'name': 'Question 1',
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
          >>> # Need create with strptime('2020-01-21', '%Y-%m-%d')
          >>> type(time0) == time.struct_time
          True
          >>> type(time1) == float
          True
          >>> difftimeA == 61344000
          True
          >>> difftimeB == 61344000.0
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
