from mido import Message, MidiFile, MidiTrack

dark_synthwave_arp_synth_pitch_duration_data = [
  # Bar 1 - 4
  (60, 0.5), (62, 0.5), (65, 0.5), (62, 0.5), (58, 0.5), (62, 0.5), (55, 0.5), (58, 0.5),  # C4, D4, F4, D4, A#3, D4, G3, A#3 - Bar 1
  (62, 0.5), (65, 0.5), (68, 0.5), (65, 0.5), (62, 0.5), (58, 0.5), (60, 0.5), (58, 0.5),  # D4, F4, A#4, F4, D4, A#3, C4, A#3 - Bar 2
  (60, 0.5), (62, 0.5), (65, 0.5), (62, 0.5), (58, 0.5), (62, 0.5), (55, 0.5), (58, 0.5),  # C4, D4, F4, D4, A#3, D4, G3, A#3 - Bar 3
  (62, 0.5), (65, 0.5), (68, 0.5), (65, 0.5), (62, 0.5), (58, 0.5), (60, 0.5), (58, 0.5),  # D4, F4, A#4, F4, D4, A#3, C4, A#3 - Bar 4

  # Bar 5 - 8
  (55, 1), (58, 0.5), (62, 0.5), (65, 0.5), (62, 0.5), (58, 1), # G3, A#3, D4, F4, D4, A#3 - Bar 5
  (60, 1), (62, 0.5), (65, 0.5), (68, 0.5), (65, 0.5), (62, 1), # C4, D4, F4, A#4, F4, D4 - Bar 6
  (55, 1), (58, 0.5), (62, 0.5), (65, 0.5), (62, 0.5), (58, 1), # G3, A#3, D4, F4, D4, A#3 - Bar 7
  (60, 1), (62, 0.5), (65, 0.5), (68, 0.5), (65, 0.5), (62, 1)  # C4, D4, F4, A#4, F4, D4 - Bar 8
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
add_notes_to_track(synth, dark_synthwave_arp_synth_pitch_duration_data)


# Save the MIDI file
mid.save('arp-intro.mid')
