test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(top_10_epi) == tables.Table
          True
          >>> top_10_epi.select('Score', 'Country').sort('Country')
          Score | Country
          79.6  | Austria
          82.5  | Denmark
          78.9  | Finland
          80    | France
          77.2  | Germany
          82.3  | Luxembourg
          77.7  | Norway
          78.7  | Sweden
          81.5  | Switzerland
          81.3  | United Kingdom
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
