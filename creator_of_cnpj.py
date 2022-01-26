


import random

def generate():
    first_number= random.randint(0,9)
    second_number=random.randint(0,9)
    second_block= random.randint(100,999)
    third_block= random.randint(100,999)
    fourth_block= '0001'
    init= f'{first_number}{second_number}{second_block}{third_block}{fourth_block}'
    return init

g= generate()

def validator(cnpj):   
    
    
    try:
        def symbols(number):
            sep=[number[i-3:i] for i in range(2,9,3)]
            dot='.'.join(sep)

            sep2= f'/{number[8:12]}-{number[12:]}'

            concatenation= f'{number[0:2]}{dot}{sep2}'
            return concatenation
    
        import re 
        refactor=re.sub(r'[./-]','',cnpj)
    
        def calculation(range1,range2,start,finish):  
        
            n=[f for f in range(range1,range2,-1)]
        
            first_five= list(refactor)[start:finish]
        
            first_combination=zip(first_five,n)
        
            duo= [x for x in first_combination]
            to_sum= [int(x) * y for x,y in duo]
            return to_sum
    
        to_sum1=sum(calculation(5,1,0,4))
        to_sum2=sum(calculation(9,1,4,12))
    
        first_digit=11 -((to_sum1+ to_sum2) % 11)
    
        if first_digit > 9:
            first_digit= 0
    
    
        to_sum3=sum(calculation(6,1,0,5))
    
        to_sum4=calculation(9,1,5,12)
    
        to_sum4.append(first_digit * 2)
        to_sum4=sum(to_sum4)
    
        second_digit= 11 -((to_sum3 + to_sum4) % 11)
    
        if second_digit > 9:
            second_digit= 0

    
        new_cnpj= f'{refactor[0:-2]}01{first_digit}{second_digit}'
       
         
        new_cnpj=symbols(new_cnpj)
        return new_cnpj
       
        
    except Exception as error:
        print(error)


print(validator(g))    