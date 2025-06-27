test = {
  'name': 'q3.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ### Testing answer to 1st open ended question in Q3 above if answer is not there or too short, fails
          >>> test_open('Question: What are the most important words in the article?',notebook,60)==1
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ### Testing answer to open ended question just above in Q3 if answer is not there or too short, fails
          >>> test_open('Question: Now what are the most important words in the article after removing stop words?',notebook,60)==1
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ### Looking for last Table without stop words
          >>> type(RSV_word_table_nostop)==tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        }
         ,
          {
          'code': r"""
          >>> ### Looking for rsv word count
          >>> type(rsv)==int
          True
          """,
          'hidden': False,
          'locked': False
        }
          
          
      ],
      'scored': True,
      'setup': '',
      'teardown': print('Note: this test only checks that you answered, not whether your answer is correct.'),
      'type': 'doctest'
    }
  ]
}
