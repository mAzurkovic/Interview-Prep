def shakes(people):
    shakes = people - 1
    num = 0
    for i in range(people):
        num += shakes
        shakes -= 1
    
    return num

def shakes2(people):
    return (people**2 - people) / 2

print(shakes(10))