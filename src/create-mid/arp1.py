from mido import Message, MidiFile, MidiTrack

arp_synth2_pitch_duration_data = [
  # Bar 1-2
  (48, 1.5),  # C3
  (51, 0.5),  # D#3
  (48, 0.5),  # C3
  (51, 0.5),  # D#3
  (48, 1.0),  # C3

  # Bar 3-4
  (51, 1.5),  # D#3
  (55, 0.5),  # G3
  (51, 0.5),  # D#3
  (55, 0.5),  # G3
  (51, 1.0),  # D#3
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
add_notes_to_track(synth, arp_synth2_pitch_duration_data)


# Save the MIDI file
mid.save('arp_sequence-4-4.mid')
