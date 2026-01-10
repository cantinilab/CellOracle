# CellOracle-lite  
### Lightweight fork of CellOracle for ReCoN / HuMMuS

> ⚠️ **Important notice**  
> This repository is a **lightweight fork** of the original **CellOracle** project  
> (https://github.com/morris-lab/CellOracle).  
>  
> It is **not affiliated with, endorsed by, or maintained by** the original CellOracle authors.

---

## What is CellOracle-lite?

**CellOracle-lite** is a reduced version of CellOracle designed to support
Gene Regulatory Network (GRN) workflows used in **ReCoN** and **HuMMuS**, while
avoiding heavy dependencies required by the full CellOracle stack.

**Version:** 0.21.0 (lite fork)  
**Import as:** `import celloracle`  
**Maintained by:** cantinilab

This fork was created because some dependency combinations required by the
full CellOracle package could not be resolved in the environments
used by ReCoN and HuMMuS.

This fork:
- keeps the core GRN-related functionality needed by ReCoN
- removes optional or heavyweight components not required for these workflows
- aims to be faster and easier to install in lightweight environments

If you need the full CellOracle feature set, please use the **official CellOracle package** instead.

---

## Original project

**CellOracle** is a Python library for *in silico* gene perturbation analyses
using single-cell omics data and Gene Regulatory Network models.

Original repository:  
https://github.com/morris-lab/CellOracle

Original publication:  
**Dissecting cell identity via network inference and in silico gene perturbation**  
https://www.nature.com/articles/s41586-022-05688-9

Original documentation:  
https://morris-lab.github.io/CellOracle.documentation/

---

## License

This fork is distributed **under the same license terms as the original CellOracle project**.

⚠️ **Non-commercial restriction applies**  
CellOracle (and therefore this fork) may be used **for non-commercial academic
research purposes only**.  
Commercial use requires permission from the original CellOracle authors.

See the `LICENSE` file for full details.

---

## Questions, issues, and support

- **For this fork**: https://github.com/cantinilab/celloracle/issues
- **For the original CellOracle**: https://github.com/morris-lab/CellOracle/issues

Please do **not** contact the original CellOracle maintainers about issues
specific to this fork.

---

## Supported species and reference genomes

*(Same as upstream; unchanged)*

- Human: ['hg38', 'hg19']
- Mouse: ['mm39', 'mm10', 'mm9']
- S.cerevisiae: ["sacCer2", "sacCer3"]
- Zebrafish: ["danRer7", "danRer10", "danRer11"]
- Xenopus tropicalis: ["xenTro2", "xenTro3"]
- Xenopus laevis: ["Xenopus_laevis_v10.1"]
- Rat: ["rn4", "rn5", "rn6"]
- Drosophila: ["dm3", "dm6"]
- C.elegans: ["ce6", "ce10"]
- Arabidopsis: ["TAIR10"]
- Chicken: ["galGal4", "galGal5", "galGal6"]
- Guinea Pig: ["Cavpor3.0"]
- Pig: ["Sscrofa11.1"]

---

## Changelog

For upstream changes, see:  
https://morris-lab.github.io/CellOracle.documentation/changelog/index.html
