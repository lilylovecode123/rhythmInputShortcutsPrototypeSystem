"""
Initialize necessary modules:
time, datetime, tkinter, keyboard, threading, numpy and PIL.
"""
import time
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import keyboard, threading
import numpy as np
from PIL import ImageGrab, Image

# create an empty list called feedback_list
feedback_list = []

# define function shortcut_function_1():
def shortcut_function_1():
    print("Saving file")
    # generate a filename based on the current datetime
    t = datetime.now().strftime("./%Y%m%d_%H_%M_%S") + ".txt"
    f = open(t, 'w')
    # write the current datetime to the file
    f.write(str(datetime.now().now()))
    f.close()
    print("Save file success")
    msg = "Save file success " + t
    # append the success msg to feedback_list
    feedback_list.append(msg)

# define function shortcut_function_2():
def shortcut_function_2():
    # take a screenshot
    print("Screenshoting")
    # capture the screen using ImageGrab
    img = ImageGrab.grab()
    # convert the image to RGB
    img = img.convert("RGB")
    # generate a filename based on the current datetime
    t = datetime.now().strftime("./%Y%m%d_%H_%M_%S") + ".jpg"
    img.save(t)
    print("Screenshot success")
    msg = "Screenshot success " + t
    # append the success msg to feedback_list
    feedback_list.append(msg)

# define function shortcut_function():
def shortcut_function_3():
    # start another new program
    print("Run another software")
    # import another_software module and run_it
    import another_software
    another_software.run()
    t = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    msg = "Run another software " + t
    # append the success msg to feedback_list
    feedback_list.append(msg)

"""
create an empty dictionary called shortcut_mapping, 
and load shortcut_mapping form a file called "rhythm.txt"
"""
shortcut_mapping = {
}

# load shortcut_mapping
f = open("rhythm.txt")
# read lines and split them
lines = f.readlines()
f.close()
for i in range(len(lines)):
    line = lines[i].split(')')[0] + ")"
    line = eval(line)
    command = lines[i].split(":")[1].strip()
    # add line contents as key-value pairs to shortcut_mapping
    shortcut_mapping[line] = command
print("init shortcut_mapping")
print(shortcut_mapping)

# initialize a list of functions called shortcuts
shortcuts = [shortcut_function_1, shortcut_function_2, shortcut_function_3]

# define class UserInterface
class UserInterface:
    # Initialize a constructor and the Tkinter window
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rhythmic Input Shortcuts System")
        self.root.geometry("400x200")

        # Initialize the dictionary to store rhythm shortcuts
        self.rhythm_shortcuts = {}

        # Add labels for each of the methods with separators
        self.record_label = tk.Label(self.root, text="Record Rhythm Shortcut")
        self.record_label.pack(fill=tk.X)
        self.record_separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.record_separator.pack(fill=tk.X, padx=5, pady=5)

        self.perform_label = tk.Label(self.root, text="Perform Rhythm Shortcut")
        self.perform_label.pack(fill=tk.X)
        self.perform_separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.perform_separator.pack(fill=tk.X, padx=5, pady=5)

        self.manage_label = tk.Label(self.root, text="Manage Rhythm Shortcuts")
        self.manage_label.pack(fill=tk.X)
        self.manage_separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.manage_separator.pack(fill=tk.X, padx=5, pady=5)

        self.feedback_label = tk.Label(self.root, text="Receive Feedback")
        self.feedback_label.pack(fill=tk.X)
        self.feedback_separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.feedback_separator.pack(fill=tk.X, padx=5, pady=5)

        # Add buttons for each of the methods
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.record_button = tk.Button(self.button_frame, text="Record", command=self.record_rhythm_shortcut)
        self.record_button.grid(row=0, column=0)

        self.perform_button = tk.Button(self.button_frame, text="Perform", command=self.perform_rhythm_shortcut)
        self.perform_button.grid(row=0, column=1)

        self.manage_button = tk.Button(self.button_frame, text="Manage", command=self.manage_rhythm_shortcut)
        self.manage_button.grid(row=0, column=2)

        self.feedback_button = tk.Button(self.button_frame, text="Feedback", command=self.receive_feedback)
        self.feedback_button.grid(row=0, column=3)

