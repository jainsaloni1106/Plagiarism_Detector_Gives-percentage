#Import all the required Libraries
from __future__ import division
import nltk, re, pprint , time
from termcolor import*
from nltk.stem.lancaster import LancasterStemmer

file_1 = open('green.txt')
file_2 = open('green2.txt')
material_1 = file_1.read()
material_2 = file_2.read()

list_material_1 = material_1.split('.')
list_material_2 = material_2.split('.')
cprint("                                              ****** The List for first file  ******                  \n",'yellow')
print(list_material_1)
list_token_1 = []
list_token_2 = []

for i in range(len(list_material_1)):
    list_token_1.append(nltk.word_tokenize(list_material_1[i].lower()))

for i in range(len(list_material_2)):
    list_token_2.append(nltk.word_tokenize(list_material_2[i].lower()))

list_pos1 = []
list_pos2 = []

for i in range(len(list_material_1)):
    list_pos1.append(nltk.pos_tag(list_token_1[i]))

for i in range(len(list_material_2)):
    list_pos2.append(nltk.pos_tag(list_token_2[i]))

st = LancasterStemmer()

#print (pos)
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#cp = nltk.RegexpParser(grammar)
#result = cp.parse(pos)
#print (result)
#result.draw()
list1 = []
list2 = []
for j in range(len(list_pos1)):
        list1 = []
        for i in range(len(list_pos1[j])):
            if list_pos1[j][i][1] == 'NN':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJ':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJR':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNS' :
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNP':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNPS' :
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'POS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RB':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBR':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'VB':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos1[j][i][0]))
        #    if list_pos1[j][i][1] == 'VBP':
         #       list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos1[j][i][0]))
        list2.append(list1)

list3 = []

for j in range(len(list_pos2)):
        list1 = []
        for i in range(len(list_pos2[j])):
            if list_pos2[j][i][1] == 'NN':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJ':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJR':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJS':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNS' :
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNP':
               list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNPS' :
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'POS':
               list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RB':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBR':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBS':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'VB':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos2[j][i][0]))
            #if list_pos2[j][i][1] == 'VBP':
             #   list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos2[j][i][0]))
        list3.append(list1)

print("\n")
cprint ("The words from document 1\n",'blue' )
print(list2)
print("\n")
cprint ("The words from document 2\n" ,'blue')
print(list3)


list4 = []
count = 0
count1 = 0
count2 = 0
for i in range(len(list2)):
    list4 = set(list2[i])
    count1 = count1 + len(list4)
    list5 = []
    list6 = []
    length = 0
    m_length = 0
    for j in range(len(list3)):
        list5 = set(list3[j])
        list6 = list4 & list5
        length = len(list6)
        if length > m_length:
            m_length = length
    count = count + m_length
print("\n")
cprint("Count of the matched words : \n",'green')
cprint("Words matched in List 1 : ", 'yellow')
print(count1,"\n")
cprint("Words matched in List 2 :",'yellow')
print(count,"\n")
a = count / count1
#b = count /count2
b = a 
x = ((a+b)/2)*100

cprint("Percentage of Plagiarism : \n",'green')
print (x ,"% ")
