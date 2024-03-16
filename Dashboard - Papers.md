# To-Do
```dataview
TABLE title AS Title, file.mtime as "Last Modified"
FROM "Papers"
WHERE todo = True
SORT file.mtime DESC
```

# Scanned Recently
```dataview
TABLE title AS Title, file.mtime as "Last Modified"
FROM "Papers"
WHERE scanned = True and read = False
SORT file.mtime DESC
```

# Read Recently
```dataview
TABLE title AS Title, file.mtime as "Last Modified"
FROM "Papers"
WHERE read = True
SORT file.mtime DESC
```
# [[Dashboard - Papers (Detailed View)]]