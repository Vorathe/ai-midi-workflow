from mido import Message, MidiFile, MidiTrack

impending_doom_arp_synth_pitch_duration_data = [
  # Bar 1 - 4
  (60, 0.5), (62, 0.5), (58, 1), (65, 1),  # C4, D4, A#3, F4 - different note durations for variety
  (64, 1), (0, 0.5), (58, 0.5), (67, 2),  # E4, Rest, A#3, G4 - note durations vary to add complexity
  (62, 0.5), (60, 1.5), (58, 0.5), (65, 1),  # D4, C4, A#3, F4 - mirroring the first bar with small changes
  (64, 0.5), (0, 1.5), (67, 0.5), (58, 1)  # E4, Rest, G4, A#3 - keeping the silence for "doom" feel
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
add_notes_to_track(synth, impending_doom_arp_synth_pitch_duration_data)


# Save the MIDI file
mid.save('arp-intro.mid')
