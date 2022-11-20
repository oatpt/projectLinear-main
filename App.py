import numpy as np
from numpy.linalg import inv
from tkinter import *
import tkinter as tk
from turtle import width

class welcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        welcome = tk.Label(self, text =('welcome'),font=("Bangna New",60),fg='white',bg='gray19').place(x=285, y = 110) #gray19 #white
        to_en_de = tk.Label(self,font = ('Bangna New',20), text ='to Encrypting - Decrypting message',fg='white',bg='gray19').place(x=220, y = 210)

        Button = tk.Button(self,font = ('Bangna New',20), text="Let's start!",bg='white',fg='black',width=15, command=lambda: controller.show_frame(firstPage))
        Button.place(x=295, y=280)
        
class firstPage(tk.Frame):
    def __init__(self, parent, controller):
        def Exit():
            self.quit()

        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Button = tk.Button(self, text="en-code",bg='darkgrey' , font=("Bangna New", 40), command=lambda: controller.show_frame(encodePage))
        Button.place(x=300, y=50)

        Button = tk.Button(self, text="de-code",bg='darkgrey' , font=("Bangna New", 40), command=lambda: controller.show_frame(decodePage))
        Button.place(x=300, y=200)

        exit = tk.Button(self, font = ('Bangna New',30),text= 'EXIT',bg='Red' , width = 5, command = Exit)
        exit.place(x=350,y=350)

class encodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        private_key0 = StringVar()
        private_key1 = StringVar()
        private_key2 = StringVar()
        private_key3 = StringVar()
        private_key4 = StringVar()
        private_key5 = StringVar()
        private_key6 = StringVar()
        private_key7 = StringVar()
        private_key8 = StringVar()
        mode = StringVar()
        Result = StringVar()
        
        
        def Encode(key,message):
            for i in range(len(key)):
                try:
                    key[i]=int(key[i])
                except:
                    key[i]=0
            matrix_key = np.reshape(key, (3, 3))
            
            if checkinverse(matrix_key):
                return ""
        
            
                
                
            
            matrix_msg=[]
            print(matrix_msg)
            for i in message:
                matrix_msg.append(ord(i)-32)
            while len(matrix_msg)%3>0:
                matrix_msg.append(0)
            matrix_msg= np.reshape(matrix_msg,(3,len(matrix_msg)//3))
            print(matrix_msg)
            ans=np.matmul(matrix_key,matrix_msg)
            print(ans)
            print(len(ans))
            ans=np.reshape(ans,(1,len(ans)*len(ans[0])))
            word=""
            for i in ans[0]:
                word+=chr(i%95+32)
            return word
        
        def checkinverse(matrix_key):
            determinant = np.linalg.det(matrix_key)
            print(determinant)
            if determinant !=0 :
                error.pack(pady=20)
                error.pack_forget()
                return False
            else :
                error.pack()
                error.place(x=240,y=420)
                return True
        
        def checkinput():
            if private_key0.get()=="" or private_key1.get()=="" or private_key2.get()=="" or private_key3.get()=="" or private_key4.get()=="" or private_key5.get()=="" or private_key6.get()=="" or private_key7.get()=="" or private_key8.get()=="" or Text.get()=="" :
                inputerror.pack()
                inputerror.place(x=240,y=420)
                return True
            else :
                inputerror.pack(pady=20)
                inputerror.pack_forget()
                return False
                
        def Mode():
            if checkinput() :
                Result.set("")
                return
            private_key = [private_key0.get() ,private_key1.get(),private_key2.get(),private_key3.get(),private_key4.get(),private_key5.get(),private_key6.get(),private_key7.get(),private_key8.get()]  
            Result.set(Encode(private_key,Text.get()))
                
        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            private_key0.set("")
            private_key1.set("")
            private_key2.set("")
            private_key3.set("")
            private_key4.set("")
            private_key5.set("")
            private_key6.set("")
            private_key7.set("")
            private_key8.set("")
            mode.set("")
            Result.set("")
            inputerror.pack(pady=20)
            inputerror.pack_forget()
            error.pack()
            error.place(x=240,y=420)
        
        
        error=tk.Label(self,font=('Bangena new',12),text='This key cannot be inverse, please enter a new key.',fg='red',bg='gray19')
        error.place(x=240,y=420)
        error.pack(pady=20)
        error.pack_forget()

        inputerror=tk.Label(self,font=('Bangena new',12),text='MESSAGE or KEY you entered is incorrect',fg='red',bg='gray19')
        inputerror.place(x=240,y=420)
        inputerror.pack(pady=20)
        inputerror.pack_forget()

        Label(self,font=('Bangena new',20),text='En - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=150,y=320)
        
        # Label(self,font=('Bangena new',12),text='This key cannot be inverse, please enter a new key.',fg='red',bg='gray19').place(x=240,y=420)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 150,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=350, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=150, y = 190)
        Entry(self, font = ('Bangena new',20), textvariable = private_key0 ,fg='Black', bg ='CadetBlue1').place(x=250, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key1 ,fg='Black', bg ='CadetBlue1').place(x=305, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key2 ,fg='Black', bg ='CadetBlue1').place(x=360, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key3 ,fg='Black', bg ='CadetBlue1').place(x=415, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key4 ,fg='Black', bg ='CadetBlue1').place(x=470, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key5 ,fg='Black', bg ='CadetBlue1').place(x=525, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key6 ,fg='Black', bg ='CadetBlue1').place(x=580, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key7 ,fg='Black', bg ='CadetBlue1').place(x=635, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key8 ,fg='Black', bg ='CadetBlue1').place(x=690, y = 190,height=40,width = 50)
        
        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)


        Button(self, font = ('Bangena new',20), text = 'ENCODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=70, y=450)
        print("Key 0 : ",private_key0)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=640, y = 450)



class decodePage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        private_key0 = StringVar()
        private_key1 = StringVar()
        private_key2 = StringVar()
        private_key3 = StringVar()
        private_key4 = StringVar()
        private_key5 = StringVar()
        private_key6 = StringVar()
        private_key7 = StringVar()
        private_key8 = StringVar()
        mode = StringVar()
        Result = StringVar()

        def Decode(key,message):
            for i in range(len(key)):
                try:
                    key[i]=int(key[i])
                except:
                    key[i]=0
            matrix_key = np.reshape(key, (3, 3))
            determinant = np.linalg.det(matrix_key)
            cofactor = np.linalg.inv(matrix_key).T * determinant        
            matrix_key = cofactor.T
            print(matrix_key)
            
            
            temp=1
            while int((determinant*temp))%95!=1:
                temp+=1
                if temp >94:
                    break
            for i in range(len(matrix_key)) :
                for k in range(len(matrix_key[i])):
                    matrix_key[i][k]=matrix_key[i][k]*temp%95
            print(matrix_key)
            matrix_msg=[]
            for i in message:
                matrix_msg.append(ord(i)-32)
            while len(matrix_msg)%3>0:
                matrix_msg.append(0)
            matrix_msg= np.reshape(matrix_msg,(3,len(matrix_msg)//3))
            ans=np.matmul(matrix_key,matrix_msg)
            ans=np.reshape(ans,(1,len(ans)*len(ans[0])))
            print(matrix_msg)
            print(ans)
            
            word=""
            
            for i in ans[0]:
                i=int(round(i, 0))
                word+=chr(i%95+32)
                print(i%95+32)
            return word

        def checkinput():
            if private_key0.get()=="" or private_key1.get()=="" or private_key2.get()=="" or private_key3.get()=="" or private_key4.get()=="" or private_key5.get()=="" or private_key6.get()=="" or private_key7.get()=="" or private_key8.get()=="" or Text.get()=="" :
                inputerror.pack()
                inputerror.place(x=240,y=420)
                return True
            else :
                inputerror.pack(pady=20)
                inputerror.pack_forget()
                return False

        def Mode():
            if checkinput() :
                Result.set("")
                return
            private_key = [private_key0.get() ,private_key1.get(),private_key2.get(),private_key3.get(),private_key4.get(),private_key5.get(),private_key6.get(),private_key7.get(),private_key8.get()]  
            Result.set(Decode(private_key,Text.get()))

        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            private_key0.set("")
            private_key1.set("")
            private_key2.set("")
            private_key3.set("")
            private_key4.set("")
            private_key5.set("")
            private_key6.set("")
            private_key7.set("")
            private_key8.set("")
            mode.set("")
            Result.set("")

        inputerror=tk.Label(self,font=('Bangena new',12),text='MESSAGE or KEY you entered is incorrect',fg='red',bg='gray19')
        inputerror.place(x=240,y=420)
        inputerror.pack(pady=20)
        inputerror.pack_forget()
        Label(self,font=('Bangena new',20),text='De - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=150,y=320)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 150,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=350, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=150, y = 190)
        Entry(self, font = ('Bangena new',20), textvariable = private_key0 ,fg='Black', bg ='CadetBlue1').place(x=250, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key1 ,fg='Black', bg ='CadetBlue1').place(x=305, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key2 ,fg='Black', bg ='CadetBlue1').place(x=360, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key3 ,fg='Black', bg ='CadetBlue1').place(x=415, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key4 ,fg='Black', bg ='CadetBlue1').place(x=470, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key5 ,fg='Black', bg ='CadetBlue1').place(x=525, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key6 ,fg='Black', bg ='CadetBlue1').place(x=580, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key7 ,fg='Black', bg ='CadetBlue1').place(x=635, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key8 ,fg='Black', bg ='CadetBlue1').place(x=690, y = 190,height=40,width = 50)

        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)

        Button(self, font = ('Bangena new',20), text = 'DECODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=70, y=450)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=640, y = 450)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (welcomePage, firstPage, encodePage, decodePage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(welcomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(1000, 800)
# width= app.winfo_screenwidth()
# height= app.winfo_screenheight()
# app.geometry("%dx%d" % (width, height))
app.mainloop()