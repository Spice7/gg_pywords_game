import os
import random
import time
from pygame import mixer

# 필요 데이터 초기화
os.environ["SDL_AUDIODRIVER"] = "pulseaudio"
words = []      # 단어 리스트   
qstAmount = 5   # 몇 문제
fadeTime = 1.5  # 사라지는 시간

mixer.init()    # mixer 초기화
correctSound = mixer.Sound('assets/good.wav')
incorrectSound = mixer.Sound('assets/bad.wav')

# 단어파일 로드 함수
def wordLoad(lst):
    with open('data/word.txt', "r") as file:
        for word in file:
            lst.append(word.strip())

# 게임 실행 함수
def gameRun():
    correctAnswer = 0   # 정답 수
    elapsedTime = 0.0   # 경과 시간
    qstList = random.sample(words, k = qstAmount)       # 문제 개수만큼 랜덤으로 생성   # 중복방지 포함

    # 단어 전체를 먼저 보여줌
    print(words)

    # 게임 시작 안내
    input("준비? 엔터를 입력하세요\n")
    startTime = time.time()     # 시간 측정 시작

    for i in range(qstAmount):
        answer = qstList[i]

        print(f"Question #{i + 1}")
        print(answer)
        time.sleep(fadeTime)
        print("\033[s" + "\033[1A" + "\033[2K" + "\033[u", end="", flush=True)      # 콘솔창 커서 한 줄 위의 내용을 지우고 기존 위치로 돌아옴

        userSubmit = input()

        if(userSubmit == answer):
            print("정답")
            correctSound.play()
            correctAnswer += 1
            print()

        else:
            print("오답")
            incorrectSound.play()
            print()

    endTime = time.time()       # 시간 측정 종료
    elapsedTime = endTime - startTime

    scorePrint(correctAnswer, elapsedTime)
    saveResult(correctAnswer, elapsedTime)


# 게임 결과 출력
def scorePrint(correctAnswer, time):
    if correctAnswer >= 3:
        print("합격했습니다")
    else:
        print("불합격했습니다")

    print(f"게임 걸린시간: {time:.2f}초, 맞춘 개수: {correctAnswer}개")
    

# 게임 결과 저장
def saveResult(correctAnswer, time):
    lineCount = 0   # 몇 줄 작성되어 있는지

    with open("word_game_score.csv", "r", encoding='utf-8') as file:
        lineCount = sum(1 for _ in file)        

    with open("word_game_score.csv", "a", encoding='utf-8') as file:
        file.write(f"[{lineCount + 1}] 게임시간: {time:.2f}초, 맞춘 개수: {correctAnswer}개 [[하드모드]]\n")


wordLoad(words)
gameRun()


