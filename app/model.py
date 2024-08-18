from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("defog/sqlcoder2")
model = AutoModelForCausalLM.from_pretrained("defog/sqlcoder2")

def generate_sql(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query
