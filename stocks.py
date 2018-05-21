
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ),
 ( 'AB', 100, '1-jul-2002', 12 ),
 ( 'CB', 500, '2-jan-1995', 1 ),
 ( 'MB', 2000, '27-jul-2001', 1000 )  ]

stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'GE':"General Electric", "AB":"Another Business","CB":"Courtney Brothers", "MB":"My Business"}

for purchase in purchases:
  for key, name in stockDict.items():
    if purchase[0] == key:
      price = purchase[1]*purchase[3]
      print("purchase history report " + name + " {0} date:{1}".format(price,purchase[2]))

## total investment by ticker symbol

for purchase in purchases:
  for key, name in stockDict.items():
    if purchase[0] == key:
      price = purchase[1]*purchase[3]
      print(key + " {0}".format(price))
