import os

# 수정할 부분은 위아래로 ----------이 있음.
# 파일 디렉터리 선언
f_dir = './algorithm_study/code_up/Python 기초 100제'

# 합친 내용을 작성할 파일 열기
# ----------------------------------------
to_write_f = open(f_dir+'/prob_기초-비교연산.py', 'a', encoding='utf8')
# ----------------------------------------

# 위에서 선언한 디렉터리 내의 파일명 탐색
for f_name in os.listdir(f_dir):
    # 파일명이 prob_로 시작하는지 확인
    if f_name.startswith('prob_'):
        f_num = f_name[5:9]

        # prob_ 이후에 숫자가 나오지 않으면 다음 파일 진행
        if not f_num.isdecimal(): continue
        else: f_num = int(f_num)  # 숫자가 맞다면 숫자 타입으로 변경
        
        # 합치려는 파일의 테마와 맞는 번호의 문제인지 확인
        # ----------------------------------------
        if f_num in list(range(6048, 6051)):
        # ----------------------------------------
            f_title = f_name[10:-3]
            to_copy = open(f_dir+'/'+f_name, 'r', encoding='utf8')  # 복사할 파일 열기
            lines = to_copy.read()
            lines = f'#---------- {f_num} {f_title} ----------\n{lines}\n\n'

            to_write_f.write(lines)
            to_copy.close()

# 모두 작성 후 파일 닫기
to_write_f.close()