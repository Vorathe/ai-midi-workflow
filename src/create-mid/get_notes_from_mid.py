#python midi_to_notes.py path_to_your_file.mid
import sys
from mido import MidiFile, tick2second

def midi_to_notes(filename):
    mid = MidiFile(filename)

    # Open a text file to save output
    with open('midi_output.txt', 'w') as output_file:
        for i, track in enumerate(mid.tracks):
            output_file.write('Track {}: {}\n'.format(i, track.name))
            
            # We'll store notes here as (note, duration) tuples
            notes = []

            # For holding notes that haven't been turned off yet
            pending = {}

            for msg in track:
                # Only interested in note on/off messages
                if not msg.type in ['note_on', 'note_off']:
                    continue

                note = msg.note

                # tick2second() converts the time attribute to seconds, using the MIDI file's ticks_per_beat and tempo
                time = tick2second(msg.time, mid.ticks_per_beat, 500000)  # Default tempo is 500000 microseconds per beat

                if msg.type == 'note_on':
                    # Add note to pending notes
                    pending[note] = time
                elif msg.type == 'note_off':
                    # If note is in pending, add it to notes with its duration
                    if note in pending:
                        duration = time - pending[note]
                        notes.append((note, duration))
                        del pending[note]

            # If there are any pending notes left at the end of the track, we can add them too
            for note in pending:
                duration = time - pending[note]
                notes.append((note, duration))

            # Write notes for this track to the file
            output_file.write(str(notes) + '\n')

# Check if a command line argument was provided
if len(sys.argv) > 1:
    # Use the function on your MIDI file
    midi_to_notes(sys.argv[1])
else:
    print("Please provide a path to a MIDI file.")
