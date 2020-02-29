
def remove(row,num,table):
    if table[row-1]>=num:
        table[row-1]-=num
    return table

def print_table(table):
    for i in range(len(table)):
        print(str(i+1)+'   '+(' '*(4-i))+(' O'*table[i])+(' '*(5-i))+'\n')

def change_player(turn):
    if turn%2==0:
        print('Player 1')
    else:
        print('Player 2')

def select(table):
    while True:
        row=int(input('Select a row (1-'+str(len(table))+'): '))
        num=int(input('Number of pieces to remove: '))
        if not (row in range(1,len(table)+1)) or not (num>0 and num<=table[row-1]):
            print('\n'+'#'*53)
            print('# Invalid row or invalid amount o pieces to remove! #')
            print('#'*53+'\n')
            print_table(table)
            continue
        else:
            break
    return row,num

def main():
    table=[1,2,3,4,5]
    s=sum(table)
    print('\n')
    print_table(table)
    turn=0
    while s>0:
        change_player(turn)
        row,num=select(table)
        print('\n')
        table=remove(row,num,table)
        s=sum(table)
        print_table(table)
        turn+=1
        if s==0:
            print('\n####################')
            change_player(turn-1)
            print('You lose!\n####################')

if __name__ == '__main__':
    main()
