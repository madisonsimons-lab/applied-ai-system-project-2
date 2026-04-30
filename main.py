from retriever import load_data, retrieve_context
from agent import run_agent
from evaluator import evaluate_output
from guardrails import check_output
import datetime

def log_run(user_input, output, evaluation):
    with open("logs/run_log.txt", "a") as f:
        f.write(f"\nTIME: {datetime.datetime.now()}\n")
        f.write(f"INPUT: {user_input}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write(f"EVAL: {evaluation}\n")

def run_system(user_input):
    data = load_data()
    context = retrieve_context(user_input, data)

    output = run_agent(user_input, context)
    safe_output = check_output(output)
    evaluation = evaluate_output(safe_output)

    log_run(user_input, safe_output, evaluation)

    return safe_output, evaluation

if __name__ == "__main__":
    user_input = "I feel sad and want calm music"
    output, eval_data = run_system(user_input)

    print("\nINPUT:", user_input)
    print("\nFINAL PLAYLIST:\n", output)
    print("\nEVALUATION:", eval_data)