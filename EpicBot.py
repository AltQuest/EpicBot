#!/usr/bin/python
#EpicBot in development by @bitcoinjake09 7/10/2019
from steem import Steem
from beem.steem import Steem
from beem.nodelist import NodeList
from steem.transactionbuilder import TransactionBuilder
from steembase import operations
import time

nodes = ['https://steemd.minnowsupportproject.org/']

PK = 'YOUR KEY GOES HERE'
accountname = 'bitcoinjake09' #replace my name with your STEEM name


betAmount = 1
AboveOrBelow = 'Above' # can be 'Above' or 'Below'
OverUnderNum = 6

#betAmount = 1
#AboveOrBelow = 'Below' # can be 'Above' or 'Below'
#OverUnderNum = 95

ops = [
	{
		'from': accountname,
		'to': 'epicdice',
		'amount': str(betAmount) + ' STEEM',
		'memo': str(AboveOrBelow) + ' ' + str(OverUnderNum)
	}
]
operations = [operations.Transfer(**x) for x in ops]


s = Steem(node = nodes, keys=[PK])

count = 1 #do not modify - is part of loop + display
sleepAmt = 4
while(count <= 1001):
	tb = TransactionBuilder()
	tb.appendOps(operations)
	tb.appendSigner(accountname, "active")
	tb.sign()
	tb.broadcast()
	print ('bet # ' + str(count))
	count = count + 1
	time.sleep(sleepAmt)
