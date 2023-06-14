import json

def write_dict_to_file_as_json(content, file_name):
    # Convert the content dictionary to a JSON string
    content_as_json_str = json.dumps(content)

    # Write the JSON string to the specified file
    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_text(client, page_id):
    # Get the list of children blocks for a given page ID using the client
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def create_simple_blocks_from_content(client, content):
    # Create a list to store the simple blocks
    page_simple_blocks = []
    
    # Iterate over each block in the content
    for block in content:
        
        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type]['rich_text']

        # If the block doesn't have any rich text, skip it
        if not rich_text:
            return
        
        # Create a simple block dictionary with the block's ID, type, and text
        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text']
        }

        # If the block has children, recursively process them and add them to the simple block
        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_from_content(client, nested_children)
        
        # Add the simple block to the list
        page_simple_blocks.append(simple_block)

    # Return the list of simple blocks
    return page_simple_blocks

def safe_get(data, dot_chained_keys):
    '''
    Utility function to safely retrieve nested values from a dictionary or list using dot-chained keys.

    Example usage:
    {'a': {'b': [{'c': 1}]}}
    safe_get(data, 'a.b.0.c') -> 1
    '''
    # Split the dot-chained keys into a list of individual keys
    keys = dot_chained_keys.split('.')
    # Traverse the data structure using the keys
    for key in keys:
        try:
            # If the data is a list, access the element using the integer key
            if isinstance(data, list):
                data = data[int(key)]
            else:
                # If the data is a dictionary, access the value using the key
                data = data[key]
        except (KeyError, TypeError, IndexError):
            # If an error occurs during traversal, return None
            return None
    # Return the retrieved data
    return data
