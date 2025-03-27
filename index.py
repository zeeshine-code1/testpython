menus = [
    {
        "name": "Margherita Pizza",
        "description": "Classic pizza with fresh mozzarella, tomatoes, and basil.",
        "price": 8.99
    },
    {
        "name": "Caesar Salad",
        "description": "Crisp romaine lettuce with Caesar dressing, croutons, and parmesan cheese.",
        "price": 7.49
    },
    {
        "name": "Spaghetti Carbonara",
        "description": "Traditional Italian pasta with creamy egg sauce, pancetta, and parmesan.",
        "price": 12.99
    },
    {
        "name": "Grilled Salmon",
        "description": "Fresh salmon fillet grilled to perfection, served with lemon butter sauce.",
        "price": 15.99
    },
    {
        "name": "Chicken Tikka Masala",
        "description": "Tender chicken pieces cooked in a rich and creamy tomato sauce.",
        "price": 13.49
    },
    {
        "name": "Beef Burger",
        "description": "Juicy beef patty with lettuce, tomato, cheese, and special sauce.",
        "price": 9.99
    },
    {
        "name": "Vegetable Stir Fry",
        "description": "Mixed vegetables stir-fried with soy sauce and sesame oil.",
        "price": 10.49
    },
    {
        "name": "Lobster Bisque",
        "description": "Creamy and rich lobster soup with a hint of sherry.",
        "price": 11.99
    },
    {
        "name": "Chocolate Lava Cake",
        "description": "Warm chocolate cake with a gooey molten center.",
        "price": 6.99
    },
    {
        "name": "Mango Smoothie",
        "description": "Refreshing smoothie made with ripe mangoes and yogurt.",
        "price": 4.99
    }
]

import openai
import os

# Set your OpenAI API key
OPENAI_API_KEY = "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"  # Replace with your actual API key

# Ensure the OpenAI API key is set
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat_with_openai():
    conversation_history = [{"role": "system", "content": "You are a restaurant AI assistant designed to provide information strictly about X-Restaurant. You will only answer questions related to the restaurant, including its menu, operating hours, location, reservations, pricing, dietary options, special offers, and policies. If a question is unrelated to the restaurant, politely inform the user that you can only provide restaurant-related details and do not engage with off-topic inquiries. Keep responses accurate, concise, and professional.."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! 👋")
            break

        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Get AI response
        response = client.chat.completions.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if needed
            messages=conversation_history
        )

        assistant_reply = response.choices[0].message.content
        print("X-Restaurant:", assistant_reply)

        # Append AI response to history
        conversation_history.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    chat_with_openai()
