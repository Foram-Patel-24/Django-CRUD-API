# @ -0,0 +1,34 @@
# Open the JSON file with BOM and remove BOM if present
with open('user_fixture.json', 'rb') as f:
    content = f.read()

# If BOM is detected (0xEF, 0xBB, 0xBF), remove it
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]

# Save the cleaned content to a new JSON file
with open('user_fixture_no_bom.json', 'wb') as f:
    f.write(content)

# print("BOM Removed. Saved as 'user_fixture_no_bom.json'.")


# # Re-encode the file to UTF-8 without BOM
# with open('user_fixture.json', 'rb') as f:
#     content = f.read()

# # Write the content back to the file as UTF-8 without BOM
# with open('user_fixture_fixed.json', 'wb') as f:
#     f.write(content)


# import chardet

# # Read the file in binary mode
# with open('user_fixture.json', 'rb') as f:
#     raw_data = f.read()

# # Detect the file encoding
# result = chardet.detect(raw_data)

# print(f"Detected encoding: {result['encoding']}")