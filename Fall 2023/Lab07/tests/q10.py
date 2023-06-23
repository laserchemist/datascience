test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> temp_law.num_columns == 17
          True
          >>> year_range.num_rows == 5543
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> haveLaws.num_rows == 3864
          True
          >>> noLaws.num_rows == 1679
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