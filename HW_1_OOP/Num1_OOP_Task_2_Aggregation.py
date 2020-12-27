class Guitar:
    def __init__(self, tool):
        self.tool = tool

    def play(self):
        print(f'I can play on bass guitar with {self.tool.tool_type}')


class Mediatior:
    def __init__(self, tool_type):
        self.tool_type = tool_type


tool = Mediatior('plastic mediator')
guitar = Guitar(tool)


if __name__ == '__main__':
    guitar.play()