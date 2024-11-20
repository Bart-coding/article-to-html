from openai import OpenAI
api_key = "YOUR_API_KEY"
client = OpenAI(api_key=api_key)

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None
    
def generate_html(full_article_prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": full_article_prompt
                }
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while generating HTML: {e}")
        return None

def save_html_to_file(html_content, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
    except Exception as e:
        print(f"An error occurred while saving to {output_file}: {e}")

if __name__ == "__main__":
    article_path = "artykul.txt"
    prompt_path = "prompt.txt"
    output_html_path = "artykul.html"

    article_content = read_txt_file(article_path)
    article_base_prompt = read_txt_file(prompt_path)

    if article_content and article_base_prompt:
        full_prompt = f"{article_content}\n\n{article_base_prompt}"
        html_content = generate_html(full_prompt)
        
        if html_content is not None:
            save_html_to_file(html_content, output_html_path)
            print(f"HTML was saved in {output_html_path}.")