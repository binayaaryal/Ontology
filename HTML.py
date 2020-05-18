
import sqlite3


c = sqlite3.connect('computers.db') 
cur = c.cursor()


cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = cur.fetchall()


datas = []
col_names = []
for table in tables:
    com = f"SELECT * FROM {table[0]}"
    cur.execute(com)
    datas.append( cur.fetchall())
    col_names.append(list(map(lambda x: x[0], cur.description)))


def to_html(coloumns, data, html_name):
    html = f"""<!DOCTYPE html>
<html>
<head>
<title>""" + \
    html_name + """</title>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
"""
    
    html += f"""<body>
<h2>{html_name}</h2>
<table>
    """
    
    temp_html = "<tr>"
    for coloumn in coloumns:
        temp_html += "\n" + f"<th>{coloumn}</th>"
    html+= temp_html + "</tr>" 

    
    for dat in data:
        temp_html = "<tr>"
        for i in range(len(dat)):
            temp_html += f"\n <td>{dat[i]}</td>"
        temp_html += "</tr>"
        html+= temp_html + "</tr>" 
    
    html += f"""</table>
</body>
</html>
"""
    with open(html_name+".html", 'w') as f:
        f.write(html)
    


for i in range(len(tables)):
    to_html(col_names[i],datas[i], tables[i][0])


with open('mainweb.html', 'w') as f:
    f.write("<html>")
    
    for table in tables:
        f_ = table[0]+".html"
        f.write(f"<p> <a href={f_}> {table[0]} </a> /n")
        
    f.write("</html>")
    

