# -*- coding: utf-8 -*-
"""
Created on Thu May 11 00:57:32 2023

@author: ASUS
"""

import tkinter as tk
import random
import time
import pandas as pd

class Stroop:
    
    def __init__(self, master):
        # Set up the root window
        self.master = master
        self.master.title('Pop-Up')
        
        # Define the colors and words for the experiment
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.words = ['red', 'green', 'blue', 'yellow']
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
        self.button = tk.Button(root, text='Start Experiment', command=self.create_random_popup)
        self.button.pack(pady=10)
        root.mainloop()
    
    # Define a function to create a random popup
    def create_random_popup(self):
        # Get the delay time range and number of trials from the user
        self.delay_min = int(self.entry_min.get())
        self.delay_max = int(self.entry_max.get())
        self.num_trials = int(self.entry_trials.get())
        self.user_ID = self.entry_user.get()
    
        # Set up the output file
        self.output = pd.DataFrame(columns=['Trial', 'Color', 'Word', 'Congruent', 'Correct', 'ReactionTime', 'DelayTime'])
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
            self.is_congruent = (self.chosen_word == self.chosen_color)
    
            # Create the popup window
            self.popup = tk.Toplevel()
            self.popup.geometry('300x200+{}+{}'.format(root.winfo_screenwidth()-300, 0))
            self.popup.attributes('-topmost', True)  # Set always on top
            self.label = tk.Label(self.popup, text=self.chosen_word, font=('Arial', 36), fg=self.chosen_color)
            self.label.pack(pady=10)
    
            # Define a function to handle the user's response
            def handle_response(event):
                
                # Calculate the reaction time
                self.reaction_time = time.time() - self.start_time
    
                # Record the trial details to the output file
                self.output.loc[self.trial_num] = [self.trial_num, self.chosen_color, self.chosen_word, self.is_congruent, event.num == 1 and self.is_congruent or event.
    num == 3 and not self.is_congruent, self.reaction_time, self.delay_time]
                self.output.to_csv(self.output_filename, index=False)
                # Destroy the popup window
                self.popup.destroy()
    
                # If this wasn't the last trial, start the next one
                if self.trial_num < self.num_trials:
                    handle_trial(self, self.trial_num+1)
    
            # Bind the response function to the label click event
            self.start_time = time.time()
            self.label.bind('<Button-1>', handle_response)
            self.label.bind('<Button-3>', handle_response)
    
        # Start the first trial
        handle_trial(self, 1)
        
root = tk.Tk()
application = Stroop(root)
root.mainloop()

    
