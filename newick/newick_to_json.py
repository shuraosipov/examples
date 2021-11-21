from ete3 import Tree
import random
from pprint import pprint

t = Tree("(A:0.1,B:0.2,(C:0.3,D:0.4)E:0.5)F;", format=1)


def get_json(node):
    # Read ETE tag for duplication or speciation events
    if not hasattr(node, 'evoltype'):
        dup = random.sample(['N','Y'], 1)[0]
    elif node.evoltype == "S":
        dup = "N"
    elif node.evoltype == "D":
        dup = "Y"
    
    json = { 
        "name": node.name, 
        "display_label": node.name,
        "duplication": dup,
        "branch_length": str(node.dist),
        "common_name": node.name,
        "seq_length": 0,
        "type": "node" if node.children else "leaf",
        "uniprot_name": "Unknown",
    }

    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    
    return json
    

result = get_json(t)

print(t)
pprint(result, indent=2)