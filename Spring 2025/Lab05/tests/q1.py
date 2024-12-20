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
          >>> number_pepperoni == 1
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