test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [

        {
            'code': r"""
            >>> # Need create new column
            >>> from datascience import *
            >>> max(COVID.column('deathrate')) > -1.0
            True
            """
        },
        {
            'code': r"""
             >>>  # Column with deathrate in COVID table sho
             >>> import numpy as np
             >>> type(COVID.column('deathrate')) == np.ndarray
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
