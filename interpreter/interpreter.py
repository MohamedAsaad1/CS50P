all = input("Expression:")

new_all = all.split(" ")

if new_all[1] == "+":
    print(float(new_all[0]) + float(new_all[2]))
elif new_all[1] == "*":
    print(float(new_all[0]) - float(new_all[2]))
elif new_all[1] == "-":
    print(float(new_all[0]) * float(new_all[2]))
else:
    print(float(new_all[0]) / float(new_all[2]))


#  another solution

#all = input("Expression:")

#x_x, y, z_z = all.split(" ")

#x = float(x_x)
#z = float(z_z)

#if y == "+":
#    print(x + z)
#elif y == "*":
#    print(x * z)
#elif y == "-":
#    print(x - z)
#else:
#    print(x / z)





