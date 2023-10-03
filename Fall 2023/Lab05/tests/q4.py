test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # A result of 99 may arise because you did not consider
          >>> # Bird or Birds (capital B at start of sentence). Try using word.lower() for each word test.
          >>> birds == 99
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You are counting words that contain bird ie. bluebird not isolated words.
          >>> birds == 208
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You missed also counting birds in addition to bird, add an elif. 
          >>> birds == 17
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # That's all of the isolated birds and birds in Darwin's work.
          >>> birds == 100
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