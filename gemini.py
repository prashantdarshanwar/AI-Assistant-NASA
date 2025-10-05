import google.generativeai as genai
import os

# Option 1: Use environment variable
os.environ["GOOGLE_API_KEY"] = "AIzaSyBnZ-O0YfOS0qKHYVxW2yQzuwlzuB_AQSk"

# Option 2: Or configure directly in code
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Now initialize your model
model = genai.GenerativeModel("models/gemini-2.5-pro")  # replace with valid model

# Example usage
prompt = "Explain what a habitable zone is in exoplanet science."
response = model.generate_content(prompt)
print(response.text)
