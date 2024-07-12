
'''
Project: ATM
Author : Nalamari Shashidhar Reddy
Started Date: 04/09/2023
Completed Date: 12/02/2024
'''
import customtkinter as tk
from tkinter import messagebox as mb
global temp_variable,t
import random
from mail import mail_sender as ms
from database import *   # 282
root = tk.CTk()
root.config(height=625,width=940)
root.resizable(False,False)
root.title("Shashidhar Reddy")
font = "Roboto"
back_button = tk.CTkButton(master=root,text="Back",font=(font,15),command=lambda: p.main_frame())
back_button.place(x=600,y=463)
def exit_function():
    temp = mb.askyesno("My App","Do you want to exit?")
    if temp:
        root.destroy()


class pingpong:
    def __init__(self) :
        self.temp_variable = 0
        self.temp_variable2 = 0
        self.exist = "user name exist"
        self.notexist = "OK"
        self.temparary = 0
        self.pass_changer_mail = ''
        self.temp_variable_z = 1

    def main_frame(self):
        back_button.configure(state=tk.DISABLED)
        self.frame1 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame1.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame1,text="ATM",font=(font,60,"bold"))
        title_lable.place(x=290,y=40)
        # entery1
        self.entery1_function()
        # entery 2
        self.entery2_function()

        login_button = tk.CTkButton(master=self.frame1,text="login",fg_color="transparent",\
                                    font=(font,17),width=3,hover_color="#6675F0",command=self.login)
        login_button.place(x=325,y=285)


        signup_label = tk.CTkLabel(master=self.frame1,text="New user?",font=("Roboto",20))
        signup_label.place(x=228,y=380)
        signup_button = tk.CTkButton(master=self.frame1,text="Click here to signup",fg_color="transparent",\
                                     font=("Roboto",17,"bold","underline")\
                                    ,text_color="green",hover_color="#313131", cursor="hand2",command=self.signup_frame)
        signup_button.place(x=325,y=380)

    def entery1_function(self):
        def on_id_enter(e):
            temp = self.entery1.get()
            if temp == 'Acc. Number':
                self.entery1.delete(0, 'end')
        def on_id_leave(e):
            temp = self.entery1.get()
            if temp == '':
                self.entery1.insert(0, 'Acc. Number')

        self.entery1 = tk.CTkEntry(master=self.frame1,font=(font,15))
        self.entery1.place(x=280,y=180)
        self.entery1.insert(0,"Acc. Number")
        self.entery1.bind('<FocusIn>', on_id_enter)
        self.entery1.bind('<FocusOut>', on_id_leave)

    def entery2_function(self):
        def on_id_enter(e):
            temp = self.entery2.get()
            if temp == 'pin':
                self.entery2.delete(0, 'end')
        def on_id_leave(e):
            temp = self.entery2.get()
            if temp == '':
                self.entery2.insert(0, 'pin')
        self.entery2 = tk.CTkEntry(master=self.frame1,font=(font,15),show="*")
        self.entery2.place(x=280,y=215)
        self.entery2.insert(0,"pin")
        self.entery2.bind('<FocusIn>', on_id_enter)
        self.entery2.bind('<FocusOut>', on_id_leave)

        self.pass_button = tk.CTkButton(master=self.frame1,hover_color="#6675F0",text="show",font=(font,15),width=5,\
                                        fg_color="transparent",command=lambda:self.show_hide(self.temp_variable))
        self.pass_button.place(x=423,y=215)

    def show_hide(self,temp_variable):
        if temp_variable == 0:
            self.pass_button.configure(text="hide")
            self.entery2.configure(show="")
            self.temp_variable = 1
        else:
            self.pass_button.configure(text="show")
            self.entery2.configure(show="*")
            self.temp_variable = 0



    def signup_frame(self):
        self.frame1.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.frame2 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame2.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame2,text="Create Your ATM Account",font=(font,40,"bold"))
        title_lable.place(x=115,y=30)


        def on_email_enter(e):
            temp = self.suentryemail.get()
            if temp == 'Email':
                self.suentryemail.delete(0, 'end')
                self.email_check.configure(text="Change mail id",text_color="red")
            elif ob.mail_fetcher(mailid=temp) == None: # ok
                self.email_check.configure(text=self.notexist,text_color="green") 
            else:
                self.email_check.configure(text="mail id exist",text_color="red")
        def on_email_leave(e):
            temp = self.suentryemail.get()
            if temp == '':
                self.suentryemail.insert(0, 'Email')
                self.email_check.configure(text="Change mail id",text_color="red")
            elif ob.mail_fetcher(mailid=temp) == None: # ok
                self.email_check.configure(text=self.notexist,text_color="green") 
            else:
                self.email_check.configure(text="mail id exist",text_color="red")
        self.suentryemail = tk.CTkEntry(master=self.frame2,font=(font,15))
        self.suentryemail.place(x=280,y=155)
        self.suentryemail.insert(0,"Email")
        self.suentryemail.bind('<FocusIn>', on_email_enter)
        self.suentryemail.bind('<FocusOut>', on_email_leave)

        self.email_check = tk.CTkLabel(master=self.frame2,text='',font=("Roboto",13,"bold"))
        self.email_check.place(x=425,y=155)


        signup_button = tk.CTkButton(master=self.frame2,text="Sign up",fg_color="transparent",\
                                     font=("Roboto",17,"bold"),width=5\
                                    ,hover_color="#6675F0", cursor="hand2",command=self.otp_page)
        signup_button.place(x=300,y=325)


    def otp_page(self):
        self.sumail = self.suentryemail.get()
        self.randomnumber = random.randint(100000,999999)
        print(self.randomnumber)
        try:
            ms(name="",email_receiver=self.sumail,otp=self.randomnumber,operation="new")
        except Exception as e:
            if "is not a valid" in str(e):
                mb.showerror("MyApp","No Mail id found")
                self.suentryemail.delete(0,"end")
            else:
                print(e)
                mb.showerror("MyApp","No internet, can't send OTP")
                self.main_frame()
                self.frame2.destroy()
        else:
            self.frame2.destroy()
            back_button.configure(state=tk.NORMAL)
            back_button.configure(command=self.signup_frame)
            self.frame3 = tk.CTkFrame(master=root,height=445,width=730)
            self.frame3.place(x=10,y=10)
            title_lable = tk.CTkLabel(master=self.frame3,text="Enter Your Otp",font=("Segoe Script",40))
            title_lable.place(x=180,y=100)
            def on_otp_enter(e):
                temp = self.otpentery.get()
                if temp == 'OTP':
                    self.otpentery.delete(0, 'end')
            def on_otp_leave(e):
                temp = self.otpentery.get()
                if temp == '':
                    self.otpentery.insert(0, 'OTP')
            self.otpentery = tk.CTkEntry(master=self.frame3,font=(font,15))
            self.otpentery.place(x=225,y=220)
            self.otpentery.insert(0,"OTP")
            self.otpentery.bind('<FocusIn>', on_otp_enter)
            self.otpentery.bind('<FocusOut>', on_otp_leave)
            self.submitbutton = tk.CTkButton(master=self.frame3,text="Submit",fg_color="transparent",\
                                        font=("Roboto",17,"bold"),width=5\
                                        ,hover_color="#6675F0", cursor="hand2",command=self.signup)
            self.submitbutton.place(x=400,y=220)
        
    def signup(self):
        self.frame3.destroy()
        a_num = ob.last_value()
        back_button.configure(command=self.main_frame)
        self.frame4 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame4.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame4,text="Enter Your Details",font=(font,40,"bold"))
        title_lable.place(x=185,y=30)
        def on_name_enter(e):
            temp = self.suentryname.get()
            if temp == 'Name':
                self.suentryname.delete(0, 'end')
        def on_name_leave(e):
            temp = self.suentryname.get()
            if temp == '':
                self.suentryname.insert(0, 'Name')
        self.suentryname = tk.CTkEntry(master=self.frame4,font=(font,15))
        self.suentryname.place(x=280,y=155)
        self.suentryname.insert(0,"Name")
        self.suentryname.bind('<FocusIn>', on_name_enter)
        self.suentryname.bind('<FocusOut>', on_name_leave)

        self.suentryusername = tk.CTkEntry(master=self.frame4,font=(font,15))
        self.suentryusername.place(x=280,y=205)
        self.suentryusername.insert(0,"Acc num:"+str(a_num))
        self.suentryusername.configure(state="readonly")

        temp_pin = random.randrange(1000,9999)
        self.supin = tk.CTkEntry(master=self.frame4,font=(font,15))
        self.supin.place(x=280,y=255)
        self.supin.insert(0,f"Pin:{temp_pin}")
        self.temp_pin = temp_pin
        self.supin.configure(state = "readonly")

        self.susubbut = tk.CTkButton(master=self.frame4,font=(font,15),text="Create Account",command=self.susubmit)
        self.susubbut.place(x=280,y=315)

    def susubmit(self):
        ob.insert_data(ob.last_value(),int(self.temp_pin),0,self.suentryname.get(),self.sumail)
        mb.showinfo("ATM","Account Created Successfully!!")
        self.frame4.destroy()
        self.main_frame()

    def data_entery(self):
        try:
            if int(self.otpentery.get()) == self.randomnumber:
                ob.insert_data(u_name=self.suusername,name=self.suname,mailid=self.sumail,password=self.supassword)
                mb.showinfo("MyApp","Account created successfully!")
                self.frame3.destroy()
                self.main_frame()
            else:
                raise ValueError
        except:
            mb.showerror("MyApp","Wrong OTP")



    def login(self):
        u_id = self.entery1.get()
        self.account_id = u_id
        password = self.entery2.get()
        if ob.fetch_password(a_num=u_id) == None:
            mb.showerror("MyApp","No User found")
            self.entery1.delete(0,"end")
        elif str(ob.fetch_password(a_num=u_id)) != password:
                mb.showerror("MyApp","Enter correct pin!")
                self.entery2.delete(0,"end")
                forgot_button = tk.CTkButton(master=self.frame1,text="change pin",fg_color="transparent",\
                                        font=("Roboto",15,"bold")\
                                        ,text_color="#F94822",hover_color="#313131", cursor="hand2",command=lambda:self.forgot_pass(1))
                forgot_button.place(x=280,y=250)
        else:
            # Here the app starts!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            s = signin(u_id)
            s.signin_lo_firstpage(u_id)


    
    def forgot_pass(self,a):
        self.a = a
        self.frame1.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.frame4 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame4.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame4,text="Change password",font=("Segoe Script",40))
        title_lable.place(x=175,y=30)
        def on_email_enter(e):
            temp = self.forgetemail.get()
            if temp == 'Email':
                self.forgetemail.delete(0, 'end')
        def on_email_leave(e):
            temp = self.forgetemail.get()
            if temp == '':
                self.forgetemail.insert(0, 'Email')
        self.forgetemail = tk.CTkEntry(master=self.frame4,font=(font,15))
        self.forgetemail.place(x=280,y=155)
        self.forgetemail.insert(0,"Email")
        self.forgetemail.bind('<FocusIn>', on_email_enter)
        self.forgetemail.bind('<FocusOut>', on_email_leave)
        self.otp_button = tk.CTkButton(master=self.frame4,text="Get otp",fg_color="transparent",\
                                        font=("Roboto",17,"bold"),width=5\
                                        ,hover_color="#6675F0", cursor="hand2",command=self.password_canger)
        self.otp_button.place(x=305,y=220)


    
    def password_canger(self):
        self.pass_changer_mail = self.forgetemail.get()
        try:
            self.forgot_pass1.destroy()
            self.forgot_pass2.destroy()
            self.show_hide_forgotpass.destroy()
            self.changebutton.destroy()
        except:
            pass

        if ob.mail_fetcher(mailid=self.pass_changer_mail) == None:
            mb.showerror("MyApp","Mail not found")
        else:
            if self.a:
                self.randomnumber2 = random.randint(100000,999999)
                print(self.randomnumber2)
                try:
                    ms(email_receiver=self.pass_changer_mail,otp=self.randomnumber2,operation="edit")
                except Exception as e:
                    if "is not a valid" in str(e):
                        mb.showerror("MyApp","No Mail id found")
                        self.forgetemail.delete(0,"end")
                    else:
                        mb.showerror("MyApp","No internet, can't send OTP")
                else:
                    back_button.configure(command=lambda:self.forgot_pass(0))
                    self.forgetemail.configure(state="readonly")
                    self.otp_button.destroy()
                    def on_otp_enter(e):
                        temp = self.forgot_otp_entery.get()
                        if temp == 'OTP':
                            self.forgot_otp_entery.delete(0, 'end')
                    def on_otp_leave(e):
                        temp = self.forgot_otp_entery.get()
                        if temp == '':
                            self.forgot_otp_entery.insert(0, 'OTP')
                    self.forgot_otp_entery = tk.CTkEntry(master=self.frame4,font=(font,15))
                    self.forgot_otp_entery.place(x=280,y=205)
                    self.forgot_otp_entery.insert(0,"OTP")
                    self.forgot_otp_entery.bind('<FocusIn>', on_otp_enter)
                    self.forgot_otp_entery.bind('<FocusOut>', on_otp_leave)
                    self.submitbutton = tk.CTkButton(master=self.frame4,text="Submit",fg_color="transparent",\
                                                    font=("Roboto",17,"bold"),width=5\
                                                    ,hover_color="#6675F0", cursor="hand2",command=self.data_entery_forgot)
                    self.submitbutton.place(x=310,y=255)

    
    def data_entery_forgot(self):
        temp = self.forgot_otp_entery.get()
        if temp != str(self.randomnumber2):
            mb.showerror("MyApp","Wrong OTP")
        else:
            back_button.configure(command=self.password_canger)
            self.forgot_otp_entery.configure(state="readonly")
            self.submitbutton.destroy()



            def on_newpass_enter(e):
                    temp = self.forgot_pass1.get()
                    if temp == 'New pin':
                        self.forgot_pass1.delete(0, 'end')
            def on_newpass_leave(e):
                    temp = self.forgot_pass1.get()
                    if temp == '':
                        self.forgot_pass1.insert(0, 'New pin')

            self.forgot_pass1 = tk.CTkEntry(master=self.frame4,font=(font,15))
            self.forgot_pass1.place(x=180,y=255)
            self.forgot_pass1.insert(0,"New pin")
            self.forgot_pass1.bind('<FocusIn>', on_newpass_enter)
            self.forgot_pass1.bind('<FocusOut>', on_newpass_leave)


            def on_newpass2_enter(e):
                    temp = self.forgot_pass2.get()
                    if temp == 'Re-enter pin':
                        self.forgot_pass2.delete(0, 'end')
            def on_newpass2_leave(e):
                    temp = self.forgot_pass2.get()
                    if temp == '':
                        self.forgot_pass2.insert(0, 'Re-enter pin')
            self.forgot_pass2 = tk.CTkEntry(master=self.frame4,font=(font,15))
            self.forgot_pass2.place(x=380,y=255)
            self.forgot_pass2.insert(0,"Re-enter pin")
            self.forgot_pass2.bind('<FocusIn>', on_newpass2_enter)
            self.forgot_pass2.bind('<FocusOut>', on_newpass2_leave)
            self.show_hide_forgotpass = tk.CTkButton(master=self.frame4,hover_color="#6675F0",text="hide",font=(font,15),width=5,\
                                        fg_color="transparent",command=lambda:self.show_hide_forgotpassfun(self.temp_variable_z))
            self.show_hide_forgotpass.place(x=530,y=255)
            self.changebutton = tk.CTkButton(master=self.frame4,text="Change",fg_color="transparent",\
                                                font=("Roboto",17,"bold"),width=5\
                                                ,hover_color="#6675F0", cursor="hand2",\
                                                command=lambda:self.password_canger_final())
            self.changebutton.place(x=310,y=305)



    def show_hide_forgotpassfun(self,temp_variable):
                if temp_variable == 0:
                    self.show_hide_forgotpass.configure(text="hide")
                    self.forgot_pass1.configure(show="")
                    self.forgot_pass2.configure(show="")
                    self.temp_variable_z = 1
                else:
                    self.show_hide_forgotpass.configure(text="show")
                    self.forgot_pass1.configure(show="*")
                    self.forgot_pass2.configure(show="*")
                    self.temp_variable_z = 0

    def password_canger_final(self):
        new_password = self.forgot_pass1.get()
        re_enter_pass = self.forgot_pass2.get()
        if new_password == re_enter_pass:
            ob.change_password(newpin=new_password,mailid=self.pass_changer_mail)
            mb.showinfo("MyApp","Password changed!!")
            self.frame4.destroy()
            self.main_frame()
        else:
            mb.showerror("MyApp","Password is not matched")


