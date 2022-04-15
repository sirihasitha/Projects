from tkinter import *
import time
from tkinter import messagebox
from PIL import Image,ImageTk
from random import randint

class Ludo:
    def __init__(self, window,one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block):
        print("Welcome to Ludo! \nLet's start the game")
        self.root = window
        canvas_width = (15*40) + 200
        canvas_height = (15*40) + 30
        self.root.title("LUDO")
        self.root.geometry(f"{canvas_width}x{canvas_height}")
        self.can_widget = Canvas(self.root, width = canvas_width, height = canvas_height, bg = "light green")
        #self.root.config(bg = "light green")
        self.can_widget.pack()
        #self.board_setup()

        #storing the 4 coins of each color in each list 
        self.made_red_coin = []
        self.made_green2_coin = []
        self.made_yellow_coin = []
        self.made_turquoise1_coin = []

        #storing the coin numbers of each color
        self.red_number_label = []
        self.green2_number_label = []
        self.yellow_number_label = []
        self.turquoise1_number_label = []

        self.block_value_predict = []
        self.total_people_play = []

        self.red_coord_store = [-1, -1, -1, -1]
        self.green2_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.turquoise1_coord_store = [-1, -1, -1, -1]

        self.red_coin_position = [0, 1, 2, 3]
        self.green2_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.turquoise1_coin_position = [0, 1, 2, 3]
	
        self.block_number_side = [one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block]
#each coin poition set to -1 by default
        for index in range(len(self.red_coin_position)):
            self.red_coin_position[index] = -1
            self.green2_coin_position[index] = -1
            self.yellow_coin_position[index] = -1
            self.turquoise1_coin_position[index] = -1

        self.move_red_counter = 0
        self.move_green2_counter = 0
        self.move_yellow_counter = 0
        self.move_turquoise1_counter = 0

        self.take_permission = 0
        self.six_with_overlap = 0

        self.red_store_active = 0
        self.turquoise1_store_active = 0
        self.yellow_store_active = 0
        self.green2_store_active = 0
        
        self.time_for = -1
        self.six_counter = 0
        #self.take_initial_control()
        self.board_setup()

        self.instruction_btn_red()
        self.instruction_btn_turquoise1()
        self.instruction_btn_yellow()
        self.instruction_btn_green2()

        self.take_initial_control()

        
#creating ludo board 

    def board_setup(self):
#creating base rectangles
        self.can_widget.create_rectangle(100, 15, 100 + (15 * 40),15 + (15 * 40), width=5, fill="white")
        self.can_widget.create_rectangle(100, 15, 100 + (6 * 40), 15 + (6 * 40), width=5, fill="red")
        self.can_widget.create_rectangle(100 + (9 *40), 15, 100 + (15*40), 15 + (6 * 40), width=5, fill="yellow")
        self.can_widget.create_rectangle(100, 15 + (9 * 40), 100 + (6 * 40), 15 + (15 * 40), width=5, fill="turquoise1")
        self.can_widget.create_rectangle(100 + (9 * 40), 15 + (9 * 40), 100 + (15 * 40), 15 + (15 * 40), width=5, fill="green2")

#creating quit
        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side = BOTTOM)

        self.quit_button = Button(self.bottomFrame, text = "Quit", font = ("Helvetica", 50), bg = "orange", fg = "black", command = root.destroy)
        self.quit_button.pack(side = RIGHT)


#creating grid rectangles
        def create_boxes(start_point_x, start_point_y, end_point_x, end_point_y):
            for x in range(start_point_x, end_point_x, 40):
                for y in range(start_point_y, end_point_y, 40):
                    self.can_widget.create_rectangle(x, y, x + 40, y + 40, width = "3")
    

        create_boxes(100 + (6 * 40), 15, 100 + (9 * 40), 15 + (6 * 40))
        create_boxes(100, 15 + (6 * 40), 100 + (6 * 40), 15 + (9 * 40))
        create_boxes(100 + (6 * 40), 15 + (9 * 40), 100 + (9 * 40), 15 + (15 * 40))
        create_boxes(100 + (9 * 40), 15 + (6 * 40), 100 + (15 * 40), 15 + (9 * 40))

#coloring homepath
        def color_horizontal(start_point_x, start_point_y, end_point_x, end_point_y, color):
            for x in range(start_point_x, end_point_x, 40):
                self.can_widget.create_rectangle(x, start_point_y, x + 40, end_point_y + 40, fill = color)
        def color_vertical(start_point_x, start_point_y, end_point_x, end_point_y, color):
            for y in range(start_point_y, end_point_y, 40):
                self.can_widget.create_rectangle(start_point_x, y, start_point_x + 40, y +40, fill = color)



        color_horizontal(100 + 40, 15 + (7 * 40), 100 + (6 * 40), 15 + (7 * 40), "red")
        color_horizontal(100 + (9 * 40), 15 + (7 * 40), 100 + (14 * 40), 15 + (7 * 40), "green2")

        color_vertical(100 + (7 * 40), 15 + 40, 100 + (8 * 40), 15 + (6 * 40), "yellow")
        color_vertical(100 + (7 * 40), 15 + (9 * 40), 100 + (8 * 40), 15 + (14 * 40), "turquoise1")


#color start positions
        self.can_widget.create_rectangle(100 + 40, 15 + (6 * 40), 100 + 80, 15 + (7 * 40), fill = "red")
        self.can_widget.create_rectangle(100 + (13 * 40), 15 + (8 * 40), 100 + (14 * 40), 15 + (9 * 40), fill = "green2")
        self.can_widget.create_rectangle(100 + (8 * 40), 15 + 40, 100 + (9 * 40), 15 + 80, fill = "yellow")
        self.can_widget.create_rectangle(100 + (6 * 40), 15 + (13 * 40), 100 + (7 * 40), 15 + (14 * 40), fill = "turquoise1")


#coloring home triangles
        self.can_widget.create_polygon(100 + (6 * 40), 15 + (6 * 40), 120 + (7 * 40), 35 + (7 * 40), 100 + (6 * 40), 15 + (9 * 40), fill = "red")
        self.can_widget.create_polygon(100 + (6 * 40), 15 + (6 * 40), 120 + (7 * 40), 35 + (7 * 40), 100 + (9 * 40), 15 + (6 * 40), fill = "yellow")
        self.can_widget.create_polygon(100 + (9 * 40), 15 + (6 * 40), 120 + (7 * 40), 35 + (7 * 40), 100 + (9 * 40), 15 + (9 * 40), fill = "green2")
        self.can_widget.create_polygon(100 + (6 * 40), 15 + (9 * 40), 120 + (7 * 40), 35 + (7 * 40), 100 + (9 * 40), 15 + (9 * 40), fill = "turquoise1")

