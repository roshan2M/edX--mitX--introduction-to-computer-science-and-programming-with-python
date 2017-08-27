# Lecture 6.3, slide 1

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]

for e in Univs:
    print('Univs contains ' + str(e) + ' which contains')
    for u in e:
        print('              ' + str(u))