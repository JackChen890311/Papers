# To-Do
```dataview
TABLE file.mtime as "Last Modified"
FROM "Non-Papers"
WHERE todo = True
SORT file.mtime DESC
```

# All
```dataview
TABLE tags as Tags, summary AS Summary, file.mtime as "Last Modified"
FROM "Non-Papers"
SORT file.mtime DESC
```










