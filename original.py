import tkinter as tk

#main window
win = tk.Tk()
win.geometry("700x1000")
win.title("好樂迪計費")

#input variables
week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
whichdays = []
hours = tk.IntVar()
people = tk.IntVar()
limjew = tk.IntVar()
birthday = tk.IntVar()

#output variables
output = tk.StringVar()
bd_output = tk.StringVar()

#data
ds = [188, 118]
kpf = 800
prices = {
    #[每人基本費, 基本時數, 每人續唱費用, 壽星送]
    "星期一": [
        [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2],
        [290, 4, 50, 3], [290, 4, 50, 3],
        [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3],
        [360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]
    ],

    "星期二": [
        [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2],
        [290, 4, 50, 3], [290, 4, 50, 3],
        [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3],
        [360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]
    ],

    "星期三": [
        [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2],
        [290, 4, 50, 3], [290, 4, 50, 3],
        [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3],
        [360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]
    ],

    "星期四": [
        [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2],
        [290, 4, 50, 3], [290, 4, 50, 3],
        [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3], [360, 4, 50, 3],
        [360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]
    ],

    "星期五": [
        [270, 5, 50, 2], [270, 5, 50, 2], [270, 5, 50, 2], [270, 4, 50, 3], [270, 4, 100, 1],
        [360, 4, 100, 1], [360, 4, 100, 1],
        [470, 3, 100, 1], [470, 3, 100, 1], [470, 3, 100, 1], [470, 3, 100, 1],
        [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1]
    ],

    "星期六": [
        [340, 4, 50, 0], [340, 4, 50, 0], [340, 4, 50, 0], [340, 3, 50, 1], [340, 3, 100, 1],
        [360, 3, 100, 1], [360, 3, 100, 1],
        [470, 3, 100, 1], [470, 3, 100, 1], [470, 3, 100, 1], [470, 3, 100, 1],
        [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1], [470, 4, 100, 1]
    ],

    "星期日": [
        [340, 4, 50, 1], [340, 4, 50, 1], [340, 4, 50, 1], [340, 4, 50, 1], [340, 4, 50, 1],
        [360, 4, 50, 1], [360, 4, 50, 3],
        [370, 4, 50, 3], [370, 4, 50, 3], [370, 4, 50, 3], [370, 4, 50, 3],
        [360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]
    ]
}
bd1_prices = {
    #[每人基本費, 基本時數, 大包廂續唱費用]
    "星期一": [
        [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660],
        [99, 3, 792], [99, 3, 792],
        [99, 3, 924], [99, 3, 924], [99, 3, 924], [99, 3, 924],
        [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792]
    ],

    "星期二": [
        [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660],
        [99, 3, 792], [99, 3, 792],
        [99, 3, 924], [99, 3, 924], [99, 3, 924], [99, 3, 924],
        [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792]
    ],

    "星期三": [
        [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660],
        [99, 3, 792], [99, 3, 792],
        [99, 3, 924], [99, 3, 924], [99, 3, 924], [99, 3, 924],
        [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792]
    ],

    "星期四": [
        [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660], [99, 3, 660],
        [99, 3, 792], [99, 3, 792],
        [99, 3, 924], [99, 3, 924], [99, 3, 924], [99, 3, 924],
        [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792], [99, 3, 792]
    ],

    "星期五": [
        [99, 3, 660], [99, 3, 660], [99, 3, 660], [660, 1, 660], [99, 1, 660],
        [1056, 1, 1056], [1056, 1, 1056],
        [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320],
        [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320], [1320, 1, 1320]
    ]
}   
bd2_prices = {
    #[包廂基本費, 基本時數, 大包廂續唱費用]
    "星期一": [
        [660, 1, 660], [660, 1, 660], [660, 1, 660], [880, 3, 660], [880, 3, 660],
        [880, 3, 792], [880, 3, 792],
        [880, 3, 924], [880, 3, 924], [880, 3, 924], [880, 3, 924],
        [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792]
    ],

    "星期二": [
        [660, 1, 660], [660, 1, 660], [660, 1, 660], [880, 3, 660], [880, 3, 660],
        [880, 3, 792], [880, 3, 792],
        [880, 3, 924], [880, 3, 924], [880, 3, 924], [880, 3, 924],
        [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792]
    ],

    "星期三": [
        [660, 1, 660], [660, 1, 660], [660, 1, 660], [880, 3, 660], [880, 3, 660],
        [880, 3, 792], [880, 3, 792],
        [880, 3, 924], [880, 3, 924], [880, 3, 924], [880, 3, 924],
        [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792]
    ],

    "星期四": [
        [660, 1, 660], [660, 1, 660], [660, 1, 660], [880, 3, 660], [880, 3, 660],
        [880, 3, 792], [880, 3, 792],
        [880, 3, 924], [880, 3, 924], [880, 3, 924], [880, 3, 924],
        [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792]
    ],

    "星期日": [
        [924, 1, 924], [924, 1, 924], [924, 1, 924], [880, 3, 924], [880, 3, 924],
        [880, 3, 1056], [880, 3, 1056],
        [880, 3, 1056], [880, 3, 1056], [880, 3, 1056], [880, 3, 1056],
        [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792], [880, 3, 792]
    ],
}  

