import requests
import time
import os
import dotenv
import asyncio
import argparse


async def rhyme_finder(message):
    user_text = f'{message}'

    url = f"https://rhyming.ir/api/rhyme-finder?api={rhyme_API_key}&w={user_text}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)

    rhymes = response.json()['data_items']
    for rhyme in rhymes:
        print("\n", rhyme)


def get_states(message):
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)

    print("List of states --------------------")
    states = response.json()
    user_state = f'{message}'
    for state in states:
        print("\n", state)
        if state['name'] == user_state:
            print(state['id'])
            state_id = state['id']

    return state_id


def get_cities(message, state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)

    print("List if cities --------------------")
    cities = response.json()
    user_city = f'{message}'
    for city in cities:
        print("\n", city)
        if city['name'] == user_city:
            print("Your city found: ")
            print("Latitude : ", city['latitude'])
            print("Longitude : ", city['longitude'])
            break
        else:
            print("Not found")


async def get_coordinates(message2, message3):
    state_id = get_states(message2)
    get_cities(message3, state_id)


async def main():
    parser = argparse.ArgumentParser(
        description="This code get text from user and find rhymes, find states and cities.")
    parser.add_argument("--message1", type=str, help="enter your text")
    parser.add_argument("--message2", type=str)
    parser.add_argument("--message3", type=str)

    args = parser.parse_args()

    await asyncio.gather(rhyme_finder(args.message1), get_coordinates(args.message2, args.message3))
    print("main ended")


if __name__ == "__main__":
    start_time = time.perf_counter()

    dotenv = dotenv.load_dotenv()

    rhyme_API_key = os.getenv('API_KEY')

    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Total time: {total_time} seconds")
