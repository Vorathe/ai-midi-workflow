from mido import Message, MidiFile, MidiTrack

adjusted_arp_synth_pitch_duration_data = [
  # Bar 1 - 4
  (60, 1.5), (58, 0.5), (60, 2), # C4, A#3, C4 - sync with C2 of the bass
  (68, 1.5), (58, 0.5), (68, 2), # G#4, A#3, G#4 - replaced D#4 with G#4 for more tension
  (60, 1.5), (58, 0.5), (60, 2), # C4, A#3, C4 - again, sync with C2 of the bass
  (68, 1.5), (58, 0.5), (68, 2), # G#4, A#3, G#4 - again, replaced D#4 with G#4

  # Bar 5 - 8
  (62, 1.5), (67, 0.5), (60, 1), (63, 1), # D4, G4, C4, D#4 - Revised bars 5-6 for more depth
  (63, 1.5), (62, 0.5), (60, 2), # D#4, D4, C4 - a descent to C4
  (68, 1.5), (58, 0.5), (60, 2),  # G#4, A#3, C4 - ends on C4 to build tension for what's coming next
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
add_notes_to_track(synth, adjusted_arp_synth_pitch_duration_data)


# Save the MIDI file
mid.save('arp-intro.mid')
