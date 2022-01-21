print('please enter card')
print('''please select language
                    1--> english
                    2--> telugu
                    3--> hindi\n''')
a=int(input())
if a==1:
    print('''please select options
                    1-->withdraw
                    2-->deposit
                    3-->mini statement''')
    b=int(input())                            
    if b==1:
        print('enter money')
        c=int(input())
        print('please wait your transaction is being processed')
        print('please collect cash{}'.format(c))
        print('thaks for using atm')
    