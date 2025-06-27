test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [

        {
            'code': r"""
            >>> # Did you use .column()?
            >>> animal_data_heavy_to_light.column("Weight (kg)")[0] == 200
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