def NewWin(trashtalk):
    newwin = tk.Toplevel()
    newwin.geometry("410x50")
    newwin.title("憨貨一個")
    talktrash = tk.Label(newwin, text = trashtalk)
    talktrash.pack(fill = "both", expand = True)
    talktrash.place(x = 0, y = 0)

def GO():
    global hours, people, whichdays, output, bd_output, day_list, entry_list, price_list, text, bd_day_list, bd_entry_list, bd_price_list, bd_text
    try:
        if hours.get() == 0: 
            NewWin("唱0小時你問我衝三小？？？")
            return 0
        elif hours.get() > 18:
            NewWin("白癡喔好樂迪根本沒開那麼久？？？")
            return 0
        elif people.get() == 0: 
            NewWin("就是有你這種人問幾個人給我回答0害林北要多寫這行不然除以0程式會爆掉")
            return 0
    except: 
        NewWin("很明顯要你輸數字哪裡看不懂？？？")
        return 0
    cnt = 0
    for i in whichdays:
        cnt += i.get()
    if not cnt:
        NewWin("阿沒給日期是要我自己猜就對了？？？")
    day_list = []
    entry_list = []
    price_list = []
    text = ""
    Price()
    bd_day_list = []
    bd_entry_list = []
    bd_price_list = []
    bd_text = ""
    if birthday.get(): BirthdayPrice()
    Output()

#lists and texts
day_list = []
entry_list = []
price_list = []
text = ""
bd_day_list = []
bd_entry_list = []
bd_price_list = []
bd_text = ""

#THE BIG BRAIN PART
def Price():
    global day_list, entry_list, price_list, text
    day_list = []
    entry_list = []
    price_list = []
    text = ""
    for j in range(len(week)): #which day
        if whichdays[j].get():
            for entrytime in range(18): 
                if entrytime + hours.get() <= 18: #find enough long period
                    now = entrytime
                    price = 0
                    hour = hours.get()
                    #first hours
                    now += prices[week[j]][entrytime][1]
                    now += prices[week[j]][entrytime][3] * birthday.get() #birthday
                    price += prices[week[j]][entrytime][0]
                    hour -= prices[week[j]][entrytime][1]
                    hour -= prices[week[j]][entrytime][3] * birthday.get() #birthday
                    #I want moreeeee
                    while hour > 0:
                        price += prices[week[j]][now][2]
                        now += 1
                        hour -= 1
                    #ds
                    if entrytime < 11: price += ds[0]
                    else: price += ds[1]
                    #kpf
                    if limjew.get(): price += int(kpf / people.get())
                    #append lists
                    day_list.append(week[j])
                    entry_list.append(entrytime)
                    price_list.append(price)

def BirthdayPrice():
    global bd_day_list, bd_entry_list, bd_price_list, bd_text
    bd_day_list = []
    bd_entry_list = []
    bd_price_list = []
    bd_text = "壽星奇怪的優惠方案：\n\n"
    #1
    for j in range(len(week) - 2): #which day
        if whichdays[j].get():
            for entrytime in range(3): 
                if entrytime + hours.get() <= 18: #find enough long period
                    now = entrytime
                    total_price = 0
                    hour = hours.get()
                    #first hours
                    now += bd1_prices[week[j]][entrytime][1]
                    total_price += bd1_prices[week[j]][entrytime][0] * min(6, people.get())
                    hour -= bd1_prices[week[j]][entrytime][1]
                    #I want moreeeee
                    while hour > 0:
                        total_price += bd1_prices[week[j]][now][2]
                        now += 1
                        hour -= 1
                    #ds
                    total_price += ds[0] * people.get()
                    #kpf
                    if limjew.get(): total_price += kpf
                    #append lists
                    bd_day_list.append("方案一" + week[j])
                    bd_entry_list.append(entrytime)
                    bd_price_list.append(int(total_price / people.get()))
    #2
    for j in [0, 1, 2, 3, 6]: #which day
        if whichdays[j].get():
            for entrytime in range(3, 18): 
                if entrytime + hours.get() <= 18: #find enough long period
                    now = entrytime
                    total_price = 0
                    hour = hours.get()
                    #first hours
                    now += bd2_prices[week[j]][entrytime][1]
                    total_price += bd2_prices[week[j]][entrytime][0]
                    hour -= bd2_prices[week[j]][entrytime][1]
                    #I want moreeeee
                    while hour > 0:
                        total_price += bd2_prices[week[j]][now][2]
                        now += 1
                        hour -= 1
                    #ds
                    total_price += ds[0] * people.get()
                    #kpf
                    if limjew.get(): total_price += kpf
                    #append lists
                    bd_day_list.append("方案二" + week[j])
                    bd_entry_list.append(entrytime)
                    bd_price_list.append(int(total_price / people.get()))