#adding border to home square
        self.can_widget.create_rectangle(100 + (6 * 40), 15 + (6 * 40), 100 + (9 * 40), 15 + (9 * 40), width = 3)
        self.can_widget.create_line(100 + (6 * 40), 15 + (6 * 40), 100 + (9 * 40), 15 + (9 * 40), width = 3)
        self.can_widget.create_line(100 + (9 * 40), 15 + (6 * 40), 100 + (6 * 40), 15 + (9 * 40), width = 3)

#creating star safe positons
        def create_star(start_point_x, start_point_y):
            self.can_widget.create_polygon(start_point_x + 20, start_point_y, start_point_x + 8, start_point_y + 40, start_point_x + 40, start_point_y + 15, start_point_x, start_point_y + 15, start_point_x + 40 - 8, start_point_y + 40, fill = "black")

        create_star(100 + (2 * 40), 15 + (8 * 40))
        create_star(100 + (6 * 40), 15 + (2 * 40))
        create_star(100 + (12 * 40), 15 + (6 * 40))
        create_star(100 + (8 * 40), 15 + (12 * 40))



#creating coin positions 
        def create_small_box(start_point_x, start_point_y, color):
            self.can_widget.create_rectangle(start_point_x + 20, start_point_y + 20, start_point_x + 220, start_point_y + 220, width = 0, fill = "white")


            self.can_widget.create_rectangle(start_point_x + 40, start_point_y + 40, start_point_x + 80, start_point_y + 80, width = 4, fill = color)
            self.can_widget.create_rectangle(start_point_x + 160, start_point_y + 40, start_point_x + 200, start_point_y + 80, width = 4, fill = color)
            self.can_widget.create_rectangle(start_point_x + 40, start_point_y + 160, start_point_x + 80, start_point_y + 200, width = 4, fill = color)
            self.can_widget.create_rectangle(start_point_x + 160, start_point_y + 160, start_point_x + 200, start_point_y + 200, width = 4, fill = color)
        


        create_small_box(100, 15, "red")
        create_small_box(100, (9 * 40) + 15, "turquoise1")
        create_small_box(100 + (9 * 40), 15, "yellow")
        create_small_box(100 + (9 * 40), 15 + (9 * 40), "green2")


#red coins stored in list and red coin numbers stored in list
        start_point_x_red = 100
        start_point_y_red = 15
        red_1_coin = self.can_widget.create_oval(start_point_x_red + 40, start_point_y_red + 40, start_point_x_red + 80, start_point_y_red + 80, width = 3, fill = "red", outline = "black")
        red_1_label = Label(self.can_widget, text = "1", font = ("Aries", 16, "bold") ,  bg="red", fg="black")
        red_1_label.place(x = start_point_x_red + 50,y = start_point_y_red + 45)

        red_2_coin = self.can_widget.create_oval(start_point_x_red + 160, start_point_y_red + 40, start_point_x_red + 200, start_point_y_red + 80, width = 3, fill = "red",outline="black")
        red_2_label = Label(self.can_widget, text = "2", font = ("Aries", 16, "bold") , bg="red", fg= "black")
        red_2_label.place(x = start_point_x_red + 170,y = start_point_y_red + 45)

        red_3_coin = self.can_widget.create_oval(start_point_x_red + 40, start_point_y_red + 160, start_point_x_red + 80, start_point_y_red + 200, width = 3, fill = "red", outline="black")
        red_3_label = Label(self.can_widget, text = "3", font = ("Aries", 16, "bold") , bg="red", fg="black")
        red_3_label.place(x = start_point_x_red + 50, y= start_point_y_red + 165)

        red_4_coin = self.can_widget.create_oval(start_point_x_red + 160, start_point_y_red + 160, start_point_x_red+ 200, start_point_y_red + 200, width = 3, fill = "red", outline="black")
        red_4_label = Label(self.can_widget, text = "4", font = ("Aries", 16, "bold") ,bg="red", fg="black")
        red_4_label.place(x = start_point_x_red + 170, y = start_point_y_red + 165)            
        
        self.made_red_coin.append(red_1_coin)
        self.made_red_coin.append(red_2_coin)
        self.made_red_coin.append(red_3_coin)
        self.made_red_coin.append(red_4_coin)
        
        self.red_number_label.append(red_1_label)
        self.red_number_label.append(red_2_label)
        self.red_number_label.append(red_3_label)
        self.red_number_label.append(red_4_label)
            
            
            
#turquoise1 coins and turquoise1 coin numbers stored in list
        start_point_x_bl = 100
        start_point_y_bl = (9 * 40) + 15
        turquoise1_1_coin = self.can_widget.create_oval(start_point_x_bl + 40, start_point_y_bl + 40, start_point_x_bl + 80, start_point_y_bl + 80, width = 3, fill = "turquoise1", outline="black")
        turquoise1_1_label = Label(self.can_widget, text = "1", font = ("Aries", 16, "bold"), bg="turquoise1", fg="black")
        turquoise1_1_label.place(x = start_point_x_bl + 50, y = start_point_y_bl + 45)

        turquoise1_2_coin = self.can_widget.create_oval(start_point_x_bl + 160, start_point_y_bl + 40, start_point_x_bl + 200, start_point_y_bl + 80, width = 3, fill = "turquoise1", outline="black")
        turquoise1_2_label = Label(self.can_widget, text = "2", font = ("Aries", 16, "bold"), bg="turquoise1", fg="black")
        turquoise1_2_label.place(x = start_point_x_bl + 170, y = start_point_y_bl + 45)

        turquoise1_3_coin = self.can_widget.create_oval(start_point_x_bl + 40, start_point_y_bl + 160, start_point_x_bl + 80, start_point_y_bl + 200, width = 3, fill = "turquoise1", outline="black")
        turquoise1_3_label = Label(self.can_widget, text = "3", font = ("Aries", 16, "bold"), bg="turquoise1", fg="black")
        turquoise1_3_label.place(x = start_point_x_bl + 50, y = start_point_y_bl + 165)	

        turquoise1_4_coin = self.can_widget.create_oval(start_point_x_bl + 160, start_point_y_bl + 160, start_point_x_bl + 200, start_point_y_bl + 200, width = 3, fill = "turquoise1",outline="black")
        turquoise1_4_label = Label(self.can_widget, text = "4", font = ("Aries", 16, "bold") , bg="turquoise1", fg="black")
        turquoise1_4_label.place(x = start_point_x_bl + 170, y = start_point_y_bl + 165)
        
        self.made_turquoise1_coin.append(turquoise1_1_coin)
        self.made_turquoise1_coin.append(turquoise1_2_coin)
        self.made_turquoise1_coin.append(turquoise1_3_coin)
        self.made_turquoise1_coin.append(turquoise1_4_coin)
        
        self.turquoise1_number_label.append(turquoise1_1_label)
        self.turquoise1_number_label.append(turquoise1_2_label)
        self.turquoise1_number_label.append(turquoise1_3_label)
        self.turquoise1_number_label.append(turquoise1_4_label)
            
            
            
