#!/usr/bin/env python 

import sys
import utils
import spider_shengpingfu
from game import Game
import zc
from datetime import datetime
import notifier

#game: hostname, guestname, leaguename, starttime, concede1, concede2, sp ...
def main():
    debug = False
    if len(sys.argv) == 2 and sys.argv[1] == 'DEBUG':
        debug = True
    games = spider_shengpingfu.spide(debug)
    compute_profits(games)

def compute_profits(games):
    print "----JOB BEGIN --- %s ---" % datetime.now()
    games = [Game(item[0], item[1], item[2], item[3], item[4], item[5], item[6:9], item[9:12]) for item in games]
    for i in range(len(games)):
        for j in range(i+1, len(games))
            catched = []
            g1, g2 = games[i], games[j]
	    print "----new try --- %s ---" % datetime.now()
	    print str(g1)
	    print str(g2)
            for sp_arra in (g1.sp_arr1, g1.sp_arr2):
	        for sp_arrb in (g2.sp_arr1, g2.sp_arr2):
	            profits = zc.get_topN_profit_2s1(sp_arra, sp_arrb, 10, buy_max=7, buy_min=7)
		    for p in profits:
		        print str(p)
		    if len(profits) > 0:
		        c = "%s - %s\t%s\t%s - %s\t%s -- %s" % (g1.hostname,str(g1.guestname).decode('utf-8'), str(sp_arra).decode('utf-8'), str(g2.hostname).decode('utf-8'), str(g2.guestname).decode('utf-8'), str(sp_arrb), ' ** '.join([str(profit) for profit in profits]))
		        catched.append(c)
            if len(catched) > 0:
	        notifier.notify(catched)
	        print 'Mail send, len(catched): %d' % len(catched)
	        return
	    catched = []
    print "----JOB END --- %s ---" % datetime.now()

if __name__ == '__main__':
    main()
