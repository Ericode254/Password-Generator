import flet as flt
import string
import random
import pyperclip as pc

def password_generator(length: int):
    choices = string.ascii_letters + string.digits + string.punctuation
    password = random.choices(choices, k=int(length))

    return "".join(password)

def myapp(page: flt.Page):
    def submit(e):
        password = password_generator(text.value)
        pc.copy(password)
        page.add(flt.Text(f"Your password is: {password}"))


    page.theme_mode = flt.ThemeMode.DARK # change DARK to LIGHT to convert it to light mode
    page.window_height = 400
    page.window_width = 500

    page.title = 'Password Generator'

    text = flt.TextField(
            label = "Size of password",
            value = "Enter only numbers",
            suffix=flt.ElevatedButton("Submit", on_click=submit),
            keyboard_type=flt.KeyboardType.NUMBER,
            on_submit=submit,
            border = flt.InputBorder.UNDERLINE
        )

    page.add(text)
    page.update()


flt.app(target=myapp)
