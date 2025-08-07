test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your function follows the correct function format/syntax, see above
          >>> callable(density)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your function does not return the correct value, check the multiplication/division, addition/subtraction 
          >>> # and use of the P, T, M paramters in your  function definition.
          >>> density(1,298,18) < 1 and  density(1,298,18) > 0.6
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
