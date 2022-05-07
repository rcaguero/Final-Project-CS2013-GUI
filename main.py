from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Module
import PIL as p
import PIL.ImageTk as ptk
import os

# Certain blocks of code were obtained from: Codemy and Sujinth Bontala. He has vidoe tutorial on youtube on how to use GUIs.

# Header Section
root = Tk()
root.title("OnlineStore.com")
root.geometry("1000x5000")
header = LabelFrame(root, bd=2, relief="groove", bg="light blue")
header.place(width=2000, height=50)
tagline = Label(header, text="WELCOME TO ROB & ANNA ONLINE STORE!", font="courier 15 bold", fg="black", bg="light blue"
"").grid(row=3,column=20, padx=280,pady=0)

# Image loading
shop_logo = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/shop bag.png")
resize = shop_logo.resize((170, 170), Image.ANTIALIAS)
sized_shop_logo = ImageTk.PhotoImage(resize)
# Tops Images
top1_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI/hoodeh.png")
resize = top1_actual.resize((172, 172), Image.ANTIALIAS)
new_top1 = ImageTk.PhotoImage(resize)
top2_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/blue tee.png")
resize2 = top2_actual.resize((172, 160), Image.ANTIALIAS)
new_top2 = ImageTk.PhotoImage(resize2)
top3_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/nike png.png")
resize3 = top3_actual.resize((172, 160), Image.ANTIALIAS)
new_top3 = ImageTk.PhotoImage(resize3)
top4_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/sweater.png")
resize4 = top4_actual.resize((172, 165), Image.ANTIALIAS)
new_top4 = ImageTk.PhotoImage(resize4)
bot1_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/pants1.png")
resize11 = bot1_actual.resize((172, 172), Image.ANTIALIAS)
new_bot1 = ImageTk.PhotoImage(resize11)
bot2_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/jeans.png")
resize12 = bot2_actual.resize((172, 172), Image.ANTIALIAS)
new_bot2 = ImageTk.PhotoImage(resize12)
bot3_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/sweatas.png")
resize13 = bot3_actual.resize((172, 172), Image.ANTIALIAS)
new_bot3 = ImageTk.PhotoImage(resize13)
bot4_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/cg.png")
resize14 = bot4_actual.resize((172, 172), Image.ANTIALIAS)
new_bot4 = ImageTk.PhotoImage(resize14)
acc1_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/wallet.png")
resize41 = acc1_actual.resize((172, 172), Image.ANTIALIAS)
new_acc1 = ImageTk.PhotoImage(resize41)
acc2_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/bracelet.png")
resize42 = acc2_actual.resize((172, 172), Image.ANTIALIAS)
new_acc2 = ImageTk.PhotoImage(resize42)
acc3_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/earrings.png")
resize43 = acc3_actual.resize((172, 172), Image.ANTIALIAS)
new_acc3 = ImageTk.PhotoImage(resize43)
acc4_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/purse.png")
resize44 = acc4_actual.resize((172, 172), Image.ANTIALIAS)
new_acc4 = ImageTk.PhotoImage(resize44)
wtop1_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/sweater1.png")
resize21 = wtop1_actual.resize((172, 170), Image.ANTIALIAS)
new_wtop1 = ImageTk.PhotoImage(resize21)
wtop2_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/fleece.png")
resize22 = wtop2_actual.resize((172, 172), Image.ANTIALIAS)
new_wtop2 = ImageTk.PhotoImage(resize22)
wtop3_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/leather.png")
resize23 = wtop3_actual.resize((172, 172), Image.ANTIALIAS)
new_wtop3 = ImageTk.PhotoImage(resize23)
wtop4_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/blacktee.png")
resize24 = wtop4_actual.resize((172, 174), Image.ANTIALIAS)
new_wtop4 = ImageTk.PhotoImage(resize24)
wbot1_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/skirt.png")
resize31 = wbot1_actual.resize((172, 172), Image.ANTIALIAS)
new_wbot1 = ImageTk.PhotoImage(resize31)
wbot2_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/sweatas2.png")
resize32 = wbot2_actual.resize((172, 172), Image.ANTIALIAS)
new_wbot2 = ImageTk.PhotoImage(resize32)
wbot3_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/leggings.png")
resize33 = wbot3_actual.resize((172, 172), Image.ANTIALIAS)
new_wbot3 = ImageTk.PhotoImage(resize33)
wbot4_actual = Image.open("C:/Users/rcagu/PycharmProjects/Final Project GUI 2/short2.png")
resize34 = wbot4_actual.resize((172, 172), Image.ANTIALIAS)
new_wbot4 = ImageTk.PhotoImage(resize34)



# Button Frame
Button_frame = LabelFrame(root, bd=2, relief="groove", bg="dark blue")
Button_frame.place(x=2, y=35, width=1999, height=70)

# Shopping Display Frame
item_frame = LabelFrame(root, bd=2, relief="groove", font="times 16 bold", fg="dark red")
item_frame.place(x=0, y=105, width=1000, height=5000)
label_welcome = Label(item_frame, text="Welcome to Our Store!\n Enjoy Shopping!", font="times 18 bold").place(x
=380, y=250)
label_logo = Label(item_frame, image=sized_shop_logo)
label_logo.grid(column=5, padx=420, pady=50)

# Clicking variables
# Tops
top1_clicked = StringVar()
top1_clicked.set("Small - $.50")
top2_clicked = StringVar()
top2_clicked.set("Small - $.65")
top3_clicked = StringVar()
top3_clicked.set("Medium - $.40")
top4_clicked = StringVar()
top4_clicked.set("Small - $.95")
tops_list = []
tops_list2 = []
#Bottoms
bot1_clicked = StringVar()
bot1_clicked.set("Small - $.30")
bot2_clicked = StringVar()
bot2_clicked.set("Small - $.50")
bot3_clicked = StringVar()
bot3_clicked.set("Small - $.280")
bot4_clicked = StringVar()
bot4_clicked.set("Small - $.15")
bots_list = []
bots_list2 = []
# Womens Tops
wtop1_clicked = StringVar()
wtop1_clicked.set("Small - $.43")
wtop2_clicked = StringVar()
wtop2_clicked.set("Small - $.90")
wtop3_clicked = StringVar()
wtop3_clicked.set("Small - $.18")
wtop4_clicked = StringVar()
wtop4_clicked.set("Small - $.29")
wtops_list = []
wtops_list2 = []

