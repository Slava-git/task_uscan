from dotenv import load_dotenv

load_dotenv()


class Settings:
    database_url: str = "postgresql://slava:password@db:5432/myscan"
    default_temperature: float = 0.7
    model_name: str = "gpt-3.5-turbo"

    prompt_template: str = """You are helpful assistant. Your aim is to answer user's question based on the context is given to you.

    User's note:
    {context}

    Remember to maintain a helpful tone in your response.

    Question: {question}
    """


settings = Settings()
