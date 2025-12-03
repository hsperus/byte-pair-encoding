from bpetokenizer.simpletokenizer import BasicTokenizer
from bpetokenizer.gptliketokenizer import GPTLikeTokenizer


# -----------------------------------------------------------------------------
# BasicTokenizer: basic byte-level BPE without regex preprocessing
# -----------------------------------------------------------------------------

# create and train a basic tokenizer
basic_tokenizer = BasicTokenizer()
training_text = "Prof. Dr. Aziz Sancar won the Nobel Prize in Chemistry in 2015 for his work on DNA repair mechanisms."
basic_tokenizer.train(training_text, vocab_size=276, verbose=True)

# encode text to token ids
text = "DNA repair"
token_ids = basic_tokenizer.encode(text)
print(f"Encoded: {token_ids}")

# decode token ids back to text
decoded_text = basic_tokenizer.decode(token_ids)
print(f"Decoded: {decoded_text}")
print(f"Round-trip successful: {decoded_text == text}\n")


# -----------------------------------------------------------------------------
# GPTLikeTokenizer: GPT-style tokenizer with regex preprocessing + special tokens
# -----------------------------------------------------------------------------

# create and train a GPT-like tokenizer
gpt_tokenizer = GPTLikeTokenizer()
training_text = "Cahit Arf (1910-1997) made fundamental contributions to algebra and number theory."
gpt_tokenizer.train(training_text, vocab_size=276, verbose=True)

# encode text to token ids
text = "Cahit Arf mathematics"
token_ids = gpt_tokenizer.encode(text)
print(f"Encoded: {token_ids}")

# decode token ids back to text
decoded_text = gpt_tokenizer.decode(token_ids)
print(f"Decoded: {decoded_text}")
print(f"Round-trip successful: {decoded_text == text}\n")


# -----------------------------------------------------------------------------
# Special tokens: register and use special tokens (GPTLikeTokenizer only)
# -----------------------------------------------------------------------------

# register special tokens
gpt_tokenizer.register_special_tokens({
    "<|endoftext|>": 1000,
    "<|startoftext|>": 1001
})

# encode with special tokens
text_with_special = "Cahit Arf <|endoftext|> mathematics"
token_ids = gpt_tokenizer.encode(text_with_special, allowed_special="all")
print(f"Encoded with special tokens: {token_ids}")

# decode back (special tokens are preserved)
decoded_with_special = gpt_tokenizer.decode(token_ids)
print(f"Decoded: {decoded_with_special}\n")


# -----------------------------------------------------------------------------
# Save and load: persist tokenizer models to disk
# -----------------------------------------------------------------------------

# save basic tokenizer
basic_tokenizer.save("basic_model")
print("Basic tokenizer saved to basic_model.model and basic_model.vocab")

# save GPT-like tokenizer
gpt_tokenizer.save("gpt_model")
print("GPT-like tokenizer saved to gpt_model.model and gpt_model.vocab")

# load a saved tokenizer
loaded_tokenizer = BasicTokenizer()
loaded_tokenizer.load("basic_model.model")
print(f"Loaded tokenizer can encode: {loaded_tokenizer.encode('DNA repair')}")


