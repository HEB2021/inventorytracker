from tkinter import *

levelCheck = 0
x = 0
save = open('name_Config.txt', 'w')
saveStock = open('stock_Config.txt', 'w')
savePrice = open('price_Config.txt', 'w')
save = open('name_Config.txt', 'r')
saveStock = open('stock_Config.txt', 'r')
savePrice = open('price_Config.txt', 'r')

# Window initialization
window=Tk()
window.geometry('980x570')
window.title('Inventory Tracker')
window.resizable(False, False)

# Labels
Name = Label(window, text='Name of Item')
Name.grid(column=0, row=0)
Name = Label(window, text='Level of Stock')
Name.grid(column=1, row=0)
Name = Label(window, text='Price of Item')
Name.grid(column=2, row=0)
Name = Label(window, text='Sell Buttons')
Name.grid(column=3, row=0)
Name = Label(window, text='Misc')
Name.grid(column=4, row=0)
Info = Label(window, text='!!All Prices should be entered as decimals, without a "$" symbol!!')
Info.grid(column=4, row=2)
Info = Label(window, text='!!Character limit is 40 characters per Name of Item!!')
Info.grid(column=4, row=3)
Info = Label(window, text='!!Move Letter Cursor to The Far Left of Each Box Before Entering New Entry!!')
Info.grid(column=4, row=4)
Counter = Label(window, text="Amount of Profit: 0")
Counter.grid(column=4, row= 1, columnspan=3)

# Misc
addCustomEntStock = Entry(window, bd=2)
addCustomEntStock.insert(0, 1)
addCustomEnt = Entry(window, bd=2)
addCustomEnt.grid(column=4, row=5)
addCustomEnt.insert(0, 0)
addCustomButt = Button(window, text="Add Custom Money Value", command=lambda: [addCustomEntStock.delete(0, 'end'),
                                                                               addCustomEntStock.insert(0, 1),
                                                                               update_Counter(float(addCustomEnt.get()),
                                                                               addCustomEntStock)])
addCustomButt.grid(column=4, row=6)



def update_Counter(price, stock):
    y = int(stock.get())
    if y != 0:
        global x
        x += price
        Counter = Label(window, text="Amount of Profit: " + str(x))
        Counter.grid(column=4, row= 1, columnspan=3)
        stock.delete(0, 'end')
        stock.insert(0, y - 1)
    else:
        print("outOfstockError")


def mainName():
    global save
    # Name entries
    global name0
    name0 = Entry(window, bd=2, width=40)
    name0.grid(column=0, row=1)

    global name1
    name1 = Entry(window, bd=2, width=40)
    name1.grid(column=0, row=2)

    global name2
    name2 = Entry(window, bd=2, width=40)
    name2.grid(column=0, row=3)

    global name3
    name3 = Entry(window, bd=2, width=40)
    name3.grid(column=0, row=4)

    global name4
    name4 = Entry(window, bd=2, width=40)
    name4.grid(column=0, row=5)

    global name5
    name5 = Entry(window, bd=2, width=40)
    name5.grid(column=0, row=6)

    global name6
    name6 = Entry(window, bd=2, width=40)
    name6.grid(column=0, row=7)

    global name7
    name7 = Entry(window, bd=2, width=40)
    name7.grid(column=0, row=8)
    name7.insert(0, save.readline(40))

    global name8
    name8 = Entry(window, bd=2, width=40)
    name8.grid(column=0, row=9)

    global name9
    name9 = Entry(window, bd=2, width=40)
    name9.grid(column=0, row=10)

    global name10
    name10 = Entry(window, bd=2, width=40)
    name10.grid(column=0, row=11)

    global name11
    name11 = Entry(window, bd=2, width=40)
    name11.grid(column=0, row=12)

    global name12
    name12 = Entry(window, bd=2, width=40)
    name12.grid(column=0, row=13)

    global name13
    name13 = Entry(window, bd=2, width=40)
    name13.grid(column=0, row=14)

    global name14
    name14 = Entry(window, bd=2, width=40)
    name14.grid(column=0, row=15)

    global name15
    name15 = Entry(window, bd=2, width=40)
    name15.grid(column=0, row=16)

    global name16
    name16 = Entry(window, bd=2, width=40)
    name16.grid(column=0, row=17)

    global name17
    name17 = Entry(window, bd=2, width=40)
    name17.grid(column=0, row=18)

    global name18
    name18 = Entry(window, bd=2, width=40)
    name18.grid(column=0, row=19)

    global name19
    name19 = Entry(window, bd=2, width=40)
    name19.grid(column=0, row=20)

    global name20
    name20 = Entry(window, bd=2, width=40)
    name20.grid(column=0, row=21)
    save.close()


