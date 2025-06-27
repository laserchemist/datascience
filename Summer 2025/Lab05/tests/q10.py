test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> type(shadow_options) == np.ndarray
          True
          >>> type(spring_options) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(shadow_options)
          2
          >>> len(spring_options)
          2
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> 'yes' in shadow_options
          True
          >>> 'no' in shadow_options
          True
          >>> 'late' in spring_options
          True
          >>> 'early' in spring_options
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_observations == 530
          True
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
