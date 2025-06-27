test = {
  'name': 'Question 12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> changes_by_country.num_rows == 233
          True
          """,
          'hidden': False,
          'locked': False
        }, 
          {
          'code': r"""
          >>> changes_by_country.take(np.arange(4))
          country        | avg changes
          Afghanistan    | 18
          Albania        | -22
          Algeria        | 9
          American Samoa | -3
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
