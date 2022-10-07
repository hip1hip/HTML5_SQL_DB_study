"""
Coding by 홍인표

Snail Algorithm
"""

## a = [ [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0] ]

a = [[0] * 6 for i in range(6)]

k = 26
c = 1
i = 1
j = 0
f = 5
# 새로운 변 수 추가
count = 0

while count < 6 :


    # 첫번째 Loop
    #


    for n in range (1,f+1) :
        k = k - 1
        j = j + c
        a[ i ] [ j ] = k


    f = f - 1

    #두번째 Loop
    #

    for n in range (1,f+1) :
        k= k - 1 
        i= i + c
        a[ i ] [ j ] = k

    #방향 전환 

    c = c * -1

    count = count + 1 

# 출력 루틴 시작

p= 6

print ( )
print ( )

for x in range ( 1 , p ) :

    for y in range ( 1 , p ) :

        print ( "%4d" % a [ x ] [ y ], end="" )

    print()
    print()

# End of coding 
















