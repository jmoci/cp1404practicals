import wikipedia
from wikipedia import suggest


def main():
    prompt = input("Enter page title: ")
    while prompt != "":
        result = wikipedia.search(prompt)[0]
        print(wikipedia.summary(result,auto_suggest = False))
        prompt = input("Enter page title: ")

if __name__ == '__main__':
    main()