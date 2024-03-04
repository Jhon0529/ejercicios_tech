def devolver_distintos(num1, num2, num3):
    total = num1 + num2 + num3 
    if total > 15 :
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else: return num3
    elif total < 10 :
        if num1 < num2 and num1 < num3:
            return num1
        elif num2 < num1 and num2 < num3:
            return num2
        else: return num3
    elif total >= 10 and total <= 15 :
        num_ordenados = sorted([num1, num2, num3])
        num_intermedio = num_ordenados[1]
        return num_intermedio
print(devolver_distintos(6,3,4))