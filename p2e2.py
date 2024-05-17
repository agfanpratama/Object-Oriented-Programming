class skipNum:
    def __init__(self, target):
        self.target = target

    def skip_number(self):
        for i in range(1, 51):
            if i == self.target:
                continue
            print(i, end=' ')

# Main program
if __name__ == "__main__":
    target = int(input('Dua digit terakhir nim: '))
    skipper = skipNum(target)
    skipper.skip_number()
