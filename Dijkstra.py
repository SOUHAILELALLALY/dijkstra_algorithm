import math as mt



v=['A','B','E','D','C','F','G','H']
e={'A':[('B',7),('E',14)],
   'B':[('C',8)],
   'E':[('F',19)],
   'C':[('D',6)],
   'D':[('F',11)],
   'F':[('G',4),('H',13)],
   'G':[('H',8)],
   'H':[]
}

v1=['M','N','E','L','T','S']
e1={'M':[('N',4),('L',7),('E',10)],
   'N':[('L',2),('S',8),('M',4)],
   'L':[('S',5),('E',8),('N',2),('M',7)],
   'E':[('T',4),('S',10),('L',8),('M',10)],
   'T':[('S',8),('E',4)],
   'S':[('T',8),('E',10),('L',5),('N',8)]
}



def chemin(t,s,fin):
    a=fin
    while fin != s:
        for i in range(0,len(t)):

            if t[i][1]==fin:
                a=a+f" {t[i][2]}"
                fin=t[i][2]
    a="".join(reversed(a))
    return a

def actualiser(v,t,e,w,y):
    r=[]
    a = len(t)
    b=len(w)
    j = e[t[a-1][1]]
    for i in range(0, len(v)):
        r.append((mt.inf, mt.inf))
    for i in range(0, len(v)):
        if y==i:
            r[i]=(0, '///')
        else:
            r[i] = w[b - 1][i]
    for i in range(0, len(v)):
        for h in range(0, len(j)):
            if v[i] == j[h][0]:
                if r[i]!=(0,'///') and (j[h][1] + t[a-1][0]) < w[a-2][i][0]:
                    r[i] = ((j[h][1] + t[a-1][0]), t[a-1][1])
    #chercher le minimum
    z = []
    for i in range(0, len(v)):
        if r[i][0]==0:
            z.append(1000)
        else:
            z.append(r[i][0])
    b = min(z)
    j = z.index(b)
    return r,j,b


def graf(s,v,e,fin):
    t=[(0,s,'')]#la colonne 0 de la table
    id=v.index(s)#l'indice de point de depart
    r = []  #ligne dans la table
    w=[]  #liste de toute les lignes

    f = 0
    for i in range(0,len(v)):
        r.append((mt.inf,mt.inf))
    r[id]=(0,'///')
    t.append((r[id][0], v[id], r[id][1]))
    w.append(r)
    y=id
    while f<100:
        #mc'est le minimum
        # y c'est l'indice de min
        r, y, m = actualiser(v, t, e, w, y)
        t.append((r[y][0], v[y], r[y][1]))
        w.append(r)
        if v[y]!=fin and m!= 1000:
            #Test si nous n'avons pas encore trouvé le point final
            continue
        else:
            print("table terminer")
            break

    for i in range(0,len(w)):
        str=''
        for j in range(0,len(w[i])):
            str=str+f" || {w[i][j]}"
        print(f"{t[i]}{str}")


    print(t)
    str = chemin(t,s,fin)
    res=f"la distance entre \"{s}\" et \"{fin}\" : {t[len(t)-1][0]} et le chemin : \"{str}\""
    return res








