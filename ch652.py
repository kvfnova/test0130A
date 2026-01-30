
111
def calculate_bmi(height, weight):
    """
    計算 BMI 值
    
    參數:
        height (float): 身高（公尺）
        weight (float): 體重（公斤）
    
    回傳:
        float: BMI 值
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)




def get_bmi_category(bmi):
    """
    根據 BMI 值判斷體重分類
    
    參數:
        bmi (float): BMI 值
    
    回傳:
        str: 體重分類
    """
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24:
        return "正常範圍"
    elif 24 <= bmi < 27:
        return "過重"
    elif 27 <= bmi < 30:
        return "輕度肥胖"
    elif 30 <= bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"


# 使用範例
if __name__ == "__main__":
    # 測試案例
    height = 1.75  # 身高 175 公分
    weight = 70    # 體重 70 公斤
    
    bmi = calculate_bmi(height, weight)
    category = get_bmi_category(bmi)
    
    print(f"身高: {height} 公尺")
    print(f"體重: {weight} 公斤")
    print(f"BMI 值: {bmi}")
    print(f"體重分類: {category}")
    
    # 互動式輸入
    print("\n" + "="*40)
    try:
        h = float(input("請輸入身高（公尺）: "))
        w = float(input("請輸入體重（公斤）: "))
        
        user_bmi = calculate_bmi(h, w)
        user_category = get_bmi_category(user_bmi)
        
        print(f"\n您的 BMI 值: {user_bmi}")
        print(f"體重分類: {user_category}")
    except ValueError:
        print("輸入錯誤，請輸入有效的數字")
    except ZeroDivisionError:
        print("身高不能為 0")