# Claude Code 写作增效 Skill 使用指南

> 安装时间：2026-06-28
> 安装位置：`D:\2026claudecode\.agents\skills\`
> 来源：npx skills add（自动安装）

---

## 已安装 Skill 一览

| Skill | 用途 | 语言 | 触发方式 |
|-------|------|------|----------|
| humanizer-zh | 中文去 AI 味 | 中文 | 直接说需求 |
| unslop | 通用去 AI-ism（主技能）| 中/英 | `/unslop` |
| unslop-file | 处理文件中的 AI 痕迹 | 中/英 | `/unslop-file` |
| unslop-commit | Git commit 信息去套路化 | 中/英 | `/unslop-commit` |
| unslop-review | 代码审查意见去 AI 味 | 中/英 | `/unslop-review` |
| unslop-reasoning | 清理推理文本的 AI 痕迹 | 中/英 | `/unslop-reasoning` |
| unslop-help | unslop 使用帮助 | 中/英 | `/unslop-help` |

---

## Humanizer-zh 用法

**触发方式**（直接说中文需求）：
- "帮我去一下 AI 味"
- "这段话太像 AI 写的了，改写一下"
- "用更像人写的方式润色这段文字"
- "审阅这段文字，去掉 AI 痕迹"

**原理**：基于维基百科 WikiProject AI Cleanup 的 33 项检测体系，包括：
- 夸大的象征意义
- 宣传性语言
- 以 -ing 结尾的肤浅分析
- 模糊归因
- 破折号过度使用
- 三段式法则
- AI 词汇（"此外""至关重要""深入探讨"等）
- 否定式排比
- 过多连接性短语

**适用场景**：中文观点文章、博客、公众号文章、日常交流、邮件

---

## unslop 用法

**模式切换**：
```
/unslop subtle          → 轻微去味
/unslop balanced        → 默认均衡
/unslop full            → 全力去味（最大力度）
/unslop voice-match     → 匹配你的写作风格
/unslop anti-detector   → 对抗 AI 检测器
```

**停止**：
```
stop unslop
normal mode
robotic mode
```

**删除/禁用的 AI 套路**：
- 谄媚开头：Great question!  / Certainly! / 好问题！/ 当然可以！
- 套路词汇：delve, tapestry, testament, 此外, 深入探讨, 格局
- 三层排比：X, Y, and Z 结构堆砌
- 五段式结构：太整齐的段落
- 破折号：每段不超过两个
- 贴标签式平衡：每个观点必加"然而"

**保留**：
- 技术术语不变
- 代码块不变
- 真实的不确定性（"我觉得""好像是""按经验来说"）

**特别技巧**：
- 制造 burstiness：故意混用长短句 → 短句直击 → 长句把一个具体想法展开到值得展开的程度 → 再短句收尾
- 模式：具体观察 → 这意味着什么 → 怎么办

---

## 常用组合

### 写中文文章
```
用 humanizer-zh 帮我把下面这段改写一下：[内容]
```

### 写小说/故事
```
/unslop full
写一段关于[主题]的故事
```

### 写技术文档（不要太 AI 味）
```
用 unslop subtle 模式，写一段关于[技术]的说明
```

### 写 Git commit
```
/unslop-commit
帮我写一个 commit message：[改动描述]
```

### 写代码审查意见
```
/unslop-review
帮我写对这段代码的 review 意见
```

---

## 安装更多 Skill

### 命令行安装（推荐）
```bash
# 安装 GitHub 上的 Claude Code Skill
npx skills add https://github.com/作者/仓库.git
```

### 手动安装
1. 从 GitHub 下载 SKILL.md 文件
2. 放到 `D:\2026claudecode\.agents\skills\技能名\` 目录下
3. 重命名为 `SKILL.md`

### 插件市场
```
/plugin              → 打开插件市场浏览
/plugin install xxx  → 安装指定插件
```

---

## GitHub 搜索技巧

按 star 数量找热门项目：
```
https://github.com/topics/claude-code
https://github.com/search?q=claude-code+skill&type=repositories&s=stars&o=desc
```

备选推荐（未安装，值得关注）：
- `OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL` — 去 AI 味 + 风格复现，中文强项
- `wwtlitee/natural-chinese-copy-core` — 句法级中文重写
- `luoling8192/technical-writing` — 中文技术文档专用
