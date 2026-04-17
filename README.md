# cantonese-hybrid-subs
This is a project to create hybrid english subtitles for Cantonese movies and TV series.

A hybrid subtitle is one where it is majority English but proper nouns,
titles, honorifics, and idioms are left as Chinese characters creating
a mixed-language subtitle.  The target is for english speakers with
enough Cantonese and Chinese ability to hear names plus visually match
characters but not enough to read Chinese subtitles at speed or to
understand the speech on its own.  This occurs pretty frequently with
diaspora populations, especially for younger folks learning the language.

The process takes advantage of the ability of modern LLMs to understand
multiple language to merge multiple, flawed, translation sources for
producing the final product.

For any given Cantonese TV/Movie media, English and and Mandarin subs
are frequently available and form the first two input sources.

However, the English is often of questionable quality, frequently using
unnatural or crass phrasing.  Sometimes it even just fabricates dialogue
(which is oddly similar to an LLM hallucination if you think of it).
The Mandarin, while often accurate, tends to drop a lot of the color
and nuance of the original Cantonese. Sometimes it also misses phrases.

For a third input source, we take an ASRed transcript of the Cantonese
track using whipserx with [Rita Frieske's Cantonese fine-tune of Whisper Large V3](
https://huggingface.co/khleeloo/whisper-large-v3-cantonese). Unfortunately,
Cantonese, as a low-resource language, does not have great ASR fidelity
so the output tends to produce setnence that are half cantonese and half
translated into mandarin (WhisperX seems to understand Cantonese fairly well,
but its decoder cannot reliably generate cantonese phrases often
accidentally translating pieces into Mandarin).

With these three input sources, we then ask Claude to merge them into
a final file using the Mandarin subs as the template for timings
and semantics, the English subs realigned to the Mandarin for initial
content, and then the Cantonese as a known-to-be-unreliable source for
extra info on linguistic tone or register.  The final output is
a patched version of the english with information added from the Mandarin
and the Cantonese.

This repository contains a sparse history of the prompts that Claude
generated for itself as this process was refined.

Why Claude? Cause when I initially tried this with ChatGPT, ChatGPT
hallucinated the subtitles like mad after a few iterations. So it
started out as a pretty good translation and then quickly started
writing an amusingly stereotypical wuxia fanfic blending all sorts
of stories.  Fun but not useful.

Claude Sonnet does a reasoanble job but Opus produced much smoother
and nuanced english so this was developed mostly on Opus 4.7.
