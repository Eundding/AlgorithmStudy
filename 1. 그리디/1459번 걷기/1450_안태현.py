import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

# 2 * w 가 s 보다 작은 경우 -> w만 써서 가도 최소
if 2 * w < s:
    print((x + y) * w) 
else:
  # 대각선을 섞어서 가면 최소
  # 더 작은 값만큼 대각선으로 이동한다
  answer = min(x, y) * s
  
  # 그 후에 w가 s보다 작다면 남은 값(v)만큼 w를 써서 이동
  # s가 w보다 작다면 v 만큼 s를 써서 이동
  # -> v가 홀수라면 목적지 도달 불가능 -> (v-1) * s + w 해줘야 함
  v = abs(x - y)
  if w < s:
    print(answer + v * w)
  else:
    if v % 2 == 0:
      print(answer + v * s)
    else:
      print(answer + (v - 1) * s + w)  
