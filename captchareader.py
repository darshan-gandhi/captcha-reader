import cv2
import tkinter as tk
from google.colab.patches import cv2_imshow
print("Hey enter your name:")
name=input()
print(f"hello {name}! Please verify yourself by entering the captcha given below")
img=cv2.imread('2b827.png')
cv2_imshow(img)
store='2b827'
print("Please enter the captcha shown above")

# master = tk.Tk()
# tk.Label(master, text="Enter your answer here").grid(row=0)
# e1 = tk.Entry(master)
# e1.grid(row=0, column=1)
# master.mainloop()

print("----------------")
answer=input("Enter the captcha:")
print("----------------")

if answer==store:
  print(f"Hey {name}! You are a valid user you may proceed ahead")
else:
  print("Bot detected!!!")
