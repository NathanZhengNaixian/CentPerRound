import tkinter as tk
from tkinter import messagebox

# -----------------------
# 全局语言状态（默认为英文）
# -----------------------
current_language = 'en'  # 'cn' 或 'en'

def update_topmost_text():
    """
    根据 current_language 和 topmost_state 更新置顶按钮文字
    """
    if current_language == 'cn':
        if topmost_state.get():
            btn_topmost.config(bg="lightgreen", text="置顶: 开")
        else:
            btn_topmost.config(bg="lightgray", text="置顶: 关")
    else:  # English
        if topmost_state.get():
            btn_topmost.config(bg="lightgreen", text="Topmost: On")
        else:
            btn_topmost.config(bg="lightgray", text="Topmost: Off")

def toggle_topmost():
    """
    切换窗口置顶状态
    """
    topmost_state.set(not topmost_state.get())
    root.attributes("-topmost", topmost_state.get())
    update_topmost_text()

def reset_fields():
    """
    重置所有输入框和结果显示
    """
    entry_subtotal.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_discount_percent.delete(0, tk.END)
    entry_discount_amount.delete(0, tk.END)
    entry_tax_amount.delete(0, tk.END)
    entry_tax_percent.delete(0, tk.END)
    entry_shipping.delete(0, tk.END)

    # 恢复默认值
    entry_subtotal.insert(0, "0.00")
    entry_quantity.insert(0, "0")
    entry_discount_percent.insert(0, "0.00")
    entry_discount_amount.insert(0, "0.00")
    entry_tax_amount.insert(0, "0.00")
    entry_tax_percent.insert(0, "0.00")
    entry_shipping.insert(0, "0.00")

    # 重置结果文本
    if current_language == 'cn':
        label_result.config(text="每发子弹成本 (CPR): $0.00")
    else:
        label_result.config(text="Cost Per Round (CPR): $0.00")

def calculate_cpr():
    """
    计算每发子弹成本 (CPR) 的主函数
    """
    try:
        sub_total_price = float(entry_subtotal.get())
        quantity = int(entry_quantity.get())

        discount_percent = float(entry_discount_percent.get()) / 100
        discount_amount = float(entry_discount_amount.get())

        custom_tax_amount = float(entry_tax_amount.get())
        custom_tax_percent = float(entry_tax_percent.get()) / 100
        shipping = float(entry_shipping.get())

        # 折扣后的价格
        discount_value = sub_total_price * discount_percent
        discounted_price = sub_total_price - discount_value - discount_amount

        # 如果有税率且税额为0，则用税率计算税额
        if custom_tax_percent > 0 and custom_tax_amount == 0:
            custom_tax_amount = discounted_price * custom_tax_percent
            entry_tax_amount.delete(0, tk.END)
            entry_tax_amount.insert(0, f"{custom_tax_amount:.2f}")

        total_cost = discounted_price + custom_tax_amount + shipping
        cpr = total_cost / quantity

        if current_language == 'cn':
            label_result.config(text=f"每发子弹成本 (CPR): ${cpr:.2f}")
        else:
            label_result.config(text=f"Cost Per Round (CPR): ${cpr:.2f}")

    except ValueError:
        if current_language == 'cn':
            messagebox.showerror("输入错误", "请输入有效的数字")
        else:
            messagebox.showerror("Error", "Please enter valid numbers")

def calculate_custom_tax():
    """
    根据自定义税率计算税额，并将结果填入"税额 ($)"输入框
    """
    try:
        sub_total_price = float(entry_subtotal.get())
        discount_percent = float(entry_discount_percent.get()) / 100
        discount_amount = float(entry_discount_amount.get())
        custom_tax_percent = float(entry_tax_percent.get()) / 100

        discount_value = sub_total_price * discount_percent
        discounted_price = sub_total_price - discount_value - discount_amount

        custom_tax_calculated = discounted_price * custom_tax_percent
        entry_tax_amount.delete(0, tk.END)
        entry_tax_amount.insert(0, f"{custom_tax_calculated:.2f}")
    except ValueError:
        if current_language == 'cn':
            messagebox.showerror("输入错误", "请输入有效的数字")
        else:
            messagebox.showerror("Error", "Please enter valid numbers")

def autofill_tax_6_percent():
    """
    默认税率 6%，根据小计价格自动计算税额
    """
    try:
        sub_total_price = float(entry_subtotal.get())
        default_tax_amount = sub_total_price * 0.06
        entry_tax_amount.delete(0, tk.END)
        entry_tax_amount.insert(0, f"{default_tax_amount:.2f}")
    except ValueError:
        if current_language == 'cn':
            messagebox.showerror("输入错误", "请输入有效的小计价格")
        else:
            messagebox.showerror("Error", "Please enter a valid subtotal")

def set_chinese():
    """
    将界面文字切换为中文
    """
    root.title("弹药CPR计算器")
    btn_reset.config(text="重置")
    # 切换按钮始终为英文，不随语言变化
    # btn_language.config(text="Switch Language")

    label_subtotal.config(text="小计价格 ($):")
    label_quantity.config(text="子弹数量:")
    label_discount_percent.config(text="折扣 (%):")
    label_discount_amount.config(text="满减 ($):")
    label_tax_amount.config(text="税额 ($):")
    label_tax_percent.config(text="税率 (%):")
    btn_calc_tax.config(text="计算")
    btn_default_tax.config(text="默认6%")
    label_shipping.config(text="运费 ($):")
    btn_calculate.config(text="计算每发价格")
    label_result.config(text="每发子弹 (CPR): $0.00")

