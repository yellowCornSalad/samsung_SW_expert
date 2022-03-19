T = str(input("문자열을 입력해주세요."))
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def test_case_reverse(T):
    for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
        return T[:: -1]

def if_palindrome(T):
    if T == test_case_reverse(T):
        return '회문(Palindrome)입니다.'
    else:
        return '회문이 아닙니다.'

# def main(T):
print(if_palindrome(T))