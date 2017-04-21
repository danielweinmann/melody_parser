<style>
  tr {
  }
  td, th {
    border-top: 1px solid lightgray;
    padding: 10px;
  }
</style>

<h2>{{len(notes)}} distinct notes</h2>
<table>
  <thead>
    <tr>
      <th>Start</th>
      <th>Frequency</th>
      <th>Name</th>
      <th>Duration</th>
    </tr>
  </thead>
  <tbody>
    % for note in notes:
      <tr>
        <td>{{note.start}}</td>
        <td>{{note.frequency}}</td>
        <td>{{note.name}}</td>
        <td>{{note.duration}}</td>
      </tr>
    % end
  </tbody>
</table>

<h2>{{len(pitches)}} pitches</h2>
<table>
  <thead>
    <tr>
      <th>Start</th>
      <th>Frequency</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    % for pitch in pitches:
      <tr>
        <td>{{pitch.start}}</td>
        <td>{{pitch.frequency}}</td>
        <td>{{pitch.name}}</td>
      </tr>
    % end
  </tbody>
</table>
