from time import sleep
print('=' * 26)
print('     10 TERM0S DE PA    ')
print('=' * 26)
PT = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
decimo = PT + (10 - 1) * razão
for c in range(PT, decimo + razão, razão):
    print(c, end=' → ')
    sleep(0.5)
print('Acabou!')
