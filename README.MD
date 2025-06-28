# MIDI Chord Recognition via Bar-Level Modeling
This is the codebase for a rule-based MIDI chord recognition system based on dynamic programming.
This codebase was used in several papers before, including:

* Wang, Z., Chen, K., Jiang, J., Zhang, Y., Xu, M., Dai, S., ... & Xia, G. (2020). Pop909: A pop-song dataset for music arrangement generation. ISMIR 2020.
* Wang, Z., Wang, D., Zhang, Y., & Xia, G. (2020). Learning interpretable representation for controllable polyphonic music generation. ISMIR 2020.

It can achieve ~80% major/minor chord accuracy on a multi-track pop music track, like the ones in the RWC Pop dataset.

## Installation

```
pip3 install -r requirements.txt
```

## Usage
```
python3 main.py ./example.mid 
```

Example output:

```
0.000000	2.666640	N
2.666640	5.333280	N
5.333280	7.999920	C#:min
7.999920	10.666560	A:maj9
10.666560	13.333200	A:maj9
13.333200	15.999840	D:maj6(9)
...
```

## Important Notice

1. The algorithm assumes that the beats and downbeats of the input MIDI file (inferred from tempo change events by ``pretty_midi``) are correct. The algorithm uses both beat and downbeat locations to infer the chords.
2. The algorithm might not work well on some music genres, e.g., classical music.

## Citation

If you use this repo in your project, please use the following citation (bibtex):

```bibtex
@misc{jiang_midi_2025,
  author       = {Junyan Jiang},
  title        = {{MIDI Chord Recognition via Bar-Level Modeling}},
  year         = {2025},
  howpublished = {\url{https://github.com/music-x-lab/midi-chord-recognition}},
  url          = {https://github.com/music-x-lab/midi-chord-recognition}
}
```


## Misc
To customize the chord dictionary, please refer to ``chord_class.py``.
