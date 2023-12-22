test = {
  'name': '10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hint: You can write the sine of 1.5*pi as:
          >>> #   math.sin(1.5 * math.pi)
          >>> import math
          >>> import numpy as np
          >>> test = np.round(math.sin(math.pi/4),8)
          >>> np.round(sine_of_pi_over_four, 8) == test
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
