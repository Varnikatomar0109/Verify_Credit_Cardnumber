card_number="5610591081018250"
odd_sum=0
even_sum=0
double_list=[]
number=list(card_number)
for (idx,val) in enumerate(number):#in this we have both idx and val beacouse we have to go through both value as well as idx and we put enumerate because we havt to loop also the idx 
    if idx % 2 != 0 :
        odd_sum += int(val)

    else: # this is for the even number
        double_list.append(int(val)*2)

#convert list into a string
double_string=""
for x in double_list:
    double_string += str(x)

#convert string into list 
double_list=list(double_string)
for x in double_list:
    even_sum += int(x)

net_sum= odd_sum+even_sum 
if net_sum % 10== 0:
    print("valid card number")

else:
    print("not a valid")

  






        

    


