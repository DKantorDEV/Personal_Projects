def beer_song():

    for num in range(99, 0, -1):
        bottle = num
        bottle_one_less = num - 1

        if bottle == 2:
            print(f"""
                {bottle} bottles of beer on the wall
                {bottle} bottles of beer
                Take one down, pass it around
                {bottle_one_less} bottle of beer on the wall
            """)

        elif bottle == 1:
            print(f"""
                {bottle} bottle of beer on the wall
                {bottle} bottle of beer
                Take one down, pass it around
                No more bottles of beer on the wall
            """)
        else:
            print(f"""
                {bottle} bottles of beer on the wall
                {bottle} bottles of beer
                Take one down, pass it around
                {bottle_one_less} bottles of beer on the wall
            """)

beer_song()