tom_list = [200, 150, 300, 240]
jo_list = [100, 230, 180, 190]

def cal_total(a_list):
    total = 0
    for i in a_list:
        total += i
    return total

print("toms's total =", cal_total(tom_list))
print("jo's total =", cal_total(jo_list))

def sum(a, b=100):
    return a + b

print(sum(30))
print(sum(30, 60))  