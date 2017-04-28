import win32api
import win32gui
import win32con

class ClickButton():
    #点击屏幕某一位置，pos是元素坐标位置，需要用get_curpos先获取
    def click(self,handle, pos):
        client_pos = win32gui.ScreenToClient(handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    #获取当前窗口句柄
    def get_win_handle(self,pos):
        return win32gui.WindowFromPoint(pos)
    #获取当前鼠标坐标位置
    def get_curpos(self):
        return win32gui.GetCursorPos()

