import json


def load_jsonl2list(filepath: str):
    """
    Load a JSON Lines file and return its contents as a list of dictionaries.

    Args:
        filepath (str): The path to the JSON Lines (.jsonl) file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a JSON object from a line in the file.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        json.JSONDecodeError: If a line in the file is not valid JSON.
    """
    data = []
    with open(filepath, "r", encoding="utf-8") as fin:
        for line in fin:
            data.append(json.loads(line.strip()))
    return data


def load_jsonl2list_assign_seq_id(filepath: str):
    """
    Load a JSON Lines (JSONL) file and return a list of dictionaries, assigning a sequential ID to each item if not present.

    Args:
        filepath (str): The path to the JSONL file.

    Returns:
        list: A list of dictionaries, each representing a JSON object from the file. Each dictionary will have an "id" key, 
              which is either taken from the original JSON object or assigned sequentially if not present.
    """
    data = []
    with open(filepath, "r", encoding="utf-8") as fin:
        for idx, line in enumerate(fin):
            dataitem = json.loads(line.strip())
            if "id" not in dataitem:
                dataitem["id"] = str(idx)
            else:
                dataitem["id"] = str(dataitem["id"])
            data.append(dataitem)
    return data
