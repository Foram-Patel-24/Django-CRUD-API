# @ -0,0 +1,16 @@
# Python script to clean the fixture file and remove unwanted characters
input_file = 'user_fixture.json'
output_file = 'user_fixture_clean.json'

with open(input_file, 'rb') as f:
    # Read the file as bytes
    content = f.read()

# Decode bytes to string (ignore any invalid characters)
cleaned_content = content.decode('utf-8', errors='ignore')

with open(output_file, 'w', encoding='utf-8') as f:
    # Save cleaned content to a new file
    f.write(cleaned_content)

print("Cleaned fixture saved as 'user_fixture_clean.json'")