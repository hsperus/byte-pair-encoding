<div align="center">

# Byte Pair Encoding (BPE) Tokenizer

<div style="margin: 20px 0;">
  <a href="https://www.youtube.com/@hsperus">
    <img src="https://img.shields.io/badge/YouTube-Hesperus-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube Channel"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status"/>
</div>

**A minimal, clean, and educational implementation of the Byte Pair Encoding (BPE) algorithm commonly used in LLM tokenization**

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Tutorials](#-educational-resources) • [Documentation](#-how-it-works)

---

</div>

<div align="center">

### 🎓 **Watch Tutorials on [Hesperus YouTube Channel](https://www.youtube.com/@hsperus)**

**English & Turkish Video Tutorials Coming Soon!**

[![YouTube Channel](https://img.shields.io/youtube/channel/subscribers/UCyour-channel-id?label=Hesperus&style=social&logo=youtube)](https://www.youtube.com/@hsperus)

---

</div>

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| **BasicTokenizer** | Simple byte-level BPE implementation without regex preprocessing |
| **GPTLikeTokenizer** | GPT-style tokenizer with regex-based text splitting and special token support |
| **Educational Focus** | Clean, well-commented code designed for learning |
| **Multi-Language** | Comprehensive Jupyter notebooks in Turkish (`tr/` directory) |
| **Save/Load** | Persist trained tokenizers to disk |
| **Lossless Encoding** | Full BPE pipeline with guaranteed round-trip conversion |

</div>

## 📚 Datasets

<div align="center">

Our educational notebooks use authentic Turkish scientific texts featuring three distinguished Turkish scientists. These datasets not only demonstrate BPE's ability to handle Turkish characters and Unicode encoding, but also celebrate the contributions of these remarkable researchers.

<div style="margin: 30px 0;">

![Turkish Scientists](./assets/prof.png)

</div>

| Dataset | Scientist | Content | Notebook |
|---------|-----------|---------|----------|
| **DNA Repair** | **Prof. Dr. Aziz Sancar** | Biography and Nobel Prize-winning work on DNA repair mechanisms (2015 Nobel Prize in Chemistry) | `1_bpe_temeller.ipynb` |
| **Many-Electron Theory** | **Prof. Dr. Oktay Sinanoğlu** | "Many-Electron Theory of Atoms and Molecules" - Academic paper translation (Youngest full professor at Yale at age 26) | `2_bpe_gelismis.ipynb` |
| **Arf Invariant** | **Ord. Prof. Dr. Cahit Arf** | Biography and mathematical contributions including "Arf Invariant", "Arf Rings", and number theory | `3_bpe_uzman.ipynb` |

These carefully curated datasets showcase:
- **Turkish Language Processing**: Unicode characters (ğ, ş, ü, ö, ı, ç)
- **Scientific Terminology**: Technical terms from chemistry, physics, and mathematics
- **Educational Value**: Real-world examples from Nobel laureates and prominent scientists

</div>

## 🎥 Educational Resources

<div align="center">

### **📺 Video Tutorials**

Watch comprehensive tutorials on the **[Hesperus YouTube Channel](https://www.youtube.com/@hsperus)**

> **Note**: Video tutorials are currently in production and will be added to this README once uploaded. Subscribe to the channel to get notified when they're released!

| Tutorial | Language | Status |
|----------|----------|--------|
| BPE Fundamentals & Unicode/UTF-8 | English | Coming Soon |
| Advanced BPE Implementation | English | Coming Soon |
| GPT-Style Tokenization | English | Coming Soon |
| BPE Temelleri & Unicode/UTF-8 | Turkish | Coming Soon |
| Gelişmiş BPE Uygulaması | Turkish | Coming Soon |
| GPT Tarzı Tokenizasyon | Turkish | Coming Soon |

### **📓 Jupyter Notebooks**

Interactive step-by-step explanations available both locally and online:

| Notebook | Description | Google Colab |
|----------|-------------|--------------|
| **1_bpe_temeller.ipynb** | Introduction to BPE, Unicode, UTF-8, and basic merge operations (featuring Prof. Dr. Aziz Sancar dataset) | [Open in Colab](https://colab.research.google.com/drive/1QGss4JP7GaxbyLg1nPFs0jGqpvE_BFF5?usp=sharing) |
| **2_bpe_gelismis.ipynb** | Complete tokenizer implementation with training and encoding/decoding (featuring Prof. Dr. Oktay Sinanoğlu dataset) | [Open in Colab](https://colab.research.google.com/drive/1DsgFM_HILWKWNmXHl3REDR69DG_NFlrd?usp=sharing) |
| **3_bpe_uzman.ipynb** | GPT-style tokenization with regex patterns and special tokens (featuring Ord. Prof. Dr. Cahit Arf dataset) | [Open in Colab](https://colab.research.google.com/drive/1L85BKt8Npn-wOH-RssCtHDRPvt-EjgWW?usp=sharing) |

All notebooks are also available in the `tr/` directory for local use.

</div>

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/byte-pair-encoding.git
cd byte-pair-encoding

# Install dependencies
pip install regex
```

## ⚡ Quick Start

### Basic Usage

```python
from bpetokenizer.simpletokenizer import BasicTokenizer

# Create and train a tokenizer
tokenizer = BasicTokenizer()
text = "Hello, world! This is a BPE tokenizer."
tokenizer.train(text, vocab_size=276, verbose=True)

# Encode text to token IDs
token_ids = tokenizer.encode("Hello world")
print(f"Token IDs: {token_ids}")

# Decode token IDs back to text
decoded = tokenizer.decode(token_ids)
print(f"Decoded: {decoded}")

# Save the trained model
tokenizer.save("my_model")
```

### GPT-Style Tokenizer

```python
from bpetokenizer.gptliketokenizer import GPTLikeTokenizer

# Create and train a GPT-like tokenizer
tokenizer = GPTLikeTokenizer()
text = "Cahit Arf (1910-1997) made fundamental contributions to algebra."
tokenizer.train(text, vocab_size=276, verbose=True)

# Register special tokens
tokenizer.register_special_tokens({
    "<|endoftext|>": 1000,
    "<|startoftext|>": 1001
})

# Encode with special tokens
token_ids = tokenizer.encode("Cahit Arf <|endoftext|> mathematics", allowed_special="all")
print(f"Token IDs: {token_ids}")

# Decode
decoded = tokenizer.decode(token_ids)
print(f"Decoded: {decoded}")
```

## 📁 Project Structure

```
byte-pair-encoding/
├── bpetokenizer/
│   ├── simpletokenizer.py    # BasicTokenizer implementation
│   └── gptliketokenizer.py   # GPTLikeTokenizer implementation
├── tr/
│   ├── 1_bpe_temeller.ipynb  # BPE Fundamentals (Turkish)
│   ├── 2_bpe_gelismis.ipynb  # Advanced BPE (Turkish)
│   └── 3_bpe_uzman.ipynb     # Expert BPE with Regex (Turkish)
├── examples.py                # Comprehensive usage examples
├── main.py                    # CLI entry point
└── README.md
```

## 🔧 How It Works

### BasicTokenizer

The `BasicTokenizer` implements byte-level BPE:

1. Converts text to UTF-8 bytes (0-255)
2. Iteratively finds the most frequent byte pair
3. Merges the pair into a new token
4. Repeats until desired vocabulary size is reached

### GPTLikeTokenizer

The `GPTLikeTokenizer` extends the basic approach:

1. Splits text using regex patterns (similar to GPT-2/GPT-4)
2. Processes each chunk separately to prevent cross-category merges
3. Supports special tokens for model control signals
4. Handles encoding with special token awareness

## 📖 Algorithm Details

The BPE algorithm works as follows:

1. **Statistics**: Count frequency of consecutive byte pairs
2. **Merge**: Replace the most frequent pair with a new token ID
3. **Iterate**: Repeat until vocabulary size is reached
4. **Encode**: Apply learned merges to new text
5. **Decode**: Reconstruct text from token IDs using vocabulary

This implementation ensures **lossless encoding/decoding**:

```python
text = "Hello, world!"
token_ids = tokenizer.encode(text)
decoded = tokenizer.decode(token_ids)
assert decoded == text  # Always True
```

## 💻 Command Line Interface

Use the CLI to quickly test tokenizers:

```bash
# Use BasicTokenizer
python main.py basic

# Use GPTLikeTokenizer
python main.py gpt
```

## 📝 Examples

See `examples.py` for comprehensive usage examples:

```bash
python examples.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

<div align="center">

### **Special Thanks to Andrej Karpathy**

This project would not have been possible without **[Andrej Karpathy's minbpe repository](https://github.com/karpathy/minbpe)**.

**Andrej**, thank you for creating such an exceptional educational resource. Your clean, minimal implementation and thorough documentation served as the foundation for this project. The core concepts, code structure, and even the philosophy of keeping code readable and educational are directly inspired by your work.

Your commitment to making complex topics accessible through well-written code and clear explanations has been a tremendous inspiration. This project is a testament to the impact of your educational approach - thank you for sharing your knowledge and making it easier for others to learn and build upon your work.

[![Andrej Karpathy's minbpe](https://img.shields.io/github/stars/karpathy/minbpe?label=minbpe&style=social)](https://github.com/karpathy/minbpe)

</div>

## 📚 References

- [GPT-2 Paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [BPE Original Paper](https://arxiv.org/abs/1508.07909) (Sennrich et al., 2015)
- [Tiktoken Library](https://github.com/openai/tiktoken)
- [Andrej Karpathy's minbpe](https://github.com/karpathy/minbpe)

---

<div align="center">

### **Credits**

**Foundation & Inspiration**: [Andrej Karpathy's minbpe](https://github.com/karpathy/minbpe)  
**Educational Content**: Turkish tutorials featuring Turkish scientists (Aziz Sancar, Cahit Arf, Oktay Sinanoğlu)  
**Video Tutorials**: [Hesperus YouTube Channel](https://www.youtube.com/@hsperus)

---

**Made with love for educational purposes**

If you find this project helpful, consider giving it a ⭐!

[⬆ Back to Top](#-byte-pair-encoding-bpe-tokenizer)

</div>
