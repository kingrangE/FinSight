from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
from scripts.db_operations import get_today_recommendations

def send_slack_message(message):
    """Slack 메시지를 전송하는 함수"""
    slack_token = "YOUR_SLACK_BOT_TOKEN"  # 실제 토큰으로 교체 필요
    client = WebClient(token=slack_token)
    
    try:
        response = client.chat_postMessage(
            channel="YOUR_CHANNEL_ID",  # 실제 채널 ID로 교체 필요
            text=message
        )
        print(f"Message sent: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message: {e}")

def send_newsletter():
    """오늘의 추천 내용을 Slack으로 전송하는 함수"""
    recommendations = get_today_recommendations()
    today = datetime.now().strftime("%Y-%m-%d")
    
    message = f"오늘 {today} 매수 추천:\n"
    for _, row in recommendations.iterrows():
        if row['Recommendation'] == "매수":
            message += f"{row['Symbol']}, "
    
    message = message.rstrip(', ')  # 마지막 쉼표와 공백 제거
    send_slack_message(message)

if __name__ == "__main__":
    send_newsletter()