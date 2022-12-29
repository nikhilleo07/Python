print('Dictionary of Anime details')
anime={'Name':'One Piece','Character Name':'Luffy','Age':21,'Fruit':'Gum Gum'}
anime['God']='Sun God'
anime['Age']=19
print(anime)
print('In '+anime['Name']+'  '+anime['Character Name']+' Eated '+anime['Fruit']+' Fruit.')
print(f'The Key words of anime {anime.keys()}')
print(f'The Values of anime {anime.values()}')
print(f'The Items in the anime details {anime.items()}')