def mainStock():
    global saveStock
    # Stock Entries
    global stock0
    stock0 = Entry(window, bd=2)
    stock0.grid(column=1, row=1)

    global stock1
    stock1 = Entry(window, bd=2)
    stock1.grid(column=1, row=2)

    global stock2
    stock2 = Entry(window, bd=2)
    stock2.grid(column=1, row=3)

    global stock3
    stock3 = Entry(window, bd=2)
    stock3.grid(column=1, row=4)

    global stock4
    stock4 = Entry(window, bd=2)
    stock4.grid(column=1, row=5)

    global stock5
    stock5 = Entry(window, bd=2)
    stock5.grid(column=1, row=6)

    global stock6
    stock6 = Entry(window, bd=2)
    stock6.grid(column=1, row=7)

    global stock7
    stock7 = Entry(window, bd=2)
    stock7.grid(column=1, row=8)

    global stock8
    stock8 = Entry(window, bd=2)
    stock8.grid(column=1, row=9)

    global stock9
    stock9 = Entry(window, bd=2)
    stock9.grid(column=1, row=10)

    global stock10
    stock10 = Entry(window, bd=2)
    stock10.grid(column=1, row=11)

    global stock11
    stock11 = Entry(window, bd=2)
    stock11.grid(column=1, row=12)

    global stock12
    stock12 = Entry(window, bd=2)
    stock12.grid(column=1, row=13)

    global stock13
    stock13 = Entry(window, bd=2)
    stock13.grid(column=1, row=14)

    global stock14
    stock14 = Entry(window, bd=2)
    stock14.grid(column=1, row=15)

    global stock15
    stock15 = Entry(window, bd=2)
    stock15.grid(column=1, row=16)

    global stock16
    stock16 = Entry(window, bd=2)
    stock16.grid(column=1, row=17)

    global stock17
    stock17 = Entry(window, bd=2)
    stock17.grid(column=1, row=18)

    global stock18
    stock18 = Entry(window, bd=2)
    stock18.grid(column=1, row=19)

    global stock19
    stock19 = Entry(window, bd=2)
    stock19.grid(column=1, row=20)

    global stock20
    stock20 = Entry(window, bd=2)
    stock20.grid(column=1, row=21)
    saveStock.close()


def mainPrice():
    global savePrice
    # Price Entries
    global price0
    price0 = Entry(window, bd=2)
    price0.grid(column=2, row=1)

    global price1
    price1 = Entry(window, bd=2)
    price1.grid(column=2, row=2)

    global price2
    price2 = Entry(window, bd=2)
    price2.grid(column=2, row=3)

    global price3
    price3 = Entry(window, bd=2)
    price3.grid(column=2, row=4)

    global price4
    price4 = Entry(window, bd=2)
    price4.grid(column=2, row=5)

    global price5
    price5 = Entry(window, bd=2)
    price5.grid(column=2, row=6)

    global price6
    price6 = Entry(window, bd=2)
    price6.grid(column=2, row=7)

    global price7
    price7 = Entry(window, bd=2)
    price7.grid(column=2, row=8)

    global price8
    price8 = Entry(window, bd=2)
    price8.grid(column=2, row=9)

    global price9
    price9 = Entry(window, bd=2)
    price9.grid(column=2, row=10)

    global price10
    price10 = Entry(window, bd=2)
    price10.grid(column=2, row=11)

    global price11
    price11 = Entry(window, bd=2)
    price11.grid(column=2, row=12)

    global price12
    price12 = Entry(window, bd=2)
    price12.grid(column=2, row=13)

    global price13
    price13 = Entry(window, bd=2)
    price13.grid(column=2, row=14)

    global price14
    price14 = Entry(window, bd=2)
    price14.grid(column=2, row=15)

    global price15
    price15 = Entry(window, bd=2)
    price15.grid(column=2, row=16)

    global price16
    price16 = Entry(window, bd=2)
    price16.grid(column=2, row=17)

    global price17
    price17 = Entry(window, bd=2)
    price17.grid(column=2, row=18)

    global price18
    price18 = Entry(window, bd=2)
    price18.grid(column=2, row=19)

    global price19
    price19 = Entry(window, bd=2)
    price19.grid(column=2, row=20)

    global price20
    price20 = Entry(window, bd=2)
    price20.grid(column=2, row=21)
    savePrice.close()


