import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyC5khD3i2U6CcWKhuXxrj-Z29sRldm2nWg")

# Select the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def extract_resume(file_path):
    """
    Reads the content of a Word or PDF file.

    Args:
      file_path (str): The path to the file.

    Returns:
      str: The extracted text content of the file.

    Raises:
      ValueError: If the file format is not supported.
    """
    if file_path.endswith(".pdf"):
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages])
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

# Load the resume from the specified file
file_path ="D:\DurgaResume.pdf"  # Replace with the actual file path
resume_info = extract_resume(file_path)

# System message for the assistant
system_content = (
    "You are a job consultant, answer the question from the user query using the provided information."
)

# User task for job predictions
user_task = "Predict a concise list of 5 most suitable jobs based on the user's resume."

# Combine the system and user messages with the resume content
prompt = f"""
System: {system_content}

INFO:
The following information is from the user's resume. Provide suggestions based on this information:
{resume_info}

TASK:
{user_task}
"""

try:
    # Generate response using Gemini API
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")