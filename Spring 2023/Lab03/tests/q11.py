test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(really_highly_rated) == tables.Table
          True
          >>> really_highly_rated.num_rows == 9
          True
          >>> print(really_highly_rated.sort(0).take([2, 8]))
          Votes   | Rating | Title                    | Year | Decade
          692753  | 9      | The Godfather: Part II   | 1974 | 1970
          1498733 | 9.2    | The Shawshank Redemption | 1994 | 1990
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
