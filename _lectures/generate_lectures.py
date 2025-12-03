import pandas


df = pandas.read_csv("lectures.csv")

for i, row in df.iterrows():
    base = f"""---
type: lecture
date: {row['date']}
title: {row['lecture']}
lecture_type: {row['lecture_type']}
thumbnail: /static_files/presentations/lec.jpg
hide_from_calendar: false
"""

    base += "links:\n"
    if isinstance(row["slides"], str):
        base += f"- url: {row['slides']}\n  name: slides\n"

    if isinstance(row["notebooks"], str):
        if "," not in row["notebooks"]:
            base += f"- url: {row['notebooks']}\n  name: notebook\n"
        else:
            for i, notebook in enumerate(row["notebooks"].split(",")):
                base += f"- url: {notebook}\n  name: notebook {i}\n"

    # need a newline
    base += "hide_from_announcments: true\n---"
    
    if isinstance(row["notes"], str):
        base += f"\n\n{row['notes']}"
    
    with open(f"{i}_lecture.md", "w") as log:
        log.write(base)
