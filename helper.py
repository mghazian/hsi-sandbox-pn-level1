from distutils import filelist

def get_heading(title):
    print(title)
    words = title.strip().split()
    i = 0
    for word in words:
        if word.find(":") != -1:
            break
        i += 1
    
    if i == len(words):
        return ("", "")
    return (words[i], " ".join(words[i + 1:]))

def format_chapter(index, title, content):
    return f"""## {index}. {title}
### Source code

```python
{content}
```

### Output

![app{index}](./images/{index}.png)

"""

files = filelist.findall(".")
iterator = filter(lambda name: name.find("\\") == -1 and name.find("app") != -1, files)

file_contents = []
for filename in iterator:
    print(f"Start: {filename}")
    order = int(filename[3:filename.find(".")])
    with open(filename, "r") as file:
        content = file.read()
        first_line = content[:content.find("\n")]
        
        timestamp, title = get_heading(first_line)
        file_contents.insert(order, format_chapter(order, title, content))

with open("README.md", "a") as readme:
    readme.writelines(file_contents)