import ctypes
import mainwindow
from mainwindow import MainWindow

ctypes.windll.shcore.SetProcessDpiAwareness(1)



if __name__ == "__main__":
    app = mainwindow.MainWindow()
    app.mainloop()
