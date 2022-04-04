from threading import Thread, Lock

mutex = Lock()
mutex.acquire()
mutex.release()

CRASH_STATUS = None

def processData(data):
  return

#t = Thread(target = processData, args = (0,))
#t.start()

