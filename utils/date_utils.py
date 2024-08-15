from datetime import datetime, timedelta

def get_today_date():
    """
    오늘 날짜를 'YYYY-MM-DD' 형식의 문자열로 반환합니다.
    
    Returns:
        str: 오늘 날짜 문자열
    """
    return datetime.now().strftime('%Y-%m-%d')

def get_yesterday_date():
    """
    어제 날짜를 'YYYY-MM-DD' 형식의 문자열로 반환합니다.
    
    Returns:
        str: 어제 날짜 문자열
    """
    return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

def is_weekend(date_str):
    """
    주어진 날짜가 주말인지 확인합니다.
    
    Args:
        date_str (str): 'YYYY-MM-DD' 형식의 날짜 문자열
    
    Returns:
        bool: 주말이면 True, 아니면 False
    """
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5  # 5는 토요일, 6은 일요일

def get_next_business_day(date_str):
    """
    주어진 날짜의 다음 영업일을 반환합니다. 주말이면 다음 월요일을 반환합니다.
    
    Args:
        date_str (str): 'YYYY-MM-DD' 형식의 날짜 문자열
    
    Returns:
        str: 다음 영업일의 'YYYY-MM-DD' 형식 문자열
    """
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_day = date + timedelta(days=1)
    while next_day.weekday() >= 5:  # 주말이면 다음 날로
        next_day += timedelta(days=1)
    return next_day.strftime('%Y-%m-%d')