import pandas as pd
import argparse
import sys

class Song:

    def __init__(self, name, artist, genre, sub_genre, energy):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.sub_genre = sub_genre
        self.energy = energy

    def __str__(self):
        return f"{self.name} by {self.artist}"
    
def is_song_in_list(name, artist, file_path):
    
    song_csv_to = pd.read_csv(file_path)
    song_csv = pd.DataFrame(song_csv_to)
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

            name_val = song_artist.iat[index_num, 0]
            artist_val = song_artist.iat[index_num, 1]
            genre_val = song_artist.iat[index_num, 2]
            sub_genre_val = song_artist.iat[index_num, 3]
            energy_val = song_artist.iat[index_num, 4]

            song_in_list = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
            

    return song_in_list

                


def recommend_song(name, artist, filepath):

    if is_song_in_list(name, artist, filepath) is None:
        return "Song not found. Try another one!"
    else: 
        base_song = is_song_in_list(name, artist, filepath)

        
        base_subgenre = base_song.sub_genre
        base_energy = base_song.energy

        song_csv = pd.read_csv(filepath)
        
        song_finder = song_csv[song_csv['Subgenre'] == base_subgenre]

        song_list = []

        for ind in range(len(song_finder)):

            name_val = song_finder.iat[ind, 0]
            artist_val = song_finder.iat[ind, 1]
            genre_val = song_finder.iat[ind, 2]
            sub_genre_val = song_finder.iat[ind, 3]
            energy_val = song_finder.iat[ind, 4]

            to_be_added = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
            song_list.append(to_be_added)

    
        song_to_return = None

        for new_songs in song_list:
            song_to_return = song_list[0]
            numb_to_calc = abs(base_energy - song_to_return.energy)
            if abs(base_energy - new_songs.energy) < numb_to_calc:
                song_to_return = new_songs

        return song_to_return
    
    
def main(name, artist, filepath):
    return recommend_song(name, artist, filepath)

def parse_args(args_list):
    parser = argparse.ArgumentParser()

    parser.add_argument('song_name', type=str, help='Song name')
    parser.add_argument('artist_name', type=str, help='Artist name')  
    parser.add_argument('spotify_csv', type=str, help='CSV of songs')

    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":
    parsed_args = parse_args(sys.argv[1:])

    print(main(parsed_args.song_name, parsed_args.artist_name, parsed_args.spotify_csv))