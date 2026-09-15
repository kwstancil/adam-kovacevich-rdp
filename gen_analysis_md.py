import json
from collections import OrderedDict

ORDER = [
    "Appointments / philosophy critique",
    "Hypocrisy / selective outrage",
    "Jeff Hauser / The Groups",
    "Funding transparency & donors",
    "Purity tests & Dem coalition",
    "Report on Dems vs tech",
]

with open('adamkovac_rdp_tweets.json', 'r', encoding='utf-8') as f:
    tweets = json.load(f)

def fmt_date(iso):
    return iso.replace('T', ' ').rstrip('Z').replace('.000', ' UTC')

lines = []
lines.append("# Categorical Analysis: Kovacevich's Tweets on the Revolving Door Project & Jeff Hauser\n")

counts = OrderedDict()
for c in ORDER:
    counts[c] = sum(1 for t in tweets if t['category'] == c)

lines.append(f"**26 tweets** (2021-09-30 → 2026-06-29) from [@adamkovac](https://x.com/adamkovac) referencing the Revolving Door Project and/or Jeff Hauser.\n")
lines.append("## Summary\n")
lines.append("| # | Category | Tweets |")
lines.append("|---:|---|---|")
for i, (c, n) in enumerate(counts.items(), 1):
    lines.append(f"| {i} | {c} | {n} |")
lines.append("")

for c in ORDER:
    n = counts[c]
    lines.append(f"## {c} ({n})\n")
    ctweets = [t for t in tweets if t['category'] == c]
    for t in ctweets:
        lines.append(f"### {t['id']} · {fmt_date(t['created_at'])}")
        lines.append(f"- **URL:** {t['url']}")
        lines.append(f"- **Matched query:** {t['matched_query']}")
        lines.append(f"")
        lines.append("> " + t['full_text'].replace('\n', '\n> ') + "\n")
    lines.append("")

with open('CATEGORY_ANALYSIS.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print("Wrote CATEGORY_ANALYSIS.md")
print("Word count:", sum(len(l.split()) for l in lines))