test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
          {
            'code': r"""
             >>> # Need to define your name at top of sheet
             >>> # rerun top cells to make sure defined
             >>> # Make sure Late2021 is defined
             >>> type(Late2021) == tables.Table
             True
             """
        },
          {
            'code': r"""
             >>> # Need to define your name at top of sheet
             >>> # rerun top cells to make sure defined
             >>> # Make sure Late2020 is correctly defined over correct date range
             >>> Late2021.num_rows == 60
             True
             """
        },

        {
            'code': r"""
            >>> # Need create two arrays, dates and deaths
            >>> import numpy as np
            >>> type(Late2020) == tables.Table
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
