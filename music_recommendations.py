"""
Ryan Boubsil, Eyosiyas Girma, Claire Jacobs
Music Recommendation Program
Professor Cruz
INST 326 Final Project
"""
# pandas will be used for data analysis to find the best songs for the user
import pandas as pd
import sys
import argparse
# tkinter will be used to make a simple interface for users
import tkinter as tk

"""Since we're going to be working out of one csv, we'll import it outside of a function"""
csv = pd.read_csv("spotify_songs")

"""user interface using tkinter, in its own file within the repository (interface.py)"""

"""Function which returns 5 songs similar to the liked song entered by the user"""
def song_recommendations():
    pass

