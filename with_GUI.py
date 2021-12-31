import time
import tkinter as tk

# Colors for till 10 plates
colors = [
    "#4C0CF5", "#F54327", "#0F95F5", "#F5E427", "#02F586",
    "#F55B02", "#F5F418", "#F50056", "#18F5F2", "#7D0CF5"]

# Set an object for all plates, BUT the valuer of plates definided
# by the user is not set or configured here. It just creates and move them (teleport)
class Plates(object):
    def __init__(self, x1, y1, x2, y2, color, width):
        self.plate = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.witdh = width

    def teleport_plates(self, x1, y1, x2, y2) -> None:
        canvas.coords(self.plate, x1, y1, x2, y2)
        canvas.update()
        time.sleep(1)   # 1 Sec



# Object for the posts (nothing special here)
class Posts(object):
    def __init__(self, x1, y1, x2, y2, color, letter):
        self.post = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.letter = canvas.create_text(x2-8, y2+35, text=letter, fill=color, font=('Helvetica 15 bold'))


# Object for stack. Responsable to set the rectangles to move
class Stack(object):
    def __init__(self) -> None:
        self.plate_to_be_moved = []

    def stack_push(self, plate_item:Plates):
        # not == but is
        if plate_item is None:
            return None
        self.plate_to_be_moved.append(plate_item)
        plate_item.teleport_plates(*set_plate(self, plate_item.witdh))

    def stack_pop(self):
        if len(self.plate_to_be_moved) > 0:
            return self.plate_to_be_moved.pop()

class Status(object):
    def __init__(self, user_input) -> None:
        self.status_plates = canvas.create_text(40, 15, text=user_input, fill="#FFFFFF", font=('Helvetica 15 bold'))
        self.status_moves = canvas.create_text(40, 35, text=(2**user_input)-1, fill="#FFFFFF", font=('Helvetica 15 bold'))
        self.status_time = canvas.create_text(40, 55, text=round((2**user_input-1)/60, 2), fill="#FFFFFF", font=('Helvetica 15 bold'))

        self.status_plates_text = canvas.create_text(120, 15, text=" User input", fill="#FFFFFF", font=('Helvetica 15 bold'))
        self.status_moves_text = canvas.create_text(120, 35, text=" Moves", fill="#FFFFFF",font=('Helvetica 15 bold'))
        self.status_time_text = canvas.create_text(120, 55, text=" Minutes (≈)", fill="#FFFFFF",font=('Helvetica 15 bold'))



#function responsable to input the rectangles in the right position.
# Fallowing the commands of Stack
def set_plate(tower: Stack, width):
    x_size = (15 * width)
    y_size = (20 * len(tower.plate_to_be_moved))
# There are 3 towers and one is the startup(towerA)
# and the other two are created in base of the distance of the first tower
    x1_towerA = 150
    y1_towerA = 700
    x2_towerA = 150
    y2_towerA = 720
    # do NOT use == here
    if tower is towerA:
        x1 = x1_towerA + x_size
        y1 = y1_towerA - y_size
        x2 = x2_towerA - x_size
        y2 = y2_towerA - y_size
        print(f'TOWERA: x1={x1} | x2={x2} | y1={y1} | y2={y2}')

    elif tower is towerB:
        x1 = (x1_towerA*4) + x_size
        y1 = y1_towerA - y_size
        x2 = (x2_towerA*4) - x_size
        y2 = y2_towerA - y_size
        print(f'TOWERB: x1={x1} | x2={x2} | y1={y1} | y2={y2}')

    elif tower is towerC:
        x1 = (x1_towerA*6.5) + x_size
        y1 = y1_towerA - y_size
        x2 = (x2_towerA*6.5) - x_size
        y2 = y2_towerA - y_size
        print(f'TOWERC: x1={x1} | x2={x2} | y1={y1} | y2={y2}')
    return(x1, y1, x2, y2)


# The whole command starts here and it will be settled by this simple function
#Recursion
def algorithm(plateX, start: Stack, temp: Stack, goal: Stack) -> None:
    if plateX == 1:
        goal.stack_push(start.stack_pop())
    else:
        algorithm(plateX-1, start, goal, temp)
        goal.stack_push(start.stack_pop())
        algorithm(plateX-1, temp, start, goal)


# Window
window = tk.Tk()
window.title("The Hanoi Tower")

# Insert frame
frame = tk.Frame(window)
frame.pack()

# Background
canvas = tk.Canvas(frame, bg="#000000", width=1200, height=800)
canvas.pack()

# Towers
towerA = Stack()
towerB = Stack()
towerC = Stack()

# Posts
postA = Posts(140, 480, 160, 700, "#FFFFFF", 'A')
postB = Posts(590, 480, 610, 700, "#FFFFFF", 'B')
postC = Posts(965, 480, 985, 700, "#FFFFFF", 'C')

user_input = 7

# Create status
status = Status(user_input)


# This for is responsable to keep the whole code alive, it only depends of user_inputs (how many Plates the user wants to try)
for plate in range(user_input, 0, -1):
    rectangle = Plates(*set_plate(towerA, plate), colors[plate - 1], plate)
    towerA.stack_push(rectangle)

# Necessary to move the plates (The Brain of the whole code)
algorithm(user_input, towerA, towerB, towerC)


# Start TK (GUI)
def main():
    window.resizable(False, False)

    window.mainloop()


if __name__ == '__main__':
    main()
