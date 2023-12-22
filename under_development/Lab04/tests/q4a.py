test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
          {
            'code': r"""
             >>> # Need to define your name at top of sheet
             >>> # rerun top cells to make sure defined
             >>> type(name) == str
             True
             """
        },


        {
            'code': r"""
            >>> # Need create two arrays, dates and deaths
            >>> import numpy as np
            >>> type(dates) == np.ndarray
            True
            """
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
   }
  ]
}
