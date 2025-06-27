test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(epi_changes) == tables.Table
          True
          >>> list(epi_changes.column('Country').take(range(3)))
          ['Bahrain', 'Seychelles', 'Croatia']
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
