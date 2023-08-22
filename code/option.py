
def Answer_outPut():
    summary_output_options = {
    "find_person": """
    - Find the person who has the conversation with the customer
    - return the customer name in the json format
    - return the sales person name in the json format

    """,
    'one_sentence' : """
     - Only one sentence
    """,

    'bullet_points': """
     - Bullet point format
     - Separate each bullet point with a new line
     - Each bullet point should be concise
    """,

    'short' : """
     - A few short sentences
     - Do not go longer than 4-5 sentences
    """,

    'long' : """
     - A verbose summary
     - You may do a few paragraphs to describe the transcript if needed
    """,
    'sentiment': """
     - Sentiment: Your task is to classify its sentiment as positive, neutral, or negative.
     - Reason: Your task is to classify the reason for the sentiment.
""",
    'extraction':"""
    - your task is to find out the title  of the conversation between the customer and sale person.
    """,
   'action_item' : """
    - your task is to find out the actions item in the conversation in the following format:
    1. Action item for  Customer Care Executive
    2. Action item  for caller
    3. Action item  for  Customer Care Represatative   
   # Exampe:
   { Action items:
      {
      "actor": "Customer Care Executive",
    "action":  Action item 1
     },
    {
  "actor": "caller",
   "action":  Action item 2
   } 
   }


    - Return Action items  in the json format for 1,2,3
       
       
    """
    }
    return  summary_output_options