# define method record_rhythm_shortcut() within UserInterface class
    def record_rhythm_shortcut(self):
        # hide the main window
        self.root.withdraw()
        self.record_window = tk.Toplevel(self.root)
        # create a new window titled "Record Rhythm Shortcut" with specified dimensions
        self.record_window.title("Record Rhythm Shortcut")
        self.record_window.geometry("400x100")

        # Add labels and separators for "Enter Rhythm" and "Save Rhythm"
        self.enter_label = tk.Label(self.record_window, text="Enter rhythm")
        self.enter_label.pack(fill=tk.X)
        self.enter_separator = tk.Frame(self.record_window, height=2, bd=1, relief=tk.SUNKEN)
        self.enter_separator.pack(fill=tk.X, padx=5, pady=5)

        self.save_label = tk.Label(self.record_window, text="Save Rhythm")
        self.save_label.pack(fill=tk.X)
        self.save_separator = tk.Frame(self.record_window, height=2, bd=1, relief=tk.SUNKEN)
        self.save_separator.pack(fill=tk.X, padx=5, pady=5)
        self.button_frame = tk.Frame(self.record_window)
        self.button_frame.pack()
        # add buttons for "Enter" and "Save"
        self.confirm_button = tk.Button(self.button_frame, text="Enter", command=self.enter_rhythm, height=1)
        self.confirm_button.grid(row=0, column=0)
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_rhythm, height=1)
        self.save_button.grid(row=0, column=1)
        # add a "Back" button to go back to the main window
        self.back_button = tk.Button(self.button_frame, text="Back", command=lambda: self.back_to_main(self.record_window), height=1)
        self.back_button.grid(row=0, column=2)
# define method select_shortcut_mapping_window within UserInterface class
    def select_shortcut_mapping_window(self):
        # hide the main window
        self.root.withdraw()
        # initialize an empty list called available_function
        self.available_function = []
        print("shortcut_mapping values", shortcut_mapping.values())
        # iterate through each function in the shortcuts list
        for f in shortcuts:
            print("str(f).split()[1]", str(f).split()[1])
            # if the funtion name is not in the values of shortcut_mapping,
            # then append the function name to available_function
            if str(f).split()[1] not in shortcut_mapping.values():
                self.available_function.append(str(f).split()[1])
        # create a new window titled "Select Rhythm Shortcut Mapping"
        # with dynamic height based on the length of available_function
        self.record_window = tk.Toplevel(self.root)
        self.record_window.title("Select Rhythm Shortcut Mapping")
        height = str(len(self.available_function) * 100)
        self.record_window.geometry("400x" + height)
        # for each available_function, add labels and separators
        for i in range(len(self.available_function)):
            # add a text box for selecting mapping
            text = str(i+1) + " : " + str(self.available_function[i])
            self.enter_label = tk.Label(self.record_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.record_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)
        self.text_mapping_select = tk.Text(self.record_window, height=1, width=10)
        self.text_mapping_select.pack()
        self.button_frame = tk.Frame(self.record_window)
        self.button_frame.pack()
        self.button_frame = tk.Frame(self.record_window)
        self.button_frame.pack()
        # add a "Confirm" button
        self.confirm_button = tk.Button(self.button_frame, text="Confirm", command=self.confirm_mapping_select, height=1)
        self.confirm_button.grid(row=0, column=0)

# define method confirm_mapping_select() within UserInterface class
    def confirm_mapping_select(self):
        # retrieve the selected mapping from the text box
        # update the shortcut_mapping dictionary with the new mapping
        selection = self.text_mapping_select.get(1.0)
        selection = int(selection)
        # save mapping
        try:
            # add the new mapping to shortcut_mapping
            shortcut_mapping[tuple(self.input_timing)] = self.available_function[selection-1]
            f = open("rhythm.txt", "w")
            for k, v in shortcut_mapping.items():
                f.write(str(k) + " : " + str(v))
                f.write("\n")
            f.close()
            self.record_window.withdraw()
        # catch exceptions and print "Bad selection"
        except Exception:
            print("Bad selection")

