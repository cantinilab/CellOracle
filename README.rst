CellOracle-lite
===============

⚠️ **Important Notice**
------------------------

This is **celloracle-lite**, a lightweight fork of the original CellOracle project
maintained by cantinilab for use with ReCoN and HuMMuS.

**This fork is NOT affiliated with, endorsed by, or maintained by the original CellOracle authors.**

Import as: ``import celloracle``

Version: **0.21.0+lite**

Original CellOracle
-------------------

CellOracle is a python library for in silico gene perturbation analyses
using single-cell omics data and Gene Regulatory Network models.

**Original repository:** https://github.com/morris-lab/CellOracle

**Original publication:** `Dissecting cell identity via network inference and in silico gene
perturbation <https://www.nature.com/articles/s41586-022-05688-9>`__

**Original documentation:** `Web documentation <https://morris-lab.github.io/CellOracle.documentation/>`__

What is CellOracle-lite?
-------------------------

CellOracle-lite is a reduced version designed to support GRN workflows in ReCoN and HuMMuS
while avoiding heavy dependency conflicts. 

This fork:

- Keeps core GRN functionality needed by ReCoN
- Removes optional or heavyweight components
- Aims for easier installation in lightweight environments

If you need the full CellOracle feature set, please use the **official CellOracle package**.

Questions and Issues
~~~~~~~~~~~~~~~~~~~~

For celloracle-lite issues: https://github.com/cantinilab/celloracle/issues

For original CellOracle: https://github.com/morris-lab/CellOracle/issues

Supported Species and reference genomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Human: [‘hg38’, ‘hg19’]
-  Mouse: [‘mm39’, ‘mm10’, ‘mm9’]
-  S.cerevisiae: [“sacCer2”, “sacCer3”]
-  Zebrafish: [“danRer7”, “danRer10”, “danRer11”]
-  Xenopus tropicalis: [“xenTro2”, “xenTro3”]
-  Xenopus laevis: [“Xenopus_laevis_v10.1”]
-  Rat: [“rn4”, “rn5”, “rn6”]
-  Drosophila: [“dm3”, “dm6”]
-  C.elegans: [“ce6”, “ce10”]
-  Arabidopsis: [“TAIR10”]
-  Chicken: [“galGal4”, “galGal5”, “galGal6”]
-  Guinea Pig: [“Cavpor3.0”]
-  Pig: [“Sscrofa11.1”]

Changelog
~~~~~~~~~

Please go to `this
page <https://morris-lab.github.io/CellOracle.documentation/changelog/index.html>`__.

.. |GitHub Workflow Status| image:: https://img.shields.io/github/actions/workflow/status/morris-lab/CellOracle/build_check.yml?branch=master
   :target: https://github.com/morris-lab/CellOracle/actions/workflows/build_check.yml
.. |PyPI| image:: https://img.shields.io/pypi/v/celloracle?color=blue
   :target: https://pypi.org/project/celloracle/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/celloracle
   :target: https://pypi.org/project/celloracle/
.. |PyPI - Wheel| image:: https://img.shields.io/pypi/wheel/celloracle
   :target: https://pypi.org/project/celloracle/
.. |Downloads| image:: https://static.pepy.tech/personalized-badge/celloracle?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/celloracle
.. |Docker Pulls| image:: https://img.shields.io/docker/pulls/kenjikamimoto126/celloracle_ubuntu?color=red
   :target: https://hub.docker.com/r/kenjikamimoto126/celloracle_ubuntu
