from tkinter import Button, Label, Entry
from auth_servise import register
from auth_servise import login
from product_servise  import  get_all_products


# def clear_window(tk):
#     for widget in tk.winfo_children:
#         widget.destroy()
def clear_window(tk):
    list = tk.grid_slaves()
    for l in list:
        l.destroy()

def render_main_screen(tk):
    Button(tk, text="Login", bg="green", fg="red", command = lambda: render_login_screen(tk)).grid(row=0, column=1)
    Button(tk, text="Register", bg="yellow", fg="red", command=lambda:render_register_screen(tk)).grid(row=0, column=0)


def render_register_screen(tk):
    clear_window(tk)
    Label(tk, text="Email").grid(row=0, column=0)
    email_entry = Entry(tk, bd=3)
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password" ).grid(row=1, column=0)
    paswword_entry = Entry(tk, bd=3, show="*")
    paswword_entry.grid(row=1, column=1)

    Label(tk, text="Confirm Password").grid(row=2, column=0)
    confirm_password_entry = Entry(tk, bd=3, show="*")
    confirm_password_entry.grid(row=2, column=1)

    def on_register():
        email = email_entry.get()
        password = paswword_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            Label(tk, text="Password doesn't match", fg="red").grid(row=3, column=1)
            return

        # print(email, password, confirm_password)
        result = register(email, password)
        if result:
            render_login_screen(tk)
        else:
            Label(tk, text="Email is already register", fg= "red").grid(row=3, column=1)

    Button(tk, text="Register", bg="yellow", fg="red",
           command=lambda: on_register()).grid(row=4, column=1)

def render_login_screen(tk):
    clear_window(tk)

    Label(tk, text="Email").grid(row=0, column=0)
    email_entry = Entry(tk, bd=3)
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password" ).grid(row=1, column=0)
    paswword_entry = Entry(tk, bd=3, show="*")
    paswword_entry.grid(row=1, column=1)

    def on_login():
        email = email_entry.get()
        password = paswword_entry.get()

        result = login(email, password)
        if result:
            render_products_list_screen(tk)
        else:
            Label(tk, text="Invalid operation", fg="red").grid(row=2, column=1)

    Button(tk, text="Login", bg="yellow", fg="red",
           command=lambda: on_login()).grid(row=3, column=1)

def render_products_list_screen(tk):
    clear_window(tk)

    products = get_all_products()
    a=5
