def search_and_store_lines(file_path, search_words):
    matching_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            # Check if any of the search words are present in the line (case-insensitive)
            if any(word.lower() in line.lower() for word in search_words):
                matching_lines.append(line.strip())

    return matching_lines

# Example usage:
file_path = 'C:\\Users\\OM MEHRA\\OneDrive\\Desktop\\Hackathon\\output_akshat.txt'  # Replace with the actual path to your text file
search_words = ['college', 'university', 'school']  # Replace with the words you want to search

result = search_and_store_lines(file_path, search_words)

# Print or use the result as needed
for line in result:
    print(line)
