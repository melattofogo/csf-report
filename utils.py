import json

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def create_simple_blocks_from_content(client, content):
    page_simple_blocks = []
    for block in content:
        
        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type]['rich_text']

        if not rich_text:
            return
        
        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text']
        }

        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_from_content(client, nested_children)
        
        page_simple_blocks.append(simple_block)

        return page_simple_blocks
