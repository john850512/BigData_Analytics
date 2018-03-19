###############################################################################################
# Date:20180305
# Name:p2.py
# StudentID:A1035501
# Author:孫茂勛
# Note:Lab1
###############################################################################################
import matplotlib.pyplot as plt

if __name__ == '__main__':
    count = dict()
    filename = input("please input the filename(must in the same workspace):")
    try:
        with open(filename+".txt","r") as f:
            document_space = f.readlines()
    except:
        print("cant open the file:",filename,".txt")
        print("closing..")
        quit()
        
    document_space = [i.strip() for i in document_space]
    for i in document_space:
        count[i] = count.get(i,0) + 1 
    print(count)

    #plot
    plt.title("Word Count",color="r")
    plt.xlabel("Word",color="r")
    plt.ylabel("Count",color="r")
    
    #Since Python 3.x,dict.keys() will return a dict_keys() object,and it cant be indexed
    #so you can inedx by convert the tpye to list,
    #e.x. plot.bar(list(dict.keys()),.....)
    #but it just can work when keys is intger or float,it keys is string type
    #you have to give it size to be indexed,an then use xticks() assign its name
    
    plt.bar(range(len(count)), count.values(),color = 'r')
    plt.xticks(range(len(count)),list(count.keys()))
    plt.legend()
    plt.show()
