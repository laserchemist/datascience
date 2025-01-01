test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [

        {
            'code': r"""
            >>> # Need create function ratio(x1,x2)
            >>> from datascience import *
            >>> round(ratio(1,4),2) < 0.4
            True
            """
        },
         {
            'code': r"""
            >>> # Need to respond to question
            >>> len(q6_answer) >20
            True
            """
         } 
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
   }
  ]
}
