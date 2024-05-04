# Music Recommendation Project

![Logo](Music_Recomandation_ٍSystem.png)

This Python project utilizes a dataset (tcc_ceds_music.csv) containing information about various music tracks, including artist name, track name, release date, genre, lyrics, and more. The project aims to provide music recommendations based on user preferences such as genre, topic, and release date range.

## Dataset Overview
The dataset contains 28,372 records with columns including:

#### artist_name: The name of the artist.
#### track_name: The name of the track.
#### release_date: The release date of the track.
#### genre: The genre of the track.
#### lyrics: The lyrics of the track.
#### len: The length of the lyrics.
#### topic: The topic of the track.

## Project Functions
### 1. filter_records(df)
This function allows users to filter records based on genre, topic, and release date range. It returns a DataFrame containing the filtered records.

### 2. show(musicList)
This function displays the details of each track in a given list, including the track name, artist name, genre, and release year.

### 3. addSong()
This function filters the DataFrame based on user preferences and allows the user to add a selected song to their playlist.

### 4. printLyrics(lyrics)
This function prints the lyrics of a song, splitting them into lines containing only eight words each.

### 5. randomPlayList()
This function creates a random playlist based on user preferences, adding songs that match the criteria to the playlist.

### 6. delet(myPlayList)
This function allows the user to delete a song from their playlist.

### 7. add_random_music(playList)
Adds random music to the playlist based on the user's existing playlist.

## Usage
To use the project, simply run the provided functions with your desired inputs. For example, you can filter records, add songs to your playlist, and manage your playlist easily.

