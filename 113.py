import math
l = 10
g = 9.81
print("Угол (градусы) | Скорость (м/с)")
print("-------------------------")
for a in range(0, 61, 5):
    angle_rad = math.radians(a)
    v = math.sqrt((4 / 3) * g * l * math.sin(angle_rad))
    print(f"{a:>15} | {v:.2f}")