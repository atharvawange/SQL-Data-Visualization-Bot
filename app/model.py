from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model directly
tokenizer = AutoTokenizer.from_pretrained("defog/sqlcoder2")
model = AutoModelForCausalLM.from_pretrained("defog/sqlcoder2")

def generate_sql(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query
