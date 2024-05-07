import nltk
import ssl
import csv


def open_file_with_mode(file_name, mode='r'):
    reader = csv.reader(open(file_name, mode), delimiter=',')
    return reader


def download_NLTKPackages():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download()


def parseCSVFile():
    file_name = 'UpdatedResumeDataSet.csv'
    reader = open_file_with_mode(file_name, mode='r')
    for line in reader:
        tokens = nltk.word_tokenize(line, language='English', preserve_line=True)
        print(tokens)


if __name__ == '__main__':
    parseCSVFile()
