import slack_sdk

def main():
  bot_user_oauth_token = 'Bot User OAuth Token'

  client = slack_sdk.WebClient(token=bot_user_oauth_token)

  # 일반 메시지 전송
  slack_msg = f'테스트 메시지 전송' 
  response = client.chat_postMessage(
      channel="private-캠핑-알림",
      text=slack_msg
  )
  
  # 맨션으로 전송
  user_id = "dchkang83"
  slack_msg = f'<@{user_id}> 맨션으로 테스트 메시지 전송'
  response = client.chat_postMessage(
      channel="private-캠핑-알림",
      text=slack_msg
  )

if __name__ == '__main__':
    main()