# ACE

This project aims to build an automatic chord estimator (ACE). The idea is to train a ML-model to estimate the present chord to a song in real time.

## Quickstart

```bash
# virt env
python3 -m venv .venv
source .venv/bin/activate

# Dependencies
pip install -r requirements.txt

# execute examples (still TODO)
python examples/basic_example.py

# Tests
python -m pytest -q

## Chord Encoding

For the training, the labels are set by four numbers. The first one refers to the time, the second one to the root of the chord, the third to the chord type, and the fourth to the bass note of the chord. For chord which are not slash chords, the bass equals the root. For the case that a time frame starts with no chord, the three last numbers are set to be N.

- **time** (float): Starting time of the chord
- **root** (int 0–11): C=0, C#=1, D=2, D#=3 … , B=11  
- **chordType** (int): 0=Dur, 1=Moll, 2=dim, 3=aug, 4=7, 5=maj7, 6=min7, 7=sus2, 8=sus4, 9=no-chord  
- **bass** (int 0–11): underlying bass note which have the numbers assigned analogously to the way for the root notes
Example: 
C-major starting at 0.00 = (0.00,0,0,0), 
D-minor with the F as the bass note starting at 1.50 = (1.50,2,1,5)