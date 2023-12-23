import requests

roblox_request_session = requests.Session()

badges_api_url = "https://badges.roblox.com/v1/universes/206509909/badges?limit=50&sortOrder=Asc"

badges_request = roblox_request_session.get(url=badges_api_url)
badges_data = badges_request.json()
badges_array = badges_data["data"]

badge_ids = [badge['id'] for badge in badges_array]
badge_id_string = ','.join(map(str, badge_ids))
badges_img_api_url = "https://thumbnails.roblox.com/v1/badges/icons?badgeIds=" + badge_id_string + "&size=150x150&format=Png&isCircular=true"

badges_img_request = roblox_request_session.get(url=badges_img_api_url)
badges_img_data = badges_img_request.json()
badges_img_array = badges_img_data["data"]

badge_table = """{| class=\"wikitable\"
|+
!'''Badge'''
!'''Name'''
!Description
!'''Rarity'''
!'''Won Ever'''
!'''How to obtain'''
"""

how_to_obtain_dict = {
    "Milo is in the Elevator!": ["Wait until the flat grass floor. On that floor, there is a random chance that Milo can enter the elevator as an NPC.", "[[File:MiloBadge.png|frameless]]"],
    "Welcome To The Luxury Elevator": ["Join The Luxury Elevator for the first time.", "[[File:WelcomeBadge.png|frameless]]"],
    "Speed Run Floor Winner": ["Complete the Speed Run Floor.", "[[File:SpeedRunBadge.png|frameless]]"],
    "The Floor Is Lava Winner": ["Complete The Floor Is Lava floor.", "[[File:TheFloorIsLavaBadge.png|frameless]]"],
    "Featured Floor: Fidget Spinner": ["Wait until the Fidget Spinner Floor.", "[[File:FidgetSpinnerBadge.png|frameless]]"],
    "Featured Floor: PPAP": ["'''(Unobtainable)''' Wait until the PPAP floor, which was removed.", ""],
    "Fan": ["Buy any shirt (not pants) from Murfy's Law.", "[[File:FanBadge.png|frameless]]"],
    "Floor 1000": ["Wait until the elevator reaches floor 1,000.", "[[File:floor1000.png|frameless]]"],
    "Floor 5000": ["Wait until the elevator reaches floor 5,000.", "[[File:floor5000.png|frameless]]"],
    "Floor 10000": ["Wait until the elevator reaches floor 10,000.", "[[File:floor10000.png|frameless]]"],
    "Floor 50000": ["Wait until the elevator reaches floor 50,000.", "[[File:floor50000.png|frameless]]"],
    "Floor 100K": ["Wait until the elevator reaches floor 100,000.", "[[File:floor100k.png|frameless]]"],
    "Floor 500K": ["Wait until the elevator reaches floor 500,000.", "[[File:floor500k.png|frameless]]"],
    "Floor 1M": ["Wait until the elevator reaches floor 1,000,000.", "[[File:floor1m.png|frameless]]"],
    "Floor 0": ["If an admin clicks the Floor 0 button on their screen, you'll get the badge.", "[[File:floor0.png|frameless]]"],
    "The Cheapest Game Pass": ["Buy [[Badges/The Cheapest Game Pass|The Cheapest Game Pass]] for 1 robux.", "[[File:WelcomeBadge.png|frameless]]"],
    "100K+ Visits": ["'''(Unobtainable)''' Visit the game when it was between 100K and 200K visits.", ""],
    "500K+ Visits": ["'''(Unobtainable)''' Visit the game when it was between 500K and 600K visits.", ""],
    "1M+ Visits": ["'''(Unobtainable)''' Visit the game when it was between 1M and 1.1M visits.", ""],
    "To Infinity and Beyond!": ["Find something to help you reach ''great heights'' and use it to fly ''beyond the elevator''...", "[[File:toinfinitybadge.png|frameless]]"],
    "Speed Run Insane Winner": ["Finish the [[Speed Run Insane]] parkour. You need to be first there to get the badge.", "[[File:speedruninsane.png|frameless]]"],
    "The Final Countdown": ["Only Ferb or Milo can activate it - the countdown destroys the server.", "[[File:finalcountdown.png|frameless]]"],
    "Ultra Secret Floor": ["No way to get it other than playing and hoping!", "[[File:ultrasecretbadge.png|frameless]]"],
    "####### ########": ["If you ###### ### #### to the #########, you can go to #### ###### and find the #############.", "[[File:secretbadge.png|frameless]]"],
    "Never gonna give you up": ["Wait for the [[Never Gonna Give You Up]] floor.", "[[File:nevergonnabadge.png|frameless]]"],
    "10M Visits": ["'''(Unobtainable)''' Visit the game when it was between 10M and 10.3M visits.", ""],
    "Old Lobby": ["Wait for the [[Dark Lobby]] floor, which only spawns at floor 1111.", ""],
    "literally nothing": ["Wait for the [[literally nothing]] floor.", ""],
    "Very Rare Floor": ["Wait for the [[Crossroads]] floor.", ""],
    "Rooftop": ["Wait for the [[Rooftop]] floor.", ""],
    "Parkour Floor Winner": ["Complete the [[Parkour]] floor.", ""],
    "Speed Run Floor Winner +": ["Complete the [[Speed Run]] floor while at floor 10,000 or above.", ""],
    "The Floor Is Lava Winner +": ["Complete the [[The Floor Is Lava|Floor Is Lava]] floor while at floor 10,000 or above.", ""],
    "Glass Jump Floor Winner": ["Complete the [[Glass Jump]] floor.", ""],
    "Laser Floor Winner": ["Complete the [[Laser Floor]].", ""],
    "Laser Floor Winner +": ["Complete the [[Laser Floor]] while at floor 10,000 or above.", ""],
    "Laser Floor Winner ++": ["Complete the [[Laser Floor]] while at floor 100,000 or above.", ""],
    "Laser Floor Winner +++": ["Complete the [[Laser Floor]] while at floor 1,000,000 or above.", ""],
    "The Floor Is Lava Winner ++": ["Complete the [[The Floor Is Lava|Floor Is Lava]] floor while at floor 50,000 or above.", ""],
    "The Floor Is Lava Winner +++": ["Complete the [[The Floor Is Lava|Floor Is Lava]] floor while at floor 100,000 or above.", ""],
    "Nostalgia Run Winner": ["Complete the [[Nostalgia Run]] floor.", ""],
    "The Truth": ["Just like the name says. Find it.", ""],
    "Speed Run Extreme Winner": ["Complete the [[Speed Run Extreme]] floor.", ""],
    "11M Visits": ["Visit the game for three weeks after hitting 11M visits. ", ""],
    "12M Visits": ["'''(Future Badge)''' Visit the game when it reaches 12M visits.", ""],
    "13M Visits": ["'''(Future Badge)''' Visit the game when it reaches 13M visits.", ""],
    "14M Visits": ["'''(Future Badge)''' Visit the game when it reaches 14M visits.", ""],
    "15M Visits": ["'''(Future Badge)''' Visit the game when it reaches 15M visits.", ""],
}

for badge_num, badge in enumerate(badges_array):
    if how_to_obtain_dict[badge["name"]][1] == "":
        image_link = "[" + badges_img_array[badge_num]["imageUrl"] + "]"
    else:
        image_link = how_to_obtain_dict[badge["name"]][1]

    badge_table += f"""|-
|{image_link}
|'''[[Badges/{badge["name"]}|{badge["name"]}]]'''
|{badge["description"]}
|{str(round(badge["statistics"]["winRatePercentage"]*100, 1))}%
|{str(badge["statistics"]["awardedCount"])}
|{how_to_obtain_dict[badge["name"]][0]}
"""


badge_table += "|}"

f = open('output.txt', 'w', encoding='utf-8')
f.write(badge_table)
f.close()
