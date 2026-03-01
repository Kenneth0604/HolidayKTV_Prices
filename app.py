import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="唱K要多少錢", page_icon="🎤")

st.title("唱K要多少錢")
st.caption("我用Python做了十個小時然後給咪咪教我放到網站上")

# --- 資料區 (完整的價格矩陣) ---
week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
ds = [188, 118]
kpf = 800

# 基礎價格資料
prices = {
    "星期一": [[270, 5, 50, 2]]*5 + [[290, 4, 50, 3]]*2 + [[360, 4, 50, 3]]*4 + [[360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]],
    "星期二": [[270, 5, 50, 2]]*5 + [[290, 4, 50, 3]]*2 + [[360, 4, 50, 3]]*4 + [[360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]],
    "星期三": [[270, 5, 50, 2]]*5 + [[290, 4, 50, 3]]*2 + [[360, 4, 50, 3]]*4 + [[360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]],
    "星期四": [[270, 5, 50, 2]]*5 + [[290, 4, 50, 3]]*2 + [[360, 4, 50, 3]]*4 + [[360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]],
    "星期五": [[270, 5, 50, 2]]*3 + [[270, 4, 50, 3], [270, 4, 100, 1]] + [[360, 4, 100, 1]]*2 + [[470, 3, 100, 1]]*4 + [[470, 4, 100, 1]]*7,
    "星期六": [[340, 4, 50, 0]]*3 + [[340, 3, 50, 1], [340, 3, 100, 1]] + [[360, 3, 100, 1]]*2 + [[470, 3, 100, 1]]*4 + [[470, 4, 100, 1]]*7,
    "星期日": [[340, 4, 50, 1]]*5 + [[360, 4, 50, 1], [360, 4, 50, 3]] + [[370, 4, 50, 3]]*4 + [[360, 7, 50, 3], [360, 6, 50, 3], [360, 5, 50, 3], [360, 4, 50, 3], [360, 3, 50, 3], [360, 2, 50, 3], [360, 1, 50, 3]]
}

bd1_prices = {
    "星期一": [[99, 3, 660]]*5 + [[99, 3, 792]]*2 + [[99, 3, 924]]*4 + [[99, 3, 792]]*7,
    "星期二": [[99, 3, 660]]*5 + [[99, 3, 792]]*2 + [[99, 3, 924]]*4 + [[99, 3, 792]]*7,
    "星期三": [[99, 3, 660]]*5 + [[99, 3, 792]]*2 + [[99, 3, 924]]*4 + [[99, 3, 792]]*7,
    "星期四": [[99, 3, 660]]*5 + [[99, 3, 792]]*2 + [[99, 3, 924]]*4 + [[99, 3, 792]]*7,
    "星期五": [[99, 3, 660]]*3 + [[660, 1, 660], [99, 1, 660]] + [[1056, 1, 1056]]*2 + [[1320, 1, 1320]]*11
}

bd2_prices = {
    "星期一": [[660, 1, 660]]*3 + [[880, 3, 660]]*2 + [[880, 3, 792]]*2 + [[880, 3, 924]]*4 + [[880, 3, 792]]*7,
    "星期二": [[660, 1, 660]]*3 + [[880, 3, 660]]*2 + [[880, 3, 792]]*2 + [[880, 3, 924]]*4 + [[880, 3, 792]]*7,
    "星期三": [[660, 1, 660]]*3 + [[880, 3, 660]]*2 + [[880, 3, 792]]*2 + [[880, 3, 924]]*4 + [[880, 3, 792]]*7,
    "星期四": [[660, 1, 660]]*3 + [[880, 3, 660]]*2 + [[880, 3, 792]]*2 + [[880, 3, 924]]*4 + [[880, 3, 792]]*7,
    "星期日": [[924, 1, 924]]*3 + [[880, 3, 924]]*2 + [[880, 3, 1056]]*6 + [[880, 3, 792]]*7
}

# --- 側邊欄輸入介面 ---
with st.sidebar:
    st.header("⚙️ 輸入參數")
    selected_days = st.multiselect("選擇星期幾：", week, default=["星期一"])
    input_hours = st.number_input("唱幾小：", min_value=0, max_value=24, value=3)
    input_people = st.number_input("幾個人：", min_value=0, max_value=100, value=1)
    
    is_drinking = st.radio("喝酒嗎：", ("我要先不", "喝爆"))
    limjew_val = 1 if is_drinking == "喝爆" else 0
    
    is_birthday = st.radio("有人生日嗎：", ("ㄐㄐ", "有喔"))
    birthday_val = 1 if is_birthday == "有喔" else 0

    calculate_btn = st.button("🚀 開算")

