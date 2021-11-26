#sys모듈
#명령행(cmd창 - 명령프롬프트 Terminal)에서 인수 전달하기
import sys

args = sys.argv[1:] #리스트 1번부터 끝까지 슬라이싱(자료추출)
print(args)
#Terminal창에서 cd day07(파이썬 파일이 있는 위치까지 간 다음)
                #python sys_ex.py 다음에(인덱스0) 원하는 인수 입력하면 리스트로 출력