# Women Bottoms
wbot1_clicked = StringVar()
wbot1_clicked.set("Small - $.40")
wbot2_clicked = StringVar()
wbot2_clicked.set("Small - $.99")
wbot3_clicked = StringVar()
wbot3_clicked.set("Small - $.85")
wbot4_clicked = StringVar()
wbot4_clicked.set("Small - $.66")
wbots_list = []
wbots_list2 = []
# Accessories
acc1_clicked = StringVar()
acc1_clicked.set("$.36")
acc2_clicked = StringVar()
acc2_clicked.set("$.15")
acc3_clicked = StringVar()
acc3_clicked.set("$.20")
acc4_clicked = StringVar()
acc4_clicked.set("$.30")
accessories_list = []
accessories_list2 = []

# Other needed functions
def loadTops():
    fp = open("tops.txt", "r")
    j = 0
    for line in fp:
        array = line.split("-")
        tops_list2.append("Tops"+str(j+1))
        tops_list2[j] = Module.Product()
        tops_list2[j].productID = array[0]
        tops_list2[j].price = array[1]
        tops_list2[j].name = array[2]
        tops_list2[j].brand = array[3]
        tops_list2[j].color = array[4]
        tops_list2[j].numOfItems = array[5]
        tops_list2[j].description = array[6]
        j += 1


def loadBots():
    fp = open("bottoms.txt", "r")
    j = 0
    for line in fp:
        array = line.split("-")
        bots_list2.append("Bottoms" + str(j + 1))
        bots_list2[j] = Module.Product()
        bots_list2[j].productID = array[0]
        bots_list2[j].price = array[1]
        bots_list2[j].name = array[2]
        bots_list2[j].brand = array[3]
        bots_list2[j].color = array[4]
        bots_list2[j].numOfItems = array[5]
        bots_list2[j].description = array[6]
        j += 1

def loadWTops():
    fp = open("wtops.txt", "r")
    j = 0
    for line in fp:
        array = line.split("-")
        wtops_list2.append("Women Tops" + str(j + 1))
        wtops_list2[j] = Module.Product()
        wtops_list2[j].productID = array[0]
        wtops_list2[j].price = array[1]
        wtops_list2[j].name = array[2]
        wtops_list2[j].brand = array[3]
        wtops_list2[j].color = array[4]
        wtops_list2[j].numOfItems = array[5]
        wtops_list2[j].description = array[6]
        j += 1

def loadWBots():
    fp = open("wbots.txt", "r")
    j = 0
    for line in fp:
        array = line.split("-")
        wbots_list2.append("Women Bottoms" + str(j + 1))
        wbots_list2[j] = Module.Product()
        wbots_list2[j].productID = array[0]
        wbots_list2[j].price = array[1]
        wbots_list2[j].name = array[2]
        wbots_list2[j].brand = array[3]
        wbots_list2[j].color = array[4]
        wbots_list2[j].numOfItems = array[5]
        wbots_list2[j].description = array[6]
        j += 1

def loadAcc():
    fp = open("accessories.txt", "r")
    j = 0
    for line in fp:
        array = line.split("-")
        accessories_list2.append("Accessories" + str(j + 1))
        accessories_list2[j] = Module.Product()
        accessories_list2[j].productID = array[0]
        accessories_list2[j].price = array[1]
        accessories_list2[j].name = array[2]
        accessories_list2[j].brand = array[3]
        accessories_list2[j].color = array[4]
        accessories_list2[j].numOfItems = array[5]
        accessories_list2[j].description = array[6]
        j += 1

def save_receipt(text):
    op = messagebox.askyesno("Invoice Saving Confirmation", "Do you want to save the invoice in a file?")
    if op:
        f = open("Receipt.txt", "w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status", "Invoice is saved successfully as a text document with name Receipt.txt")
    else:
        messagebox.showinfo("Invoice Saving Status", "The invoice is not saved into a file.")

def DestroyFrames():
    for widget in item_frame.winfo_children():
        widget.destroy()


def spacing(n, str1=" "):
    str = ""
    for i in range(n):
        str += str1
    return str

