# TFdisc


```python
import pandas as pd
import numpy as np
import pickle
import TFdisc as tc
import warnings
warnings.filterwarnings("ignore")
import os
os.environ['R_WARN'] = '0'
os.environ['R_HOME'] = "/home/hywang/anaconda3/envs/TFdisc/lib/R/"
```


```python
wt_data = pd.read_csv("./data/wt_data.csv",index_col=0)
wt_data = wt_data.T
TF_list = list(pd.read_csv("./data/TF_list.csv",index_col=0).iloc[:,0])
HVG_list = list(pd.read_csv("./data/HVG_list.csv",index_col=0).iloc[:,0])
ave_data = pd.read_csv("./data/ave_data.csv",index_col=0)
ave_data = ave_data.T
with open("./data/alltop.pkl", "rb") as tf:
    grn_result = pickle.load(tf)
```


```python
tc.train_model.TF_model(ave_data,list(set(TF_list) | set(HVG_list)),
                     grn_result,save = None,method = "krr",verbose = True,
                     test_size=0.1, model_score=False)
```

    Task Progress: 100%|███████████████████| 5644/5644 [2:51:37<00:00,  1.82s/items]

    running time = 10297.27405333519


    



```python
tc.train_model.TF_model(ave_data,list(set(TF_list) | set(HVG_list)),
                     grn_result,save = None,method = "rf",verbose = True,
                     test_size=0.1, model_score=False)
```

    Task Progress: 100%|███████████████████| 5644/5644 [8:32:07<00:00,  5.44s/items]

    running time = 5.573473691940308


    



```python
pre_data = tc.gen_model.combine_predict(ave_data,TF_list,HVG_list,grn_result,"./krr/",rf_premodel="./rf/",
                    TF="Nkx2-1",krr_time=5,rf_time=1,
                    core=30,matrix_err = 10000,min_matrix_err = 0.01)
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

## Other


```python
tc.train_model.TF_model(ave_data,list(set(TF_list) | set(HVG_list)),
                     grn_result,save = None,method = "krr",verbose = True,
                     test_size=0.1, model_score=False)
```


```python
pre_data = tc.gen_model.combine_predict(ave_data,TF_list,HVG_list,grn_result,"./krr/",rf_premodel=None,
                    TF="Nkx2-1",krr_time=5,rf_time=1,
                    core=30,matrix_err = 10000,min_matrix_err = 0.01)
```


```python