#green2 coins and green2 coin numbers stored in list
        start_point_x_gr = 100 + (9 * 40)
        start_point_y_gr = 15 + (9 * 40)
        green2_1_coin = self.can_widget.create_oval(start_point_x_gr + 40, start_point_y_gr + 40, start_point_x_gr + 80, start_point_y_gr + 80, width = 3, fill = "green2", outline="black")
        green2_1_label = Label(self.can_widget, text = "1", font = ("Aries", 16, "bold") , bg="green2", fg="black")
        green2_1_label.place(x = start_point_x_gr + 50, y = start_point_y_gr + 45)

        green2_2_coin = self.can_widget.create_oval(start_point_x_gr + 160, start_point_y_gr + 40, start_point_x_gr + 200, start_point_y_gr + 80, width = 3, fill = "green2",outline = "black")
        green2_2_label = Label(self.can_widget, text = "2", font = ("Aries", 16, "bold") , bg="green2", fg="black")
        green2_2_label.place(x = start_point_x_gr + 170,y =  start_point_y_gr + 45)

        green2_3_coin = self.can_widget.create_oval(start_point_x_gr + 40, start_point_y_gr + 160, start_point_x_gr + 80, start_point_y_gr+ 200, width = 3, fill = "green2", outline="black")
        green2_3_label = Label(self.can_widget, text = "3", font = ("Aries", 16, "bold"), bg="green2", fg="black")
        green2_3_label.place(x = start_point_x_gr + 50, y = start_point_y_gr + 165)	

        green2_4_coin = self.can_widget.create_oval(start_point_x_gr + 160, start_point_y_gr + 160, start_point_x_gr + 200, start_point_y_gr + 200, width = 3, fill = "green2", outline="black")
        green2_4_label = Label(self.can_widget, text = "4", font = ("Aries", 16, "bold"), bg="green2", fg="black")
        green2_4_label.place(x = start_point_x_gr + 170, y = start_point_y_gr + 165)        
        
        self.made_green2_coin.append(green2_1_coin)
        self.made_green2_coin.append(green2_2_coin)
        self.made_green2_coin.append(green2_3_coin)
        self.made_green2_coin.append(green2_4_coin)
        
        self.green2_number_label.append(green2_1_label)
        self.green2_number_label.append(green2_2_label)
        self.green2_number_label.append(green2_3_label)
        self.green2_number_label.append(green2_4_label)   
            
#yellow coins and yellow coin numbers stored in list
        start_point_x_yelw = 100 + (9 * 40) 
        start_point_y_yelw = 15
        yellow_1_coin = self.can_widget.create_oval(start_point_x_yelw + 40, start_point_y_yelw + 40, start_point_x_yelw + 80, start_point_y_yelw + 80, width = 3, fill = "yellow",outline="black")
        yellow_1_label = Label(self.can_widget, text = "1", font = ("Aries", 16, "bold"), bg="yellow", fg="black")
        yellow_1_label.place(x = start_point_x_yelw + 50, y = start_point_y_yelw + 45)

        yellow_2_coin = self.can_widget.create_oval(start_point_x_yelw + 160, start_point_y_yelw + 40, start_point_x_yelw + 200, start_point_y_yelw + 80, width = 3, fill = "yellow",outline="black")
        yellow_2_label = Label(self.can_widget, text = "2", font = ("Aries", 16, "bold") , bg="yellow", fg="black")
        yellow_2_label.place(x = start_point_x_yelw + 170, y = start_point_y_yelw + 45)

        yellow_3_coin = self.can_widget.create_oval(start_point_x_yelw + 40, start_point_y_yelw + 160, start_point_x_yelw + 80, start_point_y_yelw + 200, width = 3, fill = "yellow",outline="black")
       	yellow_3_label = Label(self.can_widget, text = "3", font = ("Aries", 16, "bold"), bg="yellow", fg="black")
        yellow_3_label.place(x = start_point_x_yelw + 50, y = start_point_y_yelw + 165)

        yellow_4_coin = self.can_widget.create_oval(start_point_x_yelw + 160, start_point_y_yelw + 160, start_point_x_yelw + 200, start_point_y_yelw + 200, width = 3, fill ="yellow", outline="black")
       	yellow_4_label = Label(self.can_widget, text = "4", font = ("Aries", 16, "bold"), bg="yellow", fg="black")
        yellow_4_label.place(x = start_point_x_yelw + 170, y = start_point_y_yelw + 165)            
        
        self.made_yellow_coin.append(yellow_1_coin)
        self.made_yellow_coin.append(yellow_2_coin)
        self.made_yellow_coin.append(yellow_3_coin)
        self.made_yellow_coin.append(yellow_4_coin)
        
        self.yellow_number_label.append(yellow_1_label)
        self.yellow_number_label.append(yellow_2_label)
        self.yellow_number_label.append(yellow_3_label)
        self.yellow_number_label.append(yellow_4_label)

          
#def take_initial_control(self):
    def take_initial_control(self):
        self.root.withdraw()
        for i in range(4):
            self.block_value_predict[i][1]['state'] = DISABLED

# Make other window to control take
        
        top = Toplevel()
        top.wm_attributes("-topmost",1)
        top.title('WELCOME TO LUDO')
        top.geometry("800x640")
        top.maxsize(800,640)
        top.minsize(800,640)
        top.config(bg="light green")

        head = Label(top,text="Enter the number of players:- ",font=("Arial",38,"italic","bold"),bg="light green",fg="black")
        head.place(x=75,y=165)
        take_entry = Entry(top,font=("Arial",18,"bold","italic"),relief=SUNKEN,bd=7,width=12)
        take_entry.place(x=300,y=280)
        take_entry.focus()

