test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fix distance function, Look to code above for idea:
          >>> # d_p_q = np.sqrt(sum((make_array(2,3)-make_array(4,3))**2))
          >>>  ####### FIX: IT IS CRITICAL FOR REST OF LAB COMPUTATIONS #######
          >>> distance(make_array(2),make_array(1)) ==1.0
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> # Make sure distance function properly handles arrays as input
          >>> ####### IT IS CRITICAL FOR REST OF LAB COMPUTATIONS #######
          >>> distance(np.array([3,4]),np.array([2,4])) ==1.0
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