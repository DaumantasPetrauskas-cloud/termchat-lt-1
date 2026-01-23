import openai
from termAi.models import SimpleChatBot
from termAi.data_collector import ChatLogger

# Configuration for the API
client = openai.OpenAI(
    api_key="YOUR_API_KEY",  # Replace with your actual key
    base_url="https://api.openai.com/v1"
)

# Initialize local AI and logger
local_bot = SimpleChatBot()
logger = ChatLogger()

def get_ai_response(user_message, use_api=True):
    try:
        if use_api:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are TermAi, a helpful assistant in TermChat LT."},
                    {"role": "user", "content": user_message}
                ]
            )
            ai_response = response.choices[0].message.content
        else:
            # Use local termAi library
            ai_response = local_bot.think(user_message)
        
        # Log interaction for training
        logger.log_interaction(user_message, ai_response)
        return ai_response
        
    except Exception as e:
        return f"Error: {str(e)}"