# Fake-Robux-Tool-GUI
C# + PYTHON


- playwright 로 html 값 수정하는 원리라 exe 빌드 후 크롬.exe 파일을 찾을 수 없다고 뜨면 빌드 된 폴더에 들어가서
- lib\playwright\driver\package 경로에  '.local-browsers\chromium-XXXX'\chrome-win\chrome.exe 를 추가하면 되는데 여기서 크로미옴-XXXX 에서 XXXX는 버전에 맞게 폴더 만들면 됨
- 그리고 크로미옴 zip 파일로 다운로드 받아서 chromium-xxxx 폴더 안에 압축만 풀어주면 됨

- 나 같은 경우 cx_freeze 로 파이썬 소스를 exe로 변환시켜서 pyinstaller 이나 cx_freeze 둘 중 아무거나 빌드 해서 사용해주면 되는데 pyinstaller 은 원파일로 빌드하면 오류 나니까 꼭 playwright 폴더가 생기게 같이 빌드 해줘야 함
- pyinstaller 로 빌드해도 위 같은 에러는 똑같은 방법으로 처리 시켜 주면 됨


- 녹화본임[https://youtu.be/dcLJMXo6F4k] 나중에 사기도 칠 수 있을지도?
