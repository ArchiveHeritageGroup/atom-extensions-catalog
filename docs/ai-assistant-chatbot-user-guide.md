# Collection Assistant & Translation Memory

## A Guide for Researchers and Staff

---

## What is the Collection Assistant?

The **Collection Assistant** is a chat helper that answers natural-language questions about the archival catalogue. It uses **retrieval-augmented generation (RAG)**: it first finds the catalogue records most relevant to your question, then asks the AI to answer **using only those records**, citing them by title. This keeps answers grounded in your holdings rather than the model's general knowledge.

It only ever draws on **published descriptions**, so it never surfaces drafts.

## Using the assistant

- Open the assistant from the AI/research area (`/ai/assistant`) and type a question — e.g. *"What records mention the Engelbrecht family?"* or *"Which fonds cover the 1976 period?"*
- The answer cites the catalogue records it used; follow the links to open them.
- If the catalogue doesn't contain the answer, the assistant says so and suggests how to refine your search, rather than guessing.

## Conversation history

Each conversation has a **session**, and turns are now **saved** (`ahg_ai_chatbot_message`) with the question, the answer, the cited sources, and the model used. This means a conversation can be reviewed later and provides an audit trail of what the assistant was asked and answered.

## Translation memory

When records are translated (the AI translation tools), the platform keeps a **translation memory** (`ahg_translation_memory`): each source text + target language is stored with its translation. Before translating again, the system checks this memory and **reuses a prior translation** of the same text. Benefits:

- **Consistency** — the same phrase is translated the same way across records.
- **Speed & cost** — identical text isn't re-translated.
- **Provenance** — entries are marked `machine`, `human`, or `reviewed`; a human-edited translation is never overwritten by a later machine pass.

This works behind the scenes — you simply get faster, more consistent translations over time.

## Good to know

- All AI calls route through the AHG AI gateway (`ai.theahg.co.za`) — no third-party cloud AI is involved.
- The assistant is a research aid: **always verify** important facts against the cited records.
- Answer quality depends on how well your catalogue is described — richer scope-and-content yields better answers.

## Tips

- Ask specific questions ("records about X created before Y") rather than broad ones.
- Use the cited records as a starting point, then browse/search from there.
- If an answer seems thin, refine your wording or check whether the relevant records are published.
