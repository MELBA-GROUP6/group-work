from tkinter import *
from tkinter import messagebox
import random

size = 9
root = Tk()


class disply():

    def __init__(self, gui, width, height):

        self.SOLVED, self.NOT_SOLVED, self.INCORRECT = "ትክክል ነው", "አልተጀመረም", "ትክክል አይደለም!"
        self.solution_status = StringVar(gui)
        self.gui = gui
        gui.title("Sudoku ጨዋታ")
        self.width, self.height = width, height
        gui.geometry(f'{510}x{820}')

        font = ('Arial', 35)
        color = 'white'

        Button(root, text='ቀላል', command=self.new_grid, bg='#21292c', fg='white', height=2, width=10).place(x=50, y=550)
        Button(root, text='እርዳታ', command=self.help, bg='#21292c', fg='white', height=2, width=10).place(x=410, y=750)
        Button(root, text='መካከለኛ', command=self.new_gridm, bg='#21292c', fg='white', height=2, width=10).place(x=180,
                                                                                                               y=550)
        Button(root, text='ከባድ', command=self.new_gridh, bg='#21292c', fg='white', height=2, width=10).place(x=300,
                                                                                                             y=550)
        Button(root, text='ውጤቶን ይወቁ', command=self.check_solution, bg='#21292c', fg='white', height=2, width=12).place(
            x=170, y=630)
        Label(root, textvariable=self.solution_status, fg='red', font=('Helvetica 15 bold')).place(x=100, y=700)
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.correct_cell = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        for row in range(size):
            for column in range(size):

                if (row < 3 or row > 5) and (column < 3 or column > 5):
                    color = 'orange'
                elif row in [3, 4, 5] and column in [3, 4, 5]:
                    color = 'orange'
                else:
                    color = 'white'

                self.grid[row][column] = Entry(gui, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                               highlightcolor='red', highlightthickness=1,
                                               highlightbackground='black',
                                               textvar=main_grid[row][column])
                self.grid[row][column].bind('<Motion>', self.clear)
                self.grid[row][column].bind('<FocusIn>', self.clear)
                self.grid[row][column].bind('<Button-1>', self.clear)
                self.grid[row][column].grid(row=row, column=column)

        self.new_grid()

    def clear(self, event):
        for row in range(size):
            for column in range(size):
                if main_grid[row][column].get() == '':
                    continue
                if len(main_grid[row][column].get()) > 1 or main_grid[row][column].get() not in ['1', '2', '3', '4',
                                                                                                 '5', '6', '7',
                                                                                                 '8', '9']:
                    main_grid[row][column].set('')

    def clear_grid_cell(self):
        for row in range(size):
            for column in range(size):
                main_grid[row][column].set('')

    def help(self):
        messagebox.showinfo("እርዳታ", """ወደ ሱዶኩ እንኳን ደህና መጡ!


የዚህ ጨዋታ ዓላማ 9x9 የመስመር ላይ ቁጥሮችን ከ 1 እስከ 9 በመሙላት እያንዳንዱ ረድፍ, አምድ, እና 3x3 ንዑስ ግሪድ ሁሉንም ቁጥሮች ከ 1 እስከ 9 ያለ መደጋገም ይይዛል።

ጨዋታውን ለመጀመር አስቸጋሪ የሆነ ደረጃ ይምረጡ - ቀላል , መካከለኛ ወይም ከባድ . አስቸጋሪው መጠን በሰሌዳው ላይ ያሉ ባዶ ሴሎችን ብዛት ይወስናል።

እያንዳንዱ ረድፍ፣ አምድ፣ እና 3x3 ንዑስ ግሪድ ያለመደጋገም ሁሉንም ዲጂቶች እንዲይዙ 9x9 ንዑስ ቁጥሮችን ከ1 እስከ 9 ባሉት ቁጥሮች ይሙላው።
ቁጥርን ለመሙላት አንድ ህዋስ ይጫኑ። 

 የእርስዎን ውጤት ለማጣራት የውጤቱን ቁልፍ ይጫኑ።
. """)

    def new_grid(self):
        self.clear_grid_cell()
        self.top_row()
        self.solve()
        self.save_grid()
        self.solutione()
        self.solution_status.set(f"የጨዋታ ሁኔታ: {self.NOT_SOLVED}")

    def new_gridm(self):
        self.clear_grid_cell()
        self.top_row()
        self.solve()
        self.save_grid()
        self.solutionm()
        self.solution_status.set(f"የጨዋታ ሁኔታ: {self.NOT_SOLVED}")

    def new_gridh(self):
        self.clear_grid_cell()
        self.top_row()
        self.solve()
        self.save_grid()
        self.solutionh()
        self.solution_status.set(f"የጨዋታ ሁኔታ: {self.NOT_SOLVED}")

    def solve(self):
        solution = Sudoku()

    def top_row(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        number_choice = random.sample(number_list, len(number_list))

        for n in range(size):
            main_grid[0][n].set(number_choice[n])

    def solutione(self):
        CHANCE_TO_HIDE = 63
        for column in range(size):
            for row in range(size):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_grid[row][column].set('')

    def solutionm(self):
        CHANCE_TO_HIDE = 77
        for column in range(size):
            for row in range(size):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_grid[row][column].set('')

    def solutionh(self):
        CHANCE_TO_HIDE = 87
        for column in range(size):
            for row in range(size):
                random_roll = random.randint(0, 100)
                if random_roll < CHANCE_TO_HIDE:
                    main_grid[row][column].set('')

    def save_grid(self):
        for row in range(size):
            for column in range(size):
                self.correct_cell[row][column] = main_grid[row][column].get()

    def correct_grid(self):
        for row in range(size):
            for column in range(size):
                if main_grid[row][column].get() != self.correct_cell[row][column]:
                    return False
        return True

    def check_solution(self):
        if self.correct_grid():
            self.solution_status.set(f"የጨዋታ ሁኔታ: {self.SOLVED}")
        else:
            self.solution_status.set(f"የጨዋታ ሁኔታ: {self.INCORRECT}")


class Sudoku():

    def __init__(self):
        self.set_zero()
        self.solved()

    def set_zero(self):
        for row in range(size):
            for column in range(size):
                if main_grid[row][column].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    main_grid[row][column].set(0)

    def solved(self, i=0, j=0):
        i, j = self.fill_next_grid(i, j)

        if i == -1:
            return True
        for e in range(1, 10):
            if self.real_cell(i, j, e):
                main_grid[i][j].set(e)
                if self.solved(i, j):
                    return True
                main_grid[i][j].set(0)
        return False

    def fill_next_grid(self, i, j):
        for row in range(i, size):
            for column in range(j, size):
                if main_grid[row][column].get() == '0':
                    return row, column

        for row in range(0, size):
            for column in range(0, size):
                if main_grid[row][column].get() == '0':
                    return row, column

        return -1, -1

    def real_cell(self, row, column, e):
        for x in range(size):
            if main_grid[row][x].get() == str(e):
                return False
        for x in range(size):
            if main_grid[x][column].get() == str(e):
                return False

        secTopX, secTopY = 3 * int((row / 3)), 3 * int((column / 3))
        for row in range(secTopX, secTopX + 3):
            for column in range(secTopY, secTopY + 3):
                if main_grid[row][column].get() == str(e):
                    return False

        return True


main_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

for row in range(size):
    for column in range(size):
        main_grid[row][column] = StringVar(root)

game = disply(root, 270, 340)

root.mainloop()
