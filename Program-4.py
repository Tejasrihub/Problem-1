# python program to count the frequency of elements in a list using a dictionary.
def CountFrequency (my_list);
# Creating an empty dictionary
freq = {}
for item in my_list:
  if (item in freq):
    freq[item] +=1
    else:
      freq[item] =1
      for key , value in freq.item():
        print ("% d :  % d" %(key, value))
        # Driver function 
        if__name__=="__main__":
          my_list = [1,2,3,4,5,6,7,8,9]
            countFrequency(my_list)
