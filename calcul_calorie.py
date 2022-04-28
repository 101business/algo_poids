calories_in = 2000
poids = 80
nombre_pas = 5000
minutes_cardio = 20
minutes_salle = 60

######


a = nombre_pas * 0.002 * poids
b = minutes_cardio * 0.4 * poids
c = minutes_salle * 0.1 * poids
d = poids * 2

calories_out = a + b + c + d
print('pas', a)
print('cardio', b)
print('salle',c)
print('rest',d)
print('calorie_out', calories_out)


if (calories_in > calories_out):
    print('raté, manger moins')

else:
    print('réussi, continue')
