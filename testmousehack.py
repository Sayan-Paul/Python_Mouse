import win32api, win32con,time
inc=1
while(1):
    x,y= win32api.GetCursorPos()
    #arrow keys
    l= int(win32api.GetKeyState(37))
    r= int(win32api.GetKeyState(39))
    u= int(win32api.GetKeyState(38))
    d= int(win32api.GetKeyState(40))
    h= int(win32api.GetKeyState(72))#left click
    j= int(win32api.GetKeyState(74))#right click
    e= int(win32api.GetKeyState(69))#Exit
    if not l in [0,1]:
        x-=1
        win32api.SetCursorPos([x,y])
        time.sleep(0.003)
    if not r in [0,1]:
        x+=1
        win32api.SetCursorPos([x,y])
        time.sleep(0.003)
    if not u in [0,1]:
        y-=1
        win32api.SetCursorPos([x,y])
        time.sleep(0.003)
    if not d in [0,1]:
        y+=1
        win32api.SetCursorPos([x,y])
        time.sleep(0.003)
    if not h in [0,1]:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        time.sleep(0.1)
    if not j in [0,1]:
        #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        #Hwin32api.mouse_event(win32con.MOUSEEVENTF_RIGHTTUP,x,y,0,0)
        time.sleep(0.1)
    if not e in [0,1]:
        break
    
