test = {
  'name': 'q2.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ### Testing answer to open ended question if answer is not there or too short, fails
          >>> test_open('Question 2.3 Discussion',notebook,60)==1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': print('Note: this test only checks that you answered, not whether your answer is correct.'),
      'type': 'doctest'
    }
  ]
}
