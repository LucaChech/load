def make_table(title, cols, rows, data, f):
    si,sj = data.shape
    f.write('<h1>')
    f.write(title)
    f.write('</h1>')
    f.write('<br />')
    f.write('<table border="0">')
    f.write('<tr>')
    f.write('<td>'+str(cols[0])+'</td>')
    for j in range(sj):
        f.write('<td>')
        f.write(str(cols[j+1]))
        f.write('</td>')
    f.write('</tr>')

    for i in range(si):
        f.write('<tr>')
        f.write('<td>')
        f.write(str(rows[i]))
        f.write('</td>')
        for j in range(sj):
            f.write('<td>')
            f.write(str(data[i,j]))
            f.write('</td>')
        f.write('</tr>')
    f.write('</table>')
    