# define method perform_rhythm_shortcut() within UserInterface class
    def perform_rhythm_shortcut(self):
        # create a new window for performing rhythm shortcuts
        self.perform_window = tk.Toplevel(self.root)
        self.perform_window.title("Perform Rhythm Shortcuts")
        self.perform_window.geometry("400x100")
        # hide the main window
        self.root.withdraw()
        # Add a label for entering rhythm
        self.enter_label = tk.Label(self.perform_window, text="Enter Rhythm")
        self.enter_label.pack()
        # Add buttons for entering rhythm and going back
        self.button_frame = tk.Frame(self.perform_window)
        self.button_frame.pack()
        self.confirm_button = tk.Button(self.button_frame, text="Enter", command=self.match_rhythm)
        self.confirm_button.grid(row=0, column=0)
        self.back_button = tk.Button(self.button_frame, text="Back", command=lambda: self.back_to_main(self.perform_window))
        self.back_button.grid(row=0, column=1)

# define method start_enter_rhythm_thread() within UserInterface class
    def start_enter_rhythm_thread(self):
        threading.Thread(target=self.enter_rhythm).start()

# define method enter_rhythm() within UserInterface class
    def enter_rhythm(self):
        print("Start recording rhythm shortcut...")
        # initialize empty lists rhythm_input and input_timing
        rhythm_input = []
        self.input_timing = []
        # loop indefinitely
        while True:
            # record each key event
            event = keyboard.read_event()
            # if the 'enter' key is pressed, break the loop
            if event.name == 'enter' and event.event_type == 'down':
                break
            # store the recorded rhythm and timing
            rhythm_input.append(event)
            self.input_timing.append(time.time())
        if rhythm_input:
            self.rhythm_input = rhythm_input
            # calculate the time differences between key presses and store them in input_timing
            if self.input_timing:
                for i in range(len(self.input_timing) - 1):
                    self.input_timing[i] = round(self.input_timing[i + 1] - self.input_timing[i], 3)
                self.input_timing = self.input_timing[:-1]
                self.input_timing = np.array(self.input_timing)
            print("You are recording a input_timing", self.input_timing)
            # call select_shortcut_mapping_window()
            self.select_shortcut_mapping_window()
# define method view_shortcut_mapping() within UserInterface class:
    def view_shortcut_mapping(self):
        print("Current shortcut_mapping is: ")
        # loop through each key-value pair in shortcut_mapping, and print the mapping
        for k, v in shortcut_mapping.items():
            print(str(k) + " ------ " + str(v).split()[1])
# define method select_mapping() within UserInterface class
    def select_mapping(self, timing):
        # call view_shortcut_mapping()
        self.view_shortcut_mapping()
        timing = tuple(timing)
        # Initialize an empty list called available_function
        available_function = []
        # loop through  each function in shortcuts
        for f in shortcuts:
            # if the function is not in shortcut_mapping values, append it to available_function
            if f not in shortcut_mapping.values():
                available_function.append(f)
        # if available_function is empty, print "Available Shortcut Functions" and return
        if len(available_function) == 0:
            print("Available Shortcut Functions")
            return
        # print the available functions
        print("Available Functions: ")
        for i in range(len(available_function)):
            print(i+1, str(available_function[i]).split()[1])
        # prompt user to select a shortcut function
        print("Select a shortcut function: ")
        # update shortcut_mapping with the new mapping
        selection = eval(input())
        shortcut_mapping[timing] = available_function[selection-1]
        print("Shortcut mapping updated")
        # call view_shortcut_mapping()
        self.view_shortcut_mapping()
# define method ask_save_rhythm() within UserInterface class
    def ask_save_rhythm(self):
        # show a dialog asking user if the user wants to save the rhythm
        save_rhythm = tk.messagebox.askyesno("Save Rhythm",
                                             "Rhythm input received. Do you want to save the rhythm?")
        # if yes, call save_rhythm(). Else, show an msg "Rhythm not saved"
        if save_rhythm:
            self.save_rhythm()
        else:
            tk.messagebox.showinfo("Info", "Rhythm not saved.")
