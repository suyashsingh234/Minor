#for testing

from mido import MidiFile

mid=MidiFile('new_song.mid')

for msg in mid.tracks[0]:
    print(msg)