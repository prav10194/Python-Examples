## Match title with the given list of job titles.

<b>Solution: 

 ```python
raw_title = "Software Dev from Tokyo"
clean_titles = ["Product Manager", "Biology Professor", "Software Engineer", "Software Developer"]

maxWordsMatched = 0
titleMatched = ""

for title in clean_titles:
    tempWordsMatched = len(set(raw_title.lower().split(" ")) & set(title.lower().split(" ")))
    if tempWordsMatched > maxWordsMatched:
        maxWordsMatched = tempWordsMatched
        titleMatched = title
# print(set(raw_title.lower().split(" ")) & set("Dev from".lower().split(" ")))
print(titleMatched)
 ```

</b>


