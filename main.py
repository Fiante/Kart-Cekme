import random 
Karakterler = ['Aeon', 'Bark', 'Boblin', 'Heliom', 'Leorio', 'Ren', 'Set', 'Vael', 'Vang', 'Veny', 'Glob', 'Wez', 'Tours', 'Tef']
Items= ['Et', 'Bronz', 'Kalkan', 'Kask', 'Kazan', 'Kılıç', 'Ok', 'Silver', 'Taç', ]
Goblin = ['Aeon', 'Bark', 'Boblin']
while True:
    print("Karakterin - ", random.choice(Karakterler))
    print("Gelen_İtem - ", random.choice(Items))
    print("Goblin - ", random.choice(Goblin))

    input("Yeni karakter için enter'a bas")