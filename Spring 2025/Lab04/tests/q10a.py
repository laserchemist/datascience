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
             >>>  # Need create the numpy array deathrate to add to COVID Table
             >>> import numpy as np
             >>> type(deathrate) == np.ndarray
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
