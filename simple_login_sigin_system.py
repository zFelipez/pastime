

import random
import string

def main():
    bank_of_data = (['adm','adm','adm'],)
    numeration = 0
    while True:

        def ask():
            question_ = input(
                'Are you going to: 1 (sign in), 2(log in), 3 (change password) 4(Delete User),  5(Exit), (Type a number please) ')
            return question_
        print()
        question= ask()
        
        numeration += 1


        if question.isnumeric() and question == '1' :

            sign_username= input('Type a username ')

            sign_password= input('Type a password or type 2 for the (recommendation) ')

            if sign_username == '' or sign_password == '':
                print('User ivalid !!!')
                continue

            if sign_password == '2':

                password = ''.join(random.choice(string.printable) for i in range(6))
                sign_password = password
                print()
                print(f'Your password is {sign_password},KEEP IT!!! ')


            for value in bank_of_data:
                if  sign_username in value[0] :
                    print()
                    print('Please return, this User has already been created ')
                    print()
                    go_back = input('Return? Yes or not ')

                    if 'yes' in go_back:

                        return

                    else:
                         enter= input('Enter ')
                         return
            if  sign_password == sign_username:
                print('The password cant be the same as  {0}'.format(sign_username))
                continue
            if len(sign_password) < 6 or len(sign_username) < 6 :
                print()
                print('Your password or username must be at least 6 characters ')
                continue
            else:

                print('User and Password successfully created!! ')
                bank_of_data= list(bank_of_data)
                bank_of_data.append([sign_username])
                bank_of_data[-1].append(sign_password)
                bank_of_data[-1].append({'Numbering':numeration})
                bank_of_data= tuple(bank_of_data)

                continue


        if question.isnumeric() and question == '2':
            log_in_username=  input('Type your Username,please ')
            log_in_password= input('Type your password, please ')

            for index,value in enumerate(bank_of_data,0):


                    if log_in_username not in value[0] and log_in_password not in value[1]:
                        if  bank_of_data[index] is bank_of_data[-1]:
                            print('This user has not been created')
                            go_back = input('Return? Yes or not ')
                            print()
                            if 'yes' in go_back:

                                break
                            else:
                                return
                        else:
                            continue

                    elif log_in_username in value[0] and log_in_password  in value[1]:

                        print()

                        print('Succefully logged!!! ')
                        print()
                        enter = input('Press Enter ')

                    else:
                        print('Oops, something is wrong, do it over ')

                        continue

        if question.isnumeric() and question == '3':
              user_confirmation= input('Confirm your User ')
              print()
              password_confirmation= input('Confirm your current password ' )
              print()
              new_password= input('Type your new password ')
              print()
              new_password_confirmation= input('Confirm your new password ')
              bank_of_data = list(bank_of_data)
              for index, value  in enumerate(bank_of_data,0):

                  if user_confirmation in value[0] and password_confirmation in value[1]\
                          and new_password == new_password_confirmation:


                          del value[1]
                          value.insert(1,new_password_confirmation)
                          print()
                          bank_of_data= tuple(bank_of_data)
                          print('New password created!! ')


        if question.isnumeric() and question == '4':
                delete_user = input('What is your username? ')
                print()
                confirm_password= input('Type your password to confirm the deletion ')
                bank_of_data = list(bank_of_data)

                for index,value in enumerate(bank_of_data,0):


                    if delete_user in value[0] and confirm_password in value[1] :


                        bank_of_data.pop(index)

                        bank_of_data = tuple(bank_of_data)

                        print()
                        print('User Deleted ')
                    else:
                        print('This user couldnt be found !!Type again,please ')
                        return
        if question.isnumeric() and question == '5':
            break

main()