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


read_data('faculty.csv')