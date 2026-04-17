# cantonese-hybrid-subs

## What is this project?
This is a project to create hybrid english subtitles for Cantonese movies and TV series.

A hybrid subtitle is one where it is majority English but proper nouns,
titles, honorifics, and idioms are left as Chinese characters creating
a mixed-language subtitle.

The target is for english speakers with enough Cantonese and Chinese
ability to hear names plus visually match characters but not enough to
read Chinese subtitles at speed or to understand the speech on its own.
This occurs pretty frequently with diaspora populations, especially for
younger folks learning the language.

The project also outputs fully english subtitles (no chinese characgters)
but with all pinyin redone in either jyutping or yale romanization with tones
removed. Pinyin causes a major cognative dissonance when listening since
it will say "rong-er" for "蓉兒" when a native english speaker would expect to
see something closer to "yoong-yee."  This outputs both Jyutping and Yale
because while Jyutping is definitely the dominant standard now and relatively
easy to learn, for an untrained child who only knows english the phonetics
are still harder to intuit.  Using the 蓉兒, Jyutping w/o tones produces
"jung-ji" whereas yale comes out to "yuhng-yih".

Honestly, neither Jyutping nor Yale is all that great for untrained readers
because names like that, read at the speed of subtitles, effectively become
sightwords anyways. My guess is that for folks without ANY Cantonese phonetic
training, the hybrid with CJK characters will actually be more intelligible
because the romanizations and the Chinese Characters will all effectively be
processed as sight words and in that context, the Chinese Characters will be
more distinct from one another.

## How does it work?
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

## What is in this repository?
This repository contains a sparse history of the prompts that Claude
generated for itself as this process was refined.

## Why Claude?
Why Claude? Cause when I initially tried this with ChatGPT, ChatGPT
hallucinated the subtitles like mad after a few iterations. So it
started out as a pretty good translation and then quickly started
writing an amusingly stereotypical wuxia fanfic blending all sorts
of stories.  Fun but not useful.

Claude Sonnet does a reasoanble job but Opus produced much smoother
and nuanced english so this was developed mostly on Opus 4.7.

## How was this developed? What was the initial prompts?
The initial prompts were

```
1-chi_tra.srt is an OCRed mandarin chinese subtitle for a Cantonese Language series, Legend of the Condor Heroes 1983.  1-yue.json is the output of whisperx ASR using the "khleeloo/whisper-large-v3-cantonese"  and "ctl/wav2vec2-large-xlsr-cantonese" alignment.

The 1-yue.json will contain content missing from the cha_tra, but it has many ASR errors including accidnetally normalizing into mandarin style test (我們 when it hsould be 我哋).

Please analyze the 1-yue.json and attempt to fix the ASR errors. Output the data in two fones. One in same json format and a second as an SRT whose blocks have the same timings as chi_tra.srt
```

Followed by

```
Now update the english subs here based on the yue-correct subs.  Extend timing for subtitles that get longer but DO NOT cause later subs to be delayed or overlapped.
```

which produced a response like

```
Here's the updated English subtitle file. Summary of what was done:
346 text changes and 382 timing adjustments across 446 blocks, with zero overlaps.
Key categories of corrections:
Translation fixes from corrected Cantonese:

Block 15: "Madam Ye's husband passed away" → "after the turmoil, these two went through great hardship" (the Cantonese says 呢兩個 "these two", not a specific person)
Block 20: "I didn't expect you to be so pretty!" → "Let's see how well you fight!" (殺得幾靚 means "how well you kill/fight", not "pretty")
Block 42: "Jin Wuxu" → "Jin Yanxu" (金閻旭, corrected character name)
Block 294: Added "Chancellor Han Tuozhou" (韓侂胄) — the specific historical figure
Block 350: "Yan Alie" → "Yan A'ao" (阿鰲, corrected name)
```


Refinements were made through a very large series of observations and discussions about translation errors and styling opinions prompts

```
Make a revision of the english based on inputs from both concentrating on
  (a) replacing honorifics, titles, wuxia terms, and historical terms with the Chinese
  (b) adding any context or nuance in the chinese that is missing in the english
Keep names in chinese characters. In particular, anything that is in pinyin should be turned into the chinese character equivalent.
```

and

```
Phrases like 真人 Qiu should be 丘真人.  Also, there are still a lot of pinyin names like "Guo Sheng" and "Jing" that need to be in chinese.

Lastly, Jin and Song are inconsistently in english instead of chinese characters.  stay in Chinese.
```
