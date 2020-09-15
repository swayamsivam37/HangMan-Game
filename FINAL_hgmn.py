
from tkinter import *

def level5(root3):
    root3.destroy()
    from tkinter import messagebox
    root4 = Tk()
    root4.geometry("1920x1080")
    root4.title("HANGMAN GAME")
    Level_Label = Label(root4, text = "Level 5")
    root4.configure(background='#C8C0B8')
    Level_Label.place(x=750, y =27)
    #inserting image ------------------
    canvas = Canvas(width = 350, height =350 ,bg = 'white')
    canvas.place(x = 10, y = 10)
    photo3 = PhotoImage(file='IMG6.png')
    canvas.create_image(20,20,image=photo3,anchor=NW)
    #root4.mainloop()
    chance1level5(root4)
    

def chance1level5(root4):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 5")
    a = (curr.fetchone())
    conn.commit()
    conn.close()
    #print(a)
    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Winner Winner CHICKEN Dinner!!!!","Congratulations Champ")
        if(answer=="yes"):
            root4.destroy()

        else:
            root4.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root4.quit()
            chance2level5(root4)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root4, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root4,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root4, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root4)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root4, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root4, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,2)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root4.mainloop()


def chance2level5(root4):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 5")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Winner Winner CHICKEN Dinner!!!!","Congratulations Champ")
        if(answer=="yes"):
            root4.destroy()

        else:
            root4.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root4.quit()
            chance3level5(root4)
            
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root4, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root4,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root4, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root4)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root4, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root4, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,1)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root4.mainloop()



def chance3level5(root4):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 5")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Winner Winner CHICKEN Dinner!!!!","Congratulations Champ")
        if(answer=="yes"):
            root4.destroy()

        else:
            root4.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            rp = messagebox.askquestion("Wrong Answer","Game-OVER")
            if(rp == "yes"):
                root4.destroy()
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root4, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root4,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root4, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root4)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root4, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root4, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root4,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,0)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root4.mainloop()







def level4(root2):
    root2.destroy()
    from tkinter import messagebox
    root3 = Tk()
    root3.geometry("1920x1080")
    root3.title("HANGMAN GAME")
    root3.configure(background='#C8C0B8')
    Level_Label = Label(root3, text = "Level 4")
    Level_Label.place(x=750, y =27)
    #inserting image -----------
    canvas = Canvas(width = 350, height =350 ,bg = 'white')
    canvas.place(x = 10, y = 10)
    photo2 = PhotoImage(file='IMG5.png')
    canvas.create_image(20,20,image=photo2,anchor=NW)
    #root3.mainloop()
    chance1level4(root3)

def chance1level4(root3):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 4")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level5(root3)

        else:
            root3.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root3.quit()
            chance2level4(root3)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root3, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root3,width =10, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------
#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root3,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root3, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root3)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root3, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root3, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root3,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,2)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root3.mainloop()




def chance2level4(root3):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 4")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level5(root3)

        else:
            root3.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root3.quit()
            chance3level4(root3)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root3, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root3,width =10, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root3,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root3, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root3)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root3, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root3, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root3,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,1)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root3.mainloop()



def chance3level4(root3):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 4")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level5(root3)

        else:
            root3.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            rp = messagebox.askquestion("Wrong Answer","Game-OVER")
            if(rp == "yes"):
                root3.destroy()
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root3, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root3,width =10, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root3,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root3, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root3)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root3, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root3, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root3,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,0)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root3.mainloop()











def level3(root1):
    root1.destroy()
    from tkinter import messagebox
    root2 = Tk()
    root2.geometry("1920x1080")
    root2.title("HANGMAN GAME")
    root2.configure(background='#C8C0B8')
    Level_Label = Label(root2, text = "Level 3")
    Level_Label.place(x=750, y =27)
    #inserting image -----------
    canvas = Canvas(width = 350, height =350 ,bg = 'white')
    canvas.place(x = 10, y = 10)
    photo1 = PhotoImage(file='IMG4.png')
    canvas.create_image(20,20,image=photo1,anchor=NW)
    #root2.mainloop()
    chance1level3(root2)



