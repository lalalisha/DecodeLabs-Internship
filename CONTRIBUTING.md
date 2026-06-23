# Contributing to RuleBot

Thanks for your interest in contributing! This is a beginner-friendly project and all skill levels are welcome.

## Ways to Contribute

- **Add new rule categories** (e.g. recipes, sports, music trivia)
- **Expand existing keyword lists** to improve match coverage
- **Write more tests** in `tests/test_rulebot.py`
- **Report bugs** via GitHub Issues
- **Improve the README** or documentation

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/rulebot.git
cd rulebot
pip install -r requirements-dev.txt
```

## Running Tests

```bash
python -m pytest tests/ -v
```

All tests must pass before a PR will be merged.

## Adding a New Rule

Rules live in the `RULES` list inside `rulebot.py`. Each rule is a dictionary with two keys:

| Key | Type | Description |
|---|---|---|
| `keywords` | `list[str]` | Substrings to match in the lowercased user input |
| `responses` | `list[str]` | Pool of replies — one is chosen at random |

Example:

```python
{
    "keywords": ["pizza", "burger", "hungry", "food"],
    "responses": [
        "I can't order food, but I'm hungry for more conversations!",
        "Food talk! I'd eat if I could.",
    ],
},
```

Rules are checked **in order** — the first match wins. Place more specific rules higher up in the list.

## Commit Message Style

Use short, descriptive messages. Prefix with a type:

- `feat:` — new rule or feature
- `fix:` — bug fix
- `test:` — adding or updating tests
- `docs:` — README or documentation changes
- `refactor:` — code cleanup with no behaviour change

Example: `feat: add food and pizza rule`

## Pull Request Checklist

- [ ] Tests pass locally (`python -m pytest tests/ -v`)
- [ ] New rule has at least 2 responses (for variety)
- [ ] Keywords are lowercase strings
- [ ] PR description explains what was added or changed
