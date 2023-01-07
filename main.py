from PyPDF2 import PdfReader
import pyttsx3


# открыть файл как чтение

with open('ren.pdf', 'rb') as file:
    reader = PdfReader(file)                   # Создаём обьект

    page = reader.pages[5:100]                  # начнем с третьей страницы
    text = ''                                   # создали место под текст

    # s = text.replace(" ", "")
    for pages in page:                         # раскрыли каждую
        text += pages.extract_text()      # извлекаем как текст
        text1 = text.replace("\n", " ")   # убрал перенос строки
        text2 = text1.replace("- ", "")   #  убрал пробел,чтобы слитно читалось
        # text = text.replace("-", "")
        # text1 = text.split(',')
        # text1 = text1.replace(" ', ' ", "")
        # text1 = text.join(text.splitlines())
        # text1 = text.join()
    print(text2)
    # speaker = pyttsx3.init()                  # создали обьект речи
    # speaker.say(text2)                        # запустили говорить
    # speaker.runAndWait()
    # speaker.stop()                            # остановить говорить

    engine = pyttsx3.init()                     # cоздаем движок преобразования текста в речь
    engine.setProperty('voice', 'english')      # голос
    engine.setProperty('rate', 150)             # установить скорость речи

    engine.save_to_file(text2, 'E:\\PycharmProjects\\pdf_to_audio\\audio.mp3')
    engine.runAndWait()













    # number_of_pages = len(reader.pages)        # количество страниц
    # text = ""
    # for page in reader.pages:
    #     text += page.extract_text() + "\n"
    #     print(text)


    # print(number_of_pages)
    # page = reader.pages[3]
    # text = page.extract_text()
    # print(text)

# page = reader.pages[1]
# text = page.extract_text()
# Get the handle to speaker
# speaker = pyttsx3.init()
# # Get the handle to speaker
# speaker.say(text)
# speaker.runAndWait()

# print(number_of_pages)


# # Loop through all the pages
#     for page_number in range(reader.getNumPages()):
#         # Get the current page
#         page = reader.pages[page_number]
#
#         # Extract the text from the page
#         text = page.extractText()
#
#         # Print the text
#         print(text)
#









# # Read the pdf by specifying the path in your computer
# pdfReader = PyPDF2.PdfReader(open('dj.pdf', 'rb'))
# # Get the handle to speaker
# speaker = pyttsx3.init()
# # split the pages and read one by one
# for page_num in (pdfReader.pages):
#    text = pdfReader.getPage(page_num).extractText()
#    speaker.say(text) #clcoding.com
#    speaker.runAndWait()
# # stop the speaker after completion
# speaker.stop()
# # save the audiobook at specified path
# # engine.save_to_file(text, 'E:\audio.mp3')
# # engine.runAndWait()
#


# path = open("dj.pdf", "rb")
#
# pdfReader = PyPDF2.PdfFileReader("pdf_to_audio\\dj.pdf")
#
# from_page = pdfReader.getPage(10)
# print(from_page)



# text = from_page.extractText()
# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()