def set_english():
    """
    将界面文字切换为英文
    """
    root.title("Ammo CPR Calculator")
    btn_reset.config(text="Reset")
    # 切换按钮始终为英文，不随语言变化
    # btn_language.config(text="Switch Language")

    label_subtotal.config(text="Subtotal ($):")
    label_quantity.config(text="Quantity:")
    label_discount_percent.config(text="Discount %:")
    label_discount_amount.config(text="Discount ($):")
    label_tax_amount.config(text="Tax ($):")
    label_tax_percent.config(text="Rate (%):")
    btn_calc_tax.config(text="Calculate")
    btn_default_tax.config(text="Default 6%")
    label_shipping.config(text="Shipping ($):")
    btn_calculate.config(text="Calculate CPR")
    label_result.config(text="Cost Per Round (CPR): $0.00")

def toggle_language():
    """
    在中文与英文之间切换
    """
    global current_language
    if current_language == 'en':
        current_language = 'cn'
        set_chinese()
    else:
        current_language = 'en'
        set_english()

    update_topmost_text()

# -----------------------
# 创建主窗口
# -----------------------
root = tk.Tk()
root.title("Ammo CPR Calculator")  # 默认英文标题
root.geometry("400x520")

# 让 0, 1, 2 三列都可以随窗口大小变化
for col in range(3):
    root.grid_columnconfigure(col, weight=1)

# 置顶状态
topmost_state = tk.BooleanVar()
topmost_state.set(False)

# -----------------------
# 第一行：置顶 & 重置 & 语言切换
# -----------------------
frame_top = tk.Frame(root)
frame_top.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")

btn_topmost = tk.Button(
    frame_top, text="Topmost: Off", bg="lightgray",
    command=toggle_topmost
)
btn_topmost.pack(side=tk.LEFT)

btn_reset = tk.Button(
    frame_top, text="Reset", bg="lightblue", command=reset_fields
)
btn_reset.pack(side=tk.LEFT, padx=10)

# 语言切换按钮（始终显示英文）
btn_language = tk.Button(
    frame_top, text="Switch Language", bg="lightyellow", command=toggle_language
)
btn_language.pack(side=tk.LEFT, padx=10)

# -----------------------
# 小计价格 & 子弹数量
# -----------------------
frame_basic = tk.Frame(root, relief="groove", borderwidth=2, padx=5, pady=5)
frame_basic.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

label_subtotal = tk.Label(frame_basic, text="Subtotal ($):")
label_subtotal.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry_subtotal = tk.Entry(frame_basic, width=10)
entry_subtotal.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_subtotal.insert(0, "0.00")

label_quantity = tk.Label(frame_basic, text="Quantity:")
label_quantity.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_quantity = tk.Entry(frame_basic, width=10)
entry_quantity.grid(row=1, column=1, padx=5, pady=5, sticky="w")
entry_quantity.insert(0, "0")

# -----------------------
# 折扣（百分比 & 金额）
# -----------------------
frame_discount = tk.Frame(root, relief="groove", borderwidth=2, padx=5, pady=5)
frame_discount.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

label_discount_percent = tk.Label(frame_discount, text="Discount Percent (%):")
label_discount_percent.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry_discount_percent = tk.Entry(frame_discount, width=10)
entry_discount_percent.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_discount_percent.insert(0, "0.00")

label_discount_amount = tk.Label(frame_discount, text="Discount Amount ($):")
label_discount_amount.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_discount_amount = tk.Entry(frame_discount, width=10)
entry_discount_amount.grid(row=1, column=1, padx=5, pady=5, sticky="w")
entry_discount_amount.insert(0, "0.00")

# -----------------------
# 税额 & 税率
# -----------------------
frame_tax = tk.Frame(root, relief="groove", borderwidth=2, padx=5, pady=5)
frame_tax.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

label_tax_amount = tk.Label(frame_tax, text="Tax Amount ($):")
label_tax_amount.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry_tax_amount = tk.Entry(frame_tax, width=10)
entry_tax_amount.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_tax_amount.insert(0, "0.00")

label_tax_percent = tk.Label(frame_tax, text="Tax Rate (%):")
label_tax_percent.grid(row=1, column=0, sticky="e", padx=5, pady=5)

frame_tax_percent = tk.Frame(frame_tax)
frame_tax_percent.grid(row=1, column=1, padx=5, pady=5, sticky="w")

entry_tax_percent = tk.Entry(frame_tax_percent, width=5)
entry_tax_percent.pack(side=tk.LEFT)
entry_tax_percent.insert(0, "0.00")

btn_calc_tax = tk.Button(frame_tax_percent, text="Calculate", command=calculate_custom_tax)
btn_calc_tax.pack(side=tk.LEFT, padx=5)

btn_default_tax = tk.Button(frame_tax_percent, text="Default 6%", command=autofill_tax_6_percent)
btn_default_tax.pack(side=tk.LEFT)

# -----------------------
# 运费
# -----------------------
label_shipping = tk.Label(root, text="Shipping ($):")
label_shipping.grid(row=7, column=0, sticky="e", padx=5, pady=5)

entry_shipping = tk.Entry(root, width=10)
entry_shipping.grid(row=7, column=1, padx=5, pady=5, sticky="w")
entry_shipping.insert(0, "0.00")

# -----------------------
# 计算按钮
# -----------------------
btn_calculate = tk.Button(root, text="Calculate CPR", command=calculate_cpr)
btn_calculate.grid(row=8, column=0, columnspan=3, pady=10)

# -----------------------
# 显示结果
# -----------------------
label_result = tk.Label(root, text="Cost Per Round (CPR): $0.00", fg="blue", font=("Arial", 12, "bold"))
label_result.grid(row=9, column=0, columnspan=3, pady=10)

# 启动前，先更新一下置顶按钮的文字（并保持英文初始状态）
update_topmost_text()

# 如果要默认启动时就保证所有文字是英文，可显式调用 set_english()：
set_english()

root.mainloop()
