from mido import Message, MidiFile, MidiTrack

verse_lead_synth_pitch_duration_data = [
  # Bar 33 - 36
  (72, 4), (75, 2), (72, 2),  # C5, whole note; D#5, half note; C5, half note
  (74, 4), (77, 2), (74, 2),  # D5, whole note; F5, half note; D5, half note
  
  # Bar 37 - 40
  (72, 4), (75, 2), (72, 2),  # C5, whole note; D#5, half note; C5, half note
  (74, 4), (77, 2), (74, 2),  # D5, whole note; F5, half note; D5, half note

  # Bar 41 - 44
  (72, 4), (75, 2), (72, 2),  # C5, whole note; D#5, half note; C5, half note
  (74, 4), (77, 2), (74, 2),  # D5, whole note; F5, half note; D5, half note

  # Bar 45 - 48
  (72, 4), (75, 2), (72, 2),  # C5, whole note; D#5, half note; C5, half note
  (74, 4), (77, 2), (74, 2),  # D5, whole note; F5, half note; D5, half note
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
add_notes_to_track(synth, verse_lead_synth_pitch_duration_data)


# Save the MIDI file
mid.save('synth-lead-sequence-verse-3.mid')
