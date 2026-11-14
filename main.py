def faktoriyel_hesaplama(num):
    if num ==0:
        return 1
    else:
        return num * faktoriyel_hesaplama(num-1)

def faktoriyel_toplam(num):
    if num == 0:
        return 0
    else:
        return num + faktoriyel_toplam(num-1)

print(faktoriyel_hesaplama(5))
print(faktoriyel_toplam(5))