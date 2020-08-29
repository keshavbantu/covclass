import urllib.request
import PyPDF2 as pypdf
import re
import gc
import dateRefresh as dR
import os

dateIter=dR.newDate
#dateIter="28-07-2020"	#testing, comment this later
def dload():
    baseurl="https://covid19.karnataka.gov.in/storage/pdf-files/Media-Bulletin/"
    endUrl="%20HMB%20English.pdf"
    finalUrl=baseurl+str(dateIter)+endUrl
    urllib.request.urlretrieve(finalUrl, "file.pdf")

def extract():
	global totalPages
	newNo=0
	loadFile=open('file.pdf','rb')
	readerObj=pypdf.PdfFileReader(loadFile)
	totalPages=readerObj.numPages
	for i in range(1,20):
		pageIter=totalPages-i
		pageObj=readerObj.getPage(pageIter)
		content=pageObj.extractText()
		if "Symptoms" in content:
			newNo=pageIter
			del pageObj
			del content
			break
	return newNo

def dispData(basePage):	#basepage = (keyword symptoms)
	pageContainer=[]	#contains pages with usable data
	noSpace=""
	loadFile=open('file.pdf','rb')
	readerObj=pypdf.PdfFileReader(loadFile)	
	for j in range(basePage,totalPages):
		pageContainer.append(j)
	for k in range(0,len(pageContainer)-1):	#k=no of valid data pages
		pageObj=readerObj.getPage(pageContainer[k])
		content=pageObj.extractText()
		sentence = re.sub(r"\s+", "", content, flags=re.UNICODE)
		noSpace=noSpace+sentence
	return noSpace

dload()
if (os.path.exists("file.pdf"))==True:
	print("File Found")
else:
	print("File not avilable")
newPage=extract()
cleanThis=dispData(newPage)
localdb=open("localdb.txt", "a+")
dbOps = localdb.write(cleanThis)
print('ReadOp Completed')
localdb.close()
gc.collect()


#death reporting started 23rd may
# june 21st readable data published
