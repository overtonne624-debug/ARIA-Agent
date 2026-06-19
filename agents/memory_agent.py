import json
import os

MEMORY_FILE = "memory.json"


def store_memory(text):
    memories = retrieve_memory("latest")
    memories.append(text)

    print("Saving memory to:", MEMORY_FILE) 

    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f)


def retrieve_memory(query):
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)[-3:]