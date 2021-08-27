import urllib
from bs4 import BeautifulSoup

final={}
allKeys={}

def RegexFilter(strFilter):
    n = len(strFilter)
    newstr=""
    i = 0
    while(i<n):
        if(strFilter[i]=='['):
            while(strFilter[i]!=']'):
                i+=1
        if(i<n and strFilter[i]!=']'):
            newstr+=strFilter[i]
        i+=1
    newstr=newstr.rstrip("\n\r ").lstrip("\n\r ")
    return newstr

def FetchData(totoken):
    result = {}
    exceptional_row_count = 0
    html=urllib.request.urlopen("https://en.wikipedia.org/wiki/"+totoken);
    soup = BeautifulSoup(html,'html.parser')
    #print(soup.prettify())
    table = soup.find_all('tbody')[0]
    for tr in table.find_all('tr'):
        if tr.find('th'):
            #print(tr.find('th').prettify())
            #print(tr.find('td').prettify())
            try:
            	result[tr.find('th').text] = tr.find('td').text
            except:
            	print("Missed the row : "+tr.find('th').text)
        else:
            # the first row Logos fall here
            exceptional_row_count += 1
    if exceptional_row_count > 1:
    	print()
        #print( 'WARNING ExceptionalRow>1: ', table)

    filterresult={}
    for x in result.keys():
        try:
            filterresult[x]=RegexFilter(result[x])
        except:
            print(result[x])

    return filterresult


with open("names.txt","r") as file:
	totoken=file.readlines()
	for name in totoken:
		try:
			allData=FetchData(name)
			if "Mission type" in allData.keys():
				final[name]=allData
				for x in allData.keys():
				    print(x," : ",allData[x]);
				    allKeys[x]=1
				print("\nDone : "+name+"\n")
		except:
			print("Some Load in :"+name)

print(len(final))

finalkeys=[]
for x in final.keys():
	print(x)
	finalkeys.append(x)
	print(final[x])

totkeys=[]
for x in allKeys.keys():
	print(x)
	totkeys.append(x)

mycsv=open("final.csv","w+")

arr = [["0" for j in range(len(allKeys.keys())+1)] for i in range(1+len(final))]
for i in range(len(final)):
	arr[i+1][0]=finalkeys[i]
	for j in range(len(allKeys.keys())):
		arr[0][j+1]=totkeys[j]
		try:
			arr[i+1][j+1]=final[arr[i+1][0]][arr[0][j+1]]
		except KeyError:
			arr[i+1][j+1]="0"

deleter=['\xa0','\xb0','\u2032','\u2033','\ufeff']
for i in range(len(final)+1):
	for j in range(len(allKeys.keys())+1):
		for k in deleter:
			arr[i][j]=arr[i][j].replace(k,'')
		try:
			mycsv.write(arr[i][j].rstrip('\n')+";")
		except:
			continue;
	mycsv.write("\n")

print(arr)
mycsv.close()