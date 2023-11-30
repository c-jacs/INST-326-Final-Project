import pandas as pd
import argparse
import requests
import sys

class Song:

    def __init__(self, name, artist, genre, sub_genre, energy):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.sub_genre = sub_genre
        self.energy = energy

    def __str__(self):
        return f"The name of the Song '{self.name}', the artist who made the song '{self.artist}' the genre and the sub genre of the song is '{self.genre}' and '{self.sub_genre}'"
    
def is_song_in_list(name, artist, file_path):
    
    song_csv = pd.read_csv(file_path)

    song_finder = song_csv[song_csv['Name'] == name]

    num_songs = len(song_finder)

    if num_songs < 1: 
        return None
    else:
        song_artist = song_finder[song_finder['Artist'] == artist] 

        new_num_songs = len(song_artist)
        if new_num_songs < 1:
            return None
        else:
            index_num = 0

            name_val = song_artist.at[index_num, 'Name']
            artist_val = song_artist.at[index_num, 'Artist']
            genre_val = song_artist.at[index_num, 'Genre']
            sub_genre_val = song_artist.at[index_num, 'Subgenre']
            energy_val = song_artist.at[index_num, 'Energy']

            song_in_list = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
            

    return song_in_list

                


def recommend_song(name, artist, filepath):

    if is_song_in_list(name, artist, filepath) is None:
        return "Song not found. Try another one!"
    else: 
        base_song = is_song_in_list(name, artist, filepath)

        base_artist = base_song.artist
        base_subgenre = base_song.sub_genre
        base_energy = base_song.energy

        song_csv = pd.read_csv(filepath)
        
        song_finder = song_csv[song_csv['Subgenre'] == base_subgenre]

        song_list = []

        for ind in range(len(song_finder)):
            name_val = song_finder.at[ind, 'Name']
            artist_val = song_finder.at[ind, 'Artist']
            genre_val = song_finder.at[ind, 'Genre']
            sub_genre_val = song_finder.at[ind, 'Subgenre']
            energy_val = song_finder.at[ind, 'Energy']

            to_be_added = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
            song_list.append(to_be_added)

        song_to_return = song_list[0]

        for new_songs in song_list:
            numb_to_calc = abs(base_energy - song_to_return.energy)
            if abs(base_energy - new_songs.energy) < numb_to_calc:
                song_to_return = new_songs

        return song_to_return
    
    
def main():
    return recommend_song()

def parse_args(args_list):
    parser = argparse.ArgumentParser()

    parser.add_argument('song_name', type=str, help='Song name')
    parser.add_argument('artist_name', type=int, help='Artist name')  
    
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":
    parsed_args = parse_args(sys.argv[1:])

    recommend_song(parsed_args.song_name, parsed_args.artist_name)
        