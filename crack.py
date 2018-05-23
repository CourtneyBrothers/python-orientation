for i in range (1,101):
  if (i/3.0).is_integer() and (i/5.0).is_integer():
    print('cracklepop')
  elif (i / 3.0).is_integer():
    print ('crackle')
  elif (i/5.0).is_integer():
    print('pop')
  else:
    print(i)