# Lecture 6.2, slide 3

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

print(Techs)
print(Ivys)
print(Ivys[1])
print(Ivys[:2])

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')
Techs[2] = 'WPI'

print('Univs = ' + str(Univs1))
print()
print('Univs1 = ' + str(Univs1))

for e in Univs:
    print('Univs contains ' + str(e) + ' which contains')
    for u in e:
        print('              ' + str(u))