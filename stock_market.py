import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

def show_graph():
    x=ent.get()
    data = yf.download(x,start='2024-01-01',end='2024-12-31')
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(data.index, data['Close'], label=f'{x} Closing Price')

    plot_image_path = 'stock_price_plot.png'
    fig.savefig(plot_image_path)

    img = Image.open(plot_image_path)
    img_tk = ImageTk.PhotoImage(img)

    img_lbl.config(image=img_tk)
    img_lbl.image = img_tk

def show_on_text():
    x=ent.get()
    data = yf.download(x,start='2024-01-01',end='2024-12-31')
    data_str=data.to_string()
    text.delete(1.0,tk.END)
    text.insert(tk.END,data_str)
    show_graph()
    

root=tk.Tk()
root.title("stock market")

lab = tk.Label(root,text="Select stock")
lab.grid(row=0,column=0)
ent = tk.Entry(root,width=20)
ent.grid(row=0,column=1)
but = tk.Button(root,text="GO",width=30,command=show_on_text)
but.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
text = tk.Text(root,width=175,height=40)
text.grid(row=0,column=2,rowspan=3)
img_lbl = tk.Label(root)
img_lbl.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()