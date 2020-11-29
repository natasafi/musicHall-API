# Since I did not manage to define the relationship of an artist to their songs from the consumption of the
# third-party I thought I could give it a go to json manipulation with a stubbed object.

import json
import re

filename = "lyrics1.json"
word_count = 0

# define the word count
with open(filename, 'r') as file:
    json_dict = json.load(file)

    for i in json_dict:
        lyrics = str(json_dict["lyrics"])
        replaced_strings_array = re.sub(r'\W+', ' ', lyrics).lower().strip().split(" ")
        print(len(replaced_strings_array))

        # define most common words
        counter = {}
        for word in replaced_strings_array:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        print(sorted(counter, reverse=True))