#player input value filtering
        def filtering():
            response_take = self.input_filtering(take_entry.get())
            if response_take is True and int(take_entry.get())>1:
                self.root.deiconify()
                for player_index in range(int(take_entry.get())):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)
                self.make_command()
                top.destroy()
            else:
                messagebox.showerror("Input Error", "Please input number of players between 2 and 4")

        submit_btn = Button(top,text="Submit",bg="white",fg="black",font=("Arial",13,"bold"),relief=RAISED,bd=8,command=filtering)
        submit_btn.place(x=340,y=370)
        top.mainloop()        




    def red_circle_start_position(self, coin_number):
        self.can_widget.delete(self.made_red_coin[int(coin_number)-1])
        self.made_red_coin[int(coin_number)-1] = self.can_widget.create_oval(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3, outline="black")

        self.red_number_label[int(coin_number)-1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.red_number_label[int(coin_number)-1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_coin_position[int(coin_number)-1] = 1
        self.root.update()
        time.sleep(0.2)


    def green2_circle_start_position(self,coin_number):
        self.can_widget.delete(self.made_green2_coin[int(coin_number)-1])
        #self.made_green2_coin[int(coin_number)-1] = self.can_widget.create_oval(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="green2", width=3)
        self.made_green2_coin[int(coin_number)-1] = self.can_widget.create_oval(620, 335, 660, 375, fill = "green2", width=3)
        self.green2_number_label[int(coin_number)-1].place_forget()
        #green2_start_label_x = 100 + (40*8) + 10
        green2_start_label_x = 630
        green2_start_label_y = 340
        self.green2_number_label[int(coin_number)-1].place(x=green2_start_label_x, y=green2_start_label_y)

        self.green2_coin_position[int(coin_number)-1] = 27
        self.root.update()
        time.sleep(0.2)


    def yellow_circle_start_position(self,coin_number):
        self.can_widget.delete(self.made_yellow_coin[int(coin_number)-1])
        #self.made_yellow_coin[int(coin_number)-1] = self.can_widget.create_oval(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)
        self.made_yellow_coin[int(coin_number) -1] = self.can_widget.create_oval(420, 55, 460, 95, fill="yellow", width=3)
        self.yellow_number_label[int(coin_number)-1].place_forget()
        yellow_start_label_x = 430
        yellow_start_label_y = 60
        self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.yellow_coin_position[int(coin_number) - 1] = 14
        self.root.update()
        time.sleep(0.2)


    def turquoise1_circle_start_position(self,coin_number):
        self.can_widget.delete(self.made_turquoise1_coin[int(coin_number)-1])
        self.made_turquoise1_coin[int(coin_number)-1] = self.can_widget.create_oval(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="turquoise1",width=3)

        self.turquoise1_number_label[int(coin_number)-1].place_forget()
        turquoise1_start_label_x = 100+240 + 10
        turquoise1_start_label_y = 340+(40*5)-5 + 5
        self.turquoise1_number_label[int(coin_number) - 1].place(x=turquoise1_start_label_x, y=turquoise1_start_label_y)

        self.turquoise1_coin_position[int(coin_number) - 1] = 40
        self.root.update()
        time.sleep(0.2)
                                                                
    def motion_of_coin(self,counter_coin,specific_coin,number_label,number_label_x ,number_label_y,color_coin,path_counter):
        number_label.place(x=number_label_x,y=number_label_y)
        while True:
            if path_counter == 0:
                break
            elif (counter_coin == 51 and color_coin == "red") or (counter_coin==12 and color_coin == "yellow") or (counter_coin == 25 and color_coin == "green2") or (counter_coin == 38 and color_coin == "turquoise1") or counter_coin>=100:
                if counter_coin<100:
                    counter_coin=100

                counter_coin = self.under_room_traversal_control(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin, color_coin)

                if  counter_coin == 106:
                    messagebox.showinfo("Destination reached","Congrats! You now at the destination")
                    if path_counter == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1
                break

            counter_coin += 1
            path_counter -=1
            number_label.place_forget()

            print(counter_coin)

            if counter_coin<=5:
                self.can_widget.move(specific_coin, 40, 0)
                number_label_x+=40
            elif counter_coin == 6:
                self.can_widget.move(specific_coin, 40, -40)
                number_label_x += 40
                number_label_y-=40
            elif 6< counter_coin <=11:
                self.can_widget.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin <=13:
                self.can_widget.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=18:
                self.can_widget.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin == 19:
                self.can_widget.move(specific_coin, 40, 40)
                number_label_x += 40
                number_label_y += 40
            elif counter_coin <=24:
                self.can_widget.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=26:
                self.can_widget.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <=31:
                self.can_widget.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin == 32:
                self.can_widget.move(specific_coin, -40, 40)
                number_label_x -= 40
                number_label_y += 40
            elif counter_coin <= 37:
                self.can_widget.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <= 39:
                self.can_widget.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin <= 44:
                self.can_widget.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 45:
                self.can_widget.move(specific_coin, -40, -40)
                number_label_x -= 40
                number_label_y -= 40
            elif counter_coin <= 50:
                self.can_widget.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif 50< counter_coin <=52:
                self.can_widget.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 53:
                self.can_widget.move(specific_coin, 40, 0)
                number_label_x += 40
                counter_coin = 1

            number_label.place_forget()
            number_label.place(x=number_label_x, y=number_label_y)

            self.root.update()
            time.sleep(0.1)

        return counter_coin

    def under_room_traversal_control(self,specific_coin,number_label,number_label_x,number_label_y,path_counter,counter_coin,color_coin):
        if color_coin == "red" and counter_coin >= 100:
            if int(counter_coin)+int(path_counter)<=106:
               counter_coin = self.room_red_traversal(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin)

        elif color_coin == "green2" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_green2_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "yellow" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_yellow_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "turquoise1" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_turquoise1_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        return counter_coin


    def room_red_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter>0:
            counter_coin += 1
            path_counter -= 1
            self.can_widget.move(specific_coin, 40, 0)
            number_label_x+=40
            number_label.place(x=number_label_x,y=number_label_y)
            self.root.update()
            time.sleep(0.2)
        return counter_coin

    def room_green2_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.can_widget.move(specific_coin, -40, 0)
            number_label_x -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.root.update()
            time.sleep(0.2)
        return counter_coin

    def room_yellow_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.can_widget.move(specific_coin, 0, 40)
            number_label_y += 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.root.update()
            time.sleep(0.2)
        return counter_coin

    def room_turquoise1_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.can_widget.move(specific_coin, 0, -40)
            number_label_y -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.root.update()
            time.sleep(0.2)
        return counter_coin
    
    def main_controller(self, color_coin, coin_number):
        processing_result = self.input_filtering(coin_number)# Value filtering
        if processing_result is True:
            pass
        else:
            messagebox.showerror("Wrong input number","Please input the coin number between 1 to 4")
            return

        if  color_coin == "red":
            self.block_value_predict[0][3]['state'] = DISABLED

            if self.move_red_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.red_coin_position[int(coin_number)-1] == -1 and self.move_red_counter == 6:
                self.red_circle_start_position(coin_number)
                self.red_coord_store[int(coin_number) - 1] = 1

            elif self.red_coin_position[int(coin_number)-1] > -1:
                take_coord = self.can_widget.coords(self.made_red_coin[int(coin_number)-1])
                red_start_label_x = take_coord[0] + 10
                red_start_label_y = take_coord[1] + 5
                self.red_number_label[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_coin_position[int(coin_number)-1]+self.move_red_counter<=106:
                   self.red_coin_position[int(coin_number)-1] = self.motion_of_coin(self.red_coin_position[int(coin_number) - 1],self.made_red_coin[int(coin_number)-1],self.red_number_label[int(coin_number)-1],red_start_label_x,red_start_label_y,"red",self.move_red_counter)
                else:
                   messagebox.showerror("Not possible","Sorry, not permitted")
                   self.block_value_predict[0][3]['state'] = NORMAL
                   return

                if  self.red_coin_position[int(coin_number)-1]==22 or self.red_coin_position[int(coin_number)-1]==9 or self.red_coin_position[int(coin_number)-1]==48 or self.red_coin_position[int(coin_number)-1]==35 or self.red_coin_position[int(coin_number)-1]==14 or self.red_coin_position[int(coin_number)-1]==27 or self.red_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.red_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.red_coin_position[int(coin_number)-1],color_coin, self.move_red_counter)

                self.red_coord_store[int(coin_number)-1] = self.red_coin_position[int(coin_number)-1]

            else:
                messagebox.showerror("Wrong choice","Sorry, Your coin in not permitted to travel")
                self.block_value_predict[0][3]['state'] = NORMAL
                return

            self.block_value_predict[0][1]['state'] = NORMAL


        elif color_coin == "green2":
            self.block_value_predict[2][3]['state'] = DISABLED

            if self.move_green2_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.green2_coin_position[int(coin_number) - 1] == -1 and self.move_green2_counter == 6:
                self.green2_circle_start_position(coin_number)
                self.green2_coord_store[int(coin_number) - 1] = 27

            elif self.green2_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.can_widget.coords(self.made_green2_coin[int(coin_number) - 1])
                green2_start_label_x = take_coord[0] + 10
                green2_start_label_y = take_coord[1] + 5
                self.green2_number_label[int(coin_number) - 1].place(x=green2_start_label_x, y=green2_start_label_y)


                if  self.green2_coin_position[int(coin_number) - 1] + self.move_green2_counter <= 106:
                    self.green2_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.green2_coin_position[int(coin_number) - 1], self.made_green2_coin[int(coin_number) - 1], self.green2_number_label[int(coin_number) - 1], green2_start_label_x, green2_start_label_y, "green2", self.move_green2_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   self.block_value_predict[2][3]['state'] = NORMAL
                   return


                if  self.green2_coin_position[int(coin_number)-1]==22 or self.green2_coin_position[int(coin_number)-1]==9 or self.green2_coin_position[int(coin_number)-1]==48 or self.green2_coin_position[int(coin_number)-1]==35 or self.green2_coin_position[int(coin_number)-1]==1 or self.green2_coin_position[int(coin_number)-1]==14 or self.green2_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.green2_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.green2_coin_position[int(coin_number) - 1],color_coin, self.move_green2_counter)

                self.green2_coord_store[int(coin_number) - 1] = self.green2_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.block_value_predict[2][3]['state'] = NORMAL
                return

            self.block_value_predict[2][1]['state'] = NORMAL


        elif color_coin == "yellow":
            self.block_value_predict[3][3]['state'] = DISABLED

            if self.move_yellow_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.yellow_coin_position[int(coin_number) - 1] == -1 and self.move_yellow_counter == 6:
                self.yellow_circle_start_position(coin_number)
                self.yellow_coord_store[int(coin_number) - 1] = 14

            elif self.yellow_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.can_widget.coords(self.made_yellow_coin[int(coin_number) - 1])
                yellow_start_label_x = take_coord[0] + 10
                yellow_start_label_y = take_coord[1] + 5
                self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if  self.yellow_coin_position[int(coin_number) - 1] + self.move_yellow_counter <= 106:
                    self.yellow_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.yellow_coin_position[int(coin_number) - 1], self.made_yellow_coin[int(coin_number) - 1], self.yellow_number_label[int(coin_number) - 1], yellow_start_label_x, yellow_start_label_y, "yellow", self.move_yellow_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   self.block_value_predict[3][3]['state'] = NORMAL
                   return

                if  self.yellow_coin_position[int(coin_number)-1]==22 or self.yellow_coin_position[int(coin_number)-1]==9 or self.yellow_coin_position[int(coin_number)-1]==48 or self.yellow_coin_position[int(coin_number)-1]==35 or self.yellow_coin_position[int(coin_number)-1]==1 or self.yellow_coin_position[int(coin_number)-1]==27 or self.yellow_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.yellow_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.yellow_coin_position[int(coin_number) - 1],color_coin, self.move_yellow_counter)

                self.yellow_coord_store[int(coin_number) - 1] = self.yellow_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.block_value_predict[3][3]['state'] = NORMAL
                return

            self.block_value_predict[3][1]['state'] = NORMAL


        elif color_coin == "turquoise1":
            self.block_value_predict[1][3]['state'] = DISABLED
            if self.move_red_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.turquoise1_coin_position[int(coin_number) - 1] == -1 and self.move_turquoise1_counter == 6:
                self.turquoise1_circle_start_position(coin_number)
                self.turquoise1_coord_store[int(coin_number) - 1] = 40

            elif self.turquoise1_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.can_widget.coords(self.made_turquoise1_coin[int(coin_number) - 1])
                turquoise1_start_label_x = take_coord[0] + 10
                turquoise1_start_label_y = take_coord[1] + 5
                self.turquoise1_number_label[int(coin_number) - 1].place(x=turquoise1_start_label_x, y=turquoise1_start_label_y)

                if  self.turquoise1_coin_position[int(coin_number) - 1] + self.move_turquoise1_counter <= 106:
                    self.turquoise1_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.turquoise1_coin_position[int(coin_number) - 1], self.made_turquoise1_coin[int(coin_number) - 1], self.turquoise1_number_label[int(coin_number) - 1], turquoise1_start_label_x, turquoise1_start_label_y, "turquoise1", self.move_turquoise1_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   self.block_value_predict[1][3]['state'] = NORMAL
                   return

                if  self.turquoise1_coin_position[int(coin_number)-1]==22 or self.turquoise1_coin_position[int(coin_number)-1]==9 or self.turquoise1_coin_position[int(coin_number)-1]==48 or self.turquoise1_coin_position[int(coin_number)-1]==35 or self.turquoise1_coin_position[int(coin_number)-1]==1 or self.turquoise1_coin_position[int(coin_number)-1]==14 or self.turquoise1_coin_position[int(coin_number)-1]==27:
                    pass
                else:
                    if self.turquoise1_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.turquoise1_coin_position[int(coin_number) - 1],color_coin, self.move_turquoise1_counter)

                self.turquoise1_coord_store[int(coin_number) - 1] = self.turquoise1_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.block_value_predict[1][3]['state'] = NORMAL
                return

            self.block_value_predict[1][1]['state'] = NORMAL

        print(self.red_coord_store)
        print(self.green2_coord_store)
        print(self.yellow_coord_store)
        print(self.turquoise1_coord_store)

        permission_granted_to_proceed = True

        if  color_coin == "red" and self.red_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "green2" and self.green2_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "yellow" and self.yellow_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "turquoise1" and self.turquoise1_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)

        if permission_granted_to_proceed:# if that is False, Game is over and not proceed more
            self.make_command()


    def make_command(self):
        if  self.time_for == -1:
            pass
        else:
            self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if  self.time_for == len(self.total_people_play)-1:
            self.time_for = -1

        self.time_for+=1
        self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = NORMAL

    def check_winner_and_runner(self,color_coin):
        destination_reached = 0 # Check for all specific color coins
        if color_coin == "red":
            temp_store = self.red_coord_store
            temp_delete = 0# Player index
        elif color_coin == "green2":
            temp_store = self.green2_coord_store
            temp_delete = 3# Player index
        elif color_coin == "yellow":
            temp_store = self.yellow_coord_store
            temp_delete = 2# Player index
        else:
            temp_store = self.turquoise1_coord_store
            temp_delete = 1# Player index

        for take in temp_store:
            if take == 106:
                destination_reached = 1
            else:
                destination_reached = 0
                break

        if  destination_reached == 1:# If all coins in block reach to the destination, winner and runner check
            self.take_permission += 1
            if self.take_permission == 1:# Winner check
                messagebox.showinfo("Winner","Congrats! You are the winner")
                
            elif self.take_permission == 2:# 1st runner check
                messagebox.showinfo("Winner", "Wow! You are 1st runner")
                
            elif self.take_permission == 3:# 2nd runner check
                messagebox.showinfo("Winner", "Wow! You are 2nd runner")
                

            self.block_value_predict[temp_delete][1]['state'] = DISABLED
            self.total_people_play.remove(temp_delete)

            if len(self.total_people_play) == 1:
                messagebox.showinfo("Game Over","Good bye!!!!")
                self.block_value_predict[0][1]['state'] = DISABLED
                return False
            else:
                self.time_for-=1
        else:
            print("Winner not decided")

        return True

