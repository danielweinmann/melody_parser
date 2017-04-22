from math import log, pow

class Note(object):
    A4 = 440
    C0 = A4 * pow(2, -4.75)
    names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, start = 0.0, frequency = None, name = None, duration = None):
        self.start = start
        self.frequency = frequency if frequency != None else self.__class__.frequency_by_name(name)
        if self.frequency <= 0:
            self.frequency = None
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
    def distinct(cls, notes, ending_time, minimum_duration = 0.05):
        distinct_notes = []
        last_name = None
        for note in notes:
            if last_name != note.name:
                distinct_notes += [Note(start=note.start, name=note.name)]
                last_name = note.name
        last_note = notes[len(notes) - 1]
        for index, note in enumerate(distinct_notes):
            if index < len(distinct_notes) - 1:
                duration = distinct_notes[index + 1].start - note.start
            else:
                duration = ending_time - note.start
            note.duration = duration
        distinct_notes = [note for note in distinct_notes if note.duration > minimum_duration]
        last_name = None
        for note in distinct_notes:
            if last_name == note.name:
                return cls.distinct(distinct_notes, ending_time)
            else:
                last_name = note.name
        if distinct_notes[len(distinct_notes) - 1].name == None:
            return distinct_notes[0:len(distinct_notes) - 1]
        else:
            return distinct_notes
