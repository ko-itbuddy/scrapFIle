import threading
from time import sleep, ctime

loops =[8,2]


class MyThread()





def loop(nloop, nsec):
    print ('start loop {} at: {}'.format(nloop, ctime()))
    sleep(nsec)
    print (' loop {} at:{}' .format(nloop,ctime()))


def test():

    print('starting at:'+ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()


    for i in nloops:
        threads[i].join()


    print('all Done at: {}'.format(ctime()))

if __name__ =='__main__':
    test()
