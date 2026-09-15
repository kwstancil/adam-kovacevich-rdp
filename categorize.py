import json
import csv

CATEGORIES = {
    "1443627978768982022": "Hypocrisy / selective outrage",
    "1841569321103065401": "Appointments / philosophy critique",
    "1841569442851115460": "Appointments / philosophy critique",
    "1846185690486186193": "Appointments / philosophy critique",
    "1846198531792503289": "Appointments / philosophy critique",
    "1846713591430631502": "Hypocrisy / selective outrage",
    "1849053820870971766": "Jeff Hauser / The Groups",
    "1849100459291681008": "Purity tests & Dem coalition",
    "1857494646634512604": "Purity tests & Dem coalition",
    "1861506374880108945": "Hypocrisy / selective outrage",
    "1867568303444488445": "Hypocrisy / selective outrage",
    "1868411616678834215": "Hypocrisy / selective outrage",
    "1895528691431830012": "Hypocrisy / selective outrage",
    "1906877926169317818": "Hypocrisy / selective outrage",
    "1920139885597405456": "Funding transparency & donors",
    "1928538179109531930": "Jeff Hauser / The Groups",
    "1932510705481023584": "Jeff Hauser / The Groups",
    "1932894004594762032": "Funding transparency & donors",
    "1944833369319121355": "Jeff Hauser / The Groups",
    "1965209132065325107": "Jeff Hauser / The Groups",
    "1998770205393404032": "Appointments / philosophy critique",
    "2009734430189822173": "Purity tests & Dem coalition",
    "2021285980347457895": "Funding transparency & donors",
    "2059961572014100538": "Report on Dems vs tech",
    "2060403000955269272": "Purity tests & Dem coalition",
    "2071662600442503520": "Funding transparency & donors",
}

with open('adamkovac_rdp_tweets.json', 'r', encoding='utf-8') as f:
    tweets = json.load(f)

for t in tweets:
    t['category'] = CATEGORIES.get(t['id'], 'Uncategorized')

with open('adamkovac_rdp_tweets.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, indent=2, ensure_ascii=False)

with open('adamkovac_rdp_tweets.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'created_at', 'full_text', 'url', 'matched_query', 'category'])
    writer.writeheader()
    writer.writerows(tweets)

from collections import Counter, OrderedDict
order = [
    "Appointments / philosophy critique",
    "Hypocrisy / selective outrage",
    "Jeff Hauser / The Groups",
    "Funding transparency & donors",
    "Purity tests & Dem coalition",
    "Report on Dems vs tech",
]
counts = Counter(t['category'] for t in tweets)
print("CATEGORY COUNTS:")
for c in order:
    print(f"  {counts[c]:2d}  {c}")

print("\nPER-CATEGORY TWEETS:")
for c in order:
    print(f"\n== {c} ({counts[c]}) ==")
    for t in tweets:
        if t['category'] == c:
            print(f"   [{t['id']}] {t['full_text'][:100]!r}")