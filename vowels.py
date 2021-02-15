name = input("enter name:")
place = input("enter place:")
animal = input("enter animal:")
thing = input("enter any thing:")
if animal[0] in ['a','e','i','o','u']:
    article1 = 'an'
else:
    article = 'a'
if thing[0] in ['a','e','i','o','u']:
    article2 = 'an'
else:
    article2 = 'a'
print(name,"saw",article1,animal,"sitting on top of",article2,thing,"on his way to",place)









