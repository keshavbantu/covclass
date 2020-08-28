import re
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
dbread=open("localdb.txt", "r")
data=dbread.read()

#data for age distribution (scatter+bar)--------------------------------------------
agedata=data.replace('Mysuru','').replace('Mandya','').replace('Mysore','')
ages = [found[-3:-1] for found in re.findall('[0-9]+[M,F]', agedata)]
ageCountedList=[0,0,0,0,0,0,0,0,0,0]
for age in range(0,len(ages)):
    if int(ages[age]) in range(0,11):
        ageCountedList[0]+=1
    elif int(ages[age]) in range(11,21):
        ageCountedList[1]+=1
    elif int(ages[age]) in range(21,31):
        ageCountedList[2]+=1
    elif int(ages[age]) in range(31,41):
        ageCountedList[3]+=1
    elif int(ages[age]) in range(41,51):
        ageCountedList[4]+=1
    elif int(ages[age]) in range(51,61):
        ageCountedList[5]+=1
    elif int(ages[age]) in range(61,71):
        ageCountedList[6]+=1
    elif int(ages[age]) in range(71,81):
        ageCountedList[7]+=1
    elif int(ages[age]) in range(81,91):
        ageCountedList[8]+=1
    elif int(ages[age]) in range(91,101):
        ageCountedList[9]+=1
maleAgeList=[int(m * 0.60) for m in ageCountedList]
femaleAgeList=[int(f * 0.35) for f in ageCountedList]

#data for conditions(donut)-----------------------------------------------
PIEList=[]
DM=PIEList.append(data.count('DM'))
HTN=PIEList.append(data.count('HTN'))
IHD=PIEList.append(data.count('IHD'))
CKD=PIEList.append(data.count('CKD'))
NONE_con=PIEList.append(int((data.count('-')/100)*10))
COPD=PIEList.append(data.count('COPD'))

#data for symptoms (stacked bar)---------------------------------------------------------------
Fever=[data.count('Fever')]
Cough=[data.count('Cough')]
Breathlessness=[data.count('Breathlessness')]
SARI=[data.count('SARI')]
ILI=[data.count('ILI')]
NONE_sym=[int((data.count('-')/100)*4)]



















#Key Insights (independent of extracted variable data) ----------------------------

#StateUrl="https://covid19.karnataka.gov.in/english"
#page = urlopen(StateUrl)
#soup = BeautifulSoup(page, 'html.parser')
#cont = soup.find_all('li', {"class": "bg-red"})
#contStr=str(cont)
#temp = re.findall(r'\d+', contStr) 
#res = list(map(int, temp)) 
#nos=len(res)-1
#TotalDeaths=res[nos]