class signin(pingpong):
    def __init__(self,hello_id):
        self.sender_id = hello_id
        # super().__init__() ekkada chusuko malla bugga iytav
        self.signin_lo_firstpage() # tarvata ee line tesai

    def signin_lo_firstpage(self,u_id=809):
        # self.frame1.destroy()  tarvata denni normal line chey
        back_button.configure(command=super().main_frame)
        back_button.configure(state=tk.NORMAL)
        self.sigin_frame1 = tk.CTkFrame(master=root,height=445,width=730)
        self.sigin_frame1.place(x=10,y=10)

        tk.CTkLabel(master=self.sigin_frame1,text="BANK SYSTEM",font=("Segoe Script",40)).place(x=185,y=30)
        self.money_transfeer_button = tk.CTkButton(master=self.sigin_frame1,text="Transfer Money",font=(font,15),\
                                                   command=self.money_transfeer)
        self.money_transfeer_button.place(x=290,y=130)

        self.check_balance_button = tk.CTkButton(master=self.sigin_frame1,text="Check Balance",font=(font,15),\
                                          command=self.check_balance)
        self.check_balance_button.place(x=290,y=180)

        self.withdraw_button = tk.CTkButton(master=self.sigin_frame1,text="Withdraw Money",font=(font,15),\
                                            command=self.withdraw)
        self.withdraw_button.place(x=290,y=230)

        self.deposite_button = tk.CTkButton(master=self.sigin_frame1,text="Deposite",font=(font,15),\
                                            command=self.deposite)
        self.deposite_button.place(x=290,y=280)
        
        self.log_out_button = tk.CTkButton(master=self.sigin_frame1,text="Log Out",font=(font,15), fg_color="red",\
                                           command=super().main_frame)
        self.log_out_button.place(x=290,y=330)




    def deposite(self):
        self.sigin_frame1.destroy()
        back_button.configure(command=self.signin_lo_firstpage)
        self.sigin_frame5 = tk.CTkFrame(master=root,height=445,width=730)
        self.sigin_frame5.place(x=10,y=10)
        tk.CTkLabel(master=self.sigin_frame5,text="BALANCE",font=("Segoe Script",40)).place(x=245,y=30)

        self.money_entry_deposite = tk.CTkEntry(master=self.sigin_frame5,font=(font,15))
        self.money_entry_deposite.place(x=290,y=225)
        self.money_entry_deposite.insert(0,"Enter Amount")
        def on_newpass2_enter2(e):
                temp = self.money_entry_deposite.get()
                if temp == 'Enter Amount':
                    self.money_entry_deposite.delete(0, 'end')
        def on_newpass2_leave2(e):
                temp = self.money_entry_deposite.get()
                if temp == '':
                    self.money_entry_deposite.insert(0, 'Enter Amount')
        
        self.money_entry_deposite.bind('<FocusIn>', on_newpass2_enter2)
        self.money_entry_deposite.bind('<FocusOut>', on_newpass2_leave2)

        self.w_button = tk.CTkButton(master=self.sigin_frame5,text="Deposite",font=(font,15),command=self.depositeing)
        self.w_button.place(x=290,y=300)


    def depositeing(self):
        name = ob.fetch_name(self.sender_id)
        bal = ob.fetch_balance(self.sender_id)
        amount = self.money_entry_deposite.get()
        mail = ob.mail_fetcher_once_check_db_file(self.sender_id)
        try:
            amount = int(amount)
        except:
            mb.showerror("My App","Amount must be an integer")
        else:
            if amount == 0:
                mb.showwarning("My App","Nah bro you are drunk, you can't deposite ₹0")
            elif (amount%100) != 0:
                mb.showinfo("My App","Sorry My friend, We only take ₹100 notes")
            else:
                if mb.askyesno("My App","Are you sure to deposite?"):
                    bal += amount
                    ob.update_balance(a_num=self.sender_id,new_balance=bal)
                    ms(operation="credit",email_receiver=mail,name=name,balance=bal)
                    mb.showinfo("My App","Transaction Success")
                    self.sigin_frame5.destroy()
                    self.signin_lo_firstpage()


    def withdraw(self):
        self.sigin_frame1.destroy()
        back_button.configure(command=self.signin_lo_firstpage)
        self.sigin_frame4 = tk.CTkFrame(master=root,height=445,width=730)
        self.sigin_frame4.place(x=10,y=10)
        tk.CTkLabel(master=self.sigin_frame4,text="BALANCE",font=("Segoe Script",40)).place(x=245,y=30)

        self.money_entry_withdraw = tk.CTkEntry(master=self.sigin_frame4,font=(font,15))
        self.money_entry_withdraw.place(x=290,y=225)
        self.money_entry_withdraw.insert(0,"Enter Amount")
        def on_newpass2_enter2(e):
                temp = self.money_entry_withdraw.get()
                if temp == 'Enter Amount':
                    self.money_entry_withdraw.delete(0, 'end')
        def on_newpass2_leave2(e):
                temp = self.money_entry_withdraw.get()
                if temp == '':
                    self.money_entry_withdraw.insert(0, 'Enter Amount')
        
        self.money_entry_withdraw.bind('<FocusIn>', on_newpass2_enter2)
        self.money_entry_withdraw.bind('<FocusOut>', on_newpass2_leave2)

        self.w_button = tk.CTkButton(master=self.sigin_frame4,text="Withdraw",font=(font,15),command=self.withdrawing)
        self.w_button.place(x=290,y=300)


    def withdrawing(self):
        name = ob.fetch_name(self.sender_id)
        bal = ob.fetch_balance(self.sender_id)
        amount = self.money_entry_withdraw.get()
        mail = ob.mail_fetcher_once_check_db_file(self.sender_id)
        try:
            amount = int(amount)
        except:
            mb.showerror("My App","Amount must be an integer")
        else:
            if amount == 0:
                mb.showwarning("My App","Nah bro you are drunk, you can't take ₹0")
            elif (amount%100) != 0:
                mb.showinfo("My App","Sorry My friend, We only have ₹100 notes")
            else:
                if mb.askyesno("My App","Are you sure to withdraw?"):
                    bal -= amount
                    ob.update_balance(a_num=self.sender_id,new_balance=bal)
                    ms(operation="credit",email_receiver=mail,name=name,balance=bal)
                    mb.showinfo("My App","Transaction Success")
                    self.sigin_frame4.destroy()
                    self.signin_lo_firstpage()


    def check_balance(self):
        self.sigin_frame1.destroy()
        back_button.configure(command=self.signin_lo_firstpage)
        self.sigin_frame3 = tk.CTkFrame(master=root,height=445,width=730)
        self.sigin_frame3.place(x=10,y=10)
        tk.CTkLabel(master=self.sigin_frame3,text="BALANCE",font=("Segoe Script",40)).place(x=245,y=30)
        name= ob.fetch_name(self.sender_id)
        bal = ob.fetch_balance(self.sender_id)
        tk.CTkLabel(master=self.sigin_frame3,text=f"User - {name}",font=(font,25),anchor="center").place(x=280,y=150)
        tk.CTkLabel(master=self.sigin_frame3,text=f"Account - {self.sender_id}",font=(font,25),anchor="center").place(x=280,y=200)
        tk.CTkLabel(master=self.sigin_frame3,text=f"Current - ₹ {float(bal)} \\-",font=(font,25),\
                    anchor="center").place(x=280,y=250)
        but = tk.CTkButton(master=self.sigin_frame3,text="Send to mail",font=(font,25),command=self.invoive_sender)
        but.place(x=280,y=325)

    def invoive_sender(self):
        email_receiver = ob.mail_fetcher_once_check_db_file(self.sender_id)
        id_ = self.sender_id
        name= ob.fetch_name(self.sender_id)
        bal = ob.fetch_balance(self.sender_id)
        ms(name=name,balance=bal,reciver_id=id_,operation="invoice",email_receiver=email_receiver)
        mb.showinfo("My App","Mail sent")


    def money_transfeer(self):
        self.sigin_frame1.destroy()
        back_button.configure(command=self.signin_lo_firstpage)
        self.sigin_frame2 = tk.CTkFrame(master=root,height=445,width=730)
        self.sigin_frame2.place(x=10,y=10)

        tk.CTkLabel(master=self.sigin_frame2,text="TRANSFER",font=("Segoe Script",40)).place(x=230,y=30)

        self.money_entry_transfeer = tk.CTkEntry(master=self.sigin_frame2,font=(font,15))
        self.money_entry_transfeer.place(x=290,y=150)
        self.money_entry_transfeer.insert(0,"Enter Account id")
        def on_newpass2_enter(e):
                temp = self.money_entry_transfeer.get()
                if temp == 'Enter Account id':
                    self.money_entry_transfeer.delete(0, 'end')
        def on_newpass2_leave(e):
                temp = self.money_entry_transfeer.get()
                if temp == '':
                    self.money_entry_transfeer.insert(0, 'Enter Account id')
        
        self.money_entry_transfeer.bind('<FocusIn>', on_newpass2_enter)
        self.money_entry_transfeer.bind('<FocusOut>', on_newpass2_leave)



        self.money_entry_transfeer2 = tk.CTkEntry(master=self.sigin_frame2,font=(font,15))
        self.money_entry_transfeer2.place(x=290,y=225)
        self.money_entry_transfeer2.insert(0,"Enter Amount")
        def on_newpass2_enter2(e):
                temp = self.money_entry_transfeer2.get()
                if temp == 'Enter Amount':
                    self.money_entry_transfeer2.delete(0, 'end')
        def on_newpass2_leave2(e):
                temp = self.money_entry_transfeer2.get()
                if temp == '':
                    self.money_entry_transfeer2.insert(0, 'Enter Amount')
        
        self.money_entry_transfeer2.bind('<FocusIn>', on_newpass2_enter2)
        self.money_entry_transfeer2.bind('<FocusOut>', on_newpass2_leave2)

        self.d_button = tk.CTkButton(master=self.sigin_frame2,text="Send money",font=(font,15),command=self.Transfering)
        self.d_button.place(x=290,y=300)


    def Transfering(self):
        try:
            reciver_id = self.money_entry_transfeer.get()
            reciver_id = int(reciver_id)
        except:
            mb.showerror("My App","ID must be an integer")
        try:
            amount = self.money_entry_transfeer2.get()
            amount = int(amount)
        except:
            mb.showerror("My App","Amount must be an integer")
        sender_id = self.sender_id
        back_button.configure(command=self.money_transfeer)
        actual_balance = ob.fetch_balance(sender_id)
        reciver_balance = ob.fetch_balance(reciver_id)
        if reciver_balance == None:
            mb.showerror("My App","No Account Found")
        elif reciver_id == sender_id:
            mb.showerror("My App","You can't send money to yourself Idiot!")
        elif actual_balance<amount:
            mb.showerror("My App","Low Balance!")
        # elif amount <= 0:
        #     mb.showerror("My App","Transaction is not possible")
        else:
            choice = mb.askyesno("My App","Do you wan't to send money?")
            if choice:
                actual_balance -= amount
                reciver_balance += amount
                ob.update_balance(sender_id,actual_balance)               
                ob.update_balance(reciver_id,reciver_balance)             
                reciver_name = ob.fetch_name(reciver_id)
                sender_name = ob.fetch_name(sender_id)
                reciver_mail = ob.mail_fetcher_once_check_db_file(reciver_id)
                sender_mail = ob.mail_fetcher_once_check_db_file(sender_id)
                ms(name=reciver_name,email_receiver=reciver_mail,operation="debit",balance=str(reciver_balance),reciver_id=str(sender_id))
                ms(name=sender_name,email_receiver=sender_mail,operation="credit",balance=str(actual_balance))
                mb.showinfo("My App","Transaction Success")
                self.sigin_frame2.destroy()
                self.signin_lo_firstpage()





p = signin(809)
exit_button = tk.CTkButton(master=root,text="Exit",fg_color="red",font=(font,15),command=lambda: exit_function())
exit_button.place(x=295,y=463)
home_button = tk.CTkButton(master=root,text="Home",font=(font,15),command=lambda: p.main_frame())
home_button.place(x=10,y=463)
root.mainloop()

