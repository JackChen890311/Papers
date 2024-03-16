# Papers (Sort by Time)
```dataview
TABLE time AS Publish, tags as Tags, summary AS Summary
FROM "Papers"
WHERE time > 0 and !contains(tags, "Survey")
SORT time DESC
```

# Surveys (Sort by Time)
```dataview
TABLE time AS Publish, tags as Tags, summary AS Summary
FROM "Papers"
WHERE time > 0 and contains(tags, "Survey")
SORT time DESC
```