def mainButton():

    button0 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price0.get()), stock0))
    button0.grid(column=3, row=1, columnspan=1)

    button1 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price1.get()), stock1))
    button1.grid(column=3, row=2, columnspan=1)

    button2 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price2.get()), stock2))
    button2.grid(column=3, row=3, columnspan=1)

    button3 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price3.get()), stock3))
    button3.grid(column=3, row=4, columnspan=1)

    button4 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price4.get()), stock4))
    button4.grid(column=3, row=5, columnspan=1)

    button5 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price5.get()), stock5))
    button5.grid(column=3, row=6, columnspan=1)

    button6 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price6.get()), stock6))
    button6.grid(column=3, row=7, columnspan=1)

    button7 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price7.get()), stock7))
    button7.grid(column=3, row=8, columnspan=1)

    button8 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price8.get()), stock8))
    button8.grid(column=3, row=9, columnspan=1)

    button9 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price9.get()), stock9))
    button9.grid(column=3, row=10, columnspan=1)

    button10 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price10.get()), stock10))
    button10.grid(column=3, row=11, columnspan=1)

    button11 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price11.get()), stock11))
    button11.grid(column=3, row=12, columnspan=1)

    button12 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price12.get()), stock12))
    button12.grid(column=3, row=13, columnspan=1)

    button13 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price13.get()), stock13))
    button13.grid(column=3, row=14, columnspan=1)

    button14 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price14.get()), stock14))
    button14.grid(column=3, row=15, columnspan=1)

    button15 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price15.get()), stock15))
    button15.grid(column=3, row=16, columnspan=1)

    button16 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price16.get()), stock16))
    button16.grid(column=3, row=17, columnspan=1)

    button17 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price17.get()), stock17))
    button17.grid(column=3, row=18, columnspan=1)

    button18 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price18.get()), stock18))
    button18.grid(column=3, row=19, columnspan=1)

    button19 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price19.get()), stock19))
    button19.grid(column=3, row=20, columnspan=1)

    button20 = Button(window, text="Sell 1 Item", command=lambda: update_Counter(float(price20.get()), stock20))
    button20.grid(column=3, row=21, columnspan=1)


def saveConf():
    save = open('name_Config.txt', 'w')
    saveStock = open('stock_Config.txt', 'w')
    savePrice = open('price_Config.txt', 'w')
    save.write("")
    saveStock.write("")
    savePrice.write("")
    save.close()
    saveStock.close()
    savePrice.close()

    save = open('name_Config.txt', 'a')
    saveStock = open('stock_Config.txt', 'a')
    savePrice = open('price_Config.txt', 'a')
    save.write(name0.get() + '\n')
    save.write(name1.get() + '\n')
    save.write(name2.get() + '\n')
    save.write(name3.get() + '\n')
    save.write(name4.get() + '\n')
    save.write(name5.get() + '\n')
    save.write(name6.get() + '\n')
    save.write(name7.get() + '\n')
    save.write(name8.get() + '\n')
    save.write(name9.get() + '\n')
    save.write(name10.get() + '\n')
    save.write(name11.get() + '\n')
    save.write(name12.get() + '\n')
    save.write(name13.get() + '\n')
    save.write(name14.get() + '\n')
    save.write(name15.get() + '\n')
    save.write(name16.get() + '\n')
    save.write(name17.get() + '\n')
    save.write(name18.get() + '\n')
    save.write(name19.get() + '\n')
    save.write(name20.get() + '\n')

    saveStock.write(stock0.get() + '\n')
    saveStock.write(stock1.get() + '\n')
    saveStock.write(stock2.get() + '\n')
    saveStock.write(stock3.get() + '\n')
    saveStock.write(stock4.get() + '\n')
    saveStock.write(stock5.get() + '\n')
    saveStock.write(stock6.get() + '\n')
    saveStock.write(stock7.get() + '\n')
    saveStock.write(stock8.get() + '\n')
    saveStock.write(stock9.get() + '\n')
    saveStock.write(stock10.get() + '\n')
    saveStock.write(stock11.get() + '\n')
    saveStock.write(stock12.get() + '\n')
    saveStock.write(stock13.get() + '\n')
    saveStock.write(stock14.get() + '\n')
    saveStock.write(stock15.get() + '\n')
    saveStock.write(stock16.get() + '\n')
    saveStock.write(stock17.get() + '\n')
    saveStock.write(stock18.get() + '\n')
    saveStock.write(stock19.get() + '\n')
    saveStock.write(stock20.get() + '\n')

    savePrice.write(price0.get() + '\n')
    savePrice.write(price1.get() + '\n')
    savePrice.write(price2.get() + '\n')
    savePrice.write(price3.get() + '\n')
    savePrice.write(price4.get() + '\n')
    savePrice.write(price5.get() + '\n')
    savePrice.write(price6.get() + '\n')
    savePrice.write(price7.get() + '\n')
    savePrice.write(price8.get() + '\n')
    savePrice.write(price9.get() + '\n')
    savePrice.write(price10.get() + '\n')
    savePrice.write(price11.get() + '\n')
    savePrice.write(price12.get() + '\n')
    savePrice.write(price13.get() + '\n')
    savePrice.write(price14.get() + '\n')
    savePrice.write(price15.get() + '\n')
    savePrice.write(price16.get() + '\n')
    savePrice.write(price17.get() + '\n')
    savePrice.write(price18.get() + '\n')
    savePrice.write(price19.get() + '\n')
    savePrice.write(price20.get() + '\n')


