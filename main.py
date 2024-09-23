n= int(input("Введите количество школьников"))
k= int(input("Введите количество яблок"))
everyone=(k//n)
print(f'{everyone} яблоко каждому  из лиц')
ost=k%n
if n%k !=0:
    print(f'{ost} яблок осталось в корзине')
if n>k:
    print('делёжки не будет')