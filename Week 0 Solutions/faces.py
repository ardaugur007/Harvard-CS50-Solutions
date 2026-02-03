def main():
    faces = input()
    emoji_faces = convert(faces)
    print(emoji_faces)

def convert(emoticons):
    emoji = emoticons.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
