import re

def clean_html(raw_html):
    """
    HTML 태그를 제거하고 순수한 텍스트만 추출합니다.
    
    Args:
        raw_html (str): HTML이 포함된 문자열
    
    Returns:
        str: HTML 태그가 제거된 순수한 텍스트
    """
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def truncate_string(string, length):
    """
    긴 문자열을 주어진 길이로 자르고 '...'를 추가합니다.
    
    Args:
        string (str): 원본 문자열
        length (int): 자를 길이
    
    Returns:
        str: 잘린 문자열
    """
    return string[:length] + '...' if len(string) > length else string

def format_number(number):
    """
    숫자를 천 단위로 쉼표를 넣어 포맷팅합니다.
    
    Args:
        number (int or float): 포맷팅할 숫자
    
    Returns:
        str: 포맷팅된 숫자 문자열
    """
    return f"{number:,}"

def sanitize_filename(filename):
    """
    파일 이름에서 유효하지 않은 문자를 제거합니다.
    
    Args:
        filename (str): 원본 파일 이름
    
    Returns:
        str: 유효한 문자로만 구성된 파일 이름
    """
    return re.sub(r'[^\w\-_\. ]', '', filename)