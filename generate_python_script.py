def generate_python_script(prompt, filename):
    # Create the Python script content based on the prompt
    python_script = f"""
# Automatically generated Python script
# Prompt: {prompt}

# Your Python code starts here
print("Hello, World!")
# End of generated code
    """
    
    # Write the generated script to a Python file
    with open(filename, 'w') as file:
        file.write(python_script)

if __name__ == "__main__":
    user_prompt = input("Enter a prompt for your Python script: ")
    file_name = input("Enter a name for the Python file (e.g., my_script.py): ")

    generate_python_script(user_prompt, file_name)
    print(f"Python script '{file_name}' has been generated.")
