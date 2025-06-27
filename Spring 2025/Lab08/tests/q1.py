test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ### Questions is tested against standard solution for logical answers
          >>> ck==1
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ### Testing answer to open ended question if answer is not there or too short, fails
          >>> score = test_open('What trend do you see in the data?',notebook,60)
          >>> score > .5
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