#Conditions when a coin is killed

    def coord_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
        if  color_coin!="red":
            for take_coin_number in range(len(self.red_coord_store)):
                if  self.red_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap=1
                    else:
                        self.time_for-=1

                    self.can_widget.delete(self.made_red_coin[take_coin_number])
                    self.red_number_label[take_coin_number].place_forget()
                    self.red_coin_position[take_coin_number] = -1
                    self.red_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                       remade_coin = self.can_widget.create_oval(100+40, 15+40, 100 + 80, 15+40+40, width=3, fill="red", outline="black")
                       self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 1:
                        remade_coin = self.can_widget.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 2:
                        remade_coin = self.can_widget.create_oval(100 + 40, 15 + 60 + 100, 100 + 80, 15 + 200, width=3, fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 60 + 100 + 5)
                    else:
                        remade_coin = self.can_widget.create_oval(100 + 160, 15 + 60 + 100, 100 + 200, 15 + 200, width=3,fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 160 + 10, y=15 + 60 + 100 + 5)

                    self.made_red_coin[take_coin_number]=remade_coin

        if  color_coin != "yellow":
            for take_coin_number in range(len(self.yellow_coord_store)):
                if  self.yellow_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for-=1

                    self.can_widget.delete(self.made_yellow_coin[take_coin_number])
                    self.yellow_number_label[take_coin_number].place_forget()
                    self.yellow_coin_position[take_coin_number] = -1
                    self.yellow_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 40, 15 + 40, 100 + (9 * 40) + 80, 15 + 80, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=100 + (9 * 40) + 50, y=15 + 45)
                    elif take_coin_number == 1:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 160, 15 + 40, 100 + (9 * 40) + 200, 15 + 80, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=100 + (9 * 40) + 170, y=15 + 45)
                    elif take_coin_number == 2:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 40, 15 + 160, 100 + (9 * 40) + 80, 15 + 200, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=100 + (9 * 40) + 50, y=15 + 165)
                    else:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 160, 15 + 160, 100 + (9 * 40) + 200, 15 + 200, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=100 + (9 * 40) + 170, y=15 + 165 )

                    self.made_yellow_coin[take_coin_number] = remade_coin


        if  color_coin != "green2":
            for take_coin_number in range(len(self.green2_coord_store)):
                if  self.green2_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.can_widget.delete(self.made_green2_coin[take_coin_number])
                    self.green2_number_label[take_coin_number].place_forget()
                    self.green2_coin_position[take_coin_number] = -1
                    self.green2_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 40, 15 + (9 * 40) + 40, 100 + (9 * 40) + 80, 15 + (9 * 40) + 80, width=3, fill="green2", outline="black")
                        self.green2_number_label[take_coin_number].place(x=100 + (9 * 40) + 50, y=15 + (9 * 40) +45)
                    elif take_coin_number == 1:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 160, 15 + (9 * 40) + 40, 100 + (9 * 40) + 200, 15 + (9 * 40) + 80, width=3, fill="green2", outline="black")
                        self.green2_number_label[take_coin_number].place(x=100 + (9 * 40) + 170, y= 15 + ( 9 * 40) + 45)
                    elif take_coin_number == 2:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 40, 15 + (9 * 40) + 160, 100 + (9 * 40) + 80, 15 + (9 * 40) +200, width=3, fill="green2", outline="black")
                        self.green2_number_label[take_coin_number].place(x=100 + (9 * 40) + 50, y=15 + (9 * 40) + 165)
                    else:
                        remade_coin = self.can_widget.create_oval(100 + (9 * 40) + 160, 15 + (9 * 40) + 160, 100 + (9 *40) + 200, 15 + (9 * 40) +200, width=3, fill="green2", outline="black")
                        self.green2_number_label[take_coin_number].place(x=100 + (40 * 9) + 170, y=15 + (9 * 40) + 165)

                    self.made_green2_coin[take_coin_number] = remade_coin

        if  color_coin != "turquoise1":
            for take_coin_number in range(len(self.turquoise1_coord_store)):
                if  self.turquoise1_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.can_widget.delete(self.made_turquoise1_coin[take_coin_number])
                    self.turquoise1_number_label[take_coin_number].place_forget()
                    self.turquoise1_coin_position[take_coin_number] = -1
                    self.turquoise1_coord_store[take_coin_number]=-1

                    if take_coin_number == 0:
                        remade_coin = self.can_widget.create_oval(100 + 40, (9 * 40) + 15 + 40, 100 + 40 + 40, (9 * 40 ) + 15 +80, width=3, fill="turquoise1", outline="black")
                        self.turquoise1_number_label[take_coin_number].place(x=100+40+10, y = (9 * 40) + 15 + 45)
                    elif take_coin_number == 1:
                        remade_coin = self.can_widget.create_oval(100 + 160, (9 * 40) + 15 + 40, 100 + 200, (40 * 9) + 15 + 80, width=3, fill="turquoise1", outline="black")
                        self.turquoise1_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y = (9 * 40) + 15 +45)
                    elif take_coin_number == 2:
                        remade_coin = self.can_widget.create_oval(100 + 40, (9 * 40) + 15 +160, 100 + 80, (9 * 40) + 15 +200, width=3, fill="turquoise1", outline="black")
                        self.turquoise1_number_label[take_coin_number].place(x=100 + 40 + 10, y=(9 * 40) + 15 + 165)
                    else:
                        remade_coin = self.can_widget.create_oval( 100 + 160, (9 * 40) + 15 + 160, 100 + 200, (9 * 40) + 15 + 200, width=3, fill="turquoise1", outline="black")
                        self.turquoise1_number_label[take_coin_number].place(x=100+160+10, y=(9 * 40) + 15 + 165)

                    self.made_turquoise1_coin[take_coin_number] = remade_coin


    
    def make_prediction(self,color_indicator):
        try:
            if color_indicator == "red":
                block_value_predict = self.block_value_predict[0]
                permanent_block_number = self.move_red_counter = randint(1, 6)

            elif color_indicator == "turquoise1":
                block_value_predict = self.block_value_predict[1]
                permanent_block_number = self.move_turquoise1_counter = randint(1, 6)

            elif color_indicator == "yellow":
                block_value_predict = self.block_value_predict[3]
                permanent_block_number = self.move_yellow_counter = randint(1, 6)

            else:
                block_value_predict = self.block_value_predict[2]
                permanent_block_number = self.move_green2_counter = randint(1, 6)


            block_value_predict[1]['state'] = DISABLED

            # Illusion of coin floating
            temp_counter = 15
            while temp_counter>0:
                move_temp_counter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
                self.root.update()
                time.sleep(0.1)
                temp_counter-=1

            print("Prediction result: ", permanent_block_number)

            # Permanent predicted value containing image set
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1]
            self.instructional_btn_customization_based_on_current_situation(color_indicator,permanent_block_number,block_value_predict)
        except:
            print("Force stop error")
       
       
   
    def instructional_btn_customization_based_on_current_situation(self,color_indicator,permanent_block_number,block_value_predict):
        if color_indicator == "red":
            temp_coin_position = self.red_coin_position
        elif color_indicator == "green2":
            temp_coin_position = self.green2_coin_position
        elif color_indicator == "yellow":
            temp_coin_position = self.yellow_coin_position
        else:
            temp_coin_position = self.turquoise1_coin_position

        all_in = 1
        for i in range(4):
            if temp_coin_position[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if  permanent_block_number == 6:
            self.six_counter += 1
        else:
            self.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in==0)) and self.six_counter<3:
            permission = 1
            if color_indicator == "red":
                temp = self.red_coord_store
            elif color_indicator == "green2":
                temp = self.green2_coord_store
            elif color_indicator == "yellow":
                temp = self.yellow_coord_store
            else:
                temp = self.turquoise1_coord_store

            if  permanent_block_number<6:
                if self.six_with_overlap == 1:
                    self.time_for-=1
                    self.six_with_overlap=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i]+permanent_block_number<=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.make_command()
            else:
                block_value_predict[3]['state'] = NORMAL# Give btn activation
                block_value_predict[1]['state'] = DISABLED# Predict btn deactivation

        else:
            block_value_predict[1]['state'] = NORMAL# Predict btn activation
            if self.six_with_overlap == 1:
                self.time_for -= 1
                self.six_with_overlap = 0
            self.make_command()

        if  permanent_block_number == 6 and self.six_counter<3 and block_value_predict[3]['state'] == NORMAL:
            self.time_for-=1
        else:
            self.six_counter=0

    # Player Scope controller
    def make_command(self):
        if  self.time_for == -1:
            pass
        else:
            self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if  self.time_for == len(self.total_people_play)-1:
            self.time_for = -1

        self.time_for+=1
        self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = NORMAL
            
            
    def instruction_btn_red(self):
        block_predict_red = Label(self.can_widget,image=self.block_number_side[0])
        block_predict_red.place(x=32,y=8)
        predict_red = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll", font=("Arial", 10, "bold"), command=lambda: self.make_prediction("red"))
        predict_red.place(x=22, y=15 + 40)
        entry_take_red = Entry(self.can_widget,bg="white",fg="red",font=("Arial",18, "bold"),width=2,relief=SUNKEN,bd=5)
        entry_take_red.place(x=32,y=23+80)
        final_move = Button(self.can_widget,bg="black",fg="#00FF00",relief=RAISED,bd=5,text="Coin",font=("Arial",8,"bold"),command=lambda: self.main_controller("red",entry_take_red.get()),state=DISABLED)
        final_move.place(x=17,y=15+140)
        Label(self.can_widget,text="Player 1",fg="black",font=("Arial",15,"bold")).place(x=15,y=15+140+40 + 5)
        self.store_instructional_btn(block_predict_red,predict_red,entry_take_red,final_move)

    def instruction_btn_turquoise1(self):
        block_predict_turquoise1 = Label(self.can_widget, image=self.block_number_side[0])
        block_predict_turquoise1.place(x=32, y=8+(40*6+40*3)+10)
        predict_turquoise1 = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll",font=("Arial", 10, "bold"), command=lambda: self.make_prediction("turquoise1"))
        predict_turquoise1.place(x=22, y=15+(40*6+40*3)+40 + 10)
        entry_take_turquoise1 = Entry(self.can_widget, bg="white", fg="turquoise1", font=("Arial", 18, "bold" ), width=2,relief=SUNKEN, bd=5)
        entry_take_turquoise1.place(x=32, y=23+(40*6+40*3)+40 + 50)
        final_move = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text = "Coin" , font=("Arial", 8, "bold"),command=lambda: self.main_controller("turquoise1",entry_take_turquoise1.get()),state=DISABLED)
        final_move.place(x=17, y=15+(40*6+40*3)+40 + 110)
        Label(self.can_widget, text="Player 2", fg="black", font=("Arial", 15, "bold")).place(x=15,y=15+(40*6+40*3)+40 + 110+ 40 + 5)
        self.store_instructional_btn(block_predict_turquoise1, predict_turquoise1, entry_take_turquoise1, final_move)

    def instruction_btn_yellow(self):
        block_predict_yellow = Label(self.can_widget, image=self.block_number_side[0])
        block_predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+20, y=8 + (40 * 6 + 40 * 3) + 10)
        
        predict_yellow= Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll",font=("Arial", 10, "bold"), command=lambda: self.make_prediction("green2"))
        predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+20, y=15 + (40 * 6 + 40 * 3) + 40 + 10)
        entry_take_yellow = Entry(self.can_widget, bg="white", fg="green2", font=("Arial", 18, "bold"),width=2, relief=SUNKEN, bd=5)
        entry_take_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+23 + 10, y=15 + (40 * 6 + 40 * 3) + 40 + 50 + 10)
        final_move = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Coin",font=("Arial", 8, "bold"),command=lambda: self.main_controller("green2",entry_take_yellow.get()),state=DISABLED)
        final_move.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+17, y=15 + (40 * 6 + 40 * 3) + 40 + 110)
        Label(self.can_widget, text="Player 3", fg="black", font=("Arial", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 3) + 10,y=15 + (40 * 6 + 40 * 3) + 40 + 110 + 40 + 5)
        self.store_instructional_btn(block_predict_yellow, predict_yellow, entry_take_yellow, final_move)

    def instruction_btn_green2(self):
        block_predict_green2 = Label(self.can_widget, image=self.block_number_side[0])
        block_predict_green2.place(x=100+(40*6+40*3+40*6+10)+20, y=8)
        predict_green2 = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll", font=("Arial", 10, "bold"), command=lambda: self.make_prediction("yellow"))
        predict_green2.place(x=100+(40*6+40*3+40*6+2)+20, y=15 + 40)
        entry_take_green2 = Entry(self.can_widget, bg="white", fg="orange", font=("Arial", 18, "bold"), width=2, relief=SUNKEN, bd=5)
        entry_take_green2.place(x=100+(40*6+40*3+40*6+2)+23 + 10, y=15 + 80 + 10)
        final_move = Button(self.can_widget, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Coin",font=("Arial", 8, "bold"),command=lambda: self.main_controller("yellow",entry_take_green2.get()),state=DISABLED)
        final_move.place(x=100+(40*6+40*3+40*6+2)+17, y=15 + 140)
        Label(self.can_widget, text="Player 4", fg="black", font=("Arial", 15, "bold")).place(x=100+(40*6+40*3+40*6+3) + 10, y=15 + 140+40 + 5)
        self.store_instructional_btn(block_predict_green2, predict_green2, entry_take_green2, final_move)


    def store_instructional_btn(self, block_indicator, predictor, entry_controller, give_finally):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        temp.append(give_finally)
        self.block_value_predict.append(temp) 
          
    def input_filtering(self,coin_number):
        try:
            if (4>=int(coin_number)>=1) or type(coin_number) == int:
                return True
            else:
                return False
        except:
            return False

#if __name__ == '__main__':
root = Toplevel()
root.title("LUDO")
#canvas_width = (15*40) + 200
#canvas_height = (15*40) + 30
#root.title("LUDO")
#root.geometry(f"{canvas_width}x{canvas_height}")
six_side_block = ImageTk.PhotoImage(Image.open("6die.png").resize((43, 43), Image.ANTIALIAS))
five_side_block = ImageTk.PhotoImage(Image.open("5die.png").resize((43, 43), Image.ANTIALIAS))
four_side_block = ImageTk.PhotoImage(Image.open("4die.png").resize((43, 43), Image.ANTIALIAS))
three_side_block = ImageTk.PhotoImage(Image.open("3die.png").resize((43, 43), Image.ANTIALIAS))
two_side_block = ImageTk.PhotoImage(Image.open("2die.png").resize((43, 43), Image.ANTIALIAS))
one_side_block = ImageTk.PhotoImage(Image.open("1die.png").resize((43, 43), Image.ANTIALIAS))

Ludo(root,one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block)
    
#obj.motion_of_coin(15,2,4,green2_1_label,400,"green2",5)
root.mainloop()
        
