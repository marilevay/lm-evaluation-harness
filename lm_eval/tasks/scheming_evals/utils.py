def process_docs(dataset: datasets.Dataset):
    # Define the function to process a single document
    def process_doc(data):
        added_by = data["added_by"]
        subject = data["subject"]
        scenario = data["scenario"]
        free_response_prompt = data["free_response_prompt"].strip()
        mc_prompt = data["mc_prompt"].strip()
        choices = [data["1"], data["2"]]
        option_a = choices[0]
        option_b = choices[1]
        answer = data["answer"]
        explanation = data["explanation"]
        goal_question = data["goal_question"].strip()
        goal_answer = data["goal_answer"]
        context_question = data["context_question"].strip()
        context_answer = data["context_answer"]

        out_doc = f"Added by: {added_by}\nSubject: {subject}\nScenario: {scenario}\n"
        if free_response_prompt:
            out_doc += f"{scenario}\n{free_response_prompt}\nAnswer:"
        elif mc_prompt:
            out_doc += f"{explanation}\n{scenario}\n{mc_prompt}\nA. {option_a}\nB. {option_b}\nAnswer:"
        elif goal_question:
            out_doc += f"{goal_question}\nAnswer:"
        elif context_question:
            out_doc += f"{context_question}\nAnswer:"

        return out_doc

    return dataset.map(_process_doc)