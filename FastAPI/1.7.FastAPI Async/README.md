# Async API

This Async API provides asynchronous endpoints for accessing various functionalities related to word rhyming and geographical information retrieval. It offers two distinct functionalities.

1. Rhyme Finder: Allows users to find rhymes for a given word.
2. Geographical Information Retrieval:

- - City Finder: Enables users to find cities within a specific state by providing its ID.
- - Latitude and Longitude Finder: Provides latitude and longitude coordinates for a given city.

In this program, `argparse` library is used to receive input.
you can run program by this command:

```
python3 main.py --message1 {word_for_rhyme} --message2 {your_state} --message3 {your_city}
```

for example: `python3 main.py --message1 رفت --message2 تهران --message3 تهران`
