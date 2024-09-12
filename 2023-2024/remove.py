def main():
    text = ""
    final = ''

    while text != "DONE!":
        text = input()
        if 'icon' not in text and ('xit' in text.lower() or 'do' in text.lower()):
            final += f'{text}\n'

    print(final)


if __name__ == '__main__':
    main()
