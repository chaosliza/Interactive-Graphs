import numpy as np

bond_replacement_dict = {
    "=": "",
    "-": "",
    "~": "",
    "#": "",
    ":": "",
    "$": "",
    "/": "",
    "\\": "",
    "@":"",
}

atom_replacement_dict = {
    "c": "C",
    "n": "N",
    "o": "O",
    "s": "S",
    "p": "P",
    "b": "B",
    "[CH]": "C",
    "[CH2]": "C",
    "[NH]": "N",
    "[BH]": "B",
    "[C]": "C",
    "[O]": "O",
    "[B]": "B",
    "[N]": "N",
    "[H]": "H",
    "[O+]": "O",
    "[O-]": "O",
    "[N+]": "N",
    "[N-]": "N",
    "[S+]": "S",
    "[S-]": "S",
    "[P+]": "P",
    "[P-]": "P",
    "[C+]": "C",
    "[C-]": "C",
    "[B+]": "B",
    "[B-]": "B",
}
# function to clean up dict to simplify SMILES

def simplify_smiles(dictionary):
    
    cleaned_dictionary = {}
    for key in dictionary:
        new_key = key
        for bond in bond_replacement_dict:
            new_key = new_key.replace(bond, bond_replacement_dict[bond])
        for atom in atom_replacement_dict:
            new_key = new_key.replace(atom, atom_replacement_dict[atom])
        if new_key not in cleaned_dictionary:
            cleaned_dictionary[new_key] = np.array([])

        cleaned_dictionary[new_key] = np.append(cleaned_dictionary[new_key], dictionary[key])
    return cleaned_dictionary
