from numpy import indices, msort
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('milestone2.csv')
myData=df.values
columnNames=list(df.head(0))
myDataDict={}
j=0
for i in columnNames:
    myDataDict[i]=myData[:,j]
    j=j+1
columnNames.pop(0)
print(myDataDict['Pakistan'])
# myDataDict=df.values(1)

# Average for every country
myunsortedlist =[]
avg = 0
for i in myDataDict['Pakistan']:
    avg = avg + i
avg = avg/len(myDataDict['Pakistan'])
# print(avg)
myunsortedlist.append(avg)

# Average for every country
avg = 0
for i in myDataDict['India']:
    avg = avg + i
avg = avg/len(myDataDict['India'])
# print(avg)
myunsortedlist.append(avg)

# Average for every country
avg = 0
for i in myDataDict['China']:
    avg = avg + i
avg = avg/len(myDataDict['China'])
# print(avg)
myunsortedlist.append(avg)

# Average for every country
avg = 0
for i in myDataDict['Turkey']:
    avg = avg + i
avg = avg/len(myDataDict['Turkey'])
# print(avg)
myunsortedlist.append(avg)


# Average for every country
avg = 0
for i in myDataDict['Israel']:
    avg = avg + i
avg = avg/len(myDataDict['Israel'])
# print(avg)
myunsortedlist.append(avg)

# Average for every country
avg = 0
for i in myDataDict['Switzerland']:
    avg = avg + i
avg = avg/len(myDataDict['Switzerland'])
# print(avg)
myunsortedlist.append(avg)

# Average for every country
avg = 0
for i in myDataDict['Netherlands']:
    avg = avg + i
avg = avg/len(myDataDict['Netherlands'])
# print(avg)
myunsortedlist.append(avg)




# print('The average of Pakistan is: ', myunsortedlist[0])
# print('The average of India is: ', myunsortedlist[1])
# print('The average of China is: ', myunsortedlist[2])
# print('The average of Turkey is: ', myunsortedlist[3])
# print('The average of Israeli is: ', myunsortedlist[4])
# print('The average of Switzerland is: ', myunsortedlist[5])
# print('The average of Netherlands is: ', myunsortedlist[6])
newlist = []
for i in myunsortedlist:
    newlist.append(i)
print('The unsorted list is: ', myunsortedlist)
myunsortedlist.sort()
# print(myunsortedlist)
myunsortedlist.sort()
min = 100000
sortedIndices=[]
for i in range(len(myunsortedlist)):
    for j in range(len(newlist)):
        if myunsortedlist[i] == newlist[j]:
            ind=j
    sortedIndices.append(ind)
    
    

print('The sorted list is: ', myunsortedlist)

myunsortedlist = msort(myunsortedlist)
rank = 1
i = 0
for index in myunsortedlist:
    print('The rank ',rank, "goes to ", columnNames[sortedIndices[i]], ' is with inflation of : ', myunsortedlist[i])
    rank += 1
    i+=1
sortedcountries=[]
for i in range(len(sortedIndices)):
    sortedcountries.append(columnNames[sortedIndices[i]])
df = pd.DataFrame(myunsortedlist)
df.columns = ['Average']
df.index = sortedcountries
df.plot(kind='bar' , title='Average of the countries' ,  legend=True, fontsize=15   ) 
# x = df.index
plt.title('Flow chart Diadram of Average of Countries')
plt.xlabel('Countries')
plt.ylabel('Average')
plt.show()


# # plt.ylabel('Increasing Average') 
# plt.xlabel('columnNames') 
# plt.show()



# myunsortedlist.append(avg[Pakistan])
# import pandas as pd
# import matplotlib.pyplot as plt

# # from sastapakitan import averageInflation
# df = pd.read_csv('milestone2.csv')
# columnNames = list(df.head(0))
# myData = df.values
# myDataDict = {}
# i = 0
# for column in columnNames:
#     myDataDict[column] = myData[:,i]
    # i += 1
# averageInflation = list(df.head(0))
# mydatainflation = df.values
# mydatadict = {}
# i = 0
# for inflation in averageInflation:
#     mydatadict[inflation] = mydatainflation[:,i]
#     i += 1
# plt.plot(myDataDict['Year'],myDataDict['Pakistan'],'green', label="Pakistan")
# plt.plot(myDataDict['Year'],myDataDict['Netherland'],'yellow', label="Netherland")
# # plt.plot(myDataDict['Year'],myDataDict['India'],'red', label="India")
# plt.plot(myDataDict['Year'],myDataDict['China'],'blue', label="China")

# plt.plot(mydatadict['Year'],mydatadict['Pakistan'],'green', label="Pakistan")
# plt.plot(mydatadict['Year'],mydatadict['China'],'Black', label="China")
# plt.plot(mydatadict['Year'],mydatadict['Switzerland'],'violet', label="Switzerland")
# plt.plot(mydatadict['Year'],mydatadict['Israel'],'black', label="Israel")
# plt.plot(mydatadict['Year'],mydatadict['India'],'brown', label="India")
# plt.plot(mydatadict['Year'],mydatadict['Turkey'],'red', label="Turkey")

 
# # x-coordinates of left sides of bars
# left = ['Years']
 
# # heights of bars
# height = ['Inflation']
 
# # labels for bars
# tick_label = ['years']
 
# # plotting a bar chart
# plt.bar(left, height, tick_label = tick_label,
#         width = 0.8, color = ['red', 'green'])
 

# plt.legend(loc="best")
# plt.show()
# Use myDataDict appropriately to compute the average inflation per country and then output their ranked order through print.
# Use as many helper functions from your milestone 1, as required!
# Can you use a different kind of plot (other than a line plot) to show your answer to the 'susta' question?
