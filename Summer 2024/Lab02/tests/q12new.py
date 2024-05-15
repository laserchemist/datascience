test = {
  'name': '12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you have created a list
          >>> type(ADK_highpeaks_ft) == type([400])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you converted all values
          >>> len(ADK_highpeaks_ft)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check your conversion to feet, 1 m = 3.28084 ft
          >>> import numpy as np
          >>> all(ADK_highpeaks_ft > np.array([5000,5000,4800,4800]))
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
