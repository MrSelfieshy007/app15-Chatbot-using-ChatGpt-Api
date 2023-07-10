import openai


class Chatbot:
    def __init__(self):
        # openai.api_key = "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"
        # openai.api_key = "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"
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
