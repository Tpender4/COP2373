# Imports regular expression for matching patterns
import re

# function for separating sentences from paragraph given
def sentences_separator(text: str) -> list[str]:
    # pattern to identify paragraphs with different punctuations and levels of capitalization and returning ones that match
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    return re.findall(pat, text, flags=re.DOTALL | re.MULTILINE)

# main function for input and output
def main() -> None:
    # prompts user to enter paragraph and stores it in a list
    print("Enter a paragraph: ")
    lines = []

    # reads user input line by line until a blank line is entered or an EOFError occurs
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "" and lines:
            break
        lines.append(line)
    # Combines entered lines into one string for full paragraph and removes spaces
    paragraph = "\n".join(lines).strip()

    # Calls sentences_separator function to split paragraph into individual sentences
    sentences = sentences_separator(paragraph)

    # Displays each separated sentence and then prints the total number of sentences found
    print("\nSentences:")
    for s in sentences:
        print(s.strip())
    print(f"\nSentences Total: {len(sentences)}")

# Executes main function when ran
if __name__ == "__main__":
    main()