class TextEditor:

    def __init__(self):
        self.txt = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.txt = self.txt[0:self.cursor] + text + self.txt[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:

        part = self.txt[0:self.cursor-k]
        deleted = min(len(part), k)
        self.txt = part + self.txt[self.cursor:]
        self.cursor -= deleted
        return deleted

    def cursorLeft(self, k: int) -> str:
        pass

    def cursorRight(self, k: int) -> str:
        if self.cursor == len(self.txt) - 1:
            return


if __name__ == "__main__":
    textEditor = TextEditor()

    textEditor.addText("leetcode")
    assert textEditor.deleteText(4) == 4
    textEditor.addText("practice")
    assert textEditor.cursorRight(3) == "etpractice"
    assert textEditor.cursorLeft(8) == "leet"
    assert textEditor.deleteText(10) == 4
    assert textEditor.cursorLeft(2) == ""
    assert textEditor.cursorRight(6) == "practi"
