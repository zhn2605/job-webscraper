from langchain_core.callbacks import dispatch_custom_event
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}."
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract information DIRECTLY given from {dom_content}."
    "2. **No Extra Content:** Do not provide any extra information besides those that directly matches the provided description: {parse_description}."
    "3. **Empty Response / NA Response:** If no informaiton matches the description, return an empty string (or 'Quack quack.. no matches.')"
    "4. **Direct Information Only:** Your output should contain ONLY the data that is necessary with NO ADDITIONAL comments, analysis, text, or explanation in your response. (Only useful information, nothing along the lines of 'Here's what I found regarding...')"
    "5. **Exit Message:** When you see messages like 'Exit', 'Stop', or any related prompt to stop the program, you MUST say goodbye with a duck pun / joke."
    )

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
            )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)



def search_with_ollama(search_description, search_limit=5):
    template = (
    "You are tasked with searching for the most relevant (and trustworthy) websites from the following query: {search_description}."
    "Please follow these instructions carefully: \n\n"
    "1. **Links Provided:** The links provided should be as trustworthy and useful as they can be."
    "2. **Formatting:** Links should be returned without saying customary 'Here are some...' or 'let me  know' or formatting (using * or even the name of the website... )"
    "3. **Creating Links:** Create no more than {search_limit} links. Links should all be on one line, separated by a comma and a space (, )."
    )

    prompt = ChatPromptTemplate.from_template(template)
    links = []
    output = OllamaLLM.generate(model, prompt)

    index = 0;
    while True:
        next_link_index = output

        if (output.index(", ") < 0):
            links.append(output[index, len(output)])
            break

        curr_link = output[index, ", "]

    print(links)
    return links