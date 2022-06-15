"""
Author: Andy Wicks
Code can be found at: https://lyw4.life/Resources/python.php
Date started: Mon,  19 Oct 2020
Version: 0.0
Purposes:
    - To explore how frames are swapped to create the 'many windows' effect.
    Reference: https://tkdocs.com/tutorial/grid.html
"""
import tkinter as tk             # This has all the code for GUIs.
import tkinter.font as font      # This lets us use different fonts.


def center_window_on_screen():
    """
    This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below.
    :return: Nothing
    """
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def change_to_work():
    """
    This function swaps from the quiz
    frame to the work frame.
    :return: Nothing
    """
    quiz_frame.forget()
    work_frame.pack(fill='both', expand=1)


def change_to_quiz():
    """
    This function swaps from the work
    frame to the quiz frame.
    :return: Nothing
    """
    quiz_frame.pack(fill='both', expand=1)
    work_frame.forget()


# Now we get to the program itself:-
# Let's set up the window ...
root = tk.Tk()
root.title("My Work - Swapping frames")
root.configure(bg='lightyellow')
# Set the icon used for your program
root.iconphoto(True,
               tk.PhotoImage(file='info.png'))

width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

# Here, we create two frames of which only
# one will be visible at a time.
quiz_frame = tk.Frame(root)
work_frame = tk.Frame(root)

# Let's create the fonts that we need.
font_large = font.Font(family='Georgia',
                       size='24',
                       weight='bold')
font_small = font.Font(family='Georgia',
                       size='12')

# The widgets needed for the quiz frame.
# First, let's display te logo.
img_logo = tk.PhotoImage(file='logo.png')
lbl_logo_quiz = tk.Label(quiz_frame,
                         image=img_logo)

# Next, comes the heading for this frame.
lbl_heading_quiz = tk.Label(quiz_frame,
                            text='This is the quiz frame',
                            font=font_large)
lbl_logo_quiz.pack(pady=20)
lbl_heading_quiz.pack(pady=20)

# And finally, the button to swap between the frames.
btn_change_to_work = tk.Button(quiz_frame,
                               text='Change to work',
                               font=font_small,
                               command=change_to_work)
btn_change_to_work.pack(pady=20)

# The widgets needed for the work frame.
# These are only being used in this example
# to show that both frames are working as
# expected.

# First the image gets added.
lbl_logo_work = tk.Label(work_frame,
                         image=img_logo)
lbl_logo_work.pack(pady=20)

# Next, we'll add a heading.
lbl_heading_work = tk.Label(work_frame,
                            text='This is the WORK frame',
                            font=font_large)
lbl_heading_work.pack(pady=20)

# Finally, we need the button to
# swap back to the quiz frame.
btn_change_to_quiz = tk.Button(work_frame,
                               font=font_small,
                               text='Change to quiz',
                               command=change_to_quiz)
btn_change_to_quiz.pack(pady=20)

# Only the quiz frame needs to be shown
# when the program starts.  The work frame
# will only appear when the Change button
# is clicked.
quiz_frame.pack(fill='both', expand=1)

root.mainloop()