test = {
  'name': '10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Try assigning start to a negative integer based on invented.
          >>> #   start = int(invented.replace('BC ', '-'))
          >>> start in (-106, -105)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try assigning end to a positive integer based on revolution.
          >>> # You can replace some part of a string with nothing.
          >>> #   end = int(revolution.replace('AD ', ''))
          >>> end in (1440, 1441)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end-start in (1545, 1546)
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
