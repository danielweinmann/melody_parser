from note import Note

class Melody(object):
    def __init__(self, pitches, ending_time):
        self.notes = Note.distinct(notes=pitches, ending_time=ending_time)
        for note in self.notes:
            note.pitches = []
            initial_index = 0
            end = note.start + note.duration
            for index in range(initial_index, len(pitches)):
                start = pitches[index].start
                if start < note.start:
                    continue
                if start >= end:
                    initial_index = index
                    break
                else:
                    note.pitches += [pitches[index]]
