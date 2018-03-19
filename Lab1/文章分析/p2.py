###############################################################################################
# Date:20180305
# Name:p2.py
# StudentID:A1035501
# Author:孫茂勛
# Note:Lab1
###############################################################################################
import matplotlib.pyplot as plt
#make a string contain marks we can ingore 
mark_set = "\"\',.?!*[]#:-" #without space


if __name__ == '__main__':
    count = dict()
    document_space = []
    filename = input("please input the filename(must in the same workspace):")
    try:
        with open(filename+".txt","r",encoding="utf8") as file:
            for each_row in file:
                for iterator in mark_set:
                    each_row = each_row.replace(iterator,'')
                each_row = each_row.replace('\n','') #replace space
                #print(i)
                
                document_space = each_row.split() #split word 
                #print(document_space)
                for i in document_space:
                    count[i] = count.get(i,0) + 1 #cal frequency of every word in each row
            #print(count)
                    
            #sort dict by value
            sorted_count = sorted(count.items(),key = lambda d:d[1],reverse = True)
            for i in range(10):
                print(sorted_count[i][0],sorted_count[i][1])
            #plot
            plt.title("Word Count",color="r")
            plt.xlabel("Word",color="r")
            plt.ylabel("Count",color="r")
            #in matplotlib,the output will be sorted by category, hence alphabetically...this is a bug
            plt.bar([sorted_count[i][0] for i in range(10)], [sorted_count[i][1] for i in range(10)],color = 'r')

            plt.show()
    except:
        print("Oops!some error happen...")
        print("Closing..")
        exit()
    
