import re

def solution(new_id):
    step1 = new_id.lower()
    step2 = re.sub('[^a-z0-9\.\-\_]+', '', step1)
    step3 = re.sub('[.]+', '.', step2)
    if step3 and step3[0] == '.': step3 = step3[1:]
    if step3 and step3[-1] == '.': step3 = step3[:-1]
    step4 = step3
    if len(step4) == 0: step5 = 'a'
    else: step5 = step4
    if len(step5) >= 16:
        step6 = step5[:15]
        if step6[-1] == '.': step6 = step6[:-1]
    else: step6 = step5
    if len(step6) <= 2:
        while len(step6) != 3:
            step6 += step6[-1]
    return step6