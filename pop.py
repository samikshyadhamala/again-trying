#largest no in a list
def larg_no(list_no):  
 a=-1
 for value in list_no:
    if value>a:
        larg=value
        a=value
 print(f'the largest no is {a}')   
list1=[1,2,33,444,66,12,99]
larg_no(list1)
            
        
    