# ai-midi-workflow

This repository contains experiments for generating MIDI sequences programmatically with [Mido](https://mido.readthedocs.io/). The original prototype grew a large number of stand‑alone scripts under `src/create-mid`. To make future refactoring easier the files were organized into a small package with submodules:

```
src/
  create_midi/
    arps/        # Arpeggio examples
    drums/       # Percussion patterns
    sequences/   # Longer song sections
    utils/       # Helper utilities
    docs/        # Additional notes
```

Each script still runs on its own but is now grouped by purpose. New modules can import shared helpers from `create_midi.utils` as the code evolves.
