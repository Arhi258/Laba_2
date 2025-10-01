h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))
s = int(input("Введите секунды: "))

angle_h = h * 30
angle_m = m * 0.51
angle_s = s * 0.0086
common_angle = angle_m + angle_s + angle_h

print(f"Угол между положением часовой стрелкой в начале суток и в указанный момент: {common_angle}")