# define method save_rhythm() within UserInterface class
    def save_rhythm(self):
        # Code to save the rhythm input
        if self.rhythm_input and self.input_timing:
            # Save the rhythm
            success = True  # Assume the operation was successful
            try:
                f = open("rhythm.txt", 'a')
                # write the updated shortcut_mapping to the file
                for k, v in shortcut_mapping.items():
                    f.write(str(k) + " " + str(v).split()[1])
                    f.write("\n")
                f.close()
                success = True
            except Exception:
                success = False
            if success:
                tk.messagebox.showinfo("Success", "Rhythm shortcut recorded successfully!")
            else:
                tk.messagebox.showerror("Error", "Failed to record rhythm shortcut.")
        else:
            tk.messagebox.showerror("Error", "No rhythm input detected. Please enter rhythm first.")
# define method back_to_main() within UserInterface class
    def back_to_main(self, current_window):
        # Close the current window and show the main window
        current_window.destroy()
        self.root.deiconify()

# define method execute_rhythm() within UserInterface class
    def execute_rhythm(self):
        # Code to execute the rhythm shortcut
        print("Executing rhythm shortcut...")
        threading.Thread(target=self.enter_rhythm_and_check).start()
# define method enter_rhythm_and_check() within UserInterface class
    def enter_rhythm_and_check(self):
        print("Start entering rhythm shortcut...")
        # initialize empty lists rhythm_input and input_timing
        rhythm_input = []
        self.input_timing = []
        # loop indefinitely
        while True:
            # Record each key event
            event = keyboard.read_event()
            # if the "enter" key is pressed, break the loop
            if event.name == 'enter' and event.event_type == 'down':
                break
            # store the rhythm and timing
            rhythm_input.append(event)
            self.input_timing.append(time.time())
        if rhythm_input:
            self.rhythm_input = rhythm_input
            # print recorded rhythm and timing
            print("rhythm_input", rhythm_input)
            print("input_timing", self.input_timing)
            # call match_rhythm() method in the main thread
            self.root.after(0, self.match_rhythm)
# define method match_rhythm() within UserInterface using Pearson Correlation Coefficient
    def match_rhythm(self):
        rhythm_input = []
        self.input_timing = []
        print("Enter a rhythm: ")
        while True:
            # Record each key event
            event = keyboard.read_event()
            if event.name == 'enter' and event.event_type == 'down':
                break
            rhythm_input.append(event)
            self.input_timing.append(time.time())
        if rhythm_input:
            self.rhythm_input = rhythm_input
            print("You are checking a input_timing:")
            print(self.input_timing)
        print("Matching rhythm shortcut")
        # calculate the time differences between key presses and store them in input_timing
        if self.input_timing:
            for i in range(len(self.input_timing)-1):
                self.input_timing[i] = round(self.input_timing[i+1] - self.input_timing[i], 3)
            self.input_timing = self.input_timing[:-1]
            self.input_timing = np.array(self.input_timing)
            record = []
            # open the "rhythm.txt" and read its lines
            f = open("rhythm.txt")
            lines = f.readlines()
            f.close()
            # initialize variables max_match_line and max_pearson
            max_match_line = -1
            max_pearson = -2
            command = None
            # loop through each line in the file
            for i in range(len(lines)):
                line = lines[i].split(')')[0] + ")"
                line = eval(line)
                # convert line timing to a numpy array
                line = np.array(line)
                # if the length of the line timing equals the length of input_timing,
                # calculate Pearson Correlation Coefficient
                if len(line) == len(self.input_timing):
                    corrcoef = np.corrcoef(self.input_timing, line)
                    # Update max_match_line, max_pearson, and command if the new Pearson Correlation is greater
                    if corrcoef[0][1] > max_pearson:
                        max_match_line = i
                        max_pearson = corrcoef[0][1]
                        command = lines[i].split(')')[1].split(":")[1].strip()
            # if max_pearson is greater than 0.8, print success msg and execute the matched shortcut
            if max_pearson > 0.8:
                print("Matched in line ", max_match_line)
                print("Matched command is", command)
                print("Executing matched shortcut")
                try:
                    for c in shortcuts:
                        if command in str(c):
                            threading.Thread(target=c).start()
                except Exception:
                    print("Failed to execute the matched shortcut")
            else:
                print("Max match at line but not matched", max_match_line)
