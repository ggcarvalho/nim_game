
def remove(row,num,table):
    if table[row-1]>=num:
        table[row-1]-=num
    return table

def print_table(table):
    for i in range(len(table)):
        print(str(i+1)+'   '+(' '*(4-i))+(' O'*table[i])+(' '*(5-i))+'\n')

def change_player(turn):
    if turn%2==0:
        print('Player 1\n')
    else:
        print('Player 2\n')

def check(table):
    while True:
        try:
            num=int(input('Number of pieces to remove: '))
            row=int(input('Select a row to remove from(1-'+str(len(table))+'): '))
        except ValueError:
            print('\n'+'#'*21)
            print('# Error! Try again! #')
            print('#'*21+'\n')
            continue
        else:
            return num,row
            break

def select(table):
    while True:
        num,row=check(table)
        if not (row in range(1,len(table)+1)) or not (num>0 and num<=table[row-1]):
            print('\n'+'#'*53)
            print('# Invalid row or invalid amount o pieces to remove! #')
            print('#'*53+'\n')
            print_table(table)
            continue
        else:
            break
    return num,row

def play(table):
    s=sum(table)
    print('\n')
    print_table(table)
    turn=0
    while s>0:
        change_player(turn)
        num,row=select(table)
        print('\n')
        table=remove(row,num,table)
        s=sum(table)
        print_table(table)
        turn+=1
        if s==0:
            print('\n####################')
            change_player(turn-1)
            print('You lose!\n####################')

def reset_table(n):
    return [(i+1) for i in range(n)]

def main():
    table=reset_table(5)
    play_again=True
    while play_again:
        play(table)
        again=input('\nDo you want to play it again? (y/n) ')
        if again=='y':
            table=reset_table(5)
            play(table)
        else:
            print('\nThank you for playing! See you soon!\n')
            play_again=False

if __name__ == '__main__':
    main()
