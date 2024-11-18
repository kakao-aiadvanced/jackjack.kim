**Download**
1. https://github.com/ollama/ollama 접속
2. macOS 버전 다운로드 후 설치

Reference: https://github.com/ollama/ollama/blob/main/README.md



**Quickstart**

터미널에서 아래를 입력하면, 모델을 다운로드 하고 실행합니다. (on terminal):

```
ollama run llama3
```




Terminal에 Send a message (/? for help) 메시지가 출력 되면 성공적으로 설치 / 실행된 것입니다.

`Send a message (/? for help)`

프롬프트를 입력하고 결과를 확인해보세요.

**Customization**

Prompt 를 통해 model 을 customize 해보고 (예: Temperature) 동일한 prompt 를 반복적으로 입력했을 때 전후 실행 결과를 비교해보세요.

`ollama pull llama3`


```
FROM llama3

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```



```
ollama create mario -f ./Modelfile
ollama run mario
>>> hi
Hello! It's your friend Mario.
```