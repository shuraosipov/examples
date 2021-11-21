Example tree - `(A:0.1,B:0.2,(C:0.3,D:0.4)E:0.5)F;`

```
$ python newick_to_json.py
```
Output:
```
   /-A
  |
--|--B
  |
  |   /-C
   \-|
      \-D
```

```
{ 'branch_length': '0.0',
  'children': [ { 'branch_length': '0.1',
                  'common_name': 'A',
                  'display_label': 'A',
                  'duplication': 'Y',
                  'name': 'A',
                  'seq_length': 0,
                  'type': 'leaf',
                  'uniprot_name': 'Unknown'},
                { 'branch_length': '0.2',
                  'common_name': 'B',
                  'display_label': 'B',
                  'duplication': 'Y',
                  'name': 'B',
                  'seq_length': 0,
                  'type': 'leaf',
                  'uniprot_name': 'Unknown'},
                { 'branch_length': '0.5',
                  'children': [ { 'branch_length': '0.3',
                                  'common_name': 'C',
                                  'display_label': 'C',
                                  'duplication': 'Y',
                                  'name': 'C',
                                  'seq_length': 0,
                                  'type': 'leaf',
                                  'uniprot_name': 'Unknown'},
                                { 'branch_length': '0.4',
                                  'common_name': 'D',
                                  'display_label': 'D',
                                  'duplication': 'N',
                                  'name': 'D',
                                  'seq_length': 0,
                                  'type': 'leaf',
                                  'uniprot_name': 'Unknown'}],
                  'common_name': 'E',
                  'display_label': 'E',
                  'duplication': 'Y',
                  'name': 'E',
                  'seq_length': 0,
                  'type': 'node',
                  'uniprot_name': 'Unknown'}],
  'common_name': 'F',
  'display_label': 'F',
  'duplication': 'N',
  'name': 'F',
  'seq_length': 0,
  'type': 'node',
  'uniprot_name': 'Unknown'}
```