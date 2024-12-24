.. _tutorial:

Tutorial
========

There are a number of tutorials available to demonstrate how to use TFdisc functions with demo datasets. 

This tutorial consists mainly of two examples, one using a single-cell dataset of lung epithelial cells to demonstrate TFdisc's performance on differential gene exploration,
 and one using a single-cell dataset of mouse gastrulation erythropoiesis to explore its performance in unraveling lineage alterations.
 
.. note::
   The demo datasets are available in both Seurat and Scanpy formats.
   

Three parts of the tutorial
-----------------------------

1. Get the input data
^^^^^^^^^^^^^^^^^^^^^^^

For TFdisc, it requires only a gene expression matrix and a list of transcription factors for the corresponding species.
To speed up the analysis, 5000 highly variable genes and transcription factors were selected for subsequent analysis.
Based on this, the corresponding gene regulatory network was constructed
Due to the sparsity of gene expression data, we will conduct data denoising process on the 
gene expression data and use the imputation data as the input of TFdisc.


2. Simulation using TFdisc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this step, we will build a kernel ridge regression and random forest prediction model based on the gene regulatory network obtained in the first step 
and the imputation data, and then combine to predict the expression matrix after gene perturbation.


3. Downstream analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The perturbed gene expression matrix can be combined with the original expression matrix for extensive downstream analysis,
including identifying differentially expressed genes and pathways, and predicting alterations in cell identity, lineage, and function.


Examples
----------


TFdisc¡¯s performance in predicting transcriptomic changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   :numbered: 1
   
   lung/lung_input
   lung/lung_perturbation
   lung/lung_analysis
   
   
TFdisc¡¯s performance in unraveling lineage alterations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   :numbered: 1
   
   gastrulation/gastrulation_input
   gastrulation/gastrulation_perturbation
   gastrulation/gastrulation_analysis
   



