test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
            'code': r"""
            >>> # Did you test the function yourself?
            >>> np.abs(celcius_to_farenheit(37) - 98.6) < 0.01
            True
            """
        },
        {
            'code': r"""
            >>> # Did you test the function yourself?
            >>> np.abs(celcius_to_farenheit(100) - 212) < 0.01
            True
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