# define method match_rhythm() within UserInterface class using Dynamic Time Warping (DTW)
#     def match_rhythm(self):
#         from fastdtw import fastdtw
#         # capture rhythm and timing, store them in rhythm_input and input_timing
#         rhythm_input, input_timing = self.capture_rhythm()
#         # initialize min_distance to infinity and command to None
#         min_distance = float('inf')
#         command = None
#         # open "rhythm.txt" file and read its lines
#         with open("rhythm.txt") as f:
#             lines = f.readlines()
#             # loop through each line, extract recorded_rhythm using eval()
#             for i, line in enumerate(lines):
#                 recorded_rhythm = eval(line.split(')')[0] + ")")
#                 # calculate DTW distance between input_timing and recorded_rhythm
#                 distance, _ = fastdtw(input_timing, recorded_rhythm)
#                 # if distance is less than min_distance, update min_distance and command
#                 if distance < min_distance:
#                     min_distance = distance
#                     command = line.split(')')[1].split(":")[1].strip()
#         # if min_distance is less than a pre-defined threshold, call execute_command()
#         if min_distance < threshold:
#             self.execute_command(command)
#         else:
#             print("Rhythm not matched")

# define method match_rhythm() within UserInterface class using Cross-Correlation
#     def match_rhythm(self):
#         import numpy as np
#         # capture rhythm and timing, store them in rhythm_input and input_timing
#         rhythm_input, input_timing = self.capture_rhythm()
#         max_correlation = -float('inf')
#         command = None
#         with open("rhythm.txt") as f:
#             lines = f.readlines()
#             # loop through each line
#             for i, line in enumerate(lines):
#                 # convert the recorded rhythm to a numpy array
#                 recorded_rhythm = np.array(eval(line.split(')')[0] + ")"))
#                 # calculate the cross_correlation between input_timing and recorded_rhythm
#                 cross_corr = np.correlate(input_timing, recorded_rhythm, mode='full')
#                 # if the maximum value of the max_correlation is greater than max_correlation,
#                 # update max_correlation and command
#                 if max(cross_corr) > max_correlation:
#                     max_correlation = max(cross_corr)
#                     command = line.split(')')[1].split(":")[1].strip()
#         # if max_correlation is greater than a pre-defined threshold, call execute_command()
#         if max_correlation > threshold:
#             self.execute_command(command)
#         else:
#             print("Rhythm not matched")

# define method match_rhythm() within UserInterface class using Euclidean Distance
#     def match_rhythm(self):
#         from scipy.spatial.distance import euclidean
#         rhythm_input, input_timing = self.capture_rhythm()
#         min_distance = float('inf')
#         command = None
#         with open("rhythm.txt") as f:
#             lines = f.readlines()
#             # loop through each line, and extract recorded_rhythm
#             for i, line in enumerate(lines):
#                 recorded_rhythm = eval(line.split(')')[0] + ")")
#                 # calculate the euclidean distance between input_timing and recorded_rhythm
#                 distance = euclidean(input_timing, recorded_rhythm)
#                 # if distance is less than min_distance, update min_distance and command
#                 if distance < min_distance:
#                     min_distance = distance
#                     command = line.split(')')[1].split(":")[1].strip()
#             # if min_distance id less than a pre_defined threshold, call execute_command()
#             if min_distance < threshold:
#             self.execute_command(command)
#         else:
#             print("Rhythm not matched")

# define method manage_rhythm_shortcut() within UserInterface class
    def manage_rhythm_shortcut(self):
        # Hide the main window
        self.root.withdraw()
        # Create a new window for managing rhythm shortcuts
        self.manage_window = tk.Toplevel(self.root)
        self.manage_window.title("Manage Rhythm Shortcuts")
        self.manage_window.geometry("400x150")
        # Add labels and separators for each of the actions
        self.view_label = tk.Label(self.manage_window, text="View Shortcuts")
        self.view_label.pack()
        self.view_separator = tk.Frame(self.manage_window, height=2, bd=1, relief=tk.SUNKEN, bg="black")
        self.view_separator.pack(fill=tk.X, padx=5, pady=5)
        self.edit_label = tk.Label(self.manage_window, text="Edit Shortcuts")
        self.edit_label.pack()
        self.edit_separator = tk.Frame(self.manage_window, height=2, bd=1, relief=tk.SUNKEN, bg="black")
        self.edit_separator.pack(fill=tk.X, padx=5, pady=5)
        self.delete_label = tk.Label(self.manage_window, text="Delete Shortcuts")
        self.delete_label.pack()
        self.delete_separator = tk.Frame(self.manage_window, height=2, bd=1, relief=tk.SUNKEN, bg="black")
        self.delete_separator.pack(fill=tk.X, padx=5, pady=5)
        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.manage_window)
        self.button_frame.pack()
        # Add buttons for each of the actions
        self.view_button = tk.Button(self.button_frame, text="View", command=self.view_shortcuts)
        self.view_button.grid(row=0, column=0)
        self.edit_button = tk.Button(self.button_frame, text="Edit", command=self.edit_shortcuts)
        self.edit_button.grid(row=0, column=1)
        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_shortcuts)
        self.delete_button.grid(row=0, column=2)
        # Add Back button to return to the main window
        self.back_button = tk.Button(self.button_frame, text="Back",
                                     command=lambda: self.back_to_main(self.manage_window))
        self.back_button.grid(row=0, column=3)

