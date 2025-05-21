# LAD-WebSearch

## Quick Start

### Step1: Dependencies Installation

```bash
pip install -r requirements.txt
```

### Step2: Setup WebSearch API

Setup FastAPI Server.

```bash
python -m websearch.app --lang cn --model_format gpt4 --search_engine DuckDuckGoSearch
```
```bash
python -m websearch.app --lang en --model_format gpt4 --search_engine DuckDuckGoSearch
```

- `--lang`: language of the model, `en` for English and `cn` for Chinese.
- `--model_format`: format of the model.
  - `gpt4` for GPT-4o-mini.
- `--search_engine`: Search engine.
  - `DuckDuckGoSearch` for search engine for DuckDuckGo.

