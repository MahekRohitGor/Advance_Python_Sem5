# * * * * *
# *       *
# * * * * *
# *       *
# *       * 
# *       *

row = 10
col = 5

for i in range(row):
        for j in range(col):
            if i == 0 or j == 0 or j == col - 1 or i == 4:
                print('*', end=' ')  # Print * in A pattern
            else:
                print(' ', end=' ') # Print spaces
        print()
