from llama_index.llms.ollama import Ollama
from voiceTo import voiceto as vt
from SpeechCapture import speechcapture as sc
import re

# Initialize the Ollama LLM
llm = Ollama(model="deepseek-r1:1.5b", request_timeout=30.0)

# Capture speech and get the response from the LLM
def call_deep():
    res = str(llm.complete(sc()))

    # Remove <think> tags and any other unwanted characters
    cleaned_content = re.sub(r'<think>.*?</think>', '', res, flags=re.DOTALL)

    # Extract the final numerical answer (e.g., \boxed{10} -> 10)
    final_answer = re.search(r'\\boxed\{(\d+)\}', cleaned_content)


    if final_answer:
        result = 'it is ' + final_answer.group(1) 
    else:
        result = cleaned_content


    print(result)  # Print only the numerical result
    vt(result)     # Convert the numerical result to speech