def chance1level3(root2):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 3")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level4(root2)

        else:
            root2.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root2.quit()
            chance2level3(root2)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root2, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------
#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root2,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root2, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root2)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root2, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root2, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,2)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root2.mainloop()



def chance2level3(root2):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 3")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level4(root2)

        else:
            root2.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root2.quit()
            chance3level3(root2)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root2, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root2,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root2, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root2)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root2, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root2, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,1)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root2.mainloop()



def chance3level3(root2):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 3")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level4(root2)

        else:
            root2.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            rp = messagebox.askquestion("Wrong Answer","Game-OVER")
            if(rp == "yes"):
                root2.destroy()
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root2, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root2,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root2, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root2)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root2, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root2, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root2,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,0)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root2.mainloop()





def level2():
    from tkinter import messagebox
    root1 = Tk()
    root1.geometry("1920x1080")
    root1.title("HANGMAN GAME")
    root1.configure(background='#C8C0B8')
    Level_Label = Label(root1, text = "Level 2")
    Level_Label.place(x=750, y =27)
    #inserting image -----------
    canvas = Canvas(width = 350, height =350 ,bg = 'white')
    canvas.place(x = 10, y = 10)
    photo = PhotoImage(file='IMG3.png')
    canvas.create_image(20,20,image=photo,anchor=NW)
    chance1level2(root1)
    

#---------------------------------------------------------------------------------------------------------------
def chance1level2(root1):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 2")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level3(root1)

        else:
            root1.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root1.quit()
            chance2level2(root1)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root1, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root1,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root1, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root1)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root1, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root1, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,2)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root1.mainloop()
#----------------------------------------------------------------------------------------------------------------

def chance2level2(root1):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 2")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level3(root1)

        else:
            root1.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root1.quit()
            chance3level2(root1)
            #rp = messagebox.askquestion("Wrong Answer","Try Again!!!!!")
            #if(rp == "yes"):
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root1, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root1,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root1, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root1)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root1, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root1, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,1)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root1.mainloop()

#---------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------


def chance3level2(root1):
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 2")
    a = (curr.fetchone())
    conn.commit()
    conn.close()

    def prompt_user():
        from tkinter import messagebox 
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            level3(root1)

        else:
            root1.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            rp = messagebox.askquestion("Wrong Answer","Game-OVER")
            if(rp == "yes"):
                root1.destroy()
                
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)

    

#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root1, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root1,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root1, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root1)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root1, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)

#---------------------------------------
    counter_Label = Label(root1, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root1,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,0)


#------------------------------------
#--------------------------------------
    
#---------------------------------
    root1.mainloop()
#--------------------------------------------------------------------------------------------------------------
def chance1():
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 1")
    a = (curr.fetchone())
    conn.commit()
    conn.close()



    def prompt_user():
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            root.destroy()
            level2()
        else:
            root.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root.quit()
            chance2()
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)
#------------------------------------
#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    
#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])



#-----chances_counter-----------------

    counter_Label = Label(root, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,2)
#--------------------------------------
    

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)
#--------------------------------------



#---------------------------------------

    

#---------------------------------
    root.mainloop()


#------------------------------------------------------------------------------------------------------------

def chance2():
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 1")
    a = (curr.fetchone())
    conn.commit()
    conn.close()



    def prompt_user():
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            root.destroy()
            level2()
        else:
            root.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            root.quit()
            chance3()
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)
#------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------
    
#-----------------------

#inserting hint label----------------------
    hint_Label = Label(root, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])



#-----chances_counter-----------------

    counter_Label = Label(root, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,1)
#--------------------------------------
    

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)
#--------------------------------------



#---------------------------------------

    

#---------------------------------
    root.mainloop()


