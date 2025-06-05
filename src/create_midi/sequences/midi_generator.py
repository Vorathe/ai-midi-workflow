from mido import Message, MidiFile, MidiTrack

intro_synth_pad_pitch_duration_data = [
  (48, 4), (0, 2), (51, 2),  # C3, whole note; rest, half note; D#3, half note - Bar 1
  (48, 2), (0, 2), (51, 2), (48, 2),  # C3, half note; rest, half note; D#3, half note; C3, half note - Bar 2
  (48, 4), (0, 2), (51, 2),  # C3, whole note; rest, half note; D#3, half note - Bar 3
  (48, 2), (0, 2), (51, 2), (48, 2)   # C3, half note; rest, half note; D#3, half note; C3, half note - Bar 4
]

intro_arp_synth_pitch_duration_data = [
  (60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),  # C4, D#4, G4, D#4, quarter notes - Bar 1
  (60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),  # C4, D#4, G4, D#4, quarter notes - Bar 2
  (60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),  # C4, D#4, G4, D#4, quarter notes - Bar 3
  (60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),  # C4, D#4, G4, D#4, quarter notes - Bar 4
]

intro_bass_synth_pitch_duration_data = [
  (36, 2), (0, 2), (39, 2), (36, 2),  # C2, half note; rest, half note; D#2, half note; C2, half note - Bar 1
  (36, 2), (0, 2), (39, 2), (36, 2),  # C2, half note; rest, half note; D#2, half note; C2, half note - Bar 2
  (36, 2), (0, 2), (39, 2), (36, 2),  # C2, half note; rest, half note; D#2, half note; C2, half note - Bar 3
  (36, 2), (0, 2), (39, 2), (36, 2),  # C2, half note; rest, half note; D#2, half note; C2, half note - Bar 4
]

drum_kick_pitch_duration_data = [
  (36, 1), (0, 1), (36, 1), (0, 1),  # Kick (C2) on the first and third beat of each bar
  (36, 1), (0, 1), (36, 1), (0, 1),  
  (36, 1), (0, 1), (36, 1), (0, 1),  
  (36, 1), (0, 1), (36, 1), (0, 1),
]

drum_snare_pitch_duration_data = [
  (0, 1), (38, 1), (0, 1), (38, 1),  # Snare (D#2) on the second and fourth beat of each bar
  (0, 1), (38, 1), (0, 1), (38, 1),  
  (0, 1), (38, 1), (0, 1), (38, 1),  
  (0, 1), (38, 1), (0, 1), (38, 1),
]

drum_hihat_pitch_duration_data = [
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),  # Hi-hat (F#2) on every eighth note of each bar
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),
  (42, 0.5), (42, 0.5), (42, 0.5), (42, 0.5),
]

# Create a new MIDI file and add tracks for synth and bass
mid = MidiFile(ticks_per_beat=480)  # Set ticks per beat for the MIDI file
lead_synth = MidiTrack()
bass_synth = MidiTrack()
arp_synth = MidiTrack()
kick_synth = MidiTrack()
snare_synth = MidiTrack()
hihat_synth = MidiTrack()
mid.tracks.append(lead_synth)
mid.tracks.append(bass_synth)
mid.tracks.append(arp_synth)
mid.tracks.append(kick_synth)
mid.tracks.append(snare_synth)
mid.tracks.append(hihat_synth)

# Function to add notes to the track
def add_notes_to_track(track, notes):
    for note, duration in notes:
        if note > 0:  # If the note value is not 0 (rest), add a note on and note off event
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=int(duration*mid.ticks_per_beat)))
        else:  # If the note value is 0 (rest), add a rest
            track.append(Message('note_off', note=note, velocity=64, time=int(duration*mid.ticks_per_beat)))

# Add notes to the synth and bass tracks
add_notes_to_track(lead_synth, intro_synth_pad_pitch_duration_data)
add_notes_to_track(bass_synth, intro_bass_synth_pitch_duration_data)
add_notes_to_track(arp_synth, intro_arp_synth_pitch_duration_data)
add_notes_to_track(kick_synth, drum_kick_pitch_duration_data)
add_notes_to_track(snare_synth, drum_snare_pitch_duration_data)
add_notes_to_track(hihat_synth, drum_hihat_pitch_duration_data)


# Save the MIDI file
mid.save('sequence.mid')
