test = {
  'name': '1',
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
          >>> 'expression' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't change the cell to define
          >>> # expression appropriately.  It should be a number,
          >>> # computed using Python's arithmetic.  Remember the order
          >>> # of operations. (PEMDAS)
          >>> expression != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> expression == 2022
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
