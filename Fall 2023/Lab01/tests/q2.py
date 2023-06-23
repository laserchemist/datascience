test = {
  'name': '2.1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # seconds_since_2000.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell below Question 2 where you defined
          >>> # seconds_since_2000.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'seconds_since_2000' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # seconds_since_2000 appropriately.  It should be a number,
          >>> # computed using Python's arithmetic.  For example, this is
          >>> # almost right:
          >>> #   seconds_since_2000 = 22*365*24*60*60
          >>> seconds_since_2000 != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't account for leap years.
          >>> # There were 6 leap years and 16 non-leap years in this period.
          >>> # Leap years have 366 days instead of 365.
          >>> seconds_since_2000 != 693792000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> seconds_since_2000 == 694310400
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
