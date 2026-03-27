PLACEHOLDER = "[Ali Jamil]"
with open("A:/My-work-main/udemy2/Mail Merge Project Start/Mail_Merge_Project/Input/Names/invited_names.txt") as name_file:
        names = name_file.readlines()
with open("A:/My-work-main/udemy2/Mail Merge Project Start/Mail_Merge_Project/Input/Letters/starting_letter.txt") as starting_file:
        letter_content = starting_file.read()
        for name in names:
                stripped_name = name.strip()
                new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
                with open(f"A:/My-work-main/udemy2/Mail Merge Project Start/Mail_Merge_Project/Output/ReadyToSend/Letter_for_{stripped_name}.docx",mode="w") as completed_letter:
                        completed_letter.write(new_letter)