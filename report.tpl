<h1>Server Log Details</h1>
<table border=2 bgcolor='red'>
    <tr>
        <th>IP</th>
        <th>Date</th>
        <th>Pics</th>
        <th>Web Site</th>
    </tr>
    %for i,j,k,l in res:
    <tr>
        <td>{{i}}</td>
        <td>{{j}}</td>
        <td>{{k}}</td>
        <td>{{l}}</td>
    </tr>
    %end
</table>