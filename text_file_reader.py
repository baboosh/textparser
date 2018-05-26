class Reader:

    def __init__(self, file):
        self.text_file = file
        self.read_file = self.text_file.read()
        self.words = []
        self.word_dictionary = {}

    @staticmethod
    def wordListToFreqDict(wordlist):
        wordfreq = [wordlist.count(p) for p in wordlist]
        return dict(zip(wordlist, wordfreq))

    @staticmethod
    def sortFreqDict(freqdict):
        aux = [(freqdict[key], key) for key in freqdict]
        aux.sort()
        aux.reverse()
        return aux

    def scan_file(self):
        words = self.read_file.split(' ')
        for word in words:
            self.words.append(word)
        freqdict = self.wordListToFreqDict(self.words)
        words_sorted = self.sortFreqDict(freqdict)
        for word in words_sorted:
            print(word)

if __name__ == '__main__':
    a = input('text file to sparse (include .txt): ')
    with open(a, 'r') as file:
        reader = Reader(file)
        reader.scan_file()