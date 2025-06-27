test = {
  'name': '9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Temperature not converted correctly.
          >>> #   
          >>> gasdata_convert>(27,24000)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Gas volume not coverted to mL correctly
          >>> # 
          >>> all(i>j for i,j in zip((26,24000),gasdata_convert))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(i>j for i,j in zip((27,25000),gasdata_convert)) and all(i<j for i,j in zip((26,24000),gasdata_convert))
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