def chance3():
    conn = sqlite3.connect('database.db')

    curr = conn.cursor()

    curr.execute("SELECT * FROM answer WHERE photo_id = 1")
    a = (curr.fetchone())
    conn.commit()
    conn.close()


    #---------------------------------------


    def prompt_user():
        answer= messagebox.askquestion("Next LEVEL","Do yo want to go to the next LEVEL")
        if(answer=="yes"):
            root.destroy()
            level2()
        else:
            root.destroy()
        


    

    def print_user(s):
        print(s)
        if(s==a[2]):
            prompt_user()
        else:
            rp = messagebox.askquestion("Wrong Answer","Game-OVER")
            if(rp == "yes"):
                root.destroy()           
        
        
#taking userinput--------------------

    def get_user():
        global s
        s=""
        s=user_text.get()
        print_user(s)
#------------------------------------

#-------------------KEYBOARD--------------
    def take_input(data):
        #pass
        user_text.insert(END,str(data))
    frm=Frame(root,bg='#0B53A0',bd=6,relief=RIDGE)
    frm.place(x=400,y = 300)
    Alphabetpad="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    i=0
    btn=[]
    for j in range(1,8):
        for k in range(5):
            btn.append(Button(frm,width=4,height=1,font=('arial',17,'bold'),bd=4,text=Alphabetpad[i],command=partial(take_input,Alphabetpad[i])))
            btn[i].grid(row=j,column=k,pady=5,padx=15,sticky=W)
            i=i+1


#------------------------------------------------------------

#inserting hint label----------------------
    hint_Label = Label(root, text = "Hint ?")
    hint_Label.place(x=1100, y =27)
    hint_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    hint_text.place(x=1150, y =20)
    hint_text.insert(INSERT,a[1])
#--------------------------------------





#-----chances_counter-----------------

    counter_Label = Label(root, text = "Number of Guess Remaining: ")
    counter_Label.place(x=1000, y =310)
    counter_text = Text(root,width =8, height=1, padx= 10, pady=10,bd=3)
    counter_text.place(x=1170, y =300)
    counter_text.insert(INSERT,0)
#--------------------------------------
    

    

#--------enter by user(along with submit button)-----------
    ans_label = Label(root, text = "Enter Your Response Here:->")
    ans_label.place(x=590, y =170)
    user_text = Entry(root)
    user_text.place(x=750, y =170)

#----submitButton-----

    submit_button= Button(root, text="Submit Answer",command = get_user, height=1,width=20)
    submit_button.place(x=900, y =165)



    

#---------------------------------
    root.mainloop()
#---------------main_------------------------------
#---------------------------database---------------------------


import sqlite3
conn = sqlite3.connect('database.db')

curr = conn.cursor()

#curr.execute(""" CREATE TABLE answer (photo_id integer,hint text, ans text )""")
#curr.execute("INSERT INTO answer values(1,'Computer','HP')")
#curr.execute("INSERT INTO answer values(2,'Phone','MOTOROLA')")
#curr.execute("INSERT INTO answer values(3,'Music','SPOTIFY')")
#curr.execute("INSERT INTO answer values(4,'Peripheral','LOGITECH')")
#curr.execute("INSERT INTO answer values(5,'Games','PLAY STATION')")

#curr.execute("SELECT ans FROM answer WHERE photo_id = 3")
#a = (curr.fetchone())
conn.commit()
conn.close()





#--------------------------------------------------------------
from tkinter import messagebox
from functools import partial
root = Tk()
#root.wm_attributes('-fullscreen','true')
root.geometry("1920x1080")
root.configure(background='#C8C0B8')
root.title("HANGMAN GAME")
#inserting image -----------
canvas = Canvas(width = 350, height =350 ,bg = 'white')
canvas.place(x = 10, y = 10)
photo = PhotoImage(file='IMG1.png')
canvas.create_image(20,20,image=photo,anchor=NW)
Level_Label = Label(root, text = "Level 1")
Level_Label.place(x=750, y =27)

chance1()
