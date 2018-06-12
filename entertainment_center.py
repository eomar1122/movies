import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://dgeiu3fz282x5.cloudfront.net/g/l/l-140044.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://images-na.ssl-images-amazon.com/images/I/71rj1RPn4iL._SL1425_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
#avatar.show_trailer()

braveheart = media.Movie("Braveheart", "William Wallace is the medieval Scottish patriot who is spurred into revolt against the English when the love of his life is slaughtered.", "https://m.media-amazon.com/images/M/MV5BMzkzMmU0YTYtOWM3My00YzBmLWI0YzctOGYyNTkwMWE5MTJkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=1NJO0jxBtMo")
print(braveheart.storyline)
braveheart.show_trailer()
