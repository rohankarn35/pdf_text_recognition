import subprocess

# Run the extracttext.py script as a subprocess
process = subprocess.Popen(['python', 'ExtractText.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check if there were any errors
if stderr:
    print("An error occured!! Please retry by uploading a better pdf")
else:
    # The stdout variable contains the output from extracttext.py
    extracted_text = stdout.decode('utf-8', errors='ignore')  # Use 'ignore' to skip invalid characters
    
    # You can further process or display the extracted text as needed
    print("Extracted Text:")
    print(extracted_text)
