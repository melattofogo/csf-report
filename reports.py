from utils import *

def report_cesta(client, notion_db_id, filter_fortnight):
    """
    filter_fortnight: {'Dia 5', 'Dia 20'}
    """
    db_rows = client.databases.query(notion_db_id)

    simple_rows = []

    for row in db_rows['results']:
        Família = safe_get(row, 'properties.Família.title.0.plain_text')
        Dupla = safe_get(row, 'properties.Dupla.select.name')
        Status = safe_get(row, 'properties.Status.status.name')
        Quinzena = safe_get(row, 'properties.Quinzena.select.name')
        Cesta = safe_get(row, 'properties.Cesta.select.name')

        simple_rows.append({
            'Família': Família,
            'Dupla': Dupla,
            'Status': Status,
            'Quinzena': Quinzena,
            'Cesta': Cesta
        })

    filter_simple_rows = []

    current_dupla = None
    for d in simple_rows:
        if d['Quinzena'] == filter_fortnight:
            if d['Dupla'] != current_dupla:
                current_dupla = d['Dupla']
                filter_simple_rows.append({"Dupla": current_dupla, "Família": []})
            filter_simple_rows[-1]['Família'].append({"nome": d['Família'], "Status": d['Status'], "Cesta": d['Cesta']})

    result = f"Cestas - {filter_fortnight}\n\n"
    for entry in filter_simple_rows:
        result += '*' + entry['Dupla'] + '*' + "\n"
        for fam in entry['Família']:
            result += fam['nome'] + " (" + fam['Cesta'] + ")\n"
        result += "\n"
    
    return result
