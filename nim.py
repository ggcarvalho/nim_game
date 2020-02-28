
def remove(row,num,table):
    if table[row-1]>=num:
        table[row-1]-=num
    return table

def print_table(table):
    for i in range(len(table)):
        print(str(i+1)+(' #'*table[i])+'\n')

def change_player(turn):
    if turn%2==0:
        print('Player 1')
    else:
        print('Player 2')


table=[1,2,3,4,5]

s=sum(table)
print('\n')
print_table(table)
turn=0
while s>0:
    change_player(turn)
    row=int(input('select a row (1-5):'))
    num=int(input('number of pieces to remove:'))
    print('\n')
    table=remove(row,num,table)
    s=sum(table)
    print_table(table)
    turn+=1
    if s==0:
        print('\n####################')
        change_player(turn-1)
        print('You lose!\n####################')


