# Poster Template Matcher

把一张海报或图片，匹配到 350 个视觉版型，并输出：

- 图片类型与用途
- 主模板编号、中文名、英文名和匹配度
- 辅助模板与混合风格说明
- 版式、构图、色彩、材质、信息层级解释
- 可执行的复刻方案

这个项目是一个 Hermes Agent Skill，不是一个本地重量级 AI 模型。识别由 Hermes 的 `vision_analyze` 完成，350 个模板的结构化资料由 JSONL 索引提供。

## 安装 Skill

将 `skills/poster-template-matcher/SKILL.md` 复制到 Hermes 的用户 Skill 目录，或直接把本项目作为 Skill 源使用。安装后，在对话中上传图片并说：

> 识别这张图属于350模板中的哪一种，并给我复刻方案。

## 350模板资料

`data/350_visual_templates.jsonl` 包含350条已核验记录。每条记录包含：

- `id`
- `visual_title`
- `english_title`
- `layout`
- `alignment`
- `color`
- `reuse_rule`
- `scene`
- `path`

## 本机原图包

原图包约591MB，不放进普通 Git 历史。当前本机原图目录是：

`/storage/emulated/0/Music/每日归档/2026-09/350视觉版型资料库_原图/images/`

要让 Hermes 视觉核验模板原图，设置：

```bash
export POSTER_TEMPLATE_INDEX=/path/to/350_visual_templates.jsonl
export POSTER_TEMPLATE_ROOT=/path/to/350视觉版型资料库_原图
```

如果不提供原图目录，Skill 仍然可以根据索引做结构近似匹配，但必须把结果标为“结构近似，原图未核验”。

## 识别流程

1. 用 `vision_analyze` 看用户图片。
2. 提取图片类型、主体焦点、阅读路径、网格/轴线、裁切、叠层、留白、字图比例、色彩与材质。
3. 读取全部350条索引，用结构特征检索候选。
4. 选出一个主模板和最多四个辅助模板。
5. 对主模板和最强辅助模板再做视觉核验。
6. 输出匹配理由和复刻施工单。

## 结果原则

模板是版式逻辑，不是题材名称。比如“美妆产品广告”是图片用途，“主视觉布局”才是模板结构。混合风格不强行压成一个标签；不可读的文字不猜；文件名不作为模板真实名称，优先使用图片内部标题和索引中的 `visual_title`。

## 目录

```text
skills/poster-template-matcher/SKILL.md  Hermes Skill
 data/350_visual_templates.jsonl        350条结构化模板索引
```

## 许可证

MIT。模板原图不随本仓库分发；使用者应自行确认图像素材、字体和参考设计的授权情况。
