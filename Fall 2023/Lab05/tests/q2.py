test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> plain_price == 10
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> pizza_price('veggie') == 12
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> pizza_price('pepperoni') == 13
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pizza_price('supreme') == 15
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