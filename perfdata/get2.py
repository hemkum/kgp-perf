from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import urllib2

concurrent = 200
i = 0
def doWork():
    while True:
        url = q.get()
        status, body, url = getStatus(url)
        doSomethingWithResult(status, body, url)
        q.task_done()

def getStatus(ourl):
    # try:
    res = urllib2.urlopen(ourl)
    return res.code, res.read(), ourl
    # except:
        # return "error", ourl

def doSomethingWithResult(status, body, url):
    global i
    rollno = url[-9:]
    dep = rollno[2:4]
    with open(dep+'/'+rollno+'.html', 'w') as f:
        f.write((body))
    i = i+1
    print status, i, body[:10]

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in open('urls.txt'):
        q.put('https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno='+url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)