import sys
from bpetokenizer.simpletokenizer import BasicTokenizer
from bpetokenizer.gptliketokenizer import GPTLikeTokenizer


# -----------------------------------------------------------------------------
# Entry point: put your own experiments or CLI here
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # choose tokenizer type from command line: basic | gpt
    mode = sys.argv[1] if len(sys.argv) > 1 else "basic"
    text = "Hello BPE"

    if mode == "basic":
        tokenizer = BasicTokenizer()
        tokenizer.train(text, vocab_size=260, verbose=False)
        ids = tokenizer.encode(text)
        print("Using BasicTokenizer")
    elif mode == "gpt":
        tokenizer = GPTLikeTokenizer()
        tokenizer.train(text, vocab_size=260, verbose=False)
        ids = tokenizer.encode(text)
        print("Using GPTLikeTokenizer")
    else:
        raise SystemExit("Usage: python main.py [basic|gpt]")

    print("Input text:", text)
    print("Token ids:", ids)

