from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from mido import Message, MidiFile, MidiTrack, MetaMessage

Note = Tuple[int, float]


def build_midi_file(
    tracks: Dict[str, Iterable[Note]],
    output_path: str,
    *,
    ticks_per_beat: int = 480,
    tempo: int = 500000,
    velocity: int = 64,
) -> None:
    """Create a MIDI file from note sequences.

    Parameters
    ----------
    tracks:
        Mapping of track names to sequences of ``(pitch, duration)`` tuples.
    output_path:
        Path where the MIDI file will be written.
    ticks_per_beat:
        Resolution of the MIDI file.
    tempo:
        Tempo in microseconds per beat.
    velocity:
        MIDI velocity applied to all notes.
    """
    mid = MidiFile(ticks_per_beat=ticks_per_beat)

    tempo_track = MidiTrack()
    tempo_track.append(MetaMessage("set_tempo", tempo=tempo, time=0))
    mid.tracks.append(tempo_track)

    for name, notes in tracks.items():
        track = MidiTrack()
        track.name = name
        for pitch, duration in notes:
            dt = int(duration * ticks_per_beat)
            if pitch > 0:
                track.append(Message("note_on", note=pitch, velocity=velocity, time=0))
            track.append(Message("note_off", note=pitch, velocity=velocity, time=dt))
        mid.tracks.append(track)

    mid.save(output_path)


def parse_notes(text: str) -> List[Note]:
    """Parse a textual ``[(pitch, duration), ...]`` representation.

    Besides a literal Python list of tuples, a simpler notation is
    supported where items are separated by whitespace or commas and
    each note is expressed as ``pitch:duration`` (``60:0.5``).
    """
    import ast
    import re

    original = text
    if "=" in text:
        text = text.split("=", 1)[1]
    text = text.strip()

    # Try Python literal evaluation first
    try:
        notes = ast.literal_eval(text)
        return list(notes)
    except Exception:
        pass

    # Fallback: simple ``pitch:duration`` tokens
    tokens = re.split(r"[\s,]+", text)
    notes = []
    for token in tokens:
        if not token:
            continue
        token = token.strip("()[]")
        if ":" in token:
            pitch_str, dur_str = token.split(":", 1)
        elif "-" in token:
            pitch_str, dur_str = token.split("-", 1)
        elif "/" in token:
            pitch_str, dur_str = token.split("/", 1)
        else:
            parts = token.split()
            if len(parts) != 2:
                raise ValueError(f"Cannot parse note token: '{token}' from '{original}'")
            pitch_str, dur_str = parts
        notes.append((int(pitch_str), float(dur_str)))

    return notes
