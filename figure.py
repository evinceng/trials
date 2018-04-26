# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 09:39:46 2018

@author: evin
"""
import Tkinter as Tk

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk.Tk()
var = Tk.DoubleVar()
scale = Tk.Scale( root, variable = var )
scale.pack(anchor=Tk.CENTER)

button = Tk.Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=Tk.CENTER)

label = Tk.Label(root)
label.pack()

root.mainloop()

#import tkinter as tk
#from tkinter import ttk
#
#
#class SampleApp(tk.Tk):
#
#    def __init__(self, *args, **kwargs):
#        tk.Tk.__init__(self, *args, **kwargs)
#        self.button = ttk.Button(text="start", command=self.start)
#        self.button.pack()
#        self.progress = ttk.Progressbar(self, orient="horizontal",
#                                        length=200, mode="determinate")
#        self.progress.pack()
#
#        self.bytes = 0
#        self.maxbytes = 0
#
#    def start(self):
#        self.progress["value"] = 0
#        self.maxbytes = 50000
#        self.progress["maximum"] = 50000
#        self.read_bytes()
#
#    def read_bytes(self):
#        '''simulate reading 500 bytes; update progress bar'''
#        self.bytes += 500
#        self.progress["value"] = self.bytes
#        if self.bytes < self.maxbytes:
#            # read more bytes after 100 ms
#            self.after(100, self.read_bytes) # this should be sth that can after be called some gui
#
#app = SampleApp()
#app.mainloop()
    
    
#import sys
#from subprocess import Popen
#from Tkinter import Tk, StringVar
#import ttk
#
#START, STOP = "start", "stop"
#
## just some arbitrary command for demonstration
#cmd = [sys.executable, '-c', """import sys, time
#print("!")
#sys.stdout.flush()
#for i in range(30):
#    sys.stdout.write("%d " % i)
#    sys.stdout.flush()
#    time.sleep(.05)
#"""]
#
#
#class App(object):
#    def __init__(self, parent):
#        self.process = None
#        self.after = parent.after
#        self.command = START
#        self.button_text = None
#        self.progressbar = None
#        self.make_widgets(parent)
#
#    def make_widgets(self, parent):
#        parent = ttk.Frame(parent, padding="3 3 3 3")
#        parent.pack()
#        self.progressbar = ttk.Progressbar(parent, length=200,
#                                           mode='indeterminate')
#        self.progressbar.pack()
#        self.button_text = StringVar()
#        self.button_text.set(self.command)
#        button = ttk.Button(parent, textvariable=self.button_text,
#                            command=self.toggle)
#        button.pack()
#        button.focus()
#
#    def toggle(self, event_unused=None):
#        if self.command is START:
#            self.progressbar.start()
#            try:
#                self.start_process()
#            except:
#                self.progressbar.stop()
#                raise
#            self.command = STOP
#            self.button_text.set(self.command)
#        else:
#            assert self.command is STOP
#            self.stop_process()
#
#    def stop(self):
#        self.progressbar.stop()
#        self.command = START
#        self.button_text.set(self.command)
#
#    def start_process(self):
#        self.stop_process()
#        self.process = Popen(cmd)
#
#        def poller():
#            if self.process is not None and self.process.poll() is None:
#                # process is still running
#                self.after(delay, poller)  # continue polling
#            else:
#                self.stop()
#        delay = 100  # milliseconds
#        self.after(delay, poller)
#
#    def stop_process(self):
#        if self.process is not None and self.process.poll() is None:
#            self.process.terminate()
#            # kill process in a couple of seconds if it is not terminated
#            self.after(2000, kill_process, self.process)
#        self.process = None
#
#
#def kill_process(process):
#    if process is not None and process.poll() is None:
#        process.kill()
#        process.wait()
#
#
#if __name__ == "__main__":
#    root = Tk()
#    app = App(root)
#
#    def shutdown():
#        app.stop_process()
#        root.destroy()
#
#    root.protocol("WM_DELETE_WINDOW", shutdown)
#    root.bind('<Return>', app.toggle)
#    root.mainloop()


#from Tkinter import *
#
#class StatusBar(Frame):
#
#    def __init__(self, master):
#        Frame.__init__(self, master)
#        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
#        self.label.pack(fill=X)
#
#    def set(self, format, *args):
#        self.label.config(text=format % args)
#        self.label.update_idletasks()
#
#    def clear(self):
#        self.label.config(text="")
#        self.label.update_idletasks()
#
#
#if __name__ == "__main__":
#
#    root = Tk()
#
#    Frame(root, width=400, height=200).pack()
#    status = StatusBar(root)
#    status.pack(side=BOTTOM, fill=X)
#
#    root.update()
#
#    status.set("Connecting...")
#    root.after(1000)
#    status.set("Connected, logging in...")
#    root.after(1500)
#    status.set("Login accepted...")
#    root.after(2000)
#    status.clear()
#
#    root.mainloop()
    
##Simple Chart Application  
#from pylab import show, arange,sin,plot,pi  
##set x and y values  
#x=arange(0.0,2.0,0.01)  
#y=sin(2*pi*x)  
#plot(x,y)  
##display function  
#show()  

#import Tkinter as tk
#
#counter = 0 
#def counter_label(label):
#  counter = 0
#  def count():
#    global counter
#    counter += 1
#    label.config(text=str(counter))
#    label.after(1000, count)
#  count()
# 
# 
#root = tk.Tk()
#root.title("Counting Seconds")
#label = tk.Label(root, fg="dark green")
#label.pack()
#counter_label(label)
#button = tk.Button(root, text='Stop', width=25, command=root.destroy)
#button.pack()
#root.mainloop()