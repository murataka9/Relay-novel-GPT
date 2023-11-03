import openai
import tiktoken

# generate a reply
def generate_gpt_response(text):
    conversation = [
        {"role": "system", "content": "リレー小説で物語を描いています。物語の続きの3文を考えて、必ず'''結果のみを日本語で出力'''してください。口調を前の文章に合わせてください。必ず文章を書き切るようにしてください。"},
        {"role": "user", "content": text},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", messages=conversation, max_tokens=300
    )
    return response['choices'][0]['message']['content']

# make summary
def generate_gpt_summary(prompts, max_tokens=100):
    conversation = [{"role": "system", "content": "You are japanese novel editor. You speak japanese."}] + [{"role": "user", "content": p} for p in prompts] + [{"role": "assistant", "content": "以上の物語の要約を行い必ず'''結果のみを日本語で出力'''してください。"}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversation, max_tokens=max_tokens)
    return response['choices'][0]['message']['content']

# make title
def generate_gpt_title(prompts, max_tokens=20):
    conversation = [{"role": "system", "content": "You are japanese novel writer."}] + [{"role": "user", "content": p} for p in prompts] + [{"role": "assistant", "content": "タイトルを提案し、必ず'''結果のみを日本語で出力'''してください。"}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversation, max_tokens=max_tokens)
    return response['choices'][0]['message']['content']

# calclate tokens
def count_tokens(text):
    enc = tiktoken.get_encoding("gpt2")
    tokens = enc.encode(text)
    tokens = len(tokens)
    return tokens
