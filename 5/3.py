# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes


import string

hashtag = input('Enter raw string: ')
pun = string.punctuation
for i in pun:
    if i in hashtag:
        hashtag = hashtag.replace(i, ' ')
hashtag = hashtag.title().replace(' ', '')
print(hashtag)

print(f'#{hashtag[:139]}')