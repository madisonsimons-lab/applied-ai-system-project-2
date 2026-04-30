def load_data():
    files = [
        "data/songs.txt",
        "data/mood_rules.txt",
        "data/genre_rules.txt"
    ]

    combined = []

    for f in files:
        with open(f) as file:
            combined.extend(file.readlines())

    return combined

def retrieve_context(user_input, data):
    matches = []

    for line in data:
        if any(word.lower() in line.lower() for word in user_input.split()):
            matches.append(line.strip())

    if not matches:
        matches = data[:5]

    return matches