from tkinter import *   # импорт tkinter
# создание окна
win = Tk()
win.title('Tetris')
win['bg'] = '#333336'
win.resizable(width=False, height=False)
# win.iconbitmap('icons8_tetris.ico')
win.geometry('380x400+600+200')

ip = Canvas(win, width=10 * 20, height=16 * 20, bg='#333344', bd=0, highlightthickness=1,
            relief='ridge')

for i in range(40, 10 * 20, 20):
    ip.create_line(i, 0, i, 16 * 20, fill='white')
for i in range(40, 16 * 20, 20):
    ip.create_line(0, i, 10 * 20, i, fill='white')
ip.place(x=40, y=40)
# Canvas со следующей фигурой
sf = Canvas(win, width=6 * 20, height=4 * 20, bg='#333344', bd=0, highlightthickness=1,
            relief='ridge')


# game place

for i in range(40, 6 * 20, 20):
    sf.create_line(i, 0, i, 4 * 20, fill='white')
for i in range(40, 4 * 20, 20):
    sf.create_line(0, i, 6 * 20, i, fill='white')
sf.place(x=12 * 20, y=40)
# Canvas с информацией об игре
inf = Canvas(win, width=6 * 20, height=13 * 20, bg='#333344', bd=0, highlightthickness=1, relief='ridge')
inf.create_text(3 * 20, 20, text='Очки', font='Ubuntu 13', fill='white')
inf.create_text(3 * 20, 5 * 20, text='Уровень', font='Ubuntu 13', fill='white')
inf.place(x=12 * 20, y=6 * 20)



# block T
block6 = ip.create_rectangle(140, 120, 160, 140, fill='white')
block7 = ip.create_rectangle(160, 120, 180, 140, fill='white')
block8 = ip.create_rectangle(180, 120, 200, 140, fill='white')
block9 = ip.create_rectangle(160, 140, 180, 160, fill='white')


def leftblockL(event):
    if (ip.coords(block1)[0] > 0):
        ip.move(block1, -20, 0)
        ip.move(block2, -20, 0)
        ip.move(block3, -20, 0)
        ip.move(block4, -20, 0)

    print('x=', ip.coords(block1)[0])


def rightblockL(event):
    if (ip.coords(block2)[2] < 200):
        ip.move(block1, 20, 0)
        ip.move(block2, 20, 0)
        ip.move(block3, 20, 0)
        ip.move(block4, 20, 0)
    print(ip.coords(block2)[0])


def downblockL(event):
    if (ip.coords(block2)[3] < 360):
        ip.coords(block1, ip.coords(block1)[0], 300, ip.coords(block1)[2], 320)
        ip.coords(block4, ip.coords(block4)[0], 320, ip.coords(block4)[2], 340)
        ip.coords(block3, ip.coords(block3)[0], 340, ip.coords(block3)[2], 360)
        ip.coords(block2, ip.coords(block2)[0], 340, ip.coords(block2)[2], 360)
    print(ip.coords(block2)[3])


def rotateL(event):
    print()


ip.bind('<Left>', leftblockL)
ip.bind('<Down>', downblockL)
ip.bind('<Right>', rightblockL)
ip.bind('<space>', rotateL)

ip.focus_set()
win.mainloop()
