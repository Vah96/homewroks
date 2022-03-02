# 2. Let's write a Music Player Class!
#    a) Create a Song class. The class will have 4 attributes - name, artist, album and the year.
#    b) Now let's create a Playlist. Playlist class will contain Songs. We should have a method that will load songs
#    into our playlist. A file called albums.txt is provided with this exercise. The method should take care of loading
#    the songs from the file and store them inside of our Playlist class.
#    c) Now, we need our Player itself. Create a Player class. The player may contain at least one playlist. A few
#    of its methods include play(), that will start playing from the beginning, show_now_playing, that will show the
#    information of the song that is playing now, next_song, that will start playing the next_song, prev_song, that does
#    the opposite and finally a stop() method, that stops the song that is playing.
#    d) Finally, implement __str__ method for our classes, so we can see a nice representation of each object.
# Note: The aforementioned points are necessary but it's not a complete description of a music player. Be creative
# and add more functionality wherever you'll find it useful!

# Եկեք ստեղծենք նվագարկիչի կլաս։ Կառուցվածքը հետևյալն է լինելու։ Ունենալու ենք երեք կլաս՝ Player, Playlist, Song:
# Song-ը պարունակելու է երգի մասին ինֆորմացիա, Playlist-ը պարունակելու է երգերը Song տիպի օբյեկտների տեսքով, իսկ
# Player-ը ունենալու է Playlist:
#    a) Ստեղծել Song կլաս։ Կլասը պետք է ունենա 4 ատրիբուտ - name, artist, album, year
#    b) Ստեղծենք Playlist կլասը։ Այն պարունակելու է երգերը։ Այս կլասը պետք է ունենա load songs մեթոդ։ Տվյալ տնայինի հետ
#    ձեզ եմ ուղարկում նաև albums.txt ֆայլը։ Ֆայլը պարունակում է հարյուրավոր երգերի անունները, հեղինակներին, ալբոմների
#    անունները և ձայնագրման թվականը։ Ամեն տողում մի երգի ինֆորմացիա է։ Ամեն տողի դաշտերը իրարից անջատված են tab-երով։
#    Վերոնշյալ մեթոդով պետք է կարդալ ֆայլը և բոլոր երգերը Song-ի տեսքով փոխանցենք Playlist-ին։
#    c) Ստեղծել Player կլասը։ Այն պետք է ունենա Playlist տիպի ատրիբուտ։ Այս կլասը պետք է ունենա նաև հետևյալ մեթոդները՝
#    play(), stop(), next_song(), previous_song(), show_current_song()։ Մեթոդները կանչելուց պետք է կոնսոլում տեսնենք,
#    թե որ երգն է տվյալ պահին միացած։ Նաև վալիդացիաներ են պետք։ Օրինակ, եթե նվագարկիչն անջատված է, հաջորդ երգին անցնել
#    կամ կրկին անջատել չենք կարող։
#    d) Որպեսզի ամեն երգերը ավելի գեղեցիկ ներկայացվեն, սահմանել __str__ մեթոդը։ Ցանկալի է բոլոր կլասերի համար։

# Այս կետերը պարտադիր են, սակայն չեն պարունակում նվագարկիչի ողջ բնութագրությունը։ Կարող եք ազատ ավելացնել հավելյալ
# տրամաբանություն։


class Song:

    def __init__(self, name, artist, album, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year


class Playlist:

    playlist = []

    def __init__(self, songs_file_path):
        self.songs_file_path = songs_file_path
        self = self.load_songs()

    def load_songs(self):
        with open(self.songs_file_path) as file:
            for line in file.readlines():
                artist, album, year, name = line.split('\t')
                self.playlist.append(Song(name.strip(), artist, album, year))


playlist = Playlist('songs.txt')
print(playlist)


class Player:

    def __init__(self, play_list):
        if not isinstance(play_list, Playlist):
            raise TypeError("Type Error")
        self.playlist = play_list

    def play():
        pass

    def stop():
        pass

    def next_song():
        pass

    def previous_song():
        pass

    def show_current_song():
        pass


player1 = Player("aasdas")



# 3. Create a class named Length. The default unit for length is meter. The class must contain some conversions
# information, e.g. feet -> m, km -> m, yard -> m, mile -> m etc.
#    a) Create a dictionary that will hold the metrics. Keys will be the unit name and their values will be the
#    coefficients for converting that unit to meters.
#    b) The class will have 2 instance attributes. Units and the length value itself.
#    c) Now, we can add lengths of course. So implement that method. But be careful, we can't add yard to meters, so
#    you will need to convert everything before adding.
#    d) Implement the __str__ method. This method must show the length of our Length object in meters.
#    e) Implement the __repr__ method. This method must show the length in whichever units our class is.
# Feel free to add some more features if you find them useful.

# Ստեղծել Length կլաս։ Երկարության հիմնական միավորը կհամարենք մետրը։ Կլասը պետք է ունենա որոշակի ինֆորմացիա, թե ինչպես
# փոխակերպել այլ միավորը մետրի (feet, km, yard, mile etc.)
#    a) Ստեղծել բառարան, որը կպահի վերոնշյալ ինֆորմացիան։ Բանալիները կլինեն միավորների անունները, իսկ արժեքները կլինեն
#    այն գործակիցները, որոնց օգնությամբ այդ միավորից ստանում ենք մետր։
#    b) Կլասը պետք է ունենա երկու instance attributes։ Երկարության արժեքը և միավորը։
#    c) Մենք պետք է կարողանանք երկարությունները իրար գումարել։ Սահմանել համապատասխան մեթոդը։ Ուշադրություն դարձնել
#    միավորներին։ Մենք չենք կարող ուղղակիորեն մետրը գումարել մղոնի կամ հակառակը։
#    d) Սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը մետրերով։
#    e) Սահմանել __repr__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը այն միավորով, որով սահմանվել է։
# Լրացուցիչ, կարող եք ավելացնել հավելյալ տրամաբանություն որտեղ ճիշտ կգտնեք։


class Length:

    dict_meter = {"feet": 0.3048, "km": 1000, "yard": 0.9144, "mile": 1609.344}

    def __init__(self, value, key="meter"):
        if key not in self.dict_meter.keys() and key != "meter":
            raise ValueError(f"{key} wrong key")
        self.value = value
        self.key = key

    def __str__(self):
        if self.key != "meter":
            value_meter = self.value * self.dict_meter[self.key]
        else:
            value_meter = self.value
        return f"Length: {value_meter} meter"

    def __repr__(self):
        return f"Length: {self.value} {self.key}"

    def __add__(self, other):
        if not isinstance(other, Length):
            raise TypeError
        key = self.key
        if self.key != other.key:
            if self.key != "meter":
                self.value = self.value * self.dict_meter[self.key]
            if other.key != "meter":
                other.value = other.value * self.dict_meter[other.key]
            key = "meter"
        return Length(self.value + other.value, key)


# length1 = Length(100, "km")
# length2 = Length(111)
# print(length1 + length2)
# print(repr(length1 + length2))
#
