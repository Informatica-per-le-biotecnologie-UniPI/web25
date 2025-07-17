import pandas


df = pandas.read_csv("lectures.csv")

for i, row in df.iterrows():
    base = f"""---
type: lecture
date: {row['date']}
title: {row['lecture']}
thumbnail: /static_files/presentations/lec.jpg
"""

    base += "links:"
    if isinstance(row["slides"], str):
        base += f"""
    - url: {row['slides']}
      name: slides
    """

    if isinstance(row["notebooks"], str):
        base += f"""
    - url: {row['slides']}
      name: notebook
    """

    base += "\nhide_from_announcments: true\n---"
    
    if isinstance(row["notes"], str):
        base += f"\n\n{row['notes']}"
    
    with open(f"{i}_lecture.md", "w") as log:
        log.write(base)
