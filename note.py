from math import log, pow

class Note(object):
    A4 = 440
    C0 = A4 * pow(2, -4.75)
    names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, start = 0.0, frequency = None, name = None, duration = None):
        self.start = start
        self.frequency = frequency if frequency != None else self.__class__.frequency_by_name(name)
        self.duration = duration
        self.name = name if name != None else self.__class__.name(frequency)

    @classmethod
    def name(cls, frequency):
        if frequency == 0 or frequency == None:
            return None
        h = round(12 * log(frequency / cls.C0, 2))
        octave = h // 12
        index = h % 12
        return cls.names[int(index)] + str(int(octave))

    @classmethod
    def frequency_by_name(cls, name):
        if name == None:
            return None
        index = cls.names.index(name[0:len(name)-1])
        octave = int(name[len(name)-1:])
        return round(pow(2, (float(octave * 12 + index) / 12.0)) * cls.C0, 2)

    @classmethod
    def distinct(cls, notes, minimum_duration = 0.02):
        distinct_notes = []
        last_note = None
        for note in notes:
            if last_note != note.name:
                distinct_notes += [Note(start=note.start, name=note.name)]
                last_note = note.name
        for index, note in enumerate(distinct_notes):
            if index < len(distinct_notes) - 1:
                duration = distinct_notes[index + 1].start - note.start
            else:
                duration = notes[len(notes) - 1].start - note.start
            note.duration = duration
        return [note for note in distinct_notes if note.duration > minimum_duration]