# Functions for buttons
def MenTops():
    loadTops()
    DestroyFrames()
    button_frame_checkout = Label(item_frame, bd=2, relief="groove")
    button_frame_checkout.place(x=400, y=450)
    Checkout_button = Button(button_frame_checkout, text="Checkout Cart", font="courier 18 bold", width=15, bd=6,
                             bg="dark blue",
                             fg="white", activebackground="yellow", command=Receipt)
    Checkout_button.grid(row=0, column=0)
    # Top 1
    tops_label = Label(item_frame, text="Available Tops:", font="times 18 bold", fg="black").grid(row=0, column=5,
    padx=420)
    label_frame_top1 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top1.place(x=50, y=55, width=180, height=350)
    label_top_1 = Label(label_frame_top1, image=new_top1, bd=2).grid(row=0, column=0)
    name_top_1 = Label(label_frame_top1, text=tops_list2[0].name, font="courier 10 bold").grid(row=1, column=0)
    pid_top_1 = Label(label_frame_top1, text="Product ID: "+tops_list2[0].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_top_1 = Label(label_frame_top1, text="Brand: "+tops_list2[0].brand, font = "courier 10 bold").grid(row=3, column=0)
    stock_top_1 = Label(label_frame_top1, text="Stock: "+tops_list2[0].numOfItems+" left", font="courier 10 bold").grid(row=4, column=0)
    quantity_top1 = Label(label_frame_top1, text="Sizing:", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    top1_options = ["Small - $.50", "Large – $.60"]
    global top1_clicked, top2_clicked, top3_clicked, top4_clicked
    top1_dropMen = OptionMenu(label_frame_top1, top1_clicked, *top1_options).place(x=53, y=263)

    # Top 2
    label_frame_top2 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top2.place(x=300, y=55, width=180, height=350)
    label_top_2 = Label(label_frame_top2, image=new_top2, bd=2).grid(row=0, column=0)
    name_top_2 = Label(label_frame_top2, text=tops_list2[1].name,font="courier 10 bold").grid(row=1, column=0)
    pid_top_2 = Label(label_frame_top2, text="Product ID: "+tops_list2[1].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_top_2 = Label(label_frame_top2, text="Brand: "+tops_list2[1].brand, font = "courier 10 bold").grid(row=3, column=0)
    stock_top_2 = Label(label_frame_top2, text="Stock: "+tops_list2[1].numOfItems+" left", font="courier 10 bold").grid(row=4, column=0)
    quantity_top2 = Label(label_frame_top2, text="Sizing:", bd=1, font="times 12 bold", justify="left").place(x=5,y=265)
    top2_options = ["Small - $.65,", "Medium - $.70", "Large - $.75"]
    top2_dropMen = OptionMenu(label_frame_top2, top2_clicked, *top2_options).place(x=53, y=263)

    # Top 3
    label_frame_top3 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top3.place(x=540, y=55, width=180, height=350)
    label_top_3 = Label(label_frame_top3, image=new_top3, bd=2).grid(row=0, column=0)
    name_top_3 = Label(label_frame_top3, text=tops_list2[2].name, font="courier 10 bold").grid(row=1, column=0)
    pid_top_3 = Label(label_frame_top3, text="Product ID: " + tops_list2[2].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_top_3 = Label(label_frame_top3, text="Brand: " + tops_list2[2].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_top_3 = Label(label_frame_top3, text="Stock: " + tops_list2[2].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity_top3 = Label(label_frame_top3, text="Sizing:", bd=1,font="times 12 bold", justify="left").place(x=5, y=265)
    top3_options = ["Medium - $.40", "Large - $.45"]
    top3_dropMen = OptionMenu(label_frame_top3, top3_clicked, *top3_options).place(x=50, y=263)

    # Top 4
    label_frame_top4 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top4.place(x=770, y=55, width=180, height=350)
    label_top_4 = Label(label_frame_top4, image=new_top4, bd=2).grid(row=0, column=0)
    name_top_4 = Label(label_frame_top4, text=tops_list2[3].name, font="courier 10 bold").grid(row=1, column=0)
    pid_top_4 = Label(label_frame_top4, text="Product ID: "+tops_list2[3].productID, font="courier 10 bold").grid(row=2,column=0)
    brand_top_4 = Label(label_frame_top4, text="Brand: "+tops_list2[3].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_top_4 = Label(label_frame_top4, text="Stock: "+tops_list2[3].numOfItems+" left", font="courier 10 bold").grid(row=4, column=0)
    quantity_top4 = Label(label_frame_top4, text="Sizing: ", bd=1, font="times 12 bold", justify = "left").place(x=5,y=265)
    top4_options = ["Small - $.95", "Large - $.100"]
    top4_dropMen = OptionMenu(label_frame_top4, top4_clicked, *top4_options).place(x=50, y=263)

    def topPrice(s):
        s1 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[i] != '.':
                s1 = s1 + s[i]
            else:
                break
        return int(s1[::-1])

    def topQuantity(s):
        s1 = ""
        for i in range(len(s)):
            s1 = s1 + s[i]
            if s[i] == 'g' or s[i] == 'L':
                break
        return s1

    def Top1Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Pink Hoodie", topPrice(top1_clicked.get()), topQuantity(top1_clicked.get()),
                 spacing(40 - len("Pink Hoodie"))])
            messagebox.showinfo("Item Status",
                                "Pink Pullover Hoodie (" + top1_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Pink Pullover Hoodie (" + top1_clicked.get() + ") was not added to cart.")

    def Top2Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Blue T-Shirt", topPrice(top2_clicked.get()), topQuantity(top2_clicked.get()),
                 spacing(40 - len("Blue T-Shirt"))])
            messagebox.showinfo("Item Status",
                                "Blue T-Shirt (" + top2_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Blue T-Shirt (" + top2_clicked.get() + ") was not added to cart.")

    def Top3Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Nike Tee", topPrice(top3_clicked.get()), topQuantity(top3_clicked.get()),
                 spacing(40 - len("Nike Tee"))])
            messagebox.showinfo("Item Status",
                                "Nike Tee (" + top3_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Nike Tee (" + top3_clicked.get() + ") was not added to cart.")

    def Top4Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Blue Supreme Sweatshirt", topPrice(top4_clicked.get()), topQuantity(top4_clicked.get()),
                 spacing(40 - len("Nike Tee"))])
            messagebox.showinfo("Item Status",
                                "Blue Supreme Sweatshirt (" + top4_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Blue Supreme Sweatshirt (" + top4_clicked.get() + ") was not added to cart.")

    top1_add = Button(label_frame_top1, text="Add Item", bg="black", fg="white", font="times 10 bold",
                      command=Top1Add).place(x=60, y=298)

    top2_add = Button(label_frame_top2, text="Add Item", bg="black", fg="white", font="times 10 bold",
                      command=Top2Add).place(x=60, y=298)

    top3_add = Button(label_frame_top3, text="Add Item", bg="black", fg="white", font="times 10 bold",
                      command=Top3Add).place(x=60, y=298)

    top4_add = Button(label_frame_top4, text="Add Item", bg="black", fg="white", font="times 10 bold", command=Top4Add).place(x=60, y=298)


def MenBottoms():
    loadBots()
    DestroyFrames()
    button_frame_checkout = Label(item_frame, bd=2, relief="groove")
    button_frame_checkout.place(x=400, y=450)
    Checkout_button = Button(button_frame_checkout, text="Checkout Cart", font="courier 18 bold", width=15, bd=6,
                             bg="dark blue",
                             fg="white", activebackground="yellow", command=Receipt)
    Checkout_button.grid(row=0, column=0)
    global bot1_clicked, bot2_clicked, bot3_clicked, bot4_clicked
    bots_label = Label(item_frame, text="Available Bottoms:", font="times 18 bold", fg="black").grid(row=0, column=5,
                                                                                                  padx=420)
    # Bot 1
    label_frame_bot1 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot1.place(x=50, y=55, width=180, height=350)
    label_bot_1 = Label(label_frame_bot1, image=new_bot1, bd=2).grid(row=0, column=0)
    name_bot_1 = Label(label_frame_bot1, text=bots_list2[0].name, font="courier 10 bold").grid(row=1, column=0)
    pid_bot1 = Label(label_frame_bot1, text="Product ID: "+bots_list2[0].productID, font ="courier 10 bold").grid(row=2,column=0)
    brand_bot1 = Label(label_frame_bot1, text="Brand: "+bots_list2[0].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_bot1 = Label(label_frame_bot1, text="Stock: "+bots_list2[0].numOfItems+" left", font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot1, text="Sizing: ", bd=1, font="times 12 bold", justify = "left").place(x=5,y=265)
    bot1_options = ["Small - $.30", "Medium - $.40", "XL - $.50"]
    bot1_dropMen = OptionMenu(label_frame_bot1, bot1_clicked, *bot1_options).place(x=50, y=263)

    # Bot 2
    label_frame_bot2 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot2.place(x=300, y=55, width=180, height=350)
    label_bot2 = Label(label_frame_bot2, image=new_bot2, bd=2).grid(row=0, column=0)
    name_bot_2 = Label(label_frame_bot2, text=bots_list2[1].name, font="courier 10 bold").grid(row=1,column=0)
    pid_bot2 = Label(label_frame_bot2, text="Product ID: "+bots_list2[1].productID, font="courier 10 bold").grid(row=2,column=0)
    brand_bot2 = Label(label_frame_bot2, text="Brand: "+bots_list2[1].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_bot2 = Label(label_frame_bot2, text="Stock: "+bots_list2[1].numOfItems+" left", font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot2, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    bot2_options = ["Small - $.60", "Large - $.70"]
    bot2_dropMen = OptionMenu(label_frame_bot2, bot2_clicked, *bot2_options).place(x=50, y=263)

    # Bot 3
    label_frame_bot3 = LabelFrame(item_frame,bd=2, relief="groove")
    label_frame_bot3.place(x=540, y=55, width=180, height=350)
    label_bot3 = Label(label_frame_bot3, image=new_bot3, bd=2).grid(row=0, column=0)
    name_bot_3 = Label(label_frame_bot3, text=bots_list2[2].name, font="courier 10 bold").grid(row=1, column=0)
    pid_bot2 = Label(label_frame_bot3, text="Product ID: " + bots_list2[2].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_bot2 = Label(label_frame_bot3, text="Brand: " + bots_list2[2].brand, font="courier 10 bold").grid(row=3,                                                                                                     column=0)
    stock_bot2 = Label(label_frame_bot3, text="Stock: " + bots_list2[2].numOfItems + " left", font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot3, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    bot3_options = ["Small - $.280", "Large - $.270"]
    bot3_dropMen = OptionMenu(label_frame_bot3, bot3_clicked, *bot3_options).place(x=50, y=263)

    # Bot 4
    label_frame_bot4 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot4.place(x=770, y=55, width=180, height=350)
    label_bot4 = Label(label_frame_bot4, image=new_bot4, bd=2).grid(row=0, column=0)
    name_bot_4 = Label(label_frame_bot4, text=bots_list2[3].name, font="courier 10 bold").grid(row=1, column=0)
    pid_bot4 = Label(label_frame_bot4, text="Product ID: " + bots_list2[3].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_bot4 = Label(label_frame_bot4, text="Brand: " + bots_list2[3].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_bot4 = Label(label_frame_bot4, text="Stock: " + bots_list2[3].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot4, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    bot4_options = ["Small - $.280", "Large - $.270"]
    bot4_dropMen = OptionMenu(label_frame_bot4, bot4_clicked, *bot4_options).place(x=50, y=263)

    def botPrice(s):
        s1 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[i] != '.':
                s1 = s1 + s[i]
            else:
                break
        return int(s1[::-1])

    def botQuantity(s):
        s1 = ""
        for i in range(len(s)):
            s1 = s1 + s[i]
            if s[i] == 'g' or s[i] == 'L':
                break
        return s1

    def Bot1Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            bots_list.append(
                ["Gray Levi's Slacks", botPrice(bot1_clicked.get()), botQuantity(bot1_clicked.get()),
                 spacing(40 - len("Gray Levi's Slacks"))])
            messagebox.showinfo("Item Status",
                                "Gray Levi's Slacks (" + bot1_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Gray Levi's Slacks (" + bot1_clicked.get() + ") was not added to cart.")

    def Bot2Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            bots_list.append(
                ["Carhartt Denim Jeans", botPrice(bot2_clicked.get()), botQuantity(bot2_clicked.get()),
                 spacing(40 - len("Carhartt Denim Jeans"))])
            messagebox.showinfo("Item Status",
                                "Carhartt Denim Jeans (" + bot2_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Carhartt Denim Jeans (" + bot2_clicked.get() + ") was not added to cart.")

    def Bot3Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            bots_list.append(
                ["Nike Drawstring Sweatpants", botPrice(bot3_clicked.get()), botQuantity(bot3_clicked.get()),
                 spacing(40 - len("Nike Drawstring Sweatpants"))])
            messagebox.showinfo("Item Status",
                                "Nike Drawstring Sweatpants (" + bot3_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Nike Drawstring Sweatpants (" + bot3_clicked.get() + ") was not added to cart.")

    def Bot4Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            bots_list.append(
                ["Carhartt Cargo Shorts", botPrice(bot4_clicked.get()), botQuantity(bot4_clicked.get()),
                 spacing(40 - len("Carhartt Cargo Shorts"))])
            messagebox.showinfo("Item Status",
                                "Carhartt Cargo Shorts (" + bot4_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Carhartt Cargo Shorts (" + bot4_clicked.get() + ") was not added to cart.")

    bot1_add = Button(label_frame_bot1, text="Add Item",bg="black", fg="white", font="times 10 bold", command=Bot1Add).place(x=60, y=298)
    bot2_add = Button(label_frame_bot2, text="Add Item", bg="black", fg="white", font="times 10 bold", command=Bot2Add).place(x=60, y=298)
    bot3_add = Button(label_frame_bot3, text="Add Item", bg="black", fg="white", font="times 10 bold",command=Bot3Add).place(x=60, y=298)
    bot4_add = Button(label_frame_bot4, text="Add Item", bg="black", fg="white", font="times 10 bold",command=Bot4Add).place(x=60, y=298)


def WomenTops():
    loadWTops()
    DestroyFrames()
    button_frame_checkout = Label(item_frame, bd=2, relief="groove")
    button_frame_checkout.place(x=400, y=450)
    Checkout_button = Button(button_frame_checkout, text="Checkout Cart", font="courier 18 bold", width=15, bd=6,
                             bg="dark blue",
                             fg="white", activebackground="yellow", command=Receipt)
    Checkout_button.grid(row=0, column=0)
    # Top 1
    tops_label = Label(item_frame, text="Available Tops:", font="times 18 bold", fg="black").grid(row=0, column=5, padx=420)
    label_frame_top1 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top1.place(x=50, y=55, width=180, height=350)
    label_wtop_1 = Label(label_frame_top1, image=new_wtop1, bd=2).grid(row=0, column=0)
    name_wtop_1 = Label(label_frame_top1, text=wtops_list2[0].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wtop_1 = Label(label_frame_top1, text="Product ID: " + wtops_list2[0].productID, font="courier 10 bold").grid( row=2, column=0)
    brand_wtop_1 = Label(label_frame_top1, text="Brand: " + wtops_list2[0].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wtop_1 = Label(label_frame_top1, text="Stock: " + wtops_list2[0].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity_wtop1 = Label(label_frame_top1, text="Sizing:", bd=1, font="times 12 bold", justify="left").place(x=5,y=265)
    wtop1_options = ["Small - $.43", "Large – $.60"]
    global wtop1_clicked, wtop2_clicked, wtop3_clicked, wtop4_clicked
    wtop1_dropMen = OptionMenu(label_frame_top1, wtop1_clicked, *wtop1_options).place(x=53, y=263)

    # Top 2
    label_frame_top2 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top2.place(x=300, y=55, width=180, height=350)
    label_top_2 = Label(label_frame_top2, image=new_wtop2, bd=2).grid(row=0, column=0)
    name_wtop_2 = Label(label_frame_top2, text=wtops_list2[1].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wtop_2 = Label(label_frame_top2, text="Product ID: " + wtops_list2[1].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wtop_2 = Label(label_frame_top2, text="Brand: " + wtops_list2[1].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_wtop_2 = Label(label_frame_top2, text="Stock: " + wtops_list2[1].numOfItems + " left", font="courier 10 bold").grid(row=4, column=0)
    quantity_wtop2 = Label(label_frame_top2, text="Sizing:", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wtop2_options = ["Small - $.90", "Medium - $.95", "Large - $.100"]
    wtop2_dropMen = OptionMenu(label_frame_top2, wtop2_clicked, *wtop2_options).place(x=53, y=263)

    # Top 3
    label_frame_top3 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top3.place(x=540, y=55, width=180, height=350)
    label_top_3 = Label(label_frame_top3, image=new_wtop3, bd=2).grid(row=0, column=0)
    name_wtop_3 = Label(label_frame_top3, text=wtops_list2[2].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wtop_3 = Label(label_frame_top3, text="Product ID: " + wtops_list2[2].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wtop_3 = Label(label_frame_top3, text="Brand: " + wtops_list2[2].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wtop_3 = Label(label_frame_top3, text="Stock: " + wtops_list2[2].numOfItems + " left", font="courier 10 bold").grid(row=4, column=0)
    quantity_wtop3 = Label(label_frame_top3, text="Sizing:", bd=1, font="times 12 bold", justify="left").place(x=5,y=265)
    wtop3_options = ["Medium - $.18", "Large - $.45"]
    wtop3_dropMen = OptionMenu(label_frame_top3, wtop3_clicked, *wtop3_options).place(x=50, y=263)

    # Top 4
    label_frame_top4 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_top4.place(x=770, y=55, width=180, height=350)
    label_top_4 = Label(label_frame_top4, image=new_wtop4, bd=2).grid(row=0, column=0)
    name_wtop_4 = Label(label_frame_top4, text=wtops_list2[3].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wtop_4 = Label(label_frame_top4, text="Product ID: " + wtops_list2[3].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wtop_4 = Label(label_frame_top4, text="Brand: " + wtops_list2[3].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wtop_4 = Label(label_frame_top4, text="Stock: " + wtops_list2[3].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity_wtop4 = Label(label_frame_top4, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wtop4_options = ["Small - $.28", "Large - $.35"]
    wtop4_dropMen = OptionMenu(label_frame_top4, wtop4_clicked, *wtop4_options).place(x=50, y=263)

    def topPrice(s):
        s1 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[i] != '.':
                s1 = s1 + s[i]
            else:
                break
        return int(s1[::-1])

    def topQuantity(s):
        s1 = ""
        for i in range(len(s)):
            s1 = s1 + s[i]
            if s[i] == 'g' or s[i] == 'L':
                break
        return s1

    def WTop1Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Blue Cotton Sweater", topPrice(wtop1_clicked.get()), topQuantity(wtop1_clicked.get()),
                 spacing(40 - len("Blue Cotton Sweater"))])
            messagebox.showinfo("Item Status",
                                "Blue Cotton Sweater (" + wtop1_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Blue Cotton Sweater (" + wtop1_clicked.get() + ") was not added to cart.")

    def WTop2Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Fleece Gray Sweatshirt", topPrice(wtop2_clicked.get()), topQuantity(wtop2_clicked.get()),
                 spacing(40 - len("Fleece Gray Sweatshirt"))])
            messagebox.showinfo("Item Status",
                                "Fleece Gray Sweatshirt (" + wtop2_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Fleece Gray Sweatshirt (" + wtop2_clicked.get() + ") was not added to cart.")

    def WTop3Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Yellow Gucci Jacket", topPrice(wtop3_clicked.get()), topQuantity(wtop3_clicked.get()),
                 spacing(40 - len("Yellow Gucci Jacket"))])
            messagebox.showinfo("Item Status",
                                "Yellow Gucci Jacket (" + wtop3_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Yellow Gucci Jacket (" + wtop3_clicked.get() + ") was not added to cart.")

    def WTop4Add():
        global tops_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            tops_list.append(
                ["Black TeeShirt", topPrice(wtop4_clicked.get()), topQuantity(wtop4_clicked.get()),
                 spacing(40 - len("Black TeeShirt"))])
            messagebox.showinfo("Item Status",
                                "Black TeeShirt (" + wtop4_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Black TeeShirt (" + wtop4_clicked.get() + ") was not added to cart.")

    wtop1_add = Button(label_frame_top1, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WTop1Add).place(x=60, y=298)
    wtop2_add = Button(label_frame_top2, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WTop2Add).place(x=60, y=298)
    wtop3_add = Button(label_frame_top3, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WTop3Add).place(x=60, y=298)
    wtop4_add = Button(label_frame_top4, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WTop4Add).place(x=60, y=298)


def WomenBottoms():
    loadWBots()
    DestroyFrames()
    button_frame_checkout = Label(item_frame, bd=2, relief="groove")
    button_frame_checkout.place(x=400, y=450)
    Checkout_button = Button(button_frame_checkout, text="Checkout Cart", font="courier 18 bold", width=15, bd=6,
                             bg="dark blue",
                             fg="white", activebackground="yellow", command=Receipt)
    Checkout_button.grid(row=0, column=0)
    #Women Bot 1
    global wbot1_clicked, wbot2_clicked, wbot3_clicked, wbot4_clicked
    bots_label = Label(item_frame, text="Available Bottoms:", font="times 18 bold", fg="black").grid(row=0, column=5,
                                                                                                     padx=420)
    # Bot 1
    label_frame_bot1 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot1.place(x=50, y=55, width=180, height=350)
    label_wbot_1 = Label(label_frame_bot1, image=new_wbot1, bd=2).grid(row=0, column=0)
    name_wbot_1 = Label(label_frame_bot1, text=wbots_list2[0].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wbot1 = Label(label_frame_bot1, text="Product ID: " + wbots_list2[0].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wbot1 = Label(label_frame_bot1, text="Brand: " + wbots_list2[0].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_wbot1 = Label(label_frame_bot1, text="Stock: " + wbots_list2[0].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot1, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wbot1_options = ["Small - $.40", "Medium - $.45", "XL - $.50"]
    wbot1_dropMen = OptionMenu(label_frame_bot1, wbot1_clicked, *wbot1_options).place(x=50, y=263)

    # Women Bot 2
    label_frame_bot2 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot2.place(x=300, y=55, width=180, height=350)
    label_wbot_2 = Label(label_frame_bot2, image=new_wbot2, bd=2).grid(row=0, column=0)
    name_wbot_2 = Label(label_frame_bot2, text=wbots_list2[1].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wbot2 = Label(label_frame_bot2, text="Product ID: " + wbots_list2[1].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wbot2 = Label(label_frame_bot2, text="Brand: " + wbots_list2[1].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wbot2 = Label(label_frame_bot2, text="Stock: " + wbots_list2[1].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot2, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wbot2_options = ["Small - $.99", "Medium - $.105"]
    wbot2_dropMen = OptionMenu(label_frame_bot2, wbot2_clicked, *wbot2_options).place(x=50, y=263)

    # Women Bot 3
    label_frame_bot3 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot3.place(x=540, y=55, width=180, height=350)
    label_wbot_3 = Label(label_frame_bot3, image=new_wbot3, bd=2).grid(row=0, column=0)
    name_wbot_3 = Label(label_frame_bot3, text=wbots_list2[2].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wbot3 = Label(label_frame_bot3, text="Product ID: " + wbots_list2[2].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wbot3 = Label(label_frame_bot3, text="Brand: " + wbots_list2[2].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wbot3 = Label(label_frame_bot3, text="Stock: " + wbots_list2[2].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot3, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wbot3_options = ["Small - $.85", "Medium - $.90", "XL - $.100"]
    wbot3_dropMen = OptionMenu(label_frame_bot3, wbot3_clicked, *wbot3_options).place(x=50, y=263)

    # Women Bot 4
    label_frame_bot4 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_bot4.place(x=770, y=55, width=180, height=350)
    label_wbot_4 = Label(label_frame_bot4, image=new_wbot4, bd=2).grid(row=0, column=0)
    name_wbot_4 = Label(label_frame_bot4, text=wbots_list2[3].name, font="courier 10 bold").grid(row=1, column=0)
    pid_wbot4 = Label(label_frame_bot4, text="Product ID: " + wbots_list2[3].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_wbot4 = Label(label_frame_bot4, text="Brand: " + wbots_list2[3].brand, font="courier 10 bold").grid(row=3,column=0)
    stock_wbot4 = Label(label_frame_bot4, text="Stock: " + wbots_list2[3].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity = Label(label_frame_bot4, text="Sizing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    wbot4_options = ["Small - $.66", "Medium - $.80"]
    wbot4_dropMen = OptionMenu(label_frame_bot4, wbot4_clicked, *wbot4_options).place(x=50, y=263)

    def botPrice(s):
        s1 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[i] != '.':
                s1 = s1 + s[i]
            else:
                break
        return int(s1[::-1])

    def botQuantity(s):
        s1 = ""
        for i in range(len(s)):
            s1 = s1 + s[i]
            if s[i] == 'g' or s[i] == 'L':
                break
        return s1

    def WBot1Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            wbots_list.append(
                ["Patterned Skirt", botPrice(wbot1_clicked.get()), botQuantity(wbot1_clicked.get()),
                 spacing(40 - len("Patterned Skirt"))])
            messagebox.showinfo("Item Status",
                                "Patterned Skirt (" + wbot1_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Patterned Skirt (" + wbot1_clicked.get() + ") was not added to cart.")

    def WBot2Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            wbots_list.append(
                ["Nike Gray Joggers", botPrice(wbot2_clicked.get()), botQuantity(wbot2_clicked.get()),
                 spacing(40 - len("Nike Gray Joggers"))])
            messagebox.showinfo("Item Status",
                                "Nike Gray Joggers (" + wbot2_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Nike Gray Joggers (" + wbot2_clicked.get() + ") was not added to cart.")

    def WBot3Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            wbots_list.append(
                ["Champion Black Leggings", botPrice(wbot3_clicked.get()), botQuantity(wbot3_clicked.get()),
                 spacing(40 - len("Champion Black Leggings"))])
            messagebox.showinfo("Item Status",
                                "Champion Black Leggings(" + wbot3_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Champion Black Leggings (" + wbot3_clicked.get() + ") was not added to cart.")

    def WBot4Add():
        global bots_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            wbots_list.append(
                ["Green Running Shorts", botPrice(wbot4_clicked.get()), botQuantity(wbot4_clicked.get()),
                 spacing(40 - len("Green Running Shorts"))])
            messagebox.showinfo("Item Status",
                                "Green Running Shorts (" + wbot4_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Green Running Shorts (" + wbot4_clicked.get() + ") was not added to cart.")


    wbot1_add = Button(label_frame_bot1, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WBot1Add).place(x=60, y=298)
    wbot2_add = Button(label_frame_bot2, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WBot2Add).place(x=60, y=298)
    wbot3_add = Button(label_frame_bot3, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WBot3Add).place(x=60, y=298)
    wbot4_add = Button(label_frame_bot4, text="Add Item", bg="black", fg="white", font="times 10 bold",command=WBot4Add).place(x=60, y=298)
def Accessories():
    loadAcc()
    DestroyFrames()
    button_frame_checkout = Label(item_frame, bd=2, relief="groove")
    button_frame_checkout.place(x=400, y=450)
    Checkout_button = Button(button_frame_checkout, text="Checkout Cart", font="courier 18 bold", width=15, bd=6,
                             bg="dark blue",
                             fg="white", activebackground="yellow", command=Receipt)
    Checkout_button.grid(row=0, column=0)
    # Accessory 1
    accs_label = Label(item_frame, text="Available Accessories:", font="times 18 bold", fg="black").grid(row=0,column=5,padx=420)
    label_frame_acc1 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_acc1.place(x=50, y=55, width=180, height=350)
    label_acc_1 = Label(label_frame_acc1, image=new_acc1, bd=2).grid(row=0, column=0)
    name_acc_1 = Label(label_frame_acc1, text=accessories_list2[0].name, font="courier 10 bold").grid(row=1, column=0)
    pid_acc_1 = Label(label_frame_acc1, text="Product ID: " + accessories_list2[0].productID,font="courier 10 bold").grid(row=2, column=0)
    brand_acc_1 = Label(label_frame_acc1, text="Brand: " + accessories_list2[0].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_acc_1 = Label(label_frame_acc1, text="Stock: " + accessories_list2[0].numOfItems + " left", font="courier 10 bold").grid(row=4, column=0)
    quantity_acc1 = Label(label_frame_acc1, text="Pricing:", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    acc1_options = ["$36.59"]
    global acc1_clicked, acc2_clicked, acc3_clicked, acc4_clicked
    acc1_dropMen = OptionMenu(label_frame_acc1, acc1_clicked, *acc1_options).place(x=60, y=263)

    # Accessory 2
    label_frame_acc2 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_acc2.place(x=300, y=55, width=180, height=350)
    label_acc_2 = Label(label_frame_acc2, image=new_acc2, bd=2).grid(row=0, column=0)
    name_acc_2 = Label(label_frame_acc2, text=accessories_list2[1].name, font="courier 10 bold").grid(row=1,column=0)
    pid_acc_2 = Label(label_frame_acc2, text="Product ID: " + accessories_list2[1].productID,font="courier 10 bold").grid(row=2, column=0)
    brand_acc_2 = Label(label_frame_acc2, text="Brand: " + accessories_list2[1].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_acc_2 = Label(label_frame_acc2, text="Stock: " + accessories_list2[1].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity_acc2 = Label(label_frame_acc2, text="Pricing:", bd=1, font="times 12 bold", justify="left").place(x=5,y=265)
    acc2_options = ["$15.99"]
    acc2_dropMen = OptionMenu(label_frame_acc2, acc2_clicked, *acc2_options).place(x=60, y=263)

    # Accessory 3
    label_frame_acc3 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_acc3.place(x=540, y=55, width=180, height=350)
    label_acc_3 = Label(label_frame_acc3, image=new_acc3, bd=2).grid(row=0, column=0)
    name_acc_3 = Label(label_frame_acc3, text=accessories_list2[2].name, font="courier 10 bold").grid(row=1,column=0)
    pid_acc_3 = Label(label_frame_acc3, text="Product ID: " + accessories_list2[2].productID,font="courier 10 bold").grid(row=2, column=0)
    brand_acc_3 = Label(label_frame_acc3, text="Brand: " + accessories_list2[2].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_acc_3 = Label(label_frame_acc3, text="Stock: " + accessories_list2[2].numOfItems + " left", font="courier 10 bold").grid(row=4, column=0)
    quantity_acc3 = Label(label_frame_acc3, text="Pricing:", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    acc3_options = ["$20.21"]
    acc3_dropMen = OptionMenu(label_frame_acc3, acc3_clicked, *acc3_options).place(x=60, y=263)

    # Accessory 4
    label_frame_acc4 = LabelFrame(item_frame, bd=2, relief="groove")
    label_frame_acc4.place(x=770, y=55, width=180, height=350)
    label_acc_4 = Label(label_frame_acc4, image=new_acc4, bd=2).grid(row=0, column=0)
    name_acc_4 = Label(label_frame_acc4, text=accessories_list2[3].name, font="courier 10 bold").grid(row=1,column=0)
    pid_acc_4 = Label(label_frame_acc4, text="Product ID: " + accessories_list2[3].productID, font="courier 10 bold").grid(row=2, column=0)
    brand_acc_4 = Label(label_frame_acc4, text="Brand: " + accessories_list2[3].brand, font="courier 10 bold").grid(row=3, column=0)
    stock_acc_4 = Label(label_frame_acc4, text="Stock: " + accessories_list2[3].numOfItems + " left",font="courier 10 bold").grid(row=4, column=0)
    quantity_acc4 = Label(label_frame_acc4, text="Pricing: ", bd=1, font="times 12 bold", justify="left").place(x=5, y=265)
    acc4_options = ["$30.99"]
    acc4_dropMen = OptionMenu(label_frame_acc4, acc4_clicked, *acc4_options).place(x=60, y=263)

    def AccPrice(s):
        s1 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[i] != '.':
                s1 = s1 + s[i]
            else:
                break
        return int(s1[::-1])

    def AccQuantity(s):
        s1 = ""
        for i in range(len(s)):
            s1 = s1 + s[i]
            if s[i] == 'g' or s[i] == 'L':
                break
        return s1

    def Acc1Add():
        global accessories_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            accessories_list.append(
                ["Ferrari Guys Metal Decor Wallet", AccPrice(acc1_clicked.get()), AccQuantity(acc1_clicked.get()),
                 spacing(40 - len("Guys Metal Decor Wallet"))])
            messagebox.showinfo("Item Status",
                                "Ferrari Guys Metal Decor Wallet (" + acc1_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "Ferrari Guys Metal Decor Wallet (" + acc1_clicked.get() + ") was not added to cart.")

    def Acc2Add():
        global accessories_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            accessories_list.append(
                ["GUESS Floral Decor Beaded Bracelet", AccPrice(acc2_clicked.get()), AccQuantity(acc2_clicked.get()),
                 spacing(40 - len("GUESS Floral Decor Beaded Bracelet"))])
            messagebox.showinfo("Item Status",
                                "GUESS Floral Decor Beaded Bracelet (" + acc2_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "GUESS Floral Decor Beaded Bracelet (" + acc2_clicked.get() + ") was not added to cart.")

    def Acc3Add():
        global accs_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            accessories_list.append(
                ["GUESS Star Decor Earrings", AccPrice(acc3_clicked.get()), AccQuantity(acc3_clicked.get()),
                 spacing(40 - len("GUESS Star Decor Earrings"))])
            messagebox.showinfo("Item Status",
                                "GUESS Star Decor Earrings (" + acc3_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "GUESS Star Decor Earrings (" + acc3_clicked.get() + ") was not added to cart.")

    def Acc4Add():
        global accessories_list
        choice = messagebox.askyesno("Purchase Confirmation", "Do you want to add this item to your cart?")
        if choice:
            accessories_list.append(
                ["H&M Colorblock Purse With Wristlet", AccPrice(acc4_clicked.get()), AccQuantity(acc4_clicked.get()),
                 spacing(40 - len("H&M Colorblock Purse With Wristlet"))])
            messagebox.showinfo("Item Status",
                                "H&M Colorblock Purse With Wristlet (" + acc4_clicked.get() + ") was successfully added to cart.")
        else:
            messagebox.showinfo("Item Status",
                                "H&M Colorblock Purse With Wristlet (" + acc4_clicked.get() + ") was not added to cart.")

    acc1_add = Button(label_frame_acc1, text="Add Item", bg="black", fg="white", font="times 10 bold", command=Acc1Add).place(x=60, y=298)

    acc2_add = Button(label_frame_acc2, text="Add Item", bg="black", fg="white", font="times 10 bold",command=Acc2Add).place(x=60, y=298)

    acc3_add = Button(label_frame_acc3, text="Add Item", bg="black", fg="white", font="times 10 bold",command=Acc3Add).place(x=60, y=298)

    acc4_add = Button(label_frame_acc4, text="Add Item", bg="black", fg="white", font="times 10 bold",command=Acc4Add).place(x=60, y=298)


# Button declarations
Mens_Tops = Button(Button_frame, text="Men's tops", font="times 18 bold", width=12, bd=6, bg="light blue",
                        fg="black",
                        activebackground="yellow", command=MenTops)
Mens_Tops.grid(row=0, column=0, padx=6, pady=5)
Mens_bottoms = Button(Button_frame, text="Men's bottoms", font="times 18 bold", width=12, bd=6, bg="light blue",
                            fg="black",
                            activebackground="yellow", command=MenBottoms)
Mens_bottoms.grid(row=0, column=1, padx=6, pady=5)
Womens_tops = Button(Button_frame, text="Womens tops", font="times 18 bold", width=12, bd=6, bg="light blue",
                           fg="black",
                           activebackground="yellow", command=WomenTops)
Womens_tops.grid(row=0, column=2, padx=6, pady=5)
Womens_bottoms = Button(Button_frame, text="Womens bottoms", font="times 18 bold", width=12, bd=6, bg="light blue",
                          fg="black",
                          activebackground="yellow", command=WomenBottoms)
Womens_bottoms.grid(row=0, column=3, padx=5, pady=5)
Accessories_button = Button(Button_frame, text="Accessories", font="times 18 bold", width=12, bd=6, bg="light blue",
                           fg="black",
                           activebackground="yellow", command=Accessories)
Accessories_button.grid(row=0, column=4, padx=5, pady=5)

def Receipt():
    op=messagebox.askyesno("Checkout Confirmation","You cannot add or remove items during checkout. Are you done shopping?")
    if op:
        item_frame.destroy()
        Button_frame.destroy()
        mentops_price = 0
        menbots_price = 0
        wtops_price = 0
        wbots_price = 0
        accessories_price = 0
        for i in range(0, len(tops_list)):
            mentops_price += tops_list[i][1]
        for i in range(0, len(bots_list)):
            menbots_price += bots_list[i][1]
        for i in range(0, len(wtops_list)):
            wtops_price += wtops_list[i][1]
        for i in range(0, len(wbots_list)):
            wbots_price += wbots_list[i][1]
        for i in range(0, len(accessories_list)):
            accessories_price += accessories_list[i][1]
        total_price = mentops_price + menbots_price + wtops_price + wbots_price + accessories_price

        def PrintReceipt():
            receipt_place = LabelFrame(root, bd=2, relief="groove")
            receipt_place.place(x=150, y=80, width=750, height=600)
            receipt_title = Label(receipt_place,text="CHECKOUT RECEIPT",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_down = Scrollbar(receipt_place,orient=VERTICAL)
            receipt_text_area = Text(receipt_place,yscrollcommand=scroll_down.set)
            scroll_down.pack(side=RIGHT,fill=Y)
            scroll_down.config(command=receipt_text_area.yview)
            receipt_text_area.pack(fill=BOTH, expand=1)
            receipt_text_area.insert(END, spacing(35) + "Rob And Anna Online Store\n" + spacing(90, '*') + "\n")
            if len(tops_list) > 0:
                receipt_text_area.insert(END, "Men Top(s)\n\nItem Name" + spacing(28) + "Price" + spacing(25) + "Size\n")
                for i in tops_list:
                    receipt_text_area.insert(END, i[0]+i[3]+"$"+str(i[1])+spacing(25-len(str(i[1])))+i[2]+"\n")
                receipt_text_area.insert(END, "\nTotal Men Tops Price : $"+str(mentops_price)+"\n"+spacing(90, '*')+"\n")
            if len(bots_list) > 0:
                receipt_text_area.insert(END, "Men Bottom(s)\n\nItem Name"+spacing(28)+"Price"+spacing(25)+"Sizing\n")
                for i in bots_list:
                    receipt_text_area.insert(END, i[0]+i[3]+"$"+i[2]+spacing(27-len(i[2]))+i[3]+"\n")
                receipt_text_area.insert(END, "\nTotal Men Bottoms Price : $"+str(menbots_price)+"\n"+spacing(90,'*')+"\n")
            if len(wtops_list) > 0:
                receipt_text_area.insert(END, "Women Top(s)\n\nItem Name"+spacing(28)+"Price"+spacing(25)+"Sizing\n")
                for i in wtops_list:
                    receipt_text_area.insert(END,i[0]+i[3]+"$"+i[2]+"\n")
                receipt_text_area.insert(END, "\nTotal Women Tops Price: $"+str(wtops_price)+"\n"+spacing(90,'*')+"\n")
            if len(wbots_list) > 0:
                receipt_text_area.insert(END, "Women Bottom(s)\n\nItem Name"+spacing(28)+"Price"+spacing(25)+"Sizing\n")
                for i in wbots_list:
                    receipt_text_area.insert(END, i[0]+i[3]+"$"+i[2]+"\n")
                receipt_text_area.insert(END, "\nTotal Women Bottom Price: $"+str(wbots_price)+"\n"+spacing(90,'*')+"\n")
            if len(accessories_list)> 0:
                receipt_text_area.insert(END, "Accessories(s)\n\nItem Name"+spacing(28)+"Price"+spacing(25)+"Sizing\n")
                for i in accessories_list:
                    receipt_text_area.insert(END, i[0]+i[3]+"$"+i[2]+"\n")
                receipt_text_area.insert(END, "\nTotal Accessories Price: $"+str(accessories_price)+"\n"+spacing(90,'*'))
            receipt_text_area.insert(END, "\nTotal Price:  $"+str(total_price))
            save_option = Button(root, text="Save Invoice", font="courier 20 bold", bd=6, bg="dark blue", width=15, fg="white",command=lambda: save_receipt(receipt_text_area.get("1.0", END)))
            save_option.place(x=420, y=580)
        PrintReceipt()
    else:
        messagebox.showinfo("Bill Generation Confirmation", "You can continue shopping now.")


root.mainloop()