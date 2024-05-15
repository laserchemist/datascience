test = {
  'name': 'q1.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (roll_bins == np.arange(1, modifier+2+20, 1))[0]
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
