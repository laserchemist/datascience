test = {
  'name': 'q3.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> freq.sort("frequency",descending=True).column("frequency").take(0) > 0.105
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
