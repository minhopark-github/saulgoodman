#주피터 노트북은 글꼴이 구려서 가독성이 너무 떨어진다.
#글꼴 바꾸기를 시작하기 전 cmd, jupyter notebook --generater -config
#시작부터 컽 당함. 에러 뜨는데 해결이 잘 안됨.
#주피터 노트북을 이걸로 열면 줄표시가 안되고 창 안에 창이 있다.
#작기도 하거니와 다른것보다 줄 표시가 안된다. 좀 심각해서 그냥 비주얼 스튜디오로. 주피터도 더 해보면 가능은 하겠지만 비주얼 스튜디오가 이미 작업환경이 갖춰졌는데 굳이 그걸 쓸 메리트가 없다.

print("hello world")
a=[i for i in range(1,10)]
try:
    for i in a:
        if i%2==0:
            print(i)
        continue
        print(i)
    print(i)
finally:
    print(i)

# shift enter는 드래그한 영역을 파이썬으로 실행시켜주며 파이썬을 따로 종료시키지 않는 한 같은 명령어로 계속 출력할 수 있다
#shift spacebar는 현재 문서 전체를 실행시키는데 위에서 python이 실행되는 중이면 에러가 뜬다. 폴더를 볼 수 있는 곳으로 나와서 쓰자.

print("메롱")

