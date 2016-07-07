# Learn Python the Hard Way
# Exercise 40 - Modules, Classes, Objects

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_birthday = Song(["Happy birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

print '-' * 10
happy_birthday.sing_me_a_song()
print '-' * 10
bulls_on_parade.sing_me_a_song()
print '-' * 10
