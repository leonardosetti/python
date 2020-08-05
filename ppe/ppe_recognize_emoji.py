""""
Recognize emoji by numeric code and convert

Emoji must have full 8 positions, complete missing digits padding with zeroes (0) at beginning of the string

"""

emoji_code = input(f'Insert the code from an Unicode/ Emoji i.e. 1F61A: \n').lower()

emoji_regular_prefix_string = '\\U'
emoji_full_string = (emoji_regular_prefix_string + emoji_code.zfill(8) + f"")
print(emoji_full_string)


# grinning face
print("\U0001F61A")

# grinning squinting face
print("\U0001F606")

# rolling on the floor laughing
print("\U0001F923")
