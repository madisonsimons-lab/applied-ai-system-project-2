from main import run_system

tests = [
    "sad music",
    "workout playlist",
    "chill study music",
    "party songs"
]

results = []

for t in tests:
    output, eval_data = run_system(t)

    results.append({
        "input": t,
        "score": eval_data["score"],
        "confidence": eval_data["confidence"]
    })

print("\n=== TEST RESULTS ===")
for r in results:
    print(r)

avg_score = sum(r["score"] for r in results) / len(results)
avg_conf = sum(r["confidence"] for r in results) / len(results)

print("\nAVERAGE SCORE:", avg_score)
print("AVERAGE CONFIDENCE:", avg_conf)