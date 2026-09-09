# Poster Template Matcher

把一张海报或图片，匹配到 350 个视觉版型，并输出图片类型、主/次模板、匹配理由、视觉结构解释和可执行复刻方案。

这是一个 Hermes Agent Skill：识别由 Hermes 的 `vision_analyze` 完成，350 个模板的结构化资料和原图由本项目提供。

## 安装与使用

将 `skills/poster-template-matcher/SKILL.md` 安装到 Hermes Skill 目录。然后上传图片并说：

> 识别这张图属于350模板中的哪一种，并给我复刻方案。

Skill 会先分析图片，再读取350条索引，按构图和信息层级匹配，最后打开候选模板原图核验。混合风格会输出一个主模板和辅助模板，不会强行只判定一个。

## 项目内容

- `skills/poster-template-matcher/SKILL.md`：可安装的 Hermes Skill
- `data/350_visual_templates.jsonl`：350条结构化识别索引
- GitHub Release：350张模板原图分卷包
- `SOURCE-NOTICE.md`：原始仓库来源和再整理说明

## 原图包配置

下载 Release 中的全部 `template-images-part-*.zip`，解压到同一个目录后设置：

```bash
export POSTER_TEMPLATE_INDEX=/path/to/350_visual_templates.jsonl
export POSTER_TEMPLATE_ROOT=/path/to/350视觉版型资料库_原图
```

索引中的 `path` 是相对于 `POSTER_TEMPLATE_ROOT` 的路径。未配置原图包时，Skill 仍能做结构匹配，但必须标注“结构近似，原图未核验”。

## 来源说明

350张模板原图不是本项目原创，来源于公开仓库：

https://github.com/nevertoday/350-layout-compositions

本项目只对原图做了本地整理、编号/文件名统一和结构化索引，并在 `SOURCE-NOTICE.md` 中保留来源说明。使用者应遵守原始仓库的许可证、署名要求以及第三方字体和图形素材的授权限制。本项目不把这些模板原图声明为原创。

## 许可证

本项目中的 Skill、索引和说明文件采用 MIT。模板原图的权利和授权以原始仓库及其素材许可为准，不由本项目的 MIT 声明覆盖。
