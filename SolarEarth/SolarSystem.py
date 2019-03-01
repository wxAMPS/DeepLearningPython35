from tkinter import *
from SolarEarth.Earth import Earth
import time


def btn_reaction():
    if btn_text.get() == 'Run':
        btn_text.set('Pause')
    else:
        btn_text.set('Run')

    while btn_text.get() == 'Pause':
        # earth.orbit()
        earth.dynamic_orbit(10)
        pos_text.set('X:{0:9.1f}, Y:{1:9.1f}'.format(earth[0], earth[1]))
        root.update()
        time.sleep(0.1)


def btn_reset():
    global earth
    del earth
    earth = Earth(canvas, sun, [float(vx.get()), float(vy.get())])


root = Tk()
root.title('Solar System')

# frame for animation
frm_L = Frame(root)
canvas = Canvas(frm_L, width=800, height=600)
canvas.pack()
frm_L.pack(side=LEFT)

# frame for info display
frm_R = Frame(root, bd=2, relief=SUNKEN)
Label(frm_R, text='Initial speed:').pack(pady=5, anchor='w')
frm_R1 = Frame(frm_R)
Label(frm_R1, text='Vx:').pack(side=LEFT)
vx = StringVar()
Entry(frm_R1, textvariable=vx).pack()
frm_R1.pack()
frm_R2 = Frame(frm_R)
Label(frm_R2, text='Vy:').pack(side=LEFT)
vy = StringVar()
Entry(frm_R2, textvariable=vy).pack(side=LEFT)
frm_R2.pack()

Label(frm_R, text='Earth Coordinates:').pack(pady=5, anchor='w')
pos_text = StringVar()
Label(frm_R, textvariable=pos_text).pack(pady=5, anchor='w')
btn_text = StringVar()
Button(frm_R, textvariable=btn_text, command=btn_reaction).pack(pady=15, side=BOTTOM)
Button(frm_R, text='Reset', command=lambda: btn_reset()).pack()
frm_R.pack(side=RIGHT)

root.update()

sun = canvas.create_oval(canvas.winfo_width() / 2 - 10, canvas.winfo_height() / 2 - 10,
                         canvas.winfo_width() / 2 + 10, canvas.winfo_height() / 2 + 10,
                         fill='red')
vx.set('-1')
vy.set('0')
earth = Earth(canvas, sun, [float(vx.get()), float(vy.get())])
pos_text.set('X:{0:9.1f}, Y:{1:9.1f}'.format(earth[0], earth[1]))
btn_text.set('Run')
# btn_reaction()

root.mainloop()