def loadConf():
    save = open('name_Config.txt', 'r')
    saveStock = open('stock_Config.txt', 'r')
    savePrice = open('price_Config.txt', 'r')
    save.seek(0)
    saveStock.seek(0)
    savePrice.seek(0)

    name0.delete(0, 'end')
    name0.insert(0, save.readline(40).replace('\n', ''))
    name1.delete(0, 'end')
    name1.insert(0, save.readline(40).replace('\n', ''))
    name2.delete(0, 'end')
    name2.insert(0, save.readline(40).replace('\n', ''))
    name3.delete(0, 'end')
    name3.insert(0, save.readline(40).replace('\n', ''))
    name4.delete(0, 'end')
    name4.insert(0, save.readline(40).replace('\n', ''))
    name5.delete(0, 'end')
    name5.insert(0, save.readline(40).replace('\n', ''))
    name6.delete(0, 'end')
    name6.insert(0, save.readline(40).replace('\n', ''))
    name7.delete(0, 'end')
    name7.insert(0, save.readline(40).replace('\n', ''))
    name8.delete(0, 'end')
    name8.insert(0, save.readline(40).replace('\n', ''))
    name9.delete(0, 'end')
    name9.insert(0, save.readline(40).replace('\n', ''))
    name10.delete(0, 'end')
    name10.insert(0, save.readline(40).replace('\n', ''))
    name11.delete(0, 'end')
    name11.insert(0, save.readline(40).replace('\n', ''))
    name12.delete(0, 'end')
    name12.insert(0, save.readline(40).replace('\n', ''))
    name13.delete(0, 'end')
    name13.insert(0, save.readline(40).replace('\n', ''))
    name14.delete(0, 'end')
    name14.insert(0, save.readline(40).replace('\n', ''))
    name15.delete(0, 'end')
    name15.insert(0, save.readline(40).replace('\n', ''))
    name16.delete(0, 'end')
    name16.insert(0, save.readline(40).replace('\n', ''))
    name17.delete(0, 'end')
    name17.insert(0, save.readline(40).replace('\n', ''))
    name18.delete(0, 'end')
    name18.insert(0, save.readline(40).replace('\n', ''))
    name19.delete(0, 'end')
    name19.insert(0, save.readline(40).replace('\n', ''))
    name20.delete(0, 'end')
    name20.insert(0, save.readline(40).replace('\n', ''))

    stock0.delete(0, 'end')
    stock0.insert(0, saveStock.readline().replace('\n', ''))
    stock1.delete(0, 'end')
    stock1.insert(0, saveStock.readline().replace('\n', ''))
    stock2.delete(0, 'end')
    stock2.insert(0, saveStock.readline().replace('\n', ''))
    stock3.delete(0, 'end')
    stock3.insert(0, saveStock.readline().replace('\n', ''))
    stock4.delete(0, 'end')
    stock4.insert(0, saveStock.readline().replace('\n', ''))
    stock5.delete(0, 'end')
    stock5.insert(0, saveStock.readline().replace('\n', ''))
    stock6.delete(0, 'end')
    stock6.insert(0, saveStock.readline().replace('\n', ''))
    stock7.delete(0, 'end')
    stock7.insert(0, saveStock.readline().replace('\n', ''))
    stock8.delete(0, 'end')
    stock8.insert(0, saveStock.readline().replace('\n', ''))
    stock9.delete(0, 'end')
    stock9.insert(0, saveStock.readline().replace('\n', ''))
    stock10.delete(0, 'end')
    stock10.insert(0, saveStock.readline().replace('\n', ''))
    stock11.delete(0, 'end')
    stock11.insert(0, saveStock.readline().replace('\n', ''))
    stock12.delete(0, 'end')
    stock12.insert(0, saveStock.readline().replace('\n', ''))
    stock13.delete(0, 'end')
    stock13.insert(0, saveStock.readline().replace('\n', ''))
    stock14.delete(0, 'end')
    stock14.insert(0, saveStock.readline().replace('\n', ''))
    stock15.delete(0, 'end')
    stock15.insert(0, saveStock.readline().replace('\n', ''))
    stock16.delete(0, 'end')
    stock16.insert(0, saveStock.readline().replace('\n', ''))
    stock17.delete(0, 'end')
    stock17.insert(0, saveStock.readline().replace('\n', ''))
    stock18.delete(0, 'end')
    stock18.insert(0, saveStock.readline().replace('\n', ''))
    stock19.delete(0, 'end')
    stock19.insert(0, saveStock.readline().replace('\n', ''))
    stock20.delete(0, 'end')
    stock20.insert(0, saveStock.readline().replace('\n', ''))

    price0.delete(0, 'end')
    price0.insert(0, savePrice.readline().replace('\n', ''))
    price1.delete(0, 'end')
    price1.insert(0, savePrice.readline().replace('\n', ''))
    price2.delete(0, 'end')
    price2.insert(0, savePrice.readline().replace('\n', ''))
    price3.delete(0, 'end')
    price3.insert(0, savePrice.readline().replace('\n', ''))
    price4.delete(0, 'end')
    price4.insert(0, savePrice.readline().replace('\n', ''))
    price5.delete(0, 'end')
    price5.insert(0, savePrice.readline().replace('\n', ''))
    price6.delete(0, 'end')
    price6.insert(0, savePrice.readline().replace('\n', ''))
    price7.delete(0, 'end')
    price7.insert(0, savePrice.readline().replace('\n', ''))
    price8.delete(0, 'end')
    price8.insert(0, savePrice.readline().replace('\n', ''))
    price9.delete(0, 'end')
    price9.insert(0, savePrice.readline().replace('\n', ''))
    price10.delete(0, 'end')
    price10.insert(0, savePrice.readline().replace('\n', ''))
    price11.delete(0, 'end')
    price11.insert(0, savePrice.readline().replace('\n', ''))
    price12.delete(0, 'end')
    price12.insert(0, savePrice.readline().replace('\n', ''))
    price13.delete(0, 'end')
    price13.insert(0, savePrice.readline().replace('\n', ''))
    price14.delete(0, 'end')
    price14.insert(0, savePrice.readline().replace('\n', ''))
    price15.delete(0, 'end')
    price15.insert(0, savePrice.readline().replace('\n', ''))
    price16.delete(0, 'end')
    price16.insert(0, savePrice.readline().replace('\n', ''))
    price17.delete(0, 'end')
    price17.insert(0, savePrice.readline().replace('\n', ''))
    price18.delete(0, 'end')
    price18.insert(0, savePrice.readline().replace('\n', ''))
    price19.delete(0, 'end')
    price19.insert(0, savePrice.readline().replace('\n', ''))
    price20.delete(0, 'end')
    price20.insert(0, savePrice.readline().replace('\n', ''))

    save.close()
    saveStock.close()
    savePrice.close()


mainName()
mainStock()
mainPrice()
mainButton()
loadConf()
update_Counter(0, addCustomEntStock)
addCustomEntStock.delete(0, 'end')
addCustomEntStock.insert(0, 1)

loadButt = Button(window, text='Load Entries from File', command=lambda: loadConf())
loadButt.grid(column=4, row=21)
saveButt = Button(window, text='Save Entries to File', command=lambda: saveConf())
saveButt.grid(column=4, row=20)

window.mainloop()
