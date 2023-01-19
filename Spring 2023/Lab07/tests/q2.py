test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> us.num_rows == 198
          True
          """,
          'hidden': False,
          'locked': False
        }, 
          {
          'code': r"""
          >>> us.take(np.arange(2))
          year | country       | avg     | jan    | feb    | mar   | apr   | may    | jun    | jul    | aug    | sep    | oct    | nov   | dec
          1775 | United States | 9.49917 | -1.551 | 1.506  | 5.02  | 7.663 | 14.452 | 17.684 | 21.601 | 20.844 | 15.081 | 10.256 | 5.371 | -3.937
          1777 | United States | 8.30475 | 0.174  | -0.186 | 2.504 | 5.836 | 13.739 | 17.463 | 19.176 | 19.398 | 15.27  | 7.042  | 1.882 | -2.641
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
