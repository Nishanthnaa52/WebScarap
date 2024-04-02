import customtkinter as ctk 
import requests
from bs4 import BeautifulSoup
import sys, os

app = ctk.CTk()

app.title("WebScrap")

app.geometry('1200x800')



#function section.
def url():
    try:
        url = url_input_box.get()
        code = requests.get(url)
        html_code = BeautifulSoup(code.text, 'html.parser')
        site_title.insert('end',f'Title : {html_code.title.string}')
        site_status.insert('end',f'Status code : {code}')

        if(tag_input.get() != '' and attri_input.get() != ''):
            for i in html_code.find_all(f'{tag_input.get()}'):
                html_output_box.insert('end',f'{i.get(attri_input.get())}\n')

        
        elif (tag_input.get() != ''):
            if (check_button.get() == 1):
                for i in html_code.find_all(f'{tag_input.get()}'):
                    html_output_box.insert('end',i.get_text())
            else:
                for i in html_code.find_all(f'{tag_input.get()}'):
                    html_output_box.insert('end',f'{i}\n')

        else:
            if(check_button.get() == 1):
                html_output_box.insert('end',html_code.get_text())
            else:
                html_output_box.insert('end',code.text)

    except :
        url_input_box.configure(placeholder_text='Enter corret URL (like . https://######.$$$)', placeholder_text_color='red')

def clear():
    html_output_box.delete(0.0,'end')
    site_status.delete(0.0,'end')
    site_title.delete(0.0,'end')
    url_input_box.delete(0,'end')
    tag_input.delete(0,'end')
    attri_input.delete(0,'end')

def html_save():
    f_name = file_name.get()
    user_name = os.getlogin()

    if(sys.platform == 'win32'):
        if f_name.replace(' ','') == '':
            status_label.configure(text='Set file name..!', text_color='red')        
        else:
            html = html_output_box.get(0.0,'end')
            with open(f'C:\\users\\{user_name}\\downloads\\{f_name}.html', 'w', encoding="utf-8") as f1:
                f1.write(html)
            f1.close()
            status_label.configure(text='Saved..!',text_color='green')

    
    else:
        if f_name.replace(' ','') == '':
            status_label.configure(text='Set file name..!', text_color='red')        
        else:
            html = html_output_box.get(0.0,'end')
            with open(f'/home/{user_name}/Downloads/{f_name}.html', 'w') as f1:
                f1.write(html)
            f1.close()
            status_label.configure(text='Saved..!',text_color='green')


def txt_save():
    f_name = file_name.get()
    user_name = os.getlogin()

    if(sys.platform == 'win32'):
        if f_name.replace(' ','') == '':
            status_label.configure(text='Set file name..!', text_color='red')        
        else:
            html = html_output_box.get(0.0,'end')
            with open(f'C:\\users\\{user_name}\\downloads\\{f_name}.txt', 'w', encoding="utf-8") as f1:
                f1.write(html)
            f1.close()
            status_label.configure(text='Saved..!',text_color='green')
    
    else:
        if f_name.replace(' ','') == '':
            status_label.configure(text='Set file name..!', text_color='red')        
        else:
            html = html_output_box.get(0.0,'end')
            with open(f'/home/{user_name}/Downloads/{f_name}.txt', 'w') as f1:
                f1.write(html)
            f1.close()
            status_label.configure(text='Saved..!',text_color='green')




#Main fram section.
            
main_fram  = ctk.CTkScrollableFrame(master=app,width=1000, height=800, orientation = 'vertical')
main_fram.pack(ipadx=300,pady=5)


#url input section.
frame_1 = ctk.CTkFrame(master=main_fram, width=300, height=300,)


frame_1_left = ctk.CTkFrame(master=frame_1, width=200, height=30,fg_color="transparent")

clear_button = ctk.CTkButton(master=frame_1_left, text='Clear',width=60,command=clear)
clear_button.pack(side='right')

button_1 = ctk.CTkButton(master=frame_1_left, text='Get data', width=40, command=url)
button_1.pack(side='right',padx=10, pady=10)


url_input_box = ctk.CTkEntry(master=frame_1_left, placeholder_text='URL',width=400)
url_input_box.pack(side='left',padx=10)

frame_1_left.pack(padx=10, side='left')

frame_1_right = ctk.CTkFrame(master=frame_1, width=200, height=30, fg_color='transparent')

tag_input = ctk.CTkEntry(master=frame_1_right, placeholder_text='Tag')
tag_input.pack(side='left')

attri_input = ctk.CTkEntry(master=frame_1_right, placeholder_text='Attribut')
attri_input.pack(side='left', padx=10)

check_button = ctk.CTkCheckBox(master=frame_1_right, text='Text Only')
check_button.pack(side='right')

frame_1_right.pack(side='right', padx=10)

frame_1.pack(ipady=10, pady=10)



#title and status section.
tas = ctk.CTkFrame(master=main_fram, width=1000, height=40)

site_title = ctk.CTkTextbox(master=tas, width=500, height=30,)
site_title.pack(pady=10, padx=5, side='left')

site_status = ctk.CTkTextbox(master=tas, width=500, height=30,)
site_status.pack(pady=10, padx=5, side='right')

tas.pack(pady=10)

#html output box section.
frame_2 = ctk.CTkFrame(master=main_fram, width=300, height=300)


html_output_box = ctk.CTkTextbox(master=frame_2, width=1000, height=450, wrap='none')
html_output_box.pack()

frame_2.pack()

#bottom of the out section.
frame_3 = ctk.CTkFrame(master=main_fram, width=400, height=100)


file_name = ctk.CTkEntry(master=frame_3, width=200, placeholder_text='FILE NAME')
file_name.pack(side='left', padx=10)

html_save_button = ctk.CTkButton(master=frame_3, width=80, height=30, text='HTML File', command=html_save)
html_save_button.pack(side='left',padx=10, pady=10)

text_save_button = ctk.CTkButton(master=frame_3, width=80, height=30, text='TXT File', command=txt_save)
text_save_button.pack(side='left',padx=10)

status_label = ctk.CTkLabel(master=frame_3, width=100, text='', text_color='green')
status_label.pack(pady=10, padx=10)

frame_3.pack(pady=10)

app.mainloop()