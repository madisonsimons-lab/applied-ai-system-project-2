def evaluate_output(output):
    score = 0

    if "-" in output:
        score += 1

    if len(output) > 100:
        score += 1

    if "because" in output.lower():
        score += 1

    confidence = score / 3

    return {
        "score": score,
        "confidence": confidence,
        "length": len(output)
    }