PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_file:
        names = name_file.readlines()
with open("./Input/Letters/starting_letter.txt") as starting_file:
        letter_content = starting_file.read()
        for name in names:
                stripped_name = name.strip()
                new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
                with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.docx",mode="w") as completed_letter:
                        completed_letter.write(new_letter)