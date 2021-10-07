nr_linii=int(input("Dati numarul de linii si de coloane ale matricii patratice: "))
print(nr_linii)
matrice=[]
diagonala_principala=[]
diagonala_secundara=[]
partea_de_sus_diagonala_principala=[]
partea_de_jos_diagonala_principala=[]
partea_de_jos_diagonala_secundara=[]
partea_de_sus_diagonala_secundara=[]
if(nr_linii>=2)and(nr_linii<=10):
    for i in range(nr_linii):
        linie=[]
        for j in range(nr_linii):
            linie.append(int(input(f"Dati elementul pe pozitia {i} {j} : ")))
        matrice.append(linie)
    
    for i in range(nr_linii):
        for j in range(nr_linii):
            if i==j:
                diagonala_principala.append(matrice[i][j])
            if i+j==nr_linii-1:
                diagonala_secundara.append(matrice[i][j])
            if i>j:
                partea_de_jos_diagonala_principala.append(matrice[i][j])
            if i<j:
                partea_de_sus_diagonala_principala.append(matrice[i][j])
            if i+j<nr_linii-1:
                partea_de_sus_diagonala_secundara.append(matrice[i][j])
            if i+j>nr_linii-1:
                partea_de_jos_diagonala_secundara.append(matrice[i][j])

    print(f"Suma elementelor diagonalei principale este: {sum(diagonala_principala)}")
    print(f"Suma elementelor diagonalei secundare este: {sum(diagonala_secundara)}")
    print(f"Suma elementelor mai sus de diagonala principala este : {sum(partea_de_sus_diagonala_principala)}")
    print(f"Suma elementelor mai jos de diagonala principala este : {sum(partea_de_jos_diagonala_principala)}")
    print(f"Suma elementelor mai sus de diagonala secundara este: {sum(partea_de_sus_diagonala_secundara)}")
    print(f"Suma elementelor mai jos de diagonala secundara este : {sum(partea_de_jos_diagonala_secundara)}")
else:
    print("Numarul de linii nu satisface conditiile problemei. Mai incercati")
