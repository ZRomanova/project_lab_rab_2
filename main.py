height = float(input("Введите рост: "))
weight = float(input("Введите вес: "))
steps = float(input("Колличество шагов: "))
time = float(input("Время: "))
steplength = height /+ 0.37
length = steps * steplength  
lengthk = length / 1000
speed = length / (time * 60)
E = 0.035 * weight + (speed ** 2 / height) * 0.029 * weight 
kall = E * time 
print("Пройденная дистанция в метрах:", lengthk * 1000)
print("Количество сожженных калорий:", kall)
print("Пройденная дистанция в киллометрах", lengthk)
if lengthk < 2:
  print("Старайтесь лучше")
elif lengthk < 4:
  print("Продолжайте в том же духе")
else:
  print("Хорошая работа!")