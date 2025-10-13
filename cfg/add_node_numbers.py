import re
import sys

def replace_node(match):
    node_id = match.group(1)
    attributes = match.group(2)
    # Verificar se já tem label
    label_match = re.search(r'label="([^"]*)"', attributes)
    if label_match:
        old_label = label_match.group(1)
        # Adicionar o número do nó no início do label
        new_label = f'[{node_id}] {old_label}'
        new_attributes = attributes.replace(f'label="{old_label}"', f'label="{new_label}"')
    else:
        # Se não tem label, adicionar um
        new_attributes = f'label="[{node_id}]", {attributes}'
    return f'\t{node_id}\t[{new_attributes}];'


def add_node_numbers(input_file, output_file):
    """
    Lê um arquivo .dot e adiciona numeração aos nós
    """
    with open(input_file, 'r') as f:
        content = f.read()
    # Encontrar todos os nós e seus labels
    node_pattern = r'(?<!->)\s+(\d+)\s*\[([^\]]*)\];'
    # Substituir todos os nós
    modified_content = re.sub(node_pattern, replace_node, content, flags=re.MULTILINE)
    with open(output_file, 'w') as f:
        f.write(modified_content)
    print(f"Arquivo modificado salvo em: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python add_node_numbers.py <input.dot> <output.dot>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    add_node_numbers(input_file, output_file)
