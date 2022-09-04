# Сколько богатырей добавлялось в отряд в год.
count_of_adding_heroes = 0
# Сколько лет существует отряд.
count_years_squad = 9
# Список возрастов всех богатырей.
ages_of_heroes = []
# Возраст Черномора.
age_Chernomor = 65
# На сколько лет новый богатырь младше своего предшественника.
age_step = 1
# На сколько больше, чем в предыдущем году, добавляется богатырей в отряд.
hero_step = 1
# Возраст каждого отдельно взятого богатыря(будет изменяться в цикле).
age_hero_i = age_Chernomor

for year in range(1, count_years_squad + 1):
    count_of_adding_heroes += hero_step
    #    print(year, count_of_adding_heroes, '_'*100)
    for _ in range(count_of_adding_heroes):
        #        print(age_hero_i)
        ages_of_heroes.append(age_hero_i)
        age_hero_i -= age_step

# 1. Сколько всего богатырей в отряде.
print('Всего богатырей в отряде:', len(ages_of_heroes))

# 2. Средний возраст богатырей.
print('Средний возраст богатырей:', sum(ages_of_heroes) / len(ages_of_heroes))

# 3. Сколько лет самому юному.
print('Возраст самого юного:', ages_of_heroes[-1])

# 4. Изменение среднего возраста без учета самого юного и старшего богатырей.
print("Средний возраст без учета крайних богатырей: ",
      sum(ages_of_heroes[1:-1]) / len(ages_of_heroes[1:-1]))

