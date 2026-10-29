from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.error import HTTPError, URLError



class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.ignored_tags = {"style", "script"}
        self.ignore_text = False

    def handle_starttag(self, tag, attrs):
        if tag in self.ignored_tags:
            self.ignore_text = True

    def handle_endtag(self, tag):
        if tag in self.ignored_tags:
            self.ignore_text = False

    def handle_data(self, data):
        text = data.strip()

        if text and not self.ignore_text:
            self.text_parts.append(text)



def get_page_text(url):
    with urlopen(url, timeout=10) as response:
        html = response.read().decode("utf-8", errors="replace")

    parser = TextExtractor()
    parser.feed(html)

    return "\n".join(parser.text_parts)


def main():
    url = input("Enter webpage URL: ").strip()

    try:
        text = get_page_text(url)
        print(text)

    except (HTTPError, URLError, ValueError, TimeoutError) as error:
        print(f"Error fetching webpage: {error}")


if __name__ == "__main__":
    main()
