test = {
  'name': 'q9a_open_ended',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ### Testing answer to open ended question if answer is not there or too short, fails
          >>> test_open('Approximately when was the peak date', notebook, 7) == 1
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

