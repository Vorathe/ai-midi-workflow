from mido import Message, MidiFile, MidiTrack

intro_high_hat_pitch_duration_data = [
  # Bar 13 - 16 (fills in the gap before the burst at bar 17)
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),  # F#2, all half notes - Bar 13
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),  # F#2, all half notes - Bar 14
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),  # F#2, all half notes - Bar 15
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),  # F#2, all half notes - Bar 16
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
add_notes_to_track(synth, intro_high_hat_pitch_duration_data)


# Save the MIDI file
mid.save('arp-intro.mid')