# define method view_shortcuts() within UserInterface class
    def view_shortcuts(self):
        # create a new window
        self.view_shortcuts_window = tk.Toplevel(self.root)
        self.view_shortcuts_window.title("Select Rhythm Shortcut Mapping")
        height = str(len(shortcut_mapping) * 100)
        self.view_shortcuts_window.geometry("400x" + height)
        # loop through each item in shortcut_mapping
        for k, v in shortcut_mapping.items():
            text = str(k) + " : " + str(v)
            # create label and separator to display shortcut and corresponding function
            self.enter_label = tk.Label(self.view_shortcuts_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.view_shortcuts_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)
# define method edit_shortcuts() within UserInterface class
    def edit_shortcuts(self):
        # Code to edit the recorded rhythm shortcuts
        print("Editing rhythm shortcuts...")
        # create a new window
        self.edit_shortcuts_window = tk.Toplevel(self.root)
        self.edit_shortcuts_window.title("Select Rhythm Shortcut Mapping")
        height = str(len(shortcut_mapping) * 100 * 2)
        self.edit_shortcuts_window.geometry("400x" + height)  # 设置窗口大小
        # loop through each key in shortcut_mapping
        for i in range(len(shortcut_mapping.keys())):
            text = str(i) + " : " + str(list(shortcut_mapping.keys())[i])
            # create label and separator to display the key
            self.enter_label = tk.Label(self.edit_shortcuts_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.edit_shortcuts_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)
        self.enter_label = tk.Label(self.edit_shortcuts_window, text="select a rhythm")
        self.enter_label.pack(fill=tk.X)
        self.text_shortcut_select = tk.Text(self.edit_shortcuts_window, height=1, width=10)
        self.text_shortcut_select.pack()
        # loop through each value in shortcut_mapping
        for i in range(len(shortcut_mapping.values())):
            text = str(i) + " : " + str(list(shortcut_mapping.values())[i])
            # create label and separator to display the value
            self.enter_label = tk.Label(self.edit_shortcuts_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.edit_shortcuts_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)
        self.enter_label = tk.Label(self.edit_shortcuts_window, text="select a shortcut")
        self.enter_label.pack(fill=tk.X)
        # create a Text widget for selecting a function
        self.text_timing_select = tk.Text(self.edit_shortcuts_window, height=1, width=10)
        self.text_timing_select.pack()
        # create a " Confirm button"
        self.button_frame2 = tk.Frame(self.edit_shortcuts_window)
        self.button_frame2.pack()
        self.confirm_button2 = tk.Button(self.button_frame2, text="Confirm", command=self.confirm_shortcut_edit, height=1)
        self.confirm_button2.grid(row=0, column=0)
# define method confirm_shortcut_edit() within UserInterface class
    def confirm_shortcut_edit(self):
        # read the selected shortcut and timing from Text widgets
        shortcut_selection = self.text_shortcut_select.get(1.0)
        shortcut_selection = int(shortcut_selection)
        shortcut_selection = list(shortcut_mapping.values())[shortcut_selection]
        # update mapping
        timing_selection = self.text_timing_select.get(1.0)
        timing_selection = int(timing_selection)
        timing_selection = list(shortcut_mapping.keys())[timing_selection]
        shortcut_mapping.pop(timing_selection)
        for k in shortcut_mapping:
            if shortcut_mapping[k] == shortcut_selection:
                shortcut_mapping.pop(k)
                break
        shortcut_mapping[timing_selection] = shortcut_selection
        # save the updated mapping to "rhythm.txt"
        f = open("rhythm.txt", "w")
        for k, v in shortcut_mapping.items():
            f.write(str(k) + " : " + str(v))
            f.write("\n")
        f.close()
        self.edit_shortcuts_window.withdraw()
