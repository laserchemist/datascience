test = {
  'name': '3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # expression.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell again where you defined
          >>> # expression.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'bundle_height_km' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # expression appropriately.
          >>> bundle_height_km != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your answer is off by quite a bit. Be sure to check your
          >>> # units! Convert the paper thickness to meters, then convert
          >>> # your calculated answer to kilometers.
          >>> np.abs(bundle_height_km - 13.4217728) < 0.1 
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
