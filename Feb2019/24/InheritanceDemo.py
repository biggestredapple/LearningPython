# String Formatting Demo
class StringFormattingDemo:
    Instances = 0

    def __init__(self):
        StringFormattingDemo.Instances += 1

    def formatSingleString(self, title, value):
        try:
            print(
                f"----- {title} | Instances: {self.Instances}-----")
            print(f'StringFormattingDemo.Instances: {self.Instances}')
            print('{}'.format(value))
        except Exception as error:
            print("Error in StringFormattingDemo::formatSingleString:", error)