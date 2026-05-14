from midiutil import MIDIFile
import os

os.makedirs("assets", exist_ok=True)

def create_midi(filename, notes, duration=0.4, tempo=120):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
    for i, pitch in enumerate(notes):
        midi.addNote(0, 0, pitch, i * duration * 0.6, duration, 100)
    
    with open(f"assets/{filename}.mid", "wb") as f:
        midi.writeFile(f)

create_midi("move",    [60, 64, 67, 72], duration=0.35, tempo=150)
create_midi("invalid", [48, 47, 46, 45], duration=0.45, tempo=70)
create_midi("win",     [60, 64, 67, 72, 76, 79, 84], duration=0.7, tempo=110)
create_midi("click",   [76], duration=0.12, tempo=220)
create_midi("hint",    [72, 79, 84], duration=0.25, tempo=160)

print("✅ MIDI files created in ./assets/")
