#!/usr/bin/env python
# coding: utf-8

# In[37]:


from tkinter import *
import time 


tk = Tk()


tk.title("DİJİTAL SAAT")

def counttime(time1 = ' '):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        
        clock.config(text=time2)
        clock.after(200, counttime)
        
clock = Label(tk, font=('Poppins', 50, 'bold'), bg="red", fg="white")
clock.pack(anchor= 'center')

counttime()
tk.mainloop()


# In[ ]:




