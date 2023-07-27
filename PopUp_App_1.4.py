# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:35:38 2023

@author: ASUS
"""
import tkinter as tk
import random
import time
import pandas as pd
import sys
import os


class Stroop:
    
    def __init__(self, master):
        # Set up the root window
        self.master = master
        self.master.title('Pop-Up settings')

        # get the path to the directory containing this script
        script_dir = os.path.dirname(sys.argv[0])
        root.iconbitmap(f'{script_dir}\logo.ico')

        # Define the colors and words for the experiment
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.words = ['قرمز', 'سبز', 'آبی', 'زرد']
        # Create the label and entry fields for the delay time range and number of trials
        self.label_min = tk.Label(root, text='Minimum delay time (in seconds):')
        self.label_min.pack(pady=5)
        self.entry_min = tk.Entry(root)
        self.entry_min.pack()
        self.label_max = tk.Label(root, text='Maximum delay time (in seconds):')
        self.label_max.pack(pady=5)
        self.entry_max = tk.Entry(root)
        self.entry_max.pack()
        self.label_trials = tk.Label(root, text='Number of trials:')
        self.label_trials.pack(pady=5)
        self.entry_trials = tk.Entry(root)
        self.entry_trials.pack()
        self.label_key = tk.Label(root, text='Key to press for non-congruent trials (L/R):')
        self.label_key.pack(pady=5)
        self.entry_key = tk.Entry(root)
        self.entry_key.insert(0, 'R') # set default value to right mouse button
        self.entry_key.pack()
        self.label_user = tk.Label(root, text='User ID:')
        self.label_user.pack(pady=5)
        self.entry_user = tk.Entry(root)
        self.entry_user.pack()
        self.label_duration = tk.Label(root, text='Duration of popup window (in seconds):')
        self.label_duration.pack(pady=5)
        self.entry_duration = tk.Entry(root)
        self.entry_duration.pack()
        self.button = tk.Button(root, text='Start Experiment', command=self.create_random_popup)
        self.button.pack(pady=10)
        # create a font object
        self.my_font = ('Lucida Calligraphy', 12, 'bold')
        
        # create a frame with a pink background and a border
        self.frame = tk.Frame(root, bg='pink',highlightbackground='pink' , relief='solid', borderwidth=1, width=200, height=50)
        self.frame.pack(pady=5)
        
        # create a label with the font and add it to the frame
        self.label = tk.Label(self.frame, text='mahsatorabi515@gmail.com', font=self.my_font, bg='pink')
        self.label.pack()
        root.mainloop()
        
    # Define a function to create a random popup
    def create_random_popup(self):
        # Get the delay time range and number of trials from the user
        self.delay_min = int(self.entry_min.get())
        self.delay_max = int(self.entry_max.get())
        self.num_trials = int(self.entry_trials.get())
        self.user_ID = self.entry_user.get()
        self.duration = int(self.entry_duration.get())
    
        # Set up the output file
        self.output = pd.DataFrame(columns=['Trial', 'Color', 'Word', 'Congruent',
                                            'Correct', 'ReactionTime', 'DelayTime', 'Duration'])
        self.output_filename = f'{self.user_ID}.csv'
    
        # Define a function to handle each trial
        def handle_trial(self, trial_num):
            self.trial_num = trial_num
            # Choose a random delay time within the specified range
            self.delay_time = random.randint(self.delay_min, self.delay_max)
    
            # Wait for the delay time
            time.sleep(self.delay_time)
    
            # Choose a random congruent word-color combination
            self.congruent_index = random.randint(0, len(self.colors)-1)
            self.congruent_color = self.colors[self.congruent_index]
            self.congruent_word = self.words[self.congruent_index]
    
            # Choose a random word and color
            self.color_index = random.randint(0, len(self.colors)-1)
            self.word_index = random.randint(0, len(self.words)-1)
            self.chosen_color = self.colors[self.color_index]
            self.chosen_word = self.words[self.word_index]
    
            # Check if the chosen word and color are congruent
            self.is_congruent = self.words.index(self.chosen_word) == self.colors.index(self.chosen_color)
    
            # Create the popup window
            self.popup = tk.Toplevel()
            self.popup.title('Pop-Up')
            self.popup.geometry('300x200+{}+{}'.format(root.winfo_screenwidth()-300, 0))
            self.popup.attributes('-topmost', True)  # Set always on top
            self.label = tk.Label(self.popup, text=self.chosen_word,
                                  font=('B Nazanin', 70, 'bold'), fg=self.chosen_color)
            self.label.pack(pady=10)

            # get the path to the directory containing this script
            script_dir = os.path.dirname(sys.argv[0])
            self.popup.iconbitmap(f'{script_dir}\logo.ico')
    
            # Define a function to handle the user's response
            def handle_response(event):
                # Calculate the reaction time
                self.reaction_time = time.time() - self.start_time
            
                # Record the trial details to the output file
                if event:
                    self.output.loc[self.trial_num] = [self.trial_num, self.chosen_color, self.chosen_word, self.is_congruent,
                                                        event.num == 1 and self.is_congruent or event.num == 3 and not self.is_congruent,
                                                        self.reaction_time, self.delay_time, self.duration]
                else:
                    self.output.loc[self.trial_num] = [self.trial_num, self.chosen_color, self.chosen_word, self.is_congruent,
                                                        '', '', self.delay_time, self.duration]
                self.output.to_csv(self.output_filename, index=False)
            
                # Destroy the popup window
                self.popup.destroy()
            
                # If this wasn't the last trial, start the next one
                if self.trial_num < self.num_trials:
                    handle_trial(self, self.trial_num + 1)

            self.popup.after(self.duration * 1000, lambda: handle_response(None))

            # Bind the response function to the label click event
            self.start_time = time.time()
            self.label.bind('<Button-1>', handle_response)
            self.label.bind('<Button-3>', handle_response)
    
        # Start the first trial
        handle_trial(self, 1)
        
root = tk.Tk()
application = Stroop(root)
root.mainloop()

    