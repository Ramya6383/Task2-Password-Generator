from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    number=string.digits
    special_character=string.punctuation

    all=small_alphabets+capital_alphabets+number+special_character
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+number+special_character,password_length))

    
def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='mediumpurple')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='PASSWORD GENERATOR',font=('times new roman',20,'bold'),bg='mediumpurple',fg='white')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font=Font,bg='mediumpurple',fg='white')
lengthLabel.grid(pady=5) 

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()

#RANDOM PASSWORD = 4 S x K R -y e P v A E h q Hr j h p i z s w