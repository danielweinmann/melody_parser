{
  notes: [
  % for index, note in enumerate(melody.notes):
    {
      start: {{note.start}},
      frequency: {{note.frequency if note.frequency != None else 'null'}},
      name: {{!"'" + note.name + "'" if note.name != None else 'null'}},
      pitches: [
      % for index, pitch in enumerate(note.pitches):
        {
          start: {{pitch.start}},
          frequency: {{pitch.frequency}},
        }{{',' if index < len(note.pitches) - 1 else ''}}
      % end
      ]
    }{{',' if index < len(melody.notes) - 1 else ''}}
  % end
  ]
}
