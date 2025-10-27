from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # database obj create krenge
        self.dbo = Database()
        self.apio = API() # API class ka object


        self.root = Tk()  #gui ko load krega
        self.root.title("NLPApp")
       # self.root.iconbitmap('resources/favicon.ico') # ye issue h;
        self.root.geometry("350x600")
        self.root.config(bg = '#34495E')
        self.login_gui()
        self.root.mainloop()  # gui ko screen pr hold krke rkhe ga

    def login_gui(self):
        self.clear()
        heading = Label(self.root , text = 'NLPApp' , bg = '#34495E' , fg = 'white')
        heading.pack(pady = (30 , 30))
        heading.config(font=('verdana', 24, 'bold'))

        Lable1 =    Label(self.root , text = 'Enter Email')
        Lable1.pack(pady = (10 , 10))

        self.email_input = Entry(self.root , width = 50)
        self.email_input.pack(pady = (5 , 10) , ipady = 4)

        Lable2 = Label(self.root, text='Enter Password')
        Lable2.pack(pady=(10, 10))

        self.password_input = Entry(self.root , width = 50 , show = '*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root , text = 'Login', width = 30 , height = 2 , command=self.perform_login)
        login_btn.pack(pady = (10 , 10))

        Lable3 = Label(self.root, text='Not a member?')
        Lable3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now' , command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):

        # existing gui ko hatayenge pehle
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        Lable0 = Label(self.root, text='Enter Name')
        Lable0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        Lable1 = Label(self.root , text = "Enter Email")
        Lable1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        Lable2 = Label(self.root, text='Enter Password')
        Lable2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2 ,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))
        Lable3 = Label(self.root, text='Already a member?')
        Lable3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        # ham fetch kremge data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful . You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email , password)
        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect Password/email')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Button', width=30, height=4,
                               command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,
                               command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))


        emotion_btn = Button(self.root, text='Emotion Predection', width=30, height=4,
                               command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10 , 20))
        heading2.config(font=('verdana', 24, 'bold'))

        Lable1 = Label(self.root, text='Enter The Text')
        Lable1.pack(pady=(10, 10))

        self.sentiment_input  = Entry(self.root, width=50 , show='*')
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='' , bg = '#34495E', fg = 'white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.config(font=('verdana', 16, 'bold'))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 20))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        print(result)
        self.sentiment_result['text'] = result


























nlp = NLPApp()