```


```python
grn_result = TFdisc.grn.TF_grn(wt_data,TF_list)
```

    running time :  273.91751742362976



```python
imp=imputation.imp_SAVER(wt_data1,20)
```

    R[write to console]: Loading required package: SAVER
    


    [1] "load SAVER"
    [1] ‘1.1.3’


    R[write to console]: Converting x to matrix.
    
    R[write to console]: 500 genes, 500 cells
    


    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    WARNING: ignoring environment value of R_HOME
    starting worker pid=13006 on localhost:11287 at 14:23:38.698
    starting worker pid=13000 on localhost:11287 at 14:23:38.702
    starting worker pid=13007 on localhost:11287 at 14:23:38.704
    starting worker pid=13002 on localhost:11287 at 14:23:38.713
    starting worker pid=12996 on localhost:11287 at 14:23:38.716
    starting worker pid=13015 on localhost:11287 at 14:23:38.722
    starting worker pid=12998 on localhost:11287 at 14:23:38.724
    starting worker pid=12999 on localhost:11287 at 14:23:38.725
    starting worker pid=13013 on localhost:11287 at 14:23:38.725
    starting worker pid=13009 on localhost:11287 at 14:23:38.726
    starting worker pid=13001 on localhost:11287 at 14:23:38.727
    starting worker pid=13005 on localhost:11287 at 14:23:38.729
    starting worker pid=13011 on localhost:11287 at 14:23:38.733
    starting worker pid=13014 on localhost:11287 at 14:23:38.733
    starting worker pid=13003 on localhost:11287 at 14:23:38.733
    starting worker pid=13004 on localhost:11287 at 14:23:38.736
    starting worker pid=13008 on localhost:11287 at 14:23:38.744
    starting worker pid=13010 on localhost:11287 at 14:23:38.745
    starting worker pid=13012 on localhost:11287 at 14:23:38.747
    starting worker pid=12997 on localhost:11287 at 14:23:38.749


    R[write to console]: Running SAVER with 20 worker(s)
    
    R[write to console]: Calculating predictions for 500 genes using 221 genes and 500 cells...
    
    R[write to console]: Start time: 2024-12-10 14:23:39
    
    R[write to console]: Estimating finish time...
    
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    Loading required package: SAVER
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    Loading required package: SAVER
    Loading required package: SAVER
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    Loading required package: SAVER
    loaded SAVER and set parent environment
    Loading required package: SAVER
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    R[write to console]: Finished 20/500 genes. Approximate finish time: 2024-12-10 14:25:59
    
    R[write to console]: Calculating max cor cutoff...
    
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    R[write to console]: Finished 100/500 genes. Approximate finish time: 2024-12-10 14:26:34
    
    R[write to console]: Calculating lambda coefficients...
    
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    R[write to console]: Finished 404/500 genes. Approximate finish time: 2024-12-10 14:28:01
    
    R[write to console]: Predicting remaining genes...
    
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    R[write to console]: Finished 428/500 genes. Approximate finish time: 2024-12-10 14:28:01
    
    R[write to console]: Predicting remaining genes...
    
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    loaded SAVER and set parent environment
    R[write to console]: Done!
    
    R[write to console]: Finish time: 2024-12-10 14:28:00
    
    R[write to console]: Total time: 4.34451 mins
    



```python

