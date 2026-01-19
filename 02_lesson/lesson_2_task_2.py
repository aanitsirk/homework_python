def is_year_leap(year):
    return True if year % 4 == 0 else False


year_num = 2020
result = is_year_leap(year_num)

print(f"год {year_num}: {result}")
