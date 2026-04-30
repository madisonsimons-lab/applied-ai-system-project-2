def check_output(output):
    banned = ["hate", "offensive"]

    for word in banned:
        if word in output.lower():
            return "Blocked unsafe output."

    return output