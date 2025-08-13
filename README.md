Here is the code I use for training. In the folder examples, docs.ipynb is used for training; trans.py is used for gaining the continuous model from the learning process of static solution which is from the static.h5 file. Several cm files are different continuous models gaining from the learing of static solution which could be used in the training of the dynamical process.

For adjusting the training process, you could change the code in the src folder for the file static.jl to change the time period it use for learing the static solution. Then you could get a new static.h5 file which could generate a new continuous model file cm.h5 for the initial value which could be used in the dynamical process. When you get a new cm.h5 file, you could change the code in the dynamic.jl in the src folder to change the initial continuous model file it use for training.

The julia version for compiling the files is Julia 1.9.0
