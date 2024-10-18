from langchain_core.callbacks import dispatch_custom_event
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}."
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract information DIRECTLY given from {dom_content}."
    "2. **No Extra Content:** Do not provide any extra information besides those that directly matches the provided description: {parse_description}."
    "3. **Empty Response / NA Response:** If no informaiton matches the description, return an empty string (or 'Quack quack.. no matches.')"
    "4. **Direct Data Only:** Using NO OTHER CONTENT, your output should contain only the data that is explicitly REQUESTED ({parse_description}) and explicitly PROVIDED ({dom_content})"
    "5. **Exit Message:** When you see messages like 'Exit', 'Stop', or any related prompt to stop the program, you MUST say goodbye with a duck pun / joke."
)

model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
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