# define method delete_shortcuts() within UserInterface class
    def delete_shortcuts(self):
        # create a new window
        self.delete_shortcuts_window = tk.Toplevel(self.root)
        self.delete_shortcuts_window.title("Delete Rhythm Shortcut Mapping")
        height = str(len(shortcut_mapping) * 100)
        self.delete_shortcuts_window.geometry("400x" + height)
        # loop through each value in shortcut_mapping
        for i in range(len(shortcut_mapping.values())):
            text = str(i) + " : " + str(list(shortcut_mapping.values())[i])
            # create a label and separator
            self.enter_label = tk.Label(self.delete_shortcuts_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.delete_shortcuts_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)
        self.enter_label = tk.Label(self.delete_shortcuts_window, text="select a shortcut")
        self.enter_label.pack(fill=tk.X)
        # create a Text widget for selecting a function to delete
        self.delete_timing_select = tk.Text(self.delete_shortcuts_window, height=1, width=10)
        self.delete_timing_select.pack()
        # create a "Confirm" button
        self.button_frame3 = tk.Frame(self.delete_shortcuts_window)
        self.button_frame3.pack()
        self.confirm_button2 = tk.Button(self.button_frame3, text="Confirm", command=self.confirm_shortcut_delete, height=1)
        self.confirm_button2.grid(row=0, column=0)
# define method confirm_shortcut_delete() within UserInterface class
    def confirm_shortcut_delete(self):
        # read the selected shortcut from Text widget
        shortcut_selection = self.delete_timing_select.get(1.0)
        shortcut_selection = int(shortcut_selection)
        shortcut_selection = list(shortcut_mapping.values())[shortcut_selection]
        # loop through each key-value pair in shortcut_mapping
        for k in shortcut_mapping:
            # if the value matches the selected shortcut, remove the kay_value pair
            if shortcut_mapping[k] == shortcut_selection:
                shortcut_mapping.pop(k)
                break
        # open "rhythm.txt" and update the file with the new mapping
        f = open("rhythm.txt", "w")
        for k, v in shortcut_mapping.items():
            f.write(str(k) + " : " + str(v))
            f.write("\n")
        f.close()
        self.delete_shortcuts_window.withdraw()
# define method receive_feedback() within UserInterface class
    def receive_feedback(self):
        # Create a new window for receiving feedback
        self.feedback_window = tk.Toplevel(self.root)
        self.feedback_window.title("Receive Feedback")
        self.feedback_window.geometry("400x150")
        # Add a label and a button to the new window
        self.view_label = tk.Label(self.feedback_window, text="View Feedback")
        self.view_label.pack()
        self.view_button = tk.Button(self.feedback_window, text="View", command=self.view_feedback)
        self.view_button.pack()
# define method view_feedback() within UserInterface class
    def view_feedback(self):
        # Code to display feedback to the user
        print("Viewing feedback...")
        # create a new window
        self.feedback_window = tk.Toplevel(self.root)
        self.feedback_window.title("Delete Rhythm Shortcut Mapping")
        height = str(len(shortcut_mapping) * 100)
        self.feedback_window.geometry("400x" + height)  # 设置窗口大小
        # loop through each item in feedback_list
        for i in feedback_list:
            text = i
            # create label and separator to display the feedback
            self.enter_label = tk.Label(self.feedback_window, text=text)
            self.enter_label.pack(fill=tk.X)
            self.enter_separator = tk.Frame(self.feedback_window, height=2, bd=1, relief=tk.SUNKEN)
            self.enter_separator.pack(fill=tk.X, padx=5, pady=5)

    def run(self):
        self.root.mainloop()
    # Create an instance of the UserInterface and run it
ui = UserInterface()
ui.run()
