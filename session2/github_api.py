import requests


def followers():
    responses = requests.get(
        "https://api.github.com/users/SinaHosseini/followers")
    follower = responses.json()
    print(len(follower))

    for f in range(len(follower)):
        print(follower[f]["login"])


def followings():
    response = requests.get(
        "https://api.github.com/users/SinaHosseini/following")
    following = response.json()
    print(len(following))

    for f in range(len(following)):
        print(following[f]["login"])


if __name__ == "__main__":
    inp = input("enter your request (1.following or 2.followers): ")

    if inp == "1":
        followings()
    elif inp == "2":
        followers()
    else:
        print("mesl adam vared kon.")
