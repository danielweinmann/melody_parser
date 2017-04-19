<h1>{{len(pitches)}} pitches</h1>
<ul>
  % for index, pitch in enumerate(pitches):
    <li>{{pitch}}, {{notes[index]}}</li>
  % end
</ul>
