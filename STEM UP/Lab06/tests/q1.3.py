test = {
  'name': 'q1.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(5.7 - np.std([simulate_observations(11,7) for _ in range(5000)])) < .2
          True
          >>> abs(21.5 - np.mean([simulate_observations(11,7) for _ in range(5000)])) < .2
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
