import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?://(?!\w*\.\.)[\w.]+', text)
    for match in iterator:
        result.append(match.group())
    return result