my_family = {
    'sister': {
        'name': 'Anne Peyton',
        'age': 21
    },
    'mother': {
        'name': 'Jenji',
        'age': 47
    },
      'father':{
        'name':'Carter',
        'age': 49
    },
        'sister':{
          'name':'Merf',
          'age':17
    }
  }

for key, member in my_family.items(): 
    print(" {1} is my {0} and is {2} years old".format(key,member['name'], member['age']))
  