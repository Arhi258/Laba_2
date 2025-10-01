side_length_a = int(input("Введите сторону a = "))
side_length_b = int(input("Введите сторону b = "))
side_length_c = int(input("Введите сторону c = "))

volume = side_length_a * side_length_b * side_length_c
lateral_surface = 2 * side_length_c * (side_length_a + side_length_b)

print(f"Объем прямоугольного параллелепипеда равен: {volume}")
print(f"Площадь боковой поверхности прямоугольного параллелепипеда равна: {lateral_surface}")