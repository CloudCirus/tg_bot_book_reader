BOOK_PATH = 'books/test_book_2.txt.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _check_char(idx: int, page: str, stop_chars: tuple) -> bool:
    if page[idx] in stop_chars:
        if page[idx - 1] not in stop_chars and page[idx + 1] not in stop_chars:
            return True


def _collect_text_slize(page: str, stop_chars: tuple) -> tuple[str, int] | None:
    reversed_page = page[::-1]
    for i in range(len(reversed_page)):
        if _check_char(i, reversed_page, stop_chars):
            if i != 0:
                page = page[:-i]
            return page, len(page)


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop_chars = (',', '.', '!', '?', ':', ';')
    try:
        page = text[start: (start + size)]
    except IndexError:
        page = text[start:]
    return _collect_text_slize(page, stop_chars)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding="utf-8") as file:
        book_str = file.read()
    start, page = 0, 1
    book_len = len(book_str)
    while start < book_len:
        try:
            part, part_len = _get_part_text(book_str, start, PAGE_SIZE)
        except TypeError:
            break
        book[page] = part.strip()
        start += part_len
        page += 1
