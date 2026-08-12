import random
import time
from pygame import mixer

mixer.init()    # mixer 초기화

class WordGame:
    # 속성
    # words = []
    # qstAmount = 0
    # correctSound = None
    # incorrectSound = None

    # 메서드
    def __init__(self):
        self.words = []
        self.wordLoad()
        self.qstAmount = 5
        self.correctSound = mixer.Sound('assets/good.wav')
        self.incorrectSound = mixer.Sound('assets/bad.wav')

    # 단어파일 로드 함수
    def wordLoad(self):
        with open('data/word.txt', "r") as file:
            for word in file:
                self.words.append(word.strip())

    # 게임 실행 함수
    def gameRun(self):
        correctAnswer = 0   # 정답 수
        elapsedTime = 0.0   # 경과 시간
        qstList = random.sample(self.words, k = self.qstAmount)       # 문제 개수만큼 랜덤으로 생성   # 중복방지 포함

        # 단어 전체를 먼저 보여줌
        print(self.words)

        # 게임 시작 안내
        input("준비? 엔터를 입력하세요\n")
        startTime = time.time()     # 시간 측정 시작

        for i in range(self.qstAmount):
            answer = qstList[i]

            print(f"Question #{i + 1}")
            print(answer)

            userSubmit = input()

            if(userSubmit == answer):
                print("정답")
                self.correctSound.play()
                correctAnswer += 1
                print()

            else:
                print("오답")
                self.incorrectSound.play()
                print()

        endTime = time.time()       # 시간 측정 종료
        elapsedTime = endTime - startTime

        self.scorePrint(correctAnswer, elapsedTime)
        self.saveResult(correctAnswer, elapsedTime)


    # 게임 결과 출력
    def scorePrint(self, correctAnswer, time):
        if correctAnswer >= 3:
            print("합격했습니다")
        else:
            print("불합격했습니다")

        print(f"게임 걸린시간: {time:.2f}초, 맞춘 개수: {correctAnswer}개")
    

    # 게임 결과 저장
    # output 폴더에 csv 새로 만들고 저장
    def saveResult(self, correctAnswer, time):
        lineCount = 0   # 몇 줄 작성되어 있는지

        try:
            with open("output/word_game_score.csv", "r", encoding='utf-8') as file:
                lineCount = sum(1 for _ in file)  
        # 파일이 없으면 만들고
        except FileNotFoundError:
            with open("output/word_game_score.csv", "w", encoding='utf-8') as file:
                file.write(f"[{lineCount + 1}] 게임시간: {time:.2f}초, 맞춘 개수: {correctAnswer}개\n")  

        # 파일이 있으면 append
        else:
            with open("output/word_game_score.csv", "a", encoding='utf-8') as file:
                file.write(f"[{lineCount + 1}] 게임시간: {time:.2f}초, 맞춘 개수: {correctAnswer}개\n")

#game = WordGame()
#game.gameRun()


