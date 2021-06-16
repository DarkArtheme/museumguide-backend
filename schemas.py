from pydantic import BaseModel, Field
from typing import List, Optional


class FavMuseum(BaseModel):
    user_id: str
    fav_id: int


class MuseumId(BaseModel):
    museum_id: int


class UserId(BaseModel):
    user_id: str

# class FavMuseum(BaseModel):
#     Id: int
#
#
# class AddUserData(BaseModel):
#     UserId: str
#     Favorites: List[FavMuseum]
#
#
# class GetId(BaseModel):
#     Id: str
#
#
# class TimePerDay(BaseModel):
#     time: str
#
#
# class Photo(BaseModel):
#     link: str
#
#
# class Distance(BaseModel):
#     dist: str
#
#
# class Station(BaseModel):
#     station: str
#
#
# class MuseumSchema(BaseModel):
#     id: str
#     name: str = Field(...)
#     desc: str = Field(...)
#     pictures: str = List[Photo]
#     address: str = Field(...)
#     phone: str = Field(...)
#     website: str = Field(...)
#     worktime: str = List[TimePerDay]
#     vk: str
#     inst: str
#     twitter: str
#     facebook: str
#     odnokl: str
#     youtube: str
#     eng_name: str
#     distances: List[Distance]
#     stations: List[Station]
#     payment: str


#
# class Museum(BaseModel):
#     name: str
#     description: str
#     photos:  List[Photo]
#
#
# class MuseumSchema(BaseModel):
#     name: str = Field(...)
#     desc: str = Field(...)
#     pictures: str = List[Photo]
#     address: str = Field(...)
#     phone: str = Field(...)
#     website: str = Field(...)
#     worktime: str = List[TimePerDay]
#     vk: str
#     inst: str
#     twitter: str
#     facebook: str
#     odnokl: str
#     youtube: str
#     eng_name: str
#     distances: List[Distance]
#     stations: List[Station]
#     payment: str
#
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Музей современного искусства «Гараж»",
#                  "desc": "Открытия нового здания «Гаража» не ждал, кажется, только ленивый. Трехэтажный павильон,"
#                          " который будто бы парит над газоном в парке Горького... ",
#                  "pictures": ["https://res.cloudinary.com/museums/image/upload/c_fill,h_768,q_100,w_1024/3_1_garage_museum.jpg",
#                             "https://res.cloudinary.com/museums/image/upload/c_fill,h_768,q_100,w_1024/3_2_garage_museum.jpg",
#                             "https://res.cloudinary.com/museums/image/upload/c_fill,h_768,q_100,w_1024/3_3_garage_museum.jpg",
#                             "https://res.cloudinary.com/museums/image/upload/c_fill,h_768,q_100,w_1024/3_4_garage_museum.jpg",
#                             "https://res.cloudinary.com/museums/image/upload/c_fill,h_768,q_100,w_1024/3_5_garage_museum.jpg"],
#                 "address": "ул. Крымский Вал, 9, стр. 32",
#                 "phone": "+7 (495) 645-05-20",
#                 "website": "garagemca.org",
#                 "worktime": ["11:00 - 22:00", "11:00 - 22:00", "11:00 - 22:00", "11:00 - 22:00", "11:00 - 22:00",
#                       "11:00 - 22:00", "11:00 - 22:00"],
#                 "vk": "https://vk.com/garagemca",
#                 "inst": "https://www.instagram.com/garagemca",
#                 "twitter": "https://twitter.com/garage_mca",
#                 "facebook": "https://www.facebook.com/garagemca",
#                 "odnokl": "https://ok.ru/group/54871056842772",
#                 "eng_name": "garage_museum",
#                 "distances": ["Октябрьская", "Парк Горького"],
#                 "stations": ["800 м", "580 м"],
#                 "payment": "300-500р"}
#             }
#
