import tkinter 
import random
from tkinter import Label
from tkinter.messagebox import askyesno
from tkinter import simpledialog
from tkinter import PhotoImage
import os 
import base64
import shiftwords


  
window = tkinter.Tk()
window.title("password manager")
window.geometry("400x550")
  
sample_text = tkinter.Entry(window,width=25)
sample_text.place(x=130,y=15)
############ random pass generator
randomchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+','$','!','#','5','%','(',')','=']
fill_free_space = "**************"
lenghtchar = 16
s=2
file = open("userdata.txt","a")
file.close()



def get_password():
    password = ""
    for char in range(0,lenghtchar):
        random_letter = random.choice(randomchar)
        password = random_letter + password

    sample_text.delete(0,"end")
    sample_text.insert(0, password)
  
    
   
    return password

def clear_text():
    sample_text.delete(0,tkinter.END)
    text_id.delete(0,tkinter.END)
    text_username.delete(0,tkinter.END)
    text_password.delete(0,tkinter.END)

    # sample_text.insert(0,"")


    return None

set_up_button_pass = tkinter.Button(window,width=15, text="random password", command=get_password)

### select text and copy
set_up_buttom_copy=tkinter.Button(window,text='Copy',command=lambda:[sample_text.select_range(0,'end'),sample_text.event_generate("<<Copy>>")])
set_up_button_clear=tkinter.Button(window,text="Clear ALL",command=clear_text)
set_up_button_pass.place(x=10,y=10)
set_up_buttom_copy.place(x=290,y=10)
set_up_button_clear.place(x=330,y=10)

#################
#################
#################








#################





def input_profile1():
    
    if os.path.getsize('userdata.txt') != 0:
        tkinter.messagebox.showerror(title="Error", message="you must delete data first!")




    if os.path.getsize('userdata.txt') == 0:

        id_profile = simpledialog.askstring(title="ID", prompt="Write your ID",)
        username = simpledialog.askstring(title="username", prompt="Write your username")
        password = simpledialog.askstring(title="password", prompt="Write your password")
        if os.path.getsize('userdata.txt') != 0:
            tkinter.messagebox.showinfo(title="Alert", message="the profile has been created!")
        # if os.path.getsize('userdata.txt') == 0:
        #     tkinter.messagebox.showinfo(title="Alert", message="the profile has not been created!")    
        text_id.insert(0,fill_free_space)
        text_username.insert(0,fill_free_space)
        text_password.insert(0,fill_free_space)

        file = open("userdata.txt","a") # write text
        file.write(id_profile+"!!!!!"+username+"!!!!!"+password)
        file.close()
        with  open("userdata.txt") as file:
            to_encrypt = file.readline()
            # print (message)
            to_encrypt_64 = to_encrypt.encode('ascii')
            to_encrypt_64_bytes = base64.b64encode(to_encrypt_64)
            encrypt_final = to_encrypt_64_bytes.decode('ascii')
            encrypt_final = shiftwords.ascii_shift_minus(s,encrypt_final)
            
            # file.write(encrypt_final)
            # print (encrypt_final)
            # print (type(encrypt_final))
        file = open("userdata.txt","w") # write text
        file.write(encrypt_final)
        file.close()
    
    return None









def deletedata():
    answer = askyesno(title='Alert',message='Are you sure that you want to delete?\nthis will destroy the data without chance to recover it')
    if answer:

        file = open("userdata.txt","w") #delete text
        file.close()
        text_id.delete(0, "end")
        text_username.delete(0, "end")
        text_password.delete(0, "end")

    return None

def getdata():
    if os.path.getsize('userdata.txt') == 0:
        tkinter.messagebox.showerror(title="Error", message="You must create a profile first!")


    if os.path.getsize('userdata.txt') != 0:
        file = open("userdata.txt","r") #read text
        get_encrypt = file.readline()
        get_encrypt = shiftwords.ascii_shift_plus(s,get_encrypt)
        # print(get_encrypt)
        decrypt_64= get_encrypt.encode("ascii")
        decrypt_64_bytes = base64.b64decode(decrypt_64)
        decrypt_final = decrypt_64_bytes.decode("ascii")
        
        # print(decrypt_final)
        # print(type(decrypt_final))
        split_y = decrypt_final.split("!!!!!")
     
        # print(split[0],split[1])
        text_id.delete(0, "end")
        text_id.insert(0,split_y[0])
        text_username.delete(0, "end")
        text_username.insert(0,split_y[1])
        text_password.delete(0, "end")
        text_password.insert(0,split_y[2])

    return None
  
Create_profile = tkinter.Button(window, height=1, width=12, text="Edit Profile 1",command=input_profile1)
Delete_profile = tkinter.Button(window, height=1, width=12, text="Delete data!", command=deletedata)
get_data = tkinter.Button(window,height=1,width=10,text="Show data!",command=getdata)

idlabel = Label(text="ID =")
userlabel = Label(text="Username =")
passlabel = Label(text="password =")


text_id =tkinter.Entry(window,font=20,width=28)
text_username = tkinter.Entry(window,font=20,width=28)
text_password = tkinter.Entry(window,font=20,width=28)

if os.path.getsize('userdata.txt') != 0:
    text_id.insert(0,fill_free_space)
    text_username.insert(0,fill_free_space)
    text_password.insert(0,fill_free_space)


####
photo = PhotoImage(file="img/front.png")
layout = Label(window, image=photo, bd=0)
layout.place(x=150, y=50)

window.iconbitmap("img/ico.ico")
####


Create_profile.place(x=60,y=160)
Delete_profile.place(x=160,y=160)
get_data.place(x=270,y=160)
text_id.place(x=80,y=200)
text_username.place(x=80,y=225)
text_password.place(x=80,y=250)
idlabel.place(x=1,y=200)
userlabel.place(x=1,y=225)
passlabel.place(x=1,y=250)











window.mainloop()
