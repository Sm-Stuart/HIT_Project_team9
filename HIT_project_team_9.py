from tkinter import*
import mysql.connector

class LOGIN:

            
      ##main class programee creating the 1st GUI
            
      def  __init__(self):
            self.conn=mysql.connector.connect(host="remotemysql.com",user="Du57mLVEtn",password="gQ5yyf6pwu",database="Du57mLVEtn")
            self.mycursor=self.conn.cursor()
            self.root1=Tk()                
            #self.user_menu()
            

            self.root1.title("web Form")
            self.root1.minsize(600,600)
            #self.root.maxsize(600,600)
            self.root1.configure(background="#6122bf")



            #font editing of the title
            self.Label1=Label(self.root1,text="WELCOME",bg="#6122bf",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))

            temp="CHOSE ANY ONE OF THE FOLLOWING::"


            self.Label2=Label(self.root1,text=temp,bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(30,5))

            
            self.Label3=Label(self.root1,text="""1. REGISTER\n2. LOGIN\n3.EXIT\nEnter your choice""",bg="#6122bf",fg="#FFF")
            self.Label3.configure(font=("Garamond",15))
            self.Label3.pack(pady=(10,10))


            #input entry box
            self.user_input=Entry(self.root1)
            self.user_input.pack(ipadx=6,ipady=6)
           # print(self.user_input)


            #button constrains
            self.click=Button(self.root1,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.user_menu())
            self.click.pack(pady=(5,5))

            self.root1.mainloop()
            

      def user_menu(self):
            x=self.user_input.get()
                        
            if x=="1":
                  self.register()
                 
            elif x=="2":
                  self.login()
             

            else:
                  self.Label2=Label(self.root1,text="BYE",bg="#6122bf",fg="#FFF")
                  self.Label2.configure(font=("Garamond",15))
                  self.Label2.pack(pady=(30,5))
                  self.root1.destroy()



                 
            
      def register(self):

            self.root1.destroy()                                              #destroy the 1st GUI
          
            self.root2=Tk()                                                         #creating the 2nd GUI
           
            

            ##format of 2nd GUI
            self.root2.title("Registration Form")
            self.root2.minsize(600,600)
            #self.root.maxsize(600,600)
            self.root2.configure(background="#6122bf")



            #font editing of the title
            self.Label1=Label(self.root2,text="REGISTRATION FORM",bg="#6122bf",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))


            #creating the name label
            self.Label2=Label(self.root2,text="Enter your name",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_name=Entry(self.root2)
            self.user_name.pack(ipadx=6,ipady=6)


            #creating the email label
            self.Label2=Label(self.root2,text="Enter your E-mail:",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_email=Entry(self.root2)
            self.user_email.pack(ipadx=6,ipady=6)


            #creating the password label
            self.Label2=Label(self.root2,text="Enter your password:",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_password=Entry(self.root2)
            self.user_password.pack(ipadx=6,ipady=6)

            self.click1=Button(self.root2,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.registered())
            self.click1.pack(pady=(5,5))

            self.root2.mainloop()
            

      def registered(self):


            name=self.user_name.get()
            #print(name)
            x=len(name)
            #print(name)
            if (x==0):
                   self.root=Tk()

                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID NAME",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                  
            name1=name.upper()
            email=self.user_email.get()
            f=0
         
            for i in email:
                  if(i=="@"  or i=="."):
                        f+=1

            if(f!=2):
                   self.root=Tk()
                   
                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID EMAIL",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                   
            password=self.user_password.get()
            
            try:
                   self.mycursor.execute("INSERT INTO users (users_id,name,email,password) VALUES (NULL,'{}','{}','{}')".format(name1,email,password))

                   self.conn.commit()

            except Exception as e:
                   self.root=Tk()
                   
                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID EMAIL",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                  



            
            self.root2.destroy()                      #destroyed the 2nd GUI

           
            self.root=Tk()                                  #creating the 3rd GUI


            #initials of 3rd GUI
            self.root.title("Registration Form")
            self.root.minsize(200,100)
            self.root.configure(background="#6122bf")



                  
            self.Label2=Label(self.root,text="Registered succesfully!!!!",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20,"bold"))
            self.Label2.pack(pady=(10,5))

            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
            self.click1.pack(pady=(5,5))

            self.root.mainloop()


            
      #destroy  the GUI
      def destroy(self):
            self.root.destroy()



      def register1(self):
            #print("x")
            
            self.user_name.delete(first=0,last=100)
            self.user_email.delete(first=0,last=100)
            self.user_password.delete(first=0,last=100)
            
            self.root.destroy()

      def login2(self):
            #print("x")
            
            #self.user_name.delete(first=0,last=100)
            self.user_email.delete(first=0,last=100)
            self.user_password.delete(first=0,last=100)
            
            self.root.destroy()

         

      def login(self):

            self.root1.destroy()                      #destryoing the first GUI
            
            self.root2=Tk()                                 #creating  the 2nd GUI           
                              


            #framework of GUI
            self.root2.title("Login form")
            self.root2.minsize(600,600)
            self.root2.configure(background="#6122bf")



            #font editing of the title
            self.Label1=Label(self.root2,text="LOGIN FORM",bg="#6122bf",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))


            
            #creating the emaillabel
            self.Label2=Label(self.root2,text="Enter your E-mail:",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_email=Entry(self.root2)
            self.user_email.pack(ipadx=6,ipady=6)

            #creating the password label
            self.Label2=Label(self.root2,text="Enter your password:",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_password=Entry(self.root2)
            self.user_password.pack(ipadx=6,ipady=6)

            self.click2=Button(self.root2,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.logined())
            self.click2.pack(pady=(5,5))

            self.root2.mainloop()


      def logined(self):
            
            email=self.user_email.get()
            password=self.user_password.get()


            self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' and password LIKE '{}'".format(email,password))

            self.x=self.mycursor.fetchall()

            if(len(self.x)==0):
                   self.root=Tk()

                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID DATA",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   #print("x")
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.login2())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()

            self.root2.destroy()          #destroyed the 2nd GUI

            self.root=Tk()                      #creating the GUI

            
            #frame of GUI
            self.root.title("Login Form")
            self.root.minsize(200,100)
            self.root.configure(background="#6122bf")



                  
            self.Label2=Label(self.root,text="LOGIN Successfully!!!",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20,"bold"))
            self.Label2.pack(pady=(10,5))

           
            
            self.Label2=Label(self.root,text="WELCOME",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",25))
            self.Label2.pack(pady=(10,5))
           
            y=self.x[0][1]

            self.Label2=Label(self.root,text=y,bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))

            self.z=self.x[0][0]

            self.Label2=Label(self.root,text="Your ID NO.:",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))

            
            self.Label2=Label(self.root,text=self.z,bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))


            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.to_do())
            self.click1.pack(pady=(5,5))


      def to_do(self):
            self.destroy()

            self.root=Tk()

            self.root.title("LIST")
            self.root.minsize(600,600)
            self.root.configure(background="#6122bf")



                              
            self.Label2=Label(self.root,text="CHOOSE ANY ONE OF THE FOLLOWING",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Algerian",25,"bold"))
            self.Label2.pack(pady=(10,5))

                       
                        
            self.Label2=Label(self.root,text="1. CREATE \n 2.VEIW LIST\n 3.EXIT",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))

            self.user_input=Entry(self.root)
            self.user_input.pack(ipadx=6,ipady=6)
                       

            self.click=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.list())
            self.click.pack(pady=(5,5))

            self.root.mainloop()


      def  list(self):
            x=self.user_input.get()

            if x=='1':
                  self.create()
            elif x=='2':
                  try:
                        self.view()
                  except Exception as e:
                        self.root=Tk()
                        self.root.title("ERROR Form")
                        self.root.minsize(200,300)
                        self.root.configure(background="red")
                                    
                        self.Label3=Label(self.root,text="U have entered invalid data ",bg="red",fg="#FFF")
                        self.Label3.configure(font=("Garamond",15,bold))
                        self.Label3.pack(pady=(10,5))
                        
                        self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
                        self.click2.pack(pady=(5,5))
                        self.root.mainloop()
                        

            else:
                  self.destroy()


      def create(self):
            self.destroy()

            self.root=Tk()

            self.root.title("Create")
            self.root.minsize(300,300)
            self.root.configure(background="#6122bf")


            self.Label2=Label(self.root,text="ENTER NUMBER OF TASK :",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Times Roman",25))
            self.Label2.pack(pady=(10,5))
            self.task_num=Entry(self.root)
            self.task_num.pack(ipadx=6,ipady=6)

            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.create_list())
            self.click1.pack(pady=(5,5))

            self.root.mainloop()

      def create_list(self):
            num=self.task_num.get()
            try:
                  num=int(num)

            except Exception as e:
                  self.destroy()
                  self.root=Tk()
                  self.root.title("ERROR Form")
                  self.root.minsize(200,300)
                  self.root.configure(background="red")
                                    
                  self.Label3=Label(self.root,text="U have entered invalid data ",bg="red",fg="#FFF")
                  self.Label3.configure(font=("Garamond",15,"bold"))
                  self.Label3.pack(pady=(10,5))
                        
                  self.click2=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
                  self.click2.pack(pady=(5,5))
                  self.root.mainloop()

            self.destroy()
            
            for i in range(num):
                  self.root=Tk()

                  self.root.title("Create LIST")
                  self.root.minsize(300,300)
                  self.root.configure(background="#6122bf")

                  self.Label2=Label(self.root,text="ENTER  THE TASK\n (one by one) :",bg="#6122bf",fg="#FFF")
                  self.Label2.configure(font=("Algerian",25))
                  self.Label2.pack(pady=(10,5))

                 
                  self.task_name=Entry(self.root)
                  self.task_name.pack(ipadx=6,ipady=6)

                  self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.insert_create_list())
                  self.click1.pack(pady=(5,5))

            self.root.mainloop()


            self.root=Tk()
            self.root.title("Create LIST")
            self.root.minsize(200,100)
            self.root.configure(background="#6122bf")

            self.Label2=Label(self.root,text="THANK YOU :",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))

                
            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
            self.click1.pack(pady=(5,5))

            self.root.mainloop()
                  


      def insert_create_list(self):
            taskname=self.task_name.get()
            tasksname=taskname.upper()
            self.mycursor.execute("INSERT INTO task (users_id,task_id,task_name) VALUES ({},NULL,'{}')".format(self.z,tasksname))
            self.conn.commit()
            self.destroy()


      def view(self):
            self.destroy()

            self.root=Tk()
            self.root.title("VIEW LIST")
            self.root.minsize(600,600)
            self.root.configure(background="#6122bf")


            self.mycursor.execute("""SELECT task_name
                                                      FROM task
                                                      JOIN users
                                                      ON users.users_id=task.users_id
                                                      WHERE task.users_id={}""".format(self.z))

            
            x=self.mycursor.fetchall()
            
            temp=""
            for i in x:
                  for j in i:
                        temp=temp+j+"\n"

            self.Label2=Label(self.root,text="YOUR TO-DO LIST",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Algerian",35))
            self.Label2.pack(pady=(10,5))
            

            self.Label2=Label(self.root,text="",bg="#6122bf",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))
            self.Label2.configure(text=temp)

                
            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
            self.click1.pack(pady=(5,5))

            

            
            self.root.mainloop()
                         
            
                   
obj=LOGIN()






