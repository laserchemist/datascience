test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [

        {
            'code': r"""
            >>> # Chain of step-by-step doesn't matter. 
            >>> # The test only check the final result.
            >>> light_but_long_lived.column("Animal") == make_array(['Tiger', 'Zebra'])
            array([[ True,  True]], dtype=bool)
            """
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
   }
  ]
}