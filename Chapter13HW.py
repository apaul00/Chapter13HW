#You can use check boxes for for selecting toppings (each with a different cost), radio buttons for the type 
#of crust selected (each with a different cost), buttons for calculation and quit. The input box can be used
#to record the name of the person placing the order. Use a message box to display the total cost of the pizza
#along with the name of the person placing the order. Make sure your design is well laid out and intuitive to 
#the user. Take account of spacing and packing so that everything is properly aligned and professional looking. 
#Be creative with font, color, size, etc.
import tkinter
from tkinter import font
import tkinter.messagebox
from turtle import color

from matplotlib import font_manager

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #creates window/dialogue box
        self.Font = font.nametofont("TkDefaultFont")
        self.main_window.geometry('400x600')
        self.main_window.title('Pizza Order')
        self.main_window.configure(background= '#89BB72')
        self.Font.configure(family="Comic Sans MS",
                                   size=14,
                                   weight=font.NORMAL)


        self.top_frame = tkinter.Frame(self.main_window) #creating top frame -- top frame is user defined, it is merely an attribute of an object
        self.frame_2 = tkinter.Frame(self.main_window)
        self.order_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window) #calling specific Frame method of tkinter object
        
        self.top_frame.configure(background='#F09898')
        self.frame_2.configure(background='#F09898')
        self.order_frame.configure(background='#F09898')
        self.bottom_frame.configure(background='#F09898')

        

        #adding a label for selecting toppings
        self.label1 = tkinter.Label(self.main_window, text = 'Select Your Topping(s)') #creating a label object, specify where we want it and text
        self.label1.pack(side = 'top')
        self.label1.configure(background='#F09898')

        #create 3 IntVar objects to use with the Checkbuttons
        self.cb_var1= tkinter.IntVar()
        self.cb_var2= tkinter.IntVar()
        self.cb_var3= tkinter.IntVar()
        self.cb_var4= tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)

        self.cb1  = tkinter.Checkbutton(self.top_frame, text='Pepperoni        (+$1)', variable=self.cb_var1)
        self.cb2  = tkinter.Checkbutton(self.top_frame, text='Sausage          (+$3)', variable=self.cb_var2)
        self.cb3  = tkinter.Checkbutton(self.top_frame, text='Pineapple        (+$2)', variable=self.cb_var3)
        self.cb4  = tkinter.Checkbutton(self.top_frame, text='Mooshrooms  (+$4)', variable=self.cb_var4)

        self.cb1.configure(background='#F09898')
        self.cb2.configure(background='#F09898')
        self.cb3.configure(background='#F09898')
        self.cb4.configure(background='#F09898')

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()

        #start pizza crust code
        self.label2 = tkinter.Label(self.frame_2, text = '\nSelect Your Crust Type') #creating a label object, specify where we want it and text
        self.label2.pack(side = 'top')
        self.label2.configure(background='#F09898')


        #create radio buttons for pizza crust options
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
      
        self.rb1 = tkinter.Radiobutton(self.frame_2, text = 'Regular', variable = self.radio_var, value = 1)
      
    
        self.rb2 = tkinter.Radiobutton(self.frame_2, text = 'Cheese Stuffed   (+$5)', variable = self.radio_var, value = 2)

        self.rb3 = tkinter.Radiobutton(self.frame_2, text = 'NY Style   (+$2)', variable = self.radio_var, value = 3)


        #selects regular crust by default
        self.rb1.select()
        
        
        self.rb1.configure(background='#F09898')
        self.rb2.configure(background='#F09898')
        self.rb3.configure(background='#F09898')



        
        #pack radio buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #end pizza crust code

        #adding input box for name of order

        self.prompt_label = tkinter.Label(self.order_frame, text = ' \n Enter a name for the order:')
        self.prompt_label.configure(background='#F09898')

        
        self.name_entry = tkinter.Entry(self.order_frame,width = 10)

        self.prompt_label.pack(side = 'top')
        self.name_entry.pack(side = 'top')


        self.orderButton = tkinter.Button(self.main_window, text = 'Order', command = self.calculate_topping_cost) #creating a button in main window that has text and does something when clicked

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.quit_button.pack(side = 'right')
        self.orderButton.pack(side = 'left')
        

        self.top_frame.pack(side ='top')  #PACK THE FRAMES!
        self.frame_2.pack(side = 'top')
        self.order_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

        tkinter.mainloop() 


    def calculate_topping_cost(self):
        self.message = 'Name on Order: \n'
        self.message2 = ' '
        name = (self.name_entry.get())
        
        if self.name_entry.get():
            self.message += self.name_entry.get()
        tkinter.messagebox.showinfo('Response', self.message)


        total_cost = 10 # default price for pizza
        if self.cb_var1.get() == 1:
            total_cost += 1
        if self.cb_var2.get() == 1:
            total_cost += 3
        if self.cb_var3.get() == 1:
            total_cost += 2
        if self.cb_var4.get() == 1:
            total_cost += 4
        if self.radio_var.get() == 2:
            total_cost += 5
        if self.radio_var.get() == 3:
            total_cost += 2
        self.message3 = 'Total Cost of Piza:' +' $' + str(total_cost)
        tkinter.messagebox.showinfo('Response', self.message3)


my_gui = MyGUI() #creating an instance 