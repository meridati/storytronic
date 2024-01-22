import openai

openai_key = ""
openai.api_key = openai_key

command_input = "Generate a choice based story in the follow format"
data_format = """
{
    "story": {
        "start": {
            "story_segment": "[text]",
            "branch_1": "[choice]",
            "branch_2": "[choice]"
        },
        "branch_1": {
            "story_segment": "[text]",
            "branch_3": "[choice]",
            "branch_4": "[choice]"
        },
        "branch_2": {
            "story_segment": "[text]",
            "branch_5": "[choice]",
            "branch_6": "[choice]"
        }
        // Add more branches 3,4,5 and 6
    }
}
"""

def generate_story(genre, extra_info):
    print('generating story')
    print(extra_info)
    
    gpt_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{command_input} {data_format} Genre: {genre}"
            }
        ]
    )
    
    return gpt_completion

if __name__ == "__main__":
    genre = "your_genre"
    extra_info = "your_extra_info"
    result = generate_story(genre, extra_info)
    print(result)
