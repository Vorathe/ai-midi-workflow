from mido import Message, MidiFile, MidiTrack

chorus_ride_cymbal_pattern_data = [
  (0, 2), (56, 2),  # Rest, half note; F#4, half note - Bar 1
  (56, 1), (0, 1), (56, 2),  # F#4, quarter note; rest, quarter note; F#4, half note - Bar 2
  (56, 1), (0, 1), (56, 1), (0, 1), (56, 1), (0, 1),  # F#4, quarter note; rest, quarter note; F#4, quarter note; rest, quarter note; F#4, quarter note; rest, quarter note - Bar 3
  (56, 1), (0, 1), (56, 1), (0, 1), (56, 1), (0, 1), (56, 1), (0, 1),  # F#4, quarter note; rest, quarter note; F#4, quarter note; rest, quarter note; F#4, quarter note; rest, quarter note; F#4, quarter note; rest, quarter note - Bar 4
]

# Create a new MIDI file and add tracks for synth and bass
mid = MidiFile(ticks_per_beat=480)  # Set ticks per beat for the MIDI file
synth = MidiTrack()
mid.tracks.append(synth)

# Function to add notes to the track
def add_notes_to_track(track, notes):
    for note, duration in notes:
        if note > 0:  # If the note value is not 0 (rest), add a note on and note off event
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=int(duration*mid.ticks_per_beat)))
        else:  # If the note value is 0 (rest), add a rest
            track.append(Message('note_off', note=note, velocity=64, time=int(duration*mid.ticks_per_beat)))

# Add notes to the synth and bass tracks
add_notes_to_track(synth, chorus_ride_cymbal_pattern_data)


# Save the MIDI file
mid.save('ride_seq.mid')
