test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(correct_tbl) == tables.Table
          True
          >>> correct_tbl.num_rows == 271
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(correct_tbl) == tables.Table
          True
          >>> correct_tbl.num_columns == 12
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
