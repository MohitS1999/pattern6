#6
##             *
##            **
##           *** 
##          ****        
##         *****      
def pattern(n):
    for i in range(n):
        for j in range(n):
             print('*',end='') if i+j>=n-1 else print(' ',end='')
        print()
pattern(5)
