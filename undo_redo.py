
def to_do():
    tasks=dict()
    task_redo_and_undo=[]
    question= lambda : input('New task(1), acess a task(2), Undo(3) or Redo(4) tasks?')
    def New_task():
        question_= lambda : input(f'Whats the task{len(tasks)+1}')
       
        q= question_()
        try:
            
            tasks[f'Task {len(tasks)+1}']=q
            
            return 'New task added'
        
        except Exception as error:
             return 'Unable to add it'  
    
    def access_task():
        question__= lambda : input('Name of the task to be accessed')
        q= question__()
        try: 
            
            if q in tasks.keys():
                return f'{q}:{tasks.get(q)} and others {len(tasks)- 1}'
            else:
                return 'Unable to find it'
            
        
        except Exception:
           
            return 'Unable to find it '
    
    def undo():
        def verify(x):
            last_key= list(tasks.keys())[-1]
            if x== last_key :
                task_redo_and_undo.append([last_key])
                task_redo_and_undo[-1].append(list(tasks.values())[-1])
                tasks.pop(x)
                return x
            
        try:
            
            for i in filter(verify,tasks.keys()):
                print(i,'Undone')
        
        except Exception as error: #still to handle this error, thats why i will pass it
            pass
    
    def redo():
        tasks.update({task_redo_and_undo[-1][0]:task_redo_and_undo[-1][1]})
        del(task_redo_and_undo[-1])
        return 'Redone'


    
    while True:
        answer = question()
        
        print(New_task()) if answer == '1' else ...
        
        
        print(access_task()) if answer == '2' else ...
        
        undo() if answer == '3' else ...
        
        print(redo()) if answer == '4' else ...
        
        if answer =='b':
            break
to_do()
