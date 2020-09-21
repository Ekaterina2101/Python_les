from sys import argv

script_name, per_hour, rate_per_hour, prize = argv

print(f'Заработная плата составляет {int(per_hour) * int(rate_per_hour) + int(prize)} ')
