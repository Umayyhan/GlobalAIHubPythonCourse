#Explain your work
#write a program that includes information about the grades of 5 students in a school. 
#Question 1
nots =[[57,19,60],[20,38,54],[69,90,42],[34,84,90],[10,36,65]]
students=["Mustafa AKPINAR", "Ümmühan TEPEBAŞ",
    "Necmi GÜLER","Ahsen TEK","Ali AŞGAR"]
termNots = []
infoDict = {
    'std1': {'name': 'Mustafa','surname':'AKPINAR', 'midterm':57,'final':19, 'homework':60},
    'std2': {'name': 'Ümmühan','surname':'TEPEBAŞ', 'midterm':20,'final':38, 'homework':54},
    'std3': {'name': 'Necmi','surname':'GÜLER', 'midterm':69,'final':90, 'homework':42},
    'std4': {'name': 'Ahsen','surname':'TEK', 'midterm':34,'final':84, 'homework':90},
    'std5': {'name': 'Ali','surname':'AŞGAR', 'midterm':10,'final':36, 'homework':65},
}
print(infoDict['std1'])


#ogrenciler['123123123']['final']  
#print(users['cinarturan'])
for i in infoDict.values():
   print(i)

for i in students:
    for j in nots:
        value =((nots[i][j]+nots[i][j]+nots[i][j])/3)
        print(value)
        #termNots.append(value)
print(termNots , end=" ")      
	print(a)
