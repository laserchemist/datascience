test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(epi) == tables.Table
          True
          >>> epi.num_rows == 180
          True
          >>> epi.select('Rank', 'Country', 'Score', 'Decade Change').sort(3).take(range(5))
          Rank | Country       | Score | Decade Change
          163  | Vanuatu       | 28.9  | -11.9
          170  | Burundi       | 27    | -11.1
          107  | Bhutan        | 39.3  | -9.6
          176  | Cote d'Ivoire | 25.8  | -8.5
          39   | Singapore     | 58.1  | -8.4
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