```


```r
%%R
library()
```

    File: /tmp/RtmpPRkkNN/RlibraryIQR23f9572e0470c
    Packages in library ‘/home/hywang/anaconda3/envs/TFdisc/lib/R/library’:
    
    
    
    askpass                 Safe Password Entry for R, Git, and SSH
    
    base                    The R Base Package
    
    base64enc               Tools for base64 encoding
    
    boot                    Bootstrap Functions (Originally by Angelo Canty
    
                            for S)
    
    brew                    Templating Framework for Report Generation
    
    brio                    Basic R Input Output
    
    bslib                   Custom 'Bootstrap' 'Sass' Themes for 'shiny'
    
                            and 'rmarkdown'
    
    cachem                  Cache R Objects with Automatic Pruning
    
    callr                   Call R from R
    
    class                   Functions for Classification
    
    cli                     Helpers for Developing Command Line Interfaces
    
    clipr                   Read and Write from the System Clipboard
    
    cluster                 "Finding Groups in Data": Cluster Analysis
    
                            Extended Rousseeuw et al.
    
    codetools               Code Analysis Tools for R
    
    commonmark              High Performance CommonMark and Github Markdown
    
                            Rendering in R
    
    compiler                The R Compiler Package
    
    cpp11                   A C++11 Interface for R's C Interface
    
    crayon                  Colored Terminal Output
    
    credentials             Tools for Managing SSH and Git Credentials
    
    curl                    A Modern and Flexible Web Client for R
    
    datasets                The R Datasets Package
    
    desc                    Manipulate DESCRIPTION Files
    
    devtools                Tools to Make Developing R Packages Easier
    
    diffobj                 Diffs for R Objects
    
    digest                  Create Compact Hash Digests of R Objects
    
    doParallel              Foreach Parallel Adaptor for the 'parallel'
    
                            Package
    
    downlit                 Syntax Highlighting and Automatic Linking
    
    ellipsis                Tools for Working with ...
    
    evaluate                Parsing and Evaluation Tools that Provide More
    
                            Details than the Default
    
    fansi                   ANSI Control Sequence Aware String Functions
    
    fastmap                 Fast Data Structures
    
    fontawesome             Easily Work with 'Font Awesome' Icons
    
    foreach                 Provides Foreach Looping Construct
    
    foreign                 Read Data Stored by 'Minitab', 'S', 'SAS',
    
                            'SPSS', 'Stata', 'Systat', 'Weka', 'dBase', ...
    
    fs                      Cross-Platform File System Operations Based on
    
                            'libuv'
    
    gert                    Simple Git Client for R
    
    gh                      'GitHub' 'API'
    
    gitcreds                Query 'git' Credentials from 'R'
    
    glmnet                  Lasso and Elastic-Net Regularized Generalized
    
                            Linear Models
    
    glue                    Interpreted String Literals
    
    graphics                The R Graphics Package
    
    grDevices               The R Graphics Devices and Support for Colours
    
                            and Fonts
    
    grid                    The Grid Graphics Package
    
    highr                   Syntax Highlighting for R Source Code
    
    htmltools               Tools for HTML
    
    httpuv                  HTTP and WebSocket Server Library
    
    httr                    Tools for Working with URLs and HTTP
    
    httr2                   Perform HTTP Requests and Process the Responses
    
    ini                     Read and Write '.ini' Files
    
    IRdisplay               'Jupyter' Display Machinery
    
    IRkernel                Native R Kernel for the 'Jupyter Notebook'
    
    iterators               Provides Iterator Construct
    
    jquerylib               Obtain 'jQuery' as an HTML Dependency Object
    
    jsonlite                A Simple and Robust JSON Parser and Generator
    
                            for R
    
    KernSmooth              Functions for Kernel Smoothing Supporting Wand
    
                            & Jones (1995)
    
    knitr                   A General-Purpose Package for Dynamic Report
    
                            Generation in R
    
    later                   Utilities for Scheduling Functions to Execute
    
                            Later with Event Loops
    
    lattice                 Trellis Graphics for R
    
    lifecycle               Manage the Life Cycle of your Package Functions
    
    magrittr                A Forward-Pipe Operator for R
    
    MASS                    Support Functions and Datasets for Venables and
    
                            Ripley's MASS
    
    Matrix                  Sparse and Dense Matrix Classes and Methods
    
    memoise                 'Memoisation' of Functions
    
    methods                 Formal Methods and Classes
    
    mgcv                    Mixed GAM Computation Vehicle with Automatic
    
                            Smoothness Estimation
    
    mime                    Map Filenames to MIME Types
    
    nlme                    Linear and Nonlinear Mixed Effects Models
    
    nnet                    Feed-Forward Neural Networks and Multinomial
    
                            Log-Linear Models
    
    openssl                 Toolkit for Encryption, Signatures and
    
                            Certificates Based on OpenSSL
    
    parallel                Support for Parallel computation in R
    
    pbdZMQ                  Programming with Big Data -- Interface to
    
                            'ZeroMQ'
    
    pillar                  Coloured Formatting for Columns
    
    pkgbuild                Find Tools Needed to Build R Packages
    
    pkgconfig               Private Configuration for 'R' Packages
    
    pkgload                 Simulate Package Installation and Attach
    
    praise                  Praise Users
    
    prettyunits             Pretty, Human Readable Formatting of Quantities
    
    processx                Execute and Control System Processes
    
    promises                Abstractions for Promise-Based Asynchronous
    
                            Programming
    
    ps                      List, Query, Manipulate System Processes
    
    purrr                   Functional Programming Tools
    
    R6                      Encapsulated Classes with Reference Semantics
    
    rappdirs                Application Directories: Determine Where to
    
                            Save Data, Caches, and Logs
    
    rcmdcheck               Run 'R CMD check' from 'R' and Capture Results
    
    Rcpp                    Seamless R and C++ Integration
    
    RcppEigen               'Rcpp' Integration for the 'Eigen' Templated
    
                            Linear Algebra Library
    
    rematch2                Tidy Output from Regular Expression Matching
    
    remotes                 R Package Installation from Remote
    
                            Repositories, Including 'GitHub'
    
    repr                    Serializable Representations
    
    rlang                   Functions for Base Types and Core R and
    
                            'Tidyverse' Features
    
    roxygen2                In-Line Documentation for R
    
    rpart                   Recursive Partitioning and Regression Trees
    
    rprojroot               Finding Files in Project Subdirectories
    
    rstudioapi              Safely Access the RStudio API
    
    rversions               Query 'R' Versions, Including 'r-release' and
    
                            'r-oldrel'
    
    sass                    Syntactically Awesome Style Sheets ('Sass')
    
    SAVER                   Single-Cell RNA-Seq Gene Expression Recovery
    
    sessioninfo             R Session Information
    
    shape                   Functions for Plotting Graphical Shapes, Colors
    
    sourcetools             Tools for Reading, Tokenizing and Parsing R
    
                            Code
    
    spatial                 Functions for Kriging and Point Pattern
    
                            Analysis
    
    splines                 Regression Spline Functions and Classes
    
    stats                   The R Stats Package
    
    stats4                  Statistical Functions using S4 Classes
    
    stringi                 Character String Processing Facilities
    
    stringr                 Simple, Consistent Wrappers for Common String
    
                            Operations
    
    survival                Survival Analysis
    
    sys                     Powerful and Reliable Tools for Running System
    
                            Commands in R
    
    systemfonts             System Native Font Finding
    
    tcltk                   Tcl/Tk Interface
    
    testthat                Unit Testing for R
    
    tibble                  Simple Data Frames
    
    tinytex                 Helper Functions to Install and Maintain TeX
    
                            Live, and Compile LaTeX Documents
    
    tools                   Tools for Package Development
    
    urlchecker              Run CRAN URL Checks from Older R Versions
    
    usethis                 Automate Package and Project Setup
    
    utf8                    Unicode Text Processing
    
    utils                   The R Utils Package
    
    uuid                    Tools for Generating and Handling of UUIDs
    
    vctrs                   Vector Helpers
    
    waldo                   Find Differences Between R Objects
    
    whisker                 {{mustache}} for R, Logicless Templating
    
    withr                   Run Code 'With' Temporarily Modified Global
    
                            State
    
    xfun                    Supporting Functions for Packages Maintained by
    
                            'Yihui Xie'
    
    xml2                    Parse XML
    
    xopen                   Open System Files, 'URLs', Anything
    
    xtable                  Export Tables to LaTeX or HTML
    
    yaml                    Methods to Convert R Data to YAML and Back
    
    zip                     Cross-Platform 'zip' Compression
    
    ---



```python

