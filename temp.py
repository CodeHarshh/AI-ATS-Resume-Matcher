import google.generativeai as genai

genai.configure(api_key='')
# Convert generator to list
models = list(genai.list_models())

# Print model names
for model in models:
    print(model.name)