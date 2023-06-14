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

def report_fralda(client, notion_db_id, filter_fortnight):
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
        Fralda = safe_get(row, 'properties.Fralda.select.name')

        simple_rows.append({
            'Família': Família,
            'Dupla': Dupla,
            'Status': Status,
            'Quinzena': Quinzena,
            'Fralda': Fralda
        })

    filter_simple_rows = []

    current_dupla = None
    for d in simple_rows:
        if d['Quinzena'] == filter_fortnight:
            if d['Dupla'] != current_dupla:
                current_dupla = d['Dupla']
                filter_simple_rows.append({"Dupla": current_dupla, "Família": []})
            filter_simple_rows[-1]['Família'].append({"nome": d['Família'], "Status": d['Status'], "Fralda": d['Fralda']})

    result = f"Fraldas - {filter_fortnight}"
        
    for entry in filter_simple_rows:
        if any(fam['Fralda'] is not None for fam in entry['Família']):
            result += f"\n\n*{entry['Dupla']}*"
            for fam in entry['Família']:
                if fam['Fralda'] is not None:
                    result += f"\n{fam['nome']} ({fam['Fralda']})"

    return result

def report_pedencia(client, notion_db_id, filter_fortnight):
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
        Fralda = safe_get(row, 'properties.Fralda.select.name')

        simple_rows.append({
            'Família': Família,
            'Dupla': Dupla,
            'Status': Status,
            'Quinzena': Quinzena,
            'Cesta': Cesta,
            'Fralda': Fralda
        })

    filter_simple_rows = []

    current_dupla = None
    for d in simple_rows:
        if d['Quinzena'] == filter_fortnight or d['Quinzena'] is None:
            if d['Dupla'] != current_dupla:
                current_dupla = d['Dupla']
                filter_simple_rows.append({"Dupla": current_dupla, "Família": []})
            filter_simple_rows[-1]['Família'].append({"nome": d['Família'], "Status": d['Status'], "Quinzena": d['Quinzena'], "Cesta": d['Cesta'], "Fralda": d['Fralda']})

    result = f"Pendências - {filter_fortnight}"

    for entry in filter_simple_rows:
        pending_on_cesta = any(fam['Cesta'] is None for fam in entry['Família'])
        pending_on_status = any(fam['Status'] in ['Triagem'] for fam in entry['Família'])
        pending_on_quinzena = any(fam['Quinzena'] is None for fam in entry['Família'])
        pending_on_fralda = any(fam['Fralda'] is None for fam in entry['Família'])
        if (pending_on_cesta or pending_on_status or pending_on_quinzena or pending_on_fralda) and entry['Dupla'] is not None:
            result += f"\n\n*{entry['Dupla']}*"

            for fam in entry['Família']:
                pending_is_cesta = fam['Cesta'] is None
                pending_is_status = fam['Status'] == 'Triagem'
                pending_is_quinzena = fam['Quinzena'] is None
                pending_is_fralda = fam['Fralda'] is None
                if any([pending_is_cesta, pending_is_status, pending_is_quinzena, pending_is_fralda]) and fam['Status'] != 'Lista de Espera':
                    result += f"\n{fam['nome']}"
                    if pending_is_cesta:
                        result += "\n- _Confirmar tamanho da cesta_"
                    if pending_is_status:
                        result += "\n- _Confirmar se atendimento contínuo ou emergencial_"
                    if pending_is_quinzena:
                        result += "\n- _Confirmar se visita na 1a ou 2a quinzena_"
                    if pending_is_fralda:
                        result += "\n- _Confirmar se há criança que necessita de fralda_"

    return result