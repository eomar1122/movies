import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://dgeiu3fz282x5.cloudfront.net/g/l/l-140044.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://images-na.ssl-images-amazon.com/images/I/71rj1RPn4iL._SL1425_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

braveheart = media.Movie("Braveheart", "William Wallace is the medieval Scottish patriot who is spurred into revolt against the English when the love of his life is slaughtered.", "https://m.media-amazon.com/images/M/MV5BMzkzMmU0YTYtOWM3My00YzBmLWI0YzctOGYyNTkwMWE5MTJkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=1NJO0jxBtMo")
# print(braveheart.storyline)
# braveheart.show_trailer()

gladiator = media.Movie("Gladiator", "Set in Roman times, the story of a once-powerful general forced to become a common gladiator.", "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks", "https://www.youtube.com/watch?v=do9zep1n8cU")

mission_impossible = media.Movie("Mission Impossible", "Mission: Impossible is a series of action spy films based on the television series of the same name, produced by and starring Tom Cruise as Ethan Hunt, an agent of the fictional Impossible Missions Force.", "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Missionimpossibleblurayboxset.jpg/220px-Missionimpossibleblurayboxset.jpg", "https://www.youtube.com/watch?v=gOW_azQbOjw")

die_hard = media.Movie("Die Hard", "New York City policeman John McClane (Bruce Willis) is visiting his estranged wife (Bonnie Bedelia) and two daughters on Christmas Eve. He joins her at a holiday party in the headquarters of the Japanese-owned business she works for. But the festivities are interrupted by a group of terrorists who take over the exclusive high-rise, and everyone in it. Very soon McClane realizes that there's no one to save the hostages -- but him.", "http://t3.gstatic.com/images?q=tbn:ANd9GcRagI3FRZIH6bs2V3gw3hCWorUfc-JvImrRQXSYQy_ZF-o2a_PK", "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

movies = [toy_story, avatar, braveheart, gladiator, mission_impossible, die_hard]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATING)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)