def Output():
    global day_list, entry_list, price_list, text, bd_day_list, bd_entry_list, bd_price_list, bd_text
    price_cheapest = min(price_list + bd_price_list)
    for i in range(len(entry_list)):
        if entry_list[i] < 12:
            text += (day_list[i] + str(entry_list[i] + 12) + "點進場一個人要" + str(price_list[i]) + "元")
            if price_list[i] == price_cheapest: text += " -> 最便宜\n"
            else: text += "\n"
        else: 
            text += (week[(week.index(day_list[i]) + 1) % 7] + str(entry_list[i] - 12) + "點進場一個人要" + str(price_list[i]) + "元")
            if price_list[i] == price_cheapest: text += " -> 最便宜\n"
            else: text += "\n"
    output.set(text)
    for i in range(len(bd_entry_list)):
        if bd_entry_list[i] < 12:
            bd_text += (bd_day_list[i] + str(bd_entry_list[i] + 12) + "點進場一個人要" + str(bd_price_list[i]) + "元")
            if bd_price_list[i] == price_cheapest: bd_text += " -> 最便宜\n"
            else: bd_text += "\n"
        else: 
            bd_text += (bd_day_list[i][0:3] + week[(week.index(bd_day_list[i][3:6]) + 1) % 7] + str(bd_entry_list[i] - 12) + "點進場一個人要" + str(bd_price_list[i]) + "元")
            if bd_price_list[i] == price_cheapest: bd_text += " -> 最便宜\n"
            else: bd_text += "\n"
    if bd_text == "壽星奇怪的優惠方案：\n\n": bd_text += "沒得用"
    bd_output.set(bd_text)

#whichdays frame
frame1 = tk.Frame(win, width = 200, height = 200)
frame1.place(x = 0)
label1 = tk.Label(frame1, text = "星期幾：")
label1.place(x = 10, y = 10)
for i in range(len(week)):
    tem = tk.IntVar()
    whichdays.append(tem)
    item = tk.Checkbutton(frame1, text = week[i], variable = whichdays[i])
    item.place(x = 60, y = 10 + i * 25)

#hours frame
frame2 = tk.Frame(win, width = 150, height = 100)
frame2.place(x = 150)
label2 = tk.Label(frame2, text = "唱幾小：")
label2.place(x = 10, y = 10)
entry2 = tk.Entry(frame2, textvariable = hours)
entry2.place(x = 70, y = 12)

#GO!!!
button = tk.Button(win, command = GO, text = "開算")
button.place(x = 145, y = 270)

#output frame
frame3 = tk.Frame(win, width = 350, height = 970, bg = "grey")
frame3.place(x = 330, y = 15)
msg = tk.Label(frame3, textvariable = output, justify = "left", bg = "grey")
msg.place(x = 10, y = 10)

#number of people frame
frame4 = tk.Frame(win, width = 150, height = 100)
frame4.place(x = 150, y = 50)
label4 = tk.Label(frame4, text = "幾個人：")
label4.place(x = 10, y = 10)
entry4 = tk.Entry(frame4, textvariable = people)
entry4.place(x = 70, y = 12)

#lim jew frame
frame5 = tk.Frame(win, width = 150, height = 100)
frame5.place(x = 150, y = 100)
label5 = tk.Label(frame5, text = "喝酒嗎：")
label5.place(x = 10, y = 10)
lj_yes = tk.Radiobutton(frame5, text = "喝爆", variable = limjew, value = 1)
lj_yes.place(x = 60, y = 10)
lj_no = tk.Radiobutton(frame5, text = "我要先不", variable = limjew, value = 0)
lj_no.place(x = 60, y = 30)

#birthday frame
frame6 = tk.Frame(win, width = 150, height = 100)
frame6.place(x = 150, y = 150)
label6 = tk.Label(frame6, text = "有人生日嗎：")
label6.place(x = 10, y = 10)
bd_yes = tk.Radiobutton(frame6, text = "有喔", variable = birthday, value = 1)
bd_yes.place(x = 60, y = 30)
bd_no = tk.Radiobutton(frame6, text = "ㄐㄐ", variable = birthday, value = 0)
bd_no.place(x = 60, y = 50)

#birthday output frame
frame7 = tk.Frame(win, width = 295, height = 645, bg = "grey")
frame7.place(x = 15, y = 340)
bd_msg = tk.Label(frame7, textvariable = bd_output, justify = "left", bg = "grey")
bd_msg.place(x = 10, y = 10)

#win.mainloop
win.mainloop()
