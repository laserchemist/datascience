test = {
  'name': 'q12_open_ended',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ### Testing answer to open ended question if answer is not there or too short, fails
          >>> test_open('Spring or would a coin toss at the 50 yard line', notebook, 30) == 1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': print('Note: this test only checks that you answered, not what you wrote in your feedback.'),
      'type': 'doctest'
    }
  ]
}