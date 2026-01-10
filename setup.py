# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path
import re

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

root_dir = path.abspath(path.dirname(__file__))
package_name = "celloracle"  # Keep this for directory structure
pypi_name = "celloracle-lite"  # Use this for PyPI to avoid conflict

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)


with open(path.join(root_dir, package_name, 'version.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

# Start install process
setup(
    name=pypi_name,  # Use celloracle-lite for PyPI
    version=version,
    description='[celloracle-lite] Lightweight fork of CellOracle for GRN analysis with reduced dependencies',
    long_description=readme,
    long_description_content_type='text/x-rst',
    keywords='scRNA-seq, GRN, simulation, gene perturbation, celloracle-lite',
    python_requires='>=3.6',
    license="Apache-2.0 (modified; non-commercial academic use only)",  # short human string
    license_files=("LICENSE",),  # include the license file in sdist/wheel
    classifiers=[# How mature is this project? Common values are
                #   3 - Alpha
                #   4 - Beta
                #   5 - Production/Stable
                'Development Status :: 4 - Beta',

                # Indicate who your project is intended for
                'Intended Audience :: Science/Research',
                'Intended Audience :: Developers',
                'Topic :: Scientific/Engineering :: Bio-Informatics',

                # License - NON-COMMERCIAL ONLY
                # 'License :: OSI Approved :: MIT License',

                # Specify the Python versions you support here. In particular, ensure
                # that you indicate whether you support Python 2, Python 3 or both.
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.10',
            ],
    install_requires=required,
    author=author,
    author_email=author_email,
    url=url,
    package_data={"celloracle": [
                                 "motif_analysis/tss_ref_data/*.bed",
                                 #"data/TFinfo_data/*.txt", "data/TFinfo_data/*.parquet",
                                 #"data/motif_data/*.txt", "data/motif_data/*.pfm",
                                 #"data/anndata/*.h5ad",
                                 #"data/tutorial_data/*.celloracle.oracle", "data/tutorial_data/*.celloracle.links",
                                 #"data/promoter_base_GRN/*.parquet",
                                ]},
    packages=["celloracle",
              "celloracle.data",
              "celloracle.motif_analysis",
              "celloracle.utility"
              ],
    entry_points={'console_scripts':['seuratToAnndata = celloracle.data_conversion.process_seurat_object:main']}
)
