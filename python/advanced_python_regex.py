import csv
import re

def read_data(filename):
    with open(filename,'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()
        print(headers)

        name = []
        degree = []
        title = []
        email = []
        for row in reader:
            name.append(row[0])
            degree.append(row[1].lower().replace('.',''))
            title.append(row[2].lower())
            email.append(row[3])


        # Question 1
        all_degrees = ' '.join(degree).split()
        degree_dict = {}
        for degree in all_degrees:
            if degree not in degree_dict.keys():
                degree_dict[degree] = 1
            else:
                degree_dict[degree]+=1
        print(degree_dict)

        # Question 2
        titles_list = []
        for i_title in title:
            titles_list.append(re.search('[\w\s]*professor',i_title).group())

        title_dict={}
        for i_title in titles_list:
            if i_title not in title_dict.keys():
                title_dict[i_title]= 1
            else:
                title_dict[i_title] += 1
        print(title_dict)

        # Question 3
        print(email)

        # Question 4
        EmailList = []
        for iEmail in email:
            x = (re.search('@(.*)',iEmail).group(1))
            if x not in EmailList:
                EmailList.append(x)
        print(EmailList, len(EmailList))

        # Question 5
        with open('emails.csv', 'wb') as file:
            for iEmail in email:
                file.write(iEmail)
                file.write('\n')

        # Question 6
        FirstName =[]
        LastName = []
        Q6_Dict = {}
        for iName in range(len(name)):
            x = (name[iName].split(' '))
            FirstName.append(x[0])
            LastName.append(x[-1])
            Q6_Dict[x[-1]] = [all_degrees[iName],titles_list[iName],email[iName]]
            print(Q6_Dict)

        key = sorted(Q6_Dict.iterkeys())
        for i_Sort in range(3):
            print (key[i_Sort],Q6_Dict[key[i_Sort]])


        # Question 7
        FirstName =[]
        LastName = []
        Q7_Dict = {}
        for iName in range(len(name)):
            x = (name[iName].split(' '))
            FirstName.append(x[0])
            LastName.append(x[-1])
            Q7_Dict[(x[0],x[-1])] = [all_degrees[iName],titles_list[iName],email[iName]]
            print(Q7_Dict)

        key = sorted(Q7_Dict.iterkeys())
        for i_Sort in range(3):
            print (key[i_Sort],Q7_Dict[key[i_Sort]])

        # Question 8
        def getKey(item):
            return item[1]

        key = sorted(Q7_Dict.iterkeys(), key = getKey)
        for i_Sort in range(3):
            print (key[i_Sort],Q7_Dict[key[i_Sort]])

read_data('faculty.csv')