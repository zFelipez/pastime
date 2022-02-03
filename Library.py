


#this code is only a practice 


from abc import ABC,abstractmethod


class Institution(ABC):
    
    social_analysis={
        'student':{
            'deal':10
        },
        'employee':{
            'deal':25
        },
        'normal':{
            'deal':5
        }
    }

    books= {'Book1':{
        'age': 13,
        'stars': 4,
        'price': 25
    },
    'Book2':{
        'age':18,
        'stars': 5,
        'price': 38
    },
    'Book3':{
        'age': 5,
        'stars':2,
        'price':10
    }
    }
    def __init__(self,name,age) -> None:
        self.name= name 
        self.age= age 
        self._number_of_people=0
        
    @property
    def number_of_people(self):
        return self._number_of_people
    
        
    @abstractmethod    
    def _pay(self):pass 
          


class Library(Institution):
    
    def __init__(self,name,age,social):
        Institution.__init__(self,name,age)
        self.social= social
        self.to_pay={}
        self.bill=0
        self.count= 1
    
    @classmethod
    def _listbooks(cls):
        
        x=[x for x in cls.books.keys()]
        return x
    
    @classmethod
    def _open_the_book(cls,name):
        opening=[]
        for x,y in cls.books.get(name).items():
            opening.append(x)
            
            opening.append(y)
        
        return opening
    
    @classmethod
    def _sc(cls):
        x = [x for x in cls.social_analysis.keys()]
        return x

    @classmethod
    def _social_price_decrease(cls,socialname):
        
        return cls.social_analysis.get(socialname).get('deal')
    
    def choice_and_pay(self,choice):
        
        verify = self._listbooks()
        
        try:
            if choice in verify:
                information= self._open_the_book(choice)
        
                return self._pay(information,choice)
            else:
                print('Book not found')
        except Exception:
             print('Try again')          
        
    
    def _pay(self,information,choice):
        try:
            sc = self._sc()
            
            def mapping(x):   
                if self.social == x:
        
                    percentage = self._social_price_decrease(x)
                
                    price= information[information.index('price') + 1] 
                
                    deal= price -  (price * percentage ) / 100 
                
                    return deal
            for x in map(mapping,sc):
                
                if not x == None:
                    
                    self.to_pay.update({choice:x})      
        
            total= sum([ x for x in self.to_pay.values()])
            self.bill += total
            
            print(f'Your bill  is {self.bill}')
            return self.bill

        except Exception:
            print('try again') 

    def pay(self,cash):
        try:
            if cash == self.bill or cash > self.bill:
                print(f'books paid your cashback is {cash - self.bill}')
            
                self.to_pay={}
            
                print('Nothing to pay ') if len(self.to_pay) == 0 else ... 
            
                return  
            print('Not enough money')              
        except Exception :
            print('Try again')           
        
    def __add__(self,other):
        self._number_of_people += self.count + other.count
        return  self._number_of_people


c= Library('felipe',15,'employee')
c.choice_and_pay('Book1')
c.choice_and_pay('Book2')
c.choice_and_pay('dnddnn')
c.choice_and_pay('Book1')
c.pay(114)
d=Library('joao',15,'normal')
s=Library('joana',45,'normal')

def count_the_many_users(*args,**kwargs):
    args= list(args)
    x1=0
    for x in args:
        try:
            x1+= x + (args[args.index(x) +1])
            
        except Exception as error:
            pass 
    return x1

print(count_the_many_users(c,d,s))


