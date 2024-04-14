# Fake-Robux-Tool-GUI
C# + PYTHON

**나는 바이러스 심거나 사기치라고 얘기 안 함 알아서 수정해서 써도 되는데 괜히 했다가 대부분은 안 그런데 간혹가다 깐깐한 잼민이 한테 걸려서 경찰서 가거나 해도 내 책임 아님 ㅋ**

*재미로만 알아서 적당히 가지고 놀아요*


```
# pyinstaller 또는 cx_freeze 로 파이썬 소스 exe 로 빌드하고 실행 했을때 특정 경로 폴더에 chrome.exe 또는 타 브라우저 실행 파일이 없다고 뜨는 playwright 에러가 뜨면 밑에 방법으로 해결하면 됨

# 오류가 뜰 수 있으니 cmd에 빌드한이름.exe 에 (exe이름).exe  만 치면 exe 실행되니까 오류 확인 하면 되고 모르겠으면 여기다 질문


이해 안가면 https://youtu.be/bw9PMLsV3n4 참고하셈 cx_freeze 로 빌드하는거 부터 오류 해결까지 영상으로 담아놓음


- playwright 로 html 값 수정하는 원리라 exe 빌드 후 크롬.exe 파일을 찾을 수 없다고 뜨면 빌드 된 폴더에 들어가서
- lib\playwright\driver\package 경로에  '.local-browsers\chromium-XXXX'\chrome-win\chrome.exe 를 추가하면 되는데 여기서 크로미옴-XXXX 에서 XXXX는 버전에 맞게 폴더 만들면 됨
- 그리고 크로미옴 zip 파일로 다운로드 받아서 chromium-xxxx 폴더 안에 압축만 풀어주면 됨

- 나 같은 경우 cx_freeze 로 파이썬 소스를 exe로 변환시켜서 pyinstaller 이나 cx_freeze 둘 중 아무거나 빌드 해서 사용해주면 되는데 pyinstaller 은 원파일로 빌드하면 오류 나니까 꼭 playwright 폴더가 생기게 같이 빌드 해줘야 함
- pyinstaller 로 빌드해도 위 같은 에러는 똑같은 방법으로 처리 시켜 주면 됨


```


- https://youtu.be/dcLJMXo6F4k 나중에 사기도 칠 수 있을지도?
