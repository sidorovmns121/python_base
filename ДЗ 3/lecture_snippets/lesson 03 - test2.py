zoo_pets_mass = {'lion':300,
            'elephant':5000,
            'monkey':50,
            'wolf':100}
total_mass = 0
for mass in zoo_pets_mass.values():
    print(mass)
    total_mass += mass
print('Общая масса животных', total_mass)
