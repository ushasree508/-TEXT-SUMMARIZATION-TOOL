from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extractive_summary(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

# Sample text input
text = """Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines.
It has become an essential part of the technology industry. Research in AI focuses on developing
algorithms that can learn and make decisions. AI applications include natural language processing,
robotics, and self-driving cars."""

print("Extractive Summary:")
print(extractive_summary(text))
