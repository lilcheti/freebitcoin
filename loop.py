k=5

level = 0
netwin=10
bet=10
loss=0
for i in range(20):
    print('level: '+str(level))
    print('bet: '+str(bet))
    print('loss: '+str(loss))
    print('netwin: '+str(netwin))
    level +=1
    loss += bet
    netwin += k
    bet=loss+netwin