# 1.9.6 - Assignment: Cats With Hats
# Alternative solution to assignment using dictionaries


theCats = {}

for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print("Cat {} has a hat.".format(cats))
    else:
        print("Cat {} is hatless!".format(cats))
