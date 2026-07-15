#  RuleBot — Rule-Based Chatbot

A lightweight, zero-dependency chatbot built entirely with Python if-else logic and keyword matching. No machine learning, no APIs, no internet required — just pure Python rules.

---

##  Features

| Topic | Example inputs |
|---|---|
|  Greetings | `hello`, `hey`, `good morning` |
|  Time & Date | `what time is it`, `what day is today` |
|  Weather | `is it raining`, `what's the forecast` |
|  Jokes | `tell me a joke`, `make me laugh` |
|  Math | `calculate`, `what is 5 + 3` |
|  Motivation | `inspire me`, `give me a quote` |
|  Fun Facts | `fun fact`, `did you know` |
|  Chit-chat | `how are you`, `who are you` |
|  Exit | `bye`, `quit`, `goodbye` |

---

## 🚀 Getting Started

### Requirements

- Python 3.7 or higher
- No external libraries needed

### Run the chatbot

```bash
git clone https://github.com/YOUR_USERNAME/rulebot.git
cd rulebot
python rulebot.py
```

That's it. No `pip install`, no `.env` file, no setup.

### Example session

```
==================================================
       RuleBot — Rule-Based Chatbot
==================================================
Hello! I'm RuleBot. Type 'help' to see what
I can do, or 'bye' to exit.
--------------------------------------------------
You: hello
RuleBot: Hey there! Great to see you. Type 'help' to see what I can do.

You: tell me a joke
RuleBot: Why do programmers prefer dark mode?
→ Because light attracts bugs!

You: what time is it
RuleBot: Right now it's 03:45 PM on Tuesday, June 23, 2026.

You: bye
RuleBot: Farewell! My if-else statements will miss you.
```

---

##  Project Structure

```
rulebot/
├── rulebot.py        # Main chatbot — all logic lives here
├── tests/
│   └── test_rulebot.py   # Unit tests
├── requirements.txt  # Empty — no dependencies!
├── .gitignore        # Python gitignore
├── LICENSE           # MIT License
└── README.md         # You are here
```

---

## 🔧 How It Works

RuleBot uses a simple two-step process:

1. **Normalize** — convert the user's input to lowercase and strip whitespace.
2. **Match** — scan through a list of rule dictionaries. Each rule has a `keywords` list and a `responses` list. The first rule whose keyword appears anywhere in the input wins, and a random response from that rule is returned.

```python
for rule in RULES:
    if any(kw in text for kw in rule["keywords"]):
        return random.choice(rule["responses"]), False
```

Special cases (exit keywords, live time/date) are checked before the rule table.

---

## ➕ Adding New Rules

Open `rulebot.py` and append a new dictionary to the `RULES` list:

```python
{
    "keywords": ["pizza", "food", "hungry", "eat"],
    "responses": [
        "I can't order pizza for you, but I highly recommend it!",
        "Food talk! My favourite topic (hypothetically).",
    ],
},
```

Save and re-run — no restart script needed.

---

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

---

## 🙌 Contributing

Pull requests are welcome! If you'd like to add new rule categories, improve keyword coverage, or refactor the engine, feel free to open an issue or PR.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/add-pizza-rule`
3. Commit your changes: `git commit -m "feat: add food/pizza rule"`
4. Push and open a Pull Request
