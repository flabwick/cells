class Prompt:
    def __init__(self, title, text, links):
        self.title = title
        self.text = text
        self.links = links

class Cell:
    def __init__(self, name, prompts):
        self.name = name
        self.prompts = prompts  # list of Prompt
