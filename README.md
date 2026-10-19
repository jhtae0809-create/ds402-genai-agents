# DS 402 GenAI Agents

Five OpenAI agents built with Agent Builder, based on the Week 8 GenAI applications. DS 402, Penn State, Fall 2026.

## Goal

Build and test all five agents by Oct 25, 2026. Each agent should pass at least 3 of 4 test cases.

## Agents

| Folder | Input | Output |
|---|---|---|
| `audio-to-image/` | Voice clip | Generated image |
| `image-caption/` | Image | Caption |
| `resume-bullets/` | Job title, skills | 5-6 resume bullets |
| `recipe-generator/` | Ingredients | 3 recipes + shopping list |
| `diabetes-detection/` | Health values | ML + ACT-R-style prediction |

## Setup

```bash
git clone https://github.com/<your-username>/ds402-genai-agents.git
cd ds402-genai-agents
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your OpenAI API key
python test_api.py     # checks that the key works
```

## Team

| Name | Role |
|---|---|
| Hyuntae Jeong | Everything (solo project): design, code, testing, docs |

## Contributing

Work on a feature branch, then merge into `main` with a pull request. Never commit `.env`, data, or model files.

## License

MIT
