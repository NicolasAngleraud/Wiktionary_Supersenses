from transformers import AutoTokenizer, AutoModelForCausalLM

"""
# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("lightblue/suzume-llama-3-8B-multilingual")
model = AutoModelForCausalLM.from_pretrained("lightblue/suzume-llama-3-8B-multilingual")

# Define prompt
prompt = "'chien : individu de la race des canidés'. Donne un seul mot correspondant à la classe sémantique de cette définition entre 'person' et 'animal'."

# Tokenize prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate text based on prompt
output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)

# Decode generated output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:")
print(generated_text)
"""

API_TOKEN = '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'

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B", use_auth_token=API_TOKEN)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B", use_auth_token=API_TOKEN)

prompt = """
Task: Given the following definition, identify the category it best fits into by choosing one of these semantic classes: [Animal, Vegetable, Mineral, Concept, Event]. Provide only the category name as your answer.

Definition: "A naturally occurring, typically inorganic substance having a definite chemical composition and usually a distinct crystalline form."

Choose only one word from the given classes that best describes the definition provided. Chosen class: 
"""

inputs = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(inputs, max_length=inputs.shape[-1] + 10, num_return_sequences=1)
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:")
print(decoded_output)
