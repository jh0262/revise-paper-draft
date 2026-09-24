# revise-paper-draft · 论文初稿系统修订

以“研究问题—技术动作—机制解释—验证证据—适用边界”组织论文修订，保留通用中英文与工程、机器人、仿真、辨识、优化和可靠性工作流。

## 2026-09-24 中文算法论文增强

依据17篇样本文献的定性分析，新增12项语言规则、8类章节检查、14项证据审校、16组原创改写示例、修订工作表及20个合成行为测试情境。样本观察、编辑建议与期刊要求分别处理，不把个别论文写法提升为统一规范。

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 主流程与按需调用入口 |
| [中文算法写作](references/chinese-algorithm-writing.md) | 论文类型、L01—L12语言规则、S01—S08章节检查 |
| [算法证据审校](references/algorithm-evidence-audit.md) | A01—A14：档案、自适应、协同、RL、指标、预算、统计、理论和工程边界 |
| [改写示例](references/chinese-rewrite-examples.md) | E01—E16：依据、原句、修订及核实项 |
| [来源说明](references/corpus-source-notes.md) | P01—P17书目、PDF位置与提炼边界 |
| [修订工作表](assets/chinese-revision-worksheet.md) | 主张矩阵、机制卡、术语和数值台账 |
| [通用准则](references/revision-rubric.md) | 章节、图表、文献和审稿回复 |
| [工程检查](references/engineering-robotics.md) | 模型、仿真、实验、辨识、优化和可靠性 |
| [测试情境](evals/chinese-algorithm-cases.json) | 20项行为回归输入与验收规则 |
| [结构检查](scripts/validate_skill.py) | 离线文件、链接、编号及测试情境格式检查 |
| [更新记录](CHANGELOG.md) | 改动、保留内容与边界 |

## 使用

已加载此Skill的环境中，沿用名称`revise-paper-draft`。全文修订示例：

> 使用 $revise-paper-draft 修订这篇中文多目标优化论文。先识别论文类型，再检查问题、机制、实验和结论的一致性；保留公式和数据，给出修订正文，并单列证据不足和待作者核实的问题。

局部修订示例：

> 使用 $revise-paper-draft 只修改下面的方法描述，让技术动作、条件和术语更清楚。不要重构整篇论文，不更改算子、阈值、公式或结果。

普通段落仅按需读取相关规则，不强制全套审计或工作表。GitHub更新不表示本地已安装副本自动同步；已有副本需要拉取或替换更新。

## 边界与验证

不虚构数据、参数、p值、证明、引用或创新，不将计划写为完成，不将仿真写成实测，不悄改科学内容。不分发样本PDF或原图表。

结构检查：输入为Skill目录，输出为错误及非零退出码或通过摘要。流程为`读取文件 → 检查入口/链接 → 核对规则和情境编号 → 汇总`。

```sh
python scripts/validate_skill.py
```

脚本仅作离线结构检查，不调用模型、不认证论文科学正确性，也不代表客户端兼容性测试。20个行为情境需另将request和evidence提交给已加载Skill的模型，按must/must_not人工评阅并记录版本与结果。**情境格式通过不等于20项模型行为测试通过。** 所有示例数字都是合成数据。
