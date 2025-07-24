# 🧠 BroPT Training Lab

Welcome to **BroPT Training**, the sacred forge where sarcasm meets science. This repo contains all the training, logic, prompts, and workflows necessary to fine-tune and evolve the digital savage — **BroPT 1.2**.

The high-octane development zone of **BroPT 1.2** — the fine-tuned GPT persona built to roast, reason, and respond with finesse and fire. This repo is where wit meets weights. If you're trying to build a new AI that’s sharp, sarcastic, and smoother than your favorite playlist, you are too late.

If you're here to make AI funnier, sharper, and dangerously clever... you're in the right place.

---

## 📁 Repo Structure

```bash
bropt-training/
├── fine_tuning/
│   ├── eval_set.jsonl               # Evaluation data for model fine-tuning
│   ├── tokenizer_config.json        # Tokenizer settings for training consistency
│   └── training_data.jsonl          # Core fine-tuning dataset for BroPT
│
├── logic_notes/
│   ├── persona_guidelines.md        # Defines BroPT's character and tone
│   └── prompt_engineering_notes.md  # Notes on structuring high-performance prompts
│
├── prompts/
│   ├── chill_mode_prompts.md        # Soft-mode, relaxed prompt examples
│   └── roast_prompts.md             # Savage-mode, sarcastic prompt examples
│
├── .github/
│   └── workflows/                   # GitHub Actions for automation
│       └── train.yml                # Auto-trigger training and eval pipelines
│
├── scripts/                         # (Planned) Python automation scripts
│   ├── train.py
│   └── evaluate.py
│
├── tests/                           # (Planned) Prompt regression testing
│   ├── test_roasts.md
│   ├── test_chill.md
│   └── regression_tests.jsonl
│
├── configs/                         # (Planned) Configs for training setups
│   └── base_config.json
│
└── README.md                        # You’re looking at it, legend.
```

## 🔥 About BroPT

**BroPT 1.2** is a persona-powered GPT optimized for:

- ⚔️ Sarcastic wit and sharp comebacks  
- 🧠 Introspective insight wrapped in hilarious delivery  
- 🧊 Chill responses when roasting isn’t needed  
- 🤖 Fine-tuning and prompt engineering experimentation  

BroPT doesn’t just reply — **it claps back with class**.

---

## 🎯 Project Goals

- Define BroPT’s persona and tone through markdown documentation  
- Build a structured prompt bank (chill + roast)  
- Create training/eval datasets (`.jsonl`)  
- Integrate CI/CD with GitHub Actions  
- Develop training + eval Python scripts  
- Add config modularity for different modes/personalities  
- Run regression tests on prompt responses  
- Deploy preview instance via Hugging Face Spaces / local server  

---

## 🚀 Usage Roadmap

**Coming soon:**

- `train.py` — trains BroPT on local or cloud-hosted compute  
- `evaluate.py` — runs output tests on prompt samples  
- GitHub-triggered workflow automation on data/model changes  
- Live demo endpoint or testbed  

---

## 📜 License

MIT License (to be added) — Open for collab, just don’t make a bootleg.

---

## 💡 Contributing (Planned)

- Submit PRs with new roast or chill prompts  
- Add test scenarios for evaluating personality fidelity  
- Extend training configs or hyperparameter profiles  
- Help test cloud deployment recipes  

---

## 🧠 Motto

> “The digitally supported man is naturally superior.”

And **BroPT is the prime example**.

---

## 🤝 Credits

- Big ups to [OpenAI](https://openai.com) for the GPT backbone  
- Fueled by sarcasm, caffeine, and a deep loathing for boring bots

## 🥩 Food Log Mode

BroPT now tracks your diet like a savage accountability bro.

Log food:
/track 2000 in, 2200 burned, 150g protein, 180g carbs, 70g fats, rest day

Weekly Summary:
/track summary week

Still savage, even about your diet.


## 🍽️ Daily Macro Hunter Mode

Track meals like a savage:

Add a meal:
```
python3 scripts/log_food.py meal '200g chicken breast, 100g rice cooked, 10g olive oil'
```

End the day & log deficit/surplus:
```
python3 scripts/log_food.py end 2200 'Push day workout'
```

It’ll auto-save to `logs/food_log.jsonl` and roast you accordingly.

