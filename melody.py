from note import Note

class Melody(object):
    def __init__(self, pitches, ending_time):
        self.notes = Note.distinct(notes=pitches, ending_time=ending_time)
        self.minimum_frequency = 100000.0
        for note in self.notes:
            note.pitches = []
            initial_index = 0
            end = note.start + note.duration
            if note.frequency > 0 and note.frequency < self.minimum_frequency:
                self.minimum_frequency = note.frequency
            for index in range(initial_index, len(pitches)):
                pitch = pitches[index]
                start = pitch.start
                if start < note.start:
                    continue
                if start >= end:
                    initial_index = index
                    break
                else:
                    note.pitches += [pitch]
        for note in self.notes:
            note.relative_frequency = (note.frequency - self.minimum_frequency) if note.frequency != None else None
            for pitch in note.pitches:
                pitch.relative_frequency = (pitch.frequency - note.frequency) if pitch.frequency != None and note.frequency != None else None
