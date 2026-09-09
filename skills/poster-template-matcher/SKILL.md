---
name: poster-template-matcher
description: Match posters to 350 visual templates.
version: 0.1.0
author: 郭奥成 (GACN), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [poster, visual-style, template-matching, composition, image-analysis]
    related_skills: []
---

# Poster Template Matcher Skill

Use this workflow when the user gives a poster, advertisement, social image, presentation graphic, or other visual and wants to know its style, the closest template in the 350-template library, or how to recreate it. The workflow distinguishes visual structure from subject matter: a beauty product ad may use a hero layout, while a corporate poster may use the same layout logic with different imagery.

## When to Use

- A user uploads or points to a poster/image and asks what style it uses.
- A user asks which of the 350 visual templates best matches an image.
- A user asks for an explanation or recreation plan based on a reference image.
- A user asks for primary and secondary template matches for a mixed-style design.

Don't use this for pixel-identical image copying, copyright attribution, or claims about the original designer unless evidence is provided.

## Prerequisites

- The image must be available as a local path or URL for `vision_analyze`.
- The 350-template index must be available. Set `POSTER_TEMPLATE_INDEX` to a JSONL index path when the default is unavailable.
- The corresponding template images should be available under the index's relative `path` values for visual verification.
- The default local archive for this project is documented in the repository README; do not hardcode it into portable project code.

## How to Run

Use `vision_analyze` on the input image first. Read the JSONL index with `read_file` or a small Python parser through `terminal`. For likely candidates, use `vision_analyze` again on the candidate template images. Do not claim an exact match without checking the candidate image.

## Quick Reference

1. Inspect the input image.
2. Extract visual features.
3. Search all 350 index records.
4. Rank one primary and up to four secondary matches.
5. Verify the top candidates against their template images.
6. Explain the match and provide a recreation brief.

## Procedure

1. Identify the image's purpose and content type: product ad, editorial poster, event poster, presentation slide, UI screen, infographic, brand visual, or other. Completion criterion: one concise type label is supported by visible evidence.
2. Describe the visual system without overfitting to the subject: aspect ratio, dominant focal point, grid or axis, reading path, image-to-text ratio, cropping, overlap, whitespace, typography, palette, texture, and depth. Completion criterion: every major visible structural feature has a note.
3. Search the full 350-record index using structural terms from `layout`, `alignment`, `color`, `reuse_rule`, `scene`, and `visual_title`. Subject keywords alone are insufficient. Completion criterion: a candidate list exists and includes reasons for each candidate.
4. Rank the matches. Use the template whose layout logic best explains the image as the primary match. Use secondary matches for overlays such as full-bleed framing, cropping, layered composition, diagonal flow, or image-led presentation. Completion criterion: primary and secondary labels do not contradict the image.
5. Visually verify the primary and strongest secondary template images with `vision_analyze`. If the archive image is unavailable, report “结构近似，原图未核验” rather than inventing certainty. Completion criterion: every claimed exact template has a verified file path.
6. Return the result in this order: image type; primary template with number, Chinese title, English title, and confidence; secondary templates; visual evidence; recreation brief; uncertainty notes. Completion criterion: the user can understand both what the image is and how to reproduce its structure.
7. For recreation, preserve the reference's hierarchy rather than copying unrelated template artwork. Specify canvas, safe area, focal object, background layers, text blocks, alignment, color/material language, lighting, and what must not change. Completion criterion: the brief can be handed to an image or layout-generation workflow.

## Matching Rules

- Prioritize composition and information hierarchy over color similarity.
- Treat `visual_title` as the canonical template name; do not trust stale filenames.
- A “hero layout” is a structural match: large focal visual, limited copy, clear message/action direction. It is not a requirement to copy the template's geometric decoration.
- For mixed designs, report one primary template and explain the secondary overlays.
- Never force a single template when the image clearly combines independent structures.
- Do not infer unreadable text. Mark it as unreadable or uncertain.
- Confidence describes the match to the template's visual logic, not the quality or originality of the source image.

## Pitfalls

- The archive contains 350 records and 350 renamed template images; filename/path mismatch was previously repaired. If a path looks stale, verify the current index before reporting a missing source.
- A subject category is not a template: “beauty advertisement” describes purpose, while “hero layout” describes structure.
- Similar colors do not prove a match.
- Do not use an external CDN, browser-only classifier, or local heavyweight AI model for this workflow.
- Do not silently delete, rename, or rewrite the template archive during recognition.

## Verification

Before finalizing, confirm that the index was parsed, the primary candidate exists, the primary image was visually checked when available, and all reported IDs and titles exactly match the index. State any unavailable candidate images or unresolved ambiguity explicitly.

## Repository

The portable source, index, setup notes, and helper scripts live in the `poster-template-matcher` GitHub project. The large original-image archive remains an optional local asset pack; see its README for installation and path configuration.
