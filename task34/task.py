n=(input("Введите строку: ")).split(" ")
countGlasnueFirst=0
countGlasnue=0
ritm=True
for i in range(len(n)):
    for j in range(len(n[i])):
        if((n[i])[j]=='а')|((n[i])[j]=='у')|((n[i])[j]=='е')|((n[i])[j]=='ё')|((n[i])[j]=='ы')|((n[i])[j]=='о')|((n[i])[j]=='я')|((n[i])[j]=='и')|((n[i])[j]=='ю'):
            if i==0:
                countGlasnueFirst+=1
            else:
                countGlasnue+=1
        if (i>0)&(j==(len(n[i])-1)):
            if countGlasnue!=countGlasnueFirst:
                ritm=False
            countGlasnue=0
if ritm:
    print("Парам пам-пам")
else:
    print("Пам парам")