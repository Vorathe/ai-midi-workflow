# ai-midi-workflow

Utilities for experimenting with MIDI generation using Python.

## General MIDI Builder

The `src/midi_builder.py` module provides a simple way to turn lists of
`(pitch, duration)` tuples into a MIDI file. Durations are expressed in
beats where `1` equals a whole note. Pitches are MIDI note numbers (21–96).

```
from midi_builder import build_midi_file, parse_notes

melody = parse_notes("[(60, 0.5), (63, 0.5), (67, 1), (0, 0.5)]")
build_midi_file({"melody": melody}, "output.mid")
```

See `src/create-mid/builder_example.py` for a runnable example.


