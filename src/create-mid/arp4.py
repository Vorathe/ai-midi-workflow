from mido import Message, MidiFile, MidiTrack

seductive_arp_synth_pitch_duration_data = [
  # Bar 1 - 4
  (60, 1.5), (58, 0.5), (60, 2), # C4, A#3, C4 - sync with C2 of the bass
  (63, 1.5), (58, 0.5), (63, 2), # D#4, A#3, D#4 - sync with D#2 of the bass
  (60, 1.5), (58, 0.5), (60, 2), # C4, A#3, C4 - again, sync with C2 of the bass
  (63, 1.5), (58, 0.5), (63, 2), # D#4, A#3, D#4 - again, sync with D#2 of the bass

  # Bar 5 - 8
  (62, 1.5), (60, 0.5), (62, 1), (67, 1), # D4, C4, D4, G4 - introducing new notes to create more interest
  (65, 1.5), (62, 0.5), (65, 1), (68, 1), # F4, D4, F4, G#4 - complementing the first part of this sequence
  (67, 1.5), (62, 0.5), (67, 2), # G4, D4, G4 - sync with bass but keeping the complexity
  (65, 1.5), (60, 0.5), (65, 2)  # F4, C4, F4 - ends on F4 to create tension for the next part
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
add_notes_to_track(synth, seductive_arp_synth_pitch_duration_data)


# Save the MIDI file
mid.save('arp-intro.mid')
