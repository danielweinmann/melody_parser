from bottle import route, view, run
from math import log, pow
from note import Note

@route('/')
@view('pytch')
def index():
    from aubio import source, pitch, notes, miditofreq

    filename = "/Users/danielweinmann/Desktop/piano.wav"

    downsample = 1
    samplerate = 44100 // downsample
    fft_size = 512 // downsample # fft size
    hop_size = 256  // downsample # hop size
    source_file = source(filename, samplerate, hop_size)
    samplerate = source_file.samplerate
    tolerance = 0.8

    pitch_o = pitch("yin", fft_size, hop_size, samplerate)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    total_frames = 0
    while True:
        samples, read = source_file()
        frequency = pitch_o(samples)[0]
        start = total_frames / float(samplerate)
        pitches += [Note(start=start, frequency=frequency)]
        total_frames += read
        if read < hop_size: break

    notes = Note.distinct(pitches)

    return dict(pitches=pitches, notes=notes)

run(host='localhost', port=8080, reloader=True)
