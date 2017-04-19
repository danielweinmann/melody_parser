from bottle import route, view, run
from math import log, pow

A4 = 440
C0 = A4*pow(2, -4.75)
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def note_name(frequency):
    h = round(12*log(frequency/C0, 2))
    octave = h // 12
    n = h % 12
    return note_names[int(n)] + str(int(octave))

@route('/')
@view('pytch')
def index():

    from aubio import source, pitch, notes, miditofreq

    filename = "/Users/danielweinmann/Desktop/piano_low.wav"

    downsample = 1
    samplerate = 44100 // downsample

    fft_size = 512 // downsample # fft size
    hop_size = 256  // downsample # hop size

    source_file = source(filename, samplerate, hop_size)
    samplerate = source_file.samplerate

    tolerance = 0.8

    # notes_o = notes("default", fft_size, hop_size, samplerate)

    # notes = []
    # total_frames = 0

    # while True:
    #     samples, read = source_file()
    #     new_note = notes_o(samples)
    #     if (new_note[0] != 0):
    #         frequency = miditofreq(new_note[0])
    #         name = note_name(frequency)
    #         notes += [[frequency, name]]
    #     total_frames += read
    #     if read < hop_size: break

    # return dict(notes=notes)
    
    pitch_o = pitch("yin", fft_size, hop_size, samplerate)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(tolerance)

    starts = []
    pitches = []
    confidences = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = source_file()
        pitch = pitch_o(samples)[0]
        confidence = pitch_o.get_confidence()
        starts += [total_frames / float(samplerate)]
        pitches += [pitch]
        confidences += [confidence]
        total_frames += read
        if read < hop_size: break

    clean_starts = []
    clean_pitches = []
    clean_confidences = []
    non_zero_count = 0

    for index, pitch in enumerate(pitches):
        if pitch > 0:
            non_zero_count += 1
        elif pitch == 0 and non_zero_count == 0:
            continue
        clean_starts += [starts[index]]
        clean_pitches += [pitches[index]]
        clean_confidences += [confidences[index]]

    final_starts = []
    final_pitches = []
    final_confidences = []
    non_zero_count = 0

    for index, pitch in reversed(list(enumerate(clean_pitches))):
        if pitch > 0:
            non_zero_count += 1
        elif pitch == 0 and non_zero_count == 0:
            continue
        final_starts += [clean_starts[index]]
        final_pitches += [clean_pitches[index]]
        final_confidences += [clean_confidences[index]]

    final_starts.reverse()
    final_pitches.reverse()
    final_confidences.reverse()

    notes = []
    for pitch in pitches:
        if pitch > 0:
            notes += [note_name(pitch)]
        else:
            notes += [""]

    return dict(starts=final_starts, pitches=final_pitches, confidences=final_confidences, notes=notes)

run(host='localhost', port=8080, reloader=True)