```


```python
# imp=imp_SAVER(data[TF_list].iloc[0:300,],20,normalization=False)
def imp_SAVER(data, cores=20,normalization=True):
    pandas2ri.activate()
    rscript = """
    process_saver <- function(data,cores,normalization) {
        if(require(SAVER)){
            print("load SAVER")
            print(packageVersion("SAVER"))
        }else{ 
            install.packages("SAVER")
            if(require(SAVER)){
                print("install and load SAVER")
                print(packageVersion("SAVER"))
            } else {
                stop("fail to install and load SAVER")
            }
            }
        if(require(SAVER)){
            if(normalization){
                impute_data = saver(data,ncores = cores,estimates.only = TRUE,size.factor = 1)
                return(impute_data)
            }else{
                impute_data = saver(data,ncores = cores,estimates.only = TRUE)
                return(impute_data)
            }
        }
    }
    """
    r(rscript)
    
    impute_data = r['process_saver'](pandas2ri.py2rpy(data.T),cores,normalization)
    impute_data = pd.DataFrame(impute_data.T, columns=data.columns, index=data.index)
    return impute_data
```


```python
adata = sc.AnnData(data)
```


```python
data  = pd.read_csv("./processdata/count.csv",index_col=0)
```


```python
TF_list = list(pd.read_csv("./processdata/TF_list.csv",index_col=0).iloc[:,0])
```


```python

```


```python

```
