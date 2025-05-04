from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# from typing import TypedDict
from pydantic import BaseModel
from typing import Annotated, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# Schema for data format
# class Review(TypedDict):
# class Review(BaseModel):
#     summary: Annotated[str, "A brief summary of the review content"]
#     sentiment: Annotated[
#         str,
#         "Overall sentiment expressed in the review (e.g., positive, neutral, negative)",
#     ]


class Review(BaseModel):

    key_themes: Annotated[list[str], "All key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review content"]
    sentiment: Annotated[
        str,
        "Overall sentiment expressed in the review (e.g., positive, neutral, negative)",
    ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)

review1 = "The mobile phone was delivered within the expected timeframe without any delays. It arrived in packaging that was secure, undamaged, and sufficient to protect the product. Upon inspection, the phone matched the description and specifications listed on the website. The delivery process was smooth, and there were no complications or additional steps required. Overall, the shopping experience was straightforward and met general expectations without any standout positives or negatives."


review2 = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Yash Chavan
"""

result = structured_model.invoke(review2)
print(result)
