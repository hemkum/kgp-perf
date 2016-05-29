from tornado import ioloop, httpclient
import functools
i = 0
donefile = open('done.txt', 'a+')

def handle_request(rollno, response):
  global i
  global donefile
  print(i, rollno)
  i -= 1
  if i == 0:
    ioloop.IOLoop.instance().stop()
  if response.code != 200
    return
  dep = rollno[2:4]
  with open(dep+'/'+rollno+'.html', 'w') as f:
    f.write(str(response.body))
  donefile.write("%s\n" % rollno)

http_client = httpclient.AsyncHTTPClient()
donestring = donefile.read()
for url in open('urls.txt'):
  if url.strip() in donestring:
    continue
  i += 1
  cb = functools.partial(handle_request, url.strip())
  url = 'https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno='+url.strip()
  http_client.fetch(url.strip(), cb, method='GET')
ioloop.IOLoop.instance().start()