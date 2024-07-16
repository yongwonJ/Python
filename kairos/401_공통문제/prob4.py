import requests
import pathlib as Path

path = Path('list.txt') # 같은 경로인데도 안읽혀요...

#splitline -> 리스트로 만들고 -> for문으로 lstrip -> "\n".join(contents) -> 오버라이트 하기

contents
for i in len(path):
    contents[i].lstrip()


new_contents = "\n".join(contents)

with open("w") as File:
    File.write(new_contents)
