from tkinter import *
root=Tk()
root.title("Calculator")
result=0
temp1=None
sign=None

entry1=Entry(root,width=35,borderwidth=5)
entry1.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
entry1.bind("<Key>", lambda e: "break")
#add some button functions
def add_screen1():
    entry1.insert(len(entry1.get()),"1")
def add_screen2():
    entry1.insert(len(entry1.get()),"2")
def add_screen3():
    entry1.insert(len(entry1.get()),"3")
def add_screen4():
    entry1.insert(len(entry1.get()),"4")
def add_screen5():
    entry1.insert(len(entry1.get()),"5")
def add_screen6():
    entry1.insert(len(entry1.get()),"6")
def add_screen7():
    entry1.insert(len(entry1.get()),"7")
def add_screen8():
    entry1.insert(len(entry1.get()),"8")
def add_screen9():
    entry1.insert(len(entry1.get()),"9")
def add_screen0():
    entry1.insert(len(entry1.get()),"0")
def do_operation_to_sign(sign):
    global temp1
    if(sign!=None):
        if(len(entry1.get())==0):
            return
        elif(sign=="+"):
            temp1+=int(entry1.get())
            entry1.delete(0,END)
        elif(sign=="-"):
            temp1-=int(entry1.get())
            entry1.delete(0,END)
        elif(sign=="*"):
            temp1*=int(entry1.get())
            entry1.delete(0,END)
        elif(sign=="//"):
            temp1//=int(entry1.get())
            entry1.delete(0,END)
        elif(sign=="%"):
            temp1%=int(entry1.get())
            entry1.delete(0,END)

def add_operation():
    global result
    global sign
    global temp1
    if(sign!=None):
        do_operation_to_sign(sign)
        sign="+"
        return
    sign="+"
    if(len(entry1.get())!=0 and temp1==None):
        temp1=int(entry1.get())
        entry1.delete(0,END)
    elif(len(entry1.get())!=0):
        temp1+=int(entry1.get())
        entry1.delete(0,END)
    
def minus_operation():
    global result
    global sign
    global temp1
    if(len(entry1.get())==0):
        entry1.insert(0,"-")
        return
    if(sign!=None):
        do_operation_to_sign(sign)
        sign="-"
        return
    sign="-"
    if(len(entry1.get())!=0 and temp1==None):
        temp1=int(entry1.get())
        entry1.delete(0,END)
    elif(len(entry1.get())!=0):
        temp1-=int(entry1.get())
        entry1.delete(0,END)
 

def multiply_operation():
    global result
    global sign
    global temp1
    if(sign!=None):
        do_operation_to_sign(sign)
        sign="*"
        return
    sign="*"
    if(len(entry1.get())!=0 and temp1==None):
        temp1=int(entry1.get())
        entry1.delete(0,END)
    elif(len(entry1.get())!=0):
        temp1*=int(entry1.get())
        entry1.delete(0,END)

def divide_operation():

    global result
    global sign
    global temp1
    if(sign!=None):
        do_operation_to_sign(sign)
        sign="//"
        return
    sign="//"
    if(len(entry1.get())!=0 and temp1==None):
        temp1=int(entry1.get())
        entry1.delete(0,END)
    elif(len(entry1.get())!=0):
        temp1=temp1//int(entry1.get())
        entry1.delete(0,END)

def rem_operation():
    global result
    global sign
    global temp1
    if(sign!=None):
        do_operation_to_sign(sign)
        sign="%"
        return
    sign="%"
    if(len(entry1.get())!=0 and temp1==None):
        temp1=int(entry1.get())
        entry1.delete(0,END)
    elif(len(entry1.get())!=0):
        temp1%=int(entry1.get())
        entry1.delete(0,END)
def equal_operation():
    global sign,result,temp1
    if(sign=="+"):
        result=temp1+int(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,result)
        result=0
        temp1=None
        sign=None
    elif(sign=="-"):
        result=temp1-int(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,result)
        result=0
        temp1=None
        sign=None
    elif(sign=="*"):
        result=temp1*int(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,result)
        result=0
        temp1=None
        sign=None
    elif(sign=="//"):
        result=temp1//int(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,result)
        result=0
        temp1=None
        sign=None
    elif(sign=="%"):
        result=temp1%int(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,result)
        result=0
        temp1=None
        sign=None
def delete_last():
    entry1.delete(len(entry1.get())-1,len(entry1.get()))
def reset_operation():
    global result
    global sign
    global temp1
    result=0
    temp1=None
    sign=None
    entry1.delete(0,END)


button1=Button(root,text="1",padx=22,pady=10,command=add_screen1)
button2=Button(root,text="2",padx=22,pady=10,command=add_screen2)
button3=Button(root,text="3",padx=22,pady=10,command=add_screen3)
button4=Button(root,text="4",padx=22,pady=10,command=add_screen4)
button5=Button(root,text="5",padx=22,pady=10,command=add_screen5)
button6=Button(root,text="6",padx=22,pady=10,command=add_screen6)
button7=Button(root,text="7",padx=22,pady=10,command=add_screen7)
button8=Button(root,text="8",padx=22,pady=10,command=add_screen8)
button9=Button(root,text="9",padx=22,pady=10,command=add_screen9)
button0=Button(root,text="0",padx=22,pady=10,command=add_screen0)

button_plus=Button(root,text="+",padx=22,pady=10,command=add_operation) #operations are starting
button_minus=Button(root,text="-",padx=22,pady=10,command=minus_operation)
button_multip=Button(root,text="*",padx=22,pady=10,command=multiply_operation)
button_divide=Button(root,text="//",padx=22,pady=10,command=divide_operation)
button_rem=Button(root,text="%",padx=22,pady=10,command=rem_operation)
button_equal=Button(root,text="=",padx=22,pady=10,command=equal_operation)
button_delete_last=Button(root,text="C",padx=62,pady=10,command=delete_last)
button_reset=Button(root,text="reset",padx=90,pady=10,command=reset_operation)

button1.grid(row=2,column=0,pady=5)
button2.grid(row=2,column=1,pady=5)
button3.grid(row=2,column=2,pady=5)
button4.grid(row=3,column=0,pady=5)
button5.grid(row=3,column=1,pady=5)
button6.grid(row=3,column=2,pady=5)
button7.grid(row=4,column=0,pady=5)
button8.grid(row=4,column=1,pady=5)
button9.grid(row=4,column=2,pady=5)
button0.grid(row=5,column=0,pady=5)

button_plus.grid(row=5,column=1,pady=5)
button_minus.grid(row=5,column=2,pady=5)
button_multip.grid(row=6,column=0,pady=5)
button_divide.grid(row=6,column=1,pady=5)
button_rem.grid(row=6,column=2,pady=5)
button_equal.grid(row=7,column=0,pady=5)
button_delete_last.grid(row=7,column=1,columnspan=2,pady=5)
button_reset.grid(row=8,column=0,columnspan=3,pady=5)



root.mainloop()