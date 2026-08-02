# b2b-ai-website-remodel

中文 | [English](#english)

`b2b-ai-website-remodel` 是一个 Codex Skill，用于把 B2B 企业网站从普通营销页面，改造成 AI 可理解、信任导向、买家决策友好、证据意识明确的业务知识源。

它不是通用 SEO 工具。它重点检查 AI 系统和严肃 B2B 买家是否能理解：

1. 这家公司是谁
2. 这家公司实际提供什么
3. 为什么这家公司值得信任
4. 哪些证据支持这些说法
5. 买家为什么应该选择或联系这家公司

## 适用场景

- B2B 企业官网审查
- GEO 与 AI 可读性规划
- 企业实体清晰度优化
- 产品事实结构梳理
- 信任信号分析
- 证据缺口发现
- 买家决策路径优化
- FAQ 与语义内容规划
- 保守的 Schema 与 `llms.txt` 建议
- 在保留原网站架构前提下进行安全的前端或 CMS 改造

## 核心理念

传统网站经常用宽泛营销语言描述企业。

AI 时代的 B2B 网站需要成为结构化业务知识源：让企业更容易被理解、更 factual、更可信，也更适合真实采购者和 AI 系统使用。

`b2b-ai-website-remodel` 优先强调事实清晰度、证据意识和可信表达，而不是夸张营销文案。

## 项目介绍页

公开介绍页：

https://www.shengeo.com/ai-website-remodel/

## 核心框架

这个 Skill 由六个模块化框架组成：

- `entity-framework.md`：公司身份、业务类型、行业、位置、市场和角色
- `product-fact-framework.md`：产品事实、规格、材料、流程、应用和定制能力
- `trust-signal-framework.md`：质量、能力、经验和可靠性信号
- `evidence-gap-framework.md`：未支撑主张和所需证据
- `buyer-decision-framework.md`：采购问题与转化路径
- `geo-content-patterns.md`：AI 可读性、语义结构、FAQ、Schema 和机器可读内容

## 输出结构

典型报告包括：

```markdown
## Website Understanding

- Company identity analysis
- Product understanding
- Buyer journey analysis

## AI Trust Assessment

- Current strengths
- Missing trust signals
- Evidence gaps

## GEO Improvement Plan

### High
- Critical AI understanding problems

### Medium
- Trust improvement opportunities

### Low
- Optimization suggestions

## Implementation Plan

- Actionable website changes
```

## 安全规则

- 不编造证书
- 不编造客户案例
- 不创建无支撑的企业事实
- 明确区分 existing facts、missing information 和 recommendations
- 重要信息缺失时，要求业主提供证据
- 除非明确批准重设计，否则保留原网站架构

## 仓库结构

```text
skills/
  b2b-ai-website-remodel/
    SKILL.md
    agents/
      openai.yaml
    references/
      entity-framework.md
      product-fact-framework.md
      trust-signal-framework.md
      buyer-decision-framework.md
      evidence-gap-framework.md
      geo-content-patterns.md
      output-checklists.md
      seo-preservation.md
      cms-and-wordpress-safe-mode.md
      schema-for-manufacturers.md
      llms-txt-for-b2b-sites.md
    scripts/
      check_remodel_basics.py
      detect_site_inputs.py
      extract_page_signals.py
      generate_llms_txt.py
      generate_manufacturer_schema.py
```

## 安装

把 Skill 文件夹复制到 Codex skills 目录：

```text
skills/b2b-ai-website-remodel/
```

Skill 名称：

```text
b2b-ai-website-remodel
```

调用示例：

```text
Use $b2b-ai-website-remodel to audit this B2B company website and produce an AI Trust assessment with evidence gaps and an implementation plan.
```

## 版本

当前版本：`v0.1.0`

## License

MIT License. See [LICENSE](LICENSE).

## 贡献

欢迎提交 issues 和 pull requests。本项目会保持聚焦：B2B AI 网站改造、证据意识、信任表达和买家决策清晰度。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## English

`b2b-ai-website-remodel` is a Codex skill for transforming B2B company websites from simple marketing pages into AI-readable, trust-oriented, buyer-decision-friendly, evidence-aware business knowledge sources.

It is not a generic SEO tool. It focuses on whether AI systems and serious B2B buyers can understand:

1. Who the company is
2. What the company actually provides
3. Why the company can be trusted
4. What evidence supports those claims
5. Why a buyer should choose or contact this company

## What It Helps With

- B2B website audits
- GEO and AI-readability planning
- Entity clarity improvements
- Product fact structure
- Trust signal analysis
- Evidence gap discovery
- Buyer decision journey improvements
- FAQ and semantic content planning
- Conservative schema and `llms.txt` recommendations
- Safe frontend or CMS implementation while preserving the existing website architecture

## Philosophy

Traditional websites often describe a company in broad marketing language.

AI-era B2B websites need to work as structured business knowledge sources. They should make the company understandable, factual, credible, and useful for both human buyers and AI systems.

`b2b-ai-website-remodel` prioritizes factual clarity and evidence-aware trust over exaggerated copy.

## Project Page

The public introduction page is available at:

https://www.shengeo.com/ai-website-remodel/

## Core Frameworks

The skill is organized around six modular frameworks:

- `entity-framework.md`: company identity, business type, industry, location, market, and role
- `product-fact-framework.md`: product facts, specifications, materials, processes, applications, and customization
- `trust-signal-framework.md`: quality, capability, experience, and reliability signals
- `evidence-gap-framework.md`: unsupported claims and required proof
- `buyer-decision-framework.md`: procurement questions and conversion readiness
- `geo-content-patterns.md`: AI readability, semantic structure, FAQ, schema, and machine-readable content

## Output Structure

Typical reports include:

```markdown
## Website Understanding

- Company identity analysis
- Product understanding
- Buyer journey analysis

## AI Trust Assessment

- Current strengths
- Missing trust signals
- Evidence gaps

## GEO Improvement Plan

### High
- Critical AI understanding problems

### Medium
- Trust improvement opportunities

### Low
- Optimization suggestions

## Implementation Plan

- Actionable website changes
```

## Safety Rules

- Never invent certifications
- Never fabricate customer cases
- Never create unsupported company facts
- Clearly separate existing facts, missing information, and recommendations
- Ask for evidence when important information is missing
- Preserve original website architecture unless a redesign is explicitly approved

## Repository Structure

```text
skills/
  b2b-ai-website-remodel/
    SKILL.md
    agents/
      openai.yaml
    references/
      entity-framework.md
      product-fact-framework.md
      trust-signal-framework.md
      buyer-decision-framework.md
      evidence-gap-framework.md
      geo-content-patterns.md
      output-checklists.md
      seo-preservation.md
      cms-and-wordpress-safe-mode.md
      schema-for-manufacturers.md
      llms-txt-for-b2b-sites.md
    scripts/
      check_remodel_basics.py
      detect_site_inputs.py
      extract_page_signals.py
      generate_llms_txt.py
      generate_manufacturer_schema.py
```

## Installation

Copy the skill folder into your Codex skills directory:

```text
skills/b2b-ai-website-remodel/
```

The skill name is:

```text
b2b-ai-website-remodel
```

Example invocation:

```text
Use $b2b-ai-website-remodel to audit this B2B company website and produce an AI Trust assessment with evidence gaps and an implementation plan.
```

## Version

Current release: `v0.1.0`

## License

MIT License. See [LICENSE](LICENSE).

## Contributing

Issues and pull requests are welcome. This project is designed to stay focused on B2B AI website remodeling, evidence-aware trust, and buyer decision clarity. See [CONTRIBUTING.md](CONTRIBUTING.md).
