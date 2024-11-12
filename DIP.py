# class Book():
#     def read(self):
#         print('intersting book')
#
# class StoruReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()
#
from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print('чтение интересной истории')

class AudioBook(StorySource):
    def get_story(self):
        print('чтение истории вслух')

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audiobook = AudioBook()
readerbook = StoryReader(book)
readeraudiobook = StoryReader(audiobook)

readerbook.tell_story()
readeraudiobook.tell_story()
