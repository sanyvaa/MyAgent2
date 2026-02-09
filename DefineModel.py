def InitModel():
    from dotenv import load_dotenv
    from agents import OpenAIChatCompletionsModel, AsyncOpenAI
    
    load_dotenv(override=True)

    # Configure the model
    global MyModel
    MyModel = OpenAIChatCompletionsModel( 
        model= "llama3.2",  #"qwen3-vl:4b" "deepseek-r1:1.5b"
        openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1"))
    #MyModel = "gpt-4o-mini"