# --- 計算邏輯 ---
if calculate_btn:
    # 錯誤檢查 (原本程式碼的幽默提示)
    if input_hours == 0:
        st.error("唱 0 小時你問我衝三小？？？")
    elif input_hours > 18:
        st.error("白癡喔好樂迪根本沒開那麼久？？？")
    elif input_people == 0:
        st.error("就是有你這種人問幾個人給我回答 0 害林北要多寫這行不然除以 0 程式會爆掉")
    elif not selected_days:
        st.warning("阿沒給日期是要我自己猜就對了？？？")
    else:
        # 正式進入計算邏輯
        normal_results = []
        bd_results = []
        all_prices = []

        # 1. 一般價格計算
        for day in selected_days:
            for entrytime in range(18):
                if entrytime + input_hours <= 18:
                    now = entrytime
                    price = 0
                    h_remain = input_hours
                    
                    # 初始時數價格
                    now += prices[day][entrytime][1]
                    now += prices[day][entrytime][3] * birthday_val
                    price += prices[day][entrytime][0]
                    h_remain -= prices[day][entrytime][1]
                    h_remain -= prices[day][entrytime][3] * birthday_val
                    
                    # 續唱費用
                    while h_remain > 0:
                        price += prices[day][now][2]
                        now += 1
                        h_remain -= 1
                    
                    # 清潔費/服務費
                    price += ds[0] if entrytime < 11 else ds[1]
                    
                    # 酒水基本費
                    if limjew_val:
                        price += int(kpf / input_people)
                    
                    normal_results.append({"day": day, "entry": entrytime, "price": price})
                    all_prices.append(price)

        # 2. 壽星優惠計算 (如果有的話)
        if birthday_val:
            # 方案一
            for day in [d for d in selected_days if d in bd1_prices]:
                for entrytime in range(3):
                    if entrytime + input_hours <= 18:
                        now = entrytime
                        total_p = 0
                        h_remain = input_hours
                        now += bd1_prices[day][entrytime][1]
                        total_p += bd1_prices[day][entrytime][0] * min(6, input_people)
                        h_remain -= bd1_prices[day][entrytime][1]
                        while h_remain > 0:
                            total_p += bd1_prices[day][now][2]
                            now += 1
                            h_remain -= 1
                        total_p += ds[0] * input_people
                        if limjew_val: total_p += kpf
                        final_p = int(total_p / input_people)
                        bd_results.append({"name": "方案一"+day, "entry": entrytime, "price": final_p})
                        all_prices.append(final_p)

            # 方案二
            for day in [d for d in selected_days if d in bd2_prices]:
                for entrytime in range(3, 18):
                    if entrytime + input_hours <= 18:
                        now = entrytime
                        total_p = 0
                        h_remain = input_hours
                        now += bd2_prices[day][entrytime][1]
                        total_p += bd2_prices[day][entrytime][0]
                        h_remain -= bd2_prices[day][entrytime][1]
                        while h_remain > 0:
                            total_p += bd2_prices[day][now][2]
                            now += 1
                            h_remain -= 1
                        total_p += ds[0] * input_people
                        if limjew_val: total_p += kpf
                        final_p = int(total_p / input_people)
                        bd_results.append({"name": "方案二"+day, "entry": entrytime, "price": final_p})
                        all_prices.append(final_p)

        # 找出最低價
        min_p = min(all_prices) if all_prices else 0

        # --- 顯示結果 ---
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("📊 一般計費結果")
            for res in normal_results:
                time_str = f"{res['entry']+12} 點" if res['entry'] < 12 else f"{week[(week.index(res['day'])+1)%7]} {res['entry']-12} 點"
                is_cheapest = "🔥 **最便宜!**" if res['price'] == min_p else ""
                st.write(f"{res['day']} {time_str} 進場：每人 **{res['price']}** 元 {is_cheapest}")

        with col2:
            st.header("🎂 壽星優惠方案")
            if not bd_results:
                st.write("沒得用或沒人過生日 ㄐㄐ")
            for res in bd_results:
                time_str = f"{res['entry']+12} 點" if res['entry'] < 12 else f"{res['name'][0:3]} 下一天 {res['entry']-12} 點"
                is_cheapest = "🔥 **最便宜!**" if res['price'] == min_p else ""
                st.write(f"{res['name']} {time_str} 進場：每人 **{res['price']}** 元 {is_cheapest}")

else:

    st.info("請在左側填寫資訊後按「開算」")
