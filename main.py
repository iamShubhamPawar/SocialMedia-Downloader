import module

asciiart = """
                 
░█▀▀▀█ █▀▀█ █▀▀ ─▀─ █▀▀█ █── ░█▀▄▀█ █▀▀ █▀▀▄ ─▀─ █▀▀█ 　 ░█▀▀▄ █▀▀█ █───█ █▀▀▄ █── █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
─▀▀▀▄▄ █──█ █── ▀█▀ █▄▄█ █── ░█░█░█ █▀▀ █──█ ▀█▀ █▄▄█ 　 ░█─░█ █──█ █▄█▄█ █──█ █── █──█ █▄▄█ █──█ █▀▀ █▄▄▀ 
░█▄▄▄█ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀ ░█──░█ ▀▀▀ ▀▀▀─ ▀▀▀ ▀──▀ 　 ░█▄▄▀ ▀▀▀▀ ─▀─▀─ ▀──▀ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀─▀▀                                                                      
-----------------------------------------------------------------------------------------------
            """

print(asciiart)

def save_image(filename,data):
    """
    Saves the image to the given filename.
    :param filename: The filename to save the image to.
    :param data: The image data.
    """
    with open(filename, "wb") as image_file:
        image_file.write(data)


platform = int(input("[+] From which platform would you like to download media files?:\n1. Instagram\n2. Snapchat\n3. Twitter\nEnter the number to select platform: "))

if platform == 1:
    insta = module.Instagram()
    typ = int(input("\n[+] What would you like to download?\n1. Instagram Profile Pic [320px320p]\n2.Instagram Reels/Videos [Highest Quality]\n3. Instagram Pictures/Images [Highest Quality]\nEnter the number to select operation: "))
    if typ == 1:
        username = input("\n[+] Enter the Instagram Username:")
        img = insta.profilePic(username)
        save_image(f"{username}.jpg",img)
        print(f"\n[+] Instagram Profile Pic for {username} has been downloaded successfully!")
    elif typ == 2:
        url = input("\n[+] Enter the Instagram Reel/Video URL:")
        vid = insta.reels(url)
        save_image(f"{username}.mp4",vid)
        print(f"\n[+] Instagram Reel has been downloaded successfully!")
    elif typ == 3:
        url = input("\n[+] Enter the Instagram Picture/Image URL:")
        img = insta.pic(url)
        save_image(f"{username}.jpg",img)
        print(f"\n[+] Instagram Picture/Image has been downloaded successfully!")
    else:
        print("\n[+] Invalid option!")

elif platform == 2:
    snap = module.Snapchat()
    typ = int(input("\n[+] What would you like to download?\n1. Snapchat Stories [Highest Quality]\n2. Snapchat Spotlight [Highest Quality]\nEnter the number to select operation: "))
    if typ == 1:
        url = input("\n[+] Enter the Snapchat Story URL:")
        snap.downloadStories(url)
        print(f"\n[+] Snapchat Story has been downloaded successfully!")
    elif typ == 2:
        url = input("\n[+] Enter the Snapchat Spotlight URL:")
        snap.downloadSpotlight(url)
        print(f"\n[+] Snapchat Spotlight has been downloaded successfully!")
    else:
        print("\n[+] Invalid option!")

elif typ == 3:
    twit = module.Twitter()
    url = int(input("\n[+] Enter the URL of Twitter post: "))
    twit.getMedia(url)
    print(f"\n[+] Twitter post has been downloaded successfully!")

else:
    print("\n[+] Invalid option!")

