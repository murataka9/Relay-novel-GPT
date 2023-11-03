import openai

# generate a reply
def generate_gpt_response(text):
    prompts = [text]  # 文章要約 などの機能がここに追加される
    response = openai.Completion.create(prompt=prompts, engine="GPT-4", max_tokens=100)
    return response.choices[0].text.strip()

# make summary
def generate_gpt_summary(prompts, max_tokens=30):
    summary_prompt = f"物語の要約:\n\n{prompts}\n\n要約:"
    response = openai.Completion.create(prompt=summary_prompt, engine="GPT-4", max_tokens=max_tokens)
    return response.choices[0].text.strip()

# make title
def generate_gpt_title(prompts, max_tokens=20):
    title_prompt = f"この物語の新しいタイトル:\n\n{prompts}\n\nタイトル:"
    response = openai.Completion.create(prompt=title_prompt, engine="GPT-4", max_tokens=max_tokens)
    return response.choices[0].text.strip()

# calclate tokens
def count_tokens(text):
    return len(openai.Tokenizer.tokenize(text))

