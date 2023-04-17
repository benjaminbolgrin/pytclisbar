# pytclisbar
## A threaded CLI status bar written in Python.
### Usage:

from pytclisbar import StatusBar

statusBarHeadline: str = 'Loading'
totalIterations: int = 10_000

statusBar: StatusBar = StatusBar(statusBarHeadline, totalIterations)


statusBar.start()


for i in range(0, 10000):


  statusBar.setCurrentIteration(i+1)



statusBar.join()
