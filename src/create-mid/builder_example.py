import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from midi_builder import build_midi_file, parse_notes

melody_text = "[(60, 0.5), (63, 0.5), (67, 1), (0, 0.5)]"
bass_text = "[(36, 2), (31, 2)]"

tracks = {
    "lead": parse_notes(melody_text),
    "bass": parse_notes(bass_text),
}

build_midi_file(tracks, "builder_example.mid")
