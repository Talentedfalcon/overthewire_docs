cipher="PNUKLYLWRQKGKBE"

flag=""

shifts=[]

known_plain="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
known_cipher="EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"

for i in range(len(cipher)):
    shifts.append(ord(known_cipher[i])-ord(known_plain[i]))
    flag+=chr(((ord(cipher[i])-65-shifts[i])%26)+65)

print(shifts)
print(flag)