
arrSkor = [[]]
# teamA = str(input("Klub A : "))
# teamB = str(input("Klub B : "))
i = 0
skorA,skorB = input(f"Pertandingan {i+1} : ").split()

while int(skorA) >= 0 and int(skorB) >= 0 :
    arrSkor.insert(int(skorA),i,i)
    arrSkor.insert(int(skorB), i, i+1)
    i += 1
    skorA, skorB = input(f"Pertandingan {i+1} : ").split()
print(arrSkor)
