# Сумма возрастов матери и старшей дочери.
sum_age_of_mom_old_sis = 55
# Возраст младшей сестры согласно одному из условий задачи.
x_age_of_young_sis = 18

# Список со всеми возможными вариантами возрастов.
variants = []
# По условию возраст матери не может превышать 55 лет,следовательно переменная x, отвечающая за разряд десятков,
# ограничена до 5 включительно. Y перебирает все цифры.
for x in range(1, 6):
    for y in range(10):
        moms_age = x * 10 + y
        old_sis_age = y * 10 + x
        if moms_age + old_sis_age == sum_age_of_mom_old_sis \
                and moms_age > old_sis_age:
            variants.append((old_sis_age, moms_age))

new_variants = []
for old_sis_age, moms_age in variants:
    for diff in range(old_sis_age + 1):
        young_sis_age = old_sis_age - diff
        moms_new_age = moms_age + diff
        #        print(diff, str(moms_new_age)[::-1], str(young_sis_age))

        if int(str(moms_new_age)[::-1]) == young_sis_age:  # \
            new_variants.append((young_sis_age, old_sis_age, moms_age))

for num_var, fam_ages in enumerate(new_variants):
    young_sis_age = fam_ages[0]
    # Если нынешний возраст младшей сестры больше 18, то разница в скобках будет меньше нуля,
    # следовательно нынешний возраст отца будет увеличиваться.
    # Иначе разница в скобках - положительная, и возраст отца будет уменьшаться.
    father_age = sum(fam_ages) - (x_age_of_young_sis - young_sis_age)

    print("""Вариант {}, 
Возраст младшей сестры: {},
Возраст старшей сестры: {},
Возраст матери: {},
Возраст отца: {}; \n""".format(num_var, fam_ages[0], fam_ages[1], fam_ages[2], father_age))

