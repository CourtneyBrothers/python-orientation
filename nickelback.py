# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Nickelback','Far Away'),
    ('Young Father','Lord'),
    ('Lorde','Supercut'),
    ('Beyonce','I was here'),
    ('Drake', 'Nice for What')
}

newSet = [song for song in songs 
  if song[0] != 'Nickelback'
]

print(newSet)