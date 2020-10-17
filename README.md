Hyperparameter Naming Project


Requirements:

The project requires to train a machine learning model that accepts a set of tunable hyperparameters. The hyperparameters are specified in a Python dictionary as follows:

H = {
   “learning_rate”: 0.1,
   “dropout_in”: 0.5,
   “dropout_out”: 0.3,
   “use_cutout”: True,
   “use_skip”: False,
   “momentum”: 0.9
}

The requirement is to serialize the hyperparameters into a string such that the experiments can be easily remembered. 
for example, to create a function get_experiment_name(hyperparameters_dict, prefix_length=-1) that returns a string. prefix_length specifies the length of the hyperparameter prefix that will be reported in the experiment name string. In the case that two hyperparameters have the same prefix of length prefix_length, the function returns the minimum length prefix that can uniquely identify the hyperparameter.

A few example usages are:

get_experiment_name(H) -> “learningrate_0.1_dropoutin_0.5_dropoutout_0.3_usecutout_True_useskip_False_momentum_0.9”

get_experiment_name(H, 3) ->
“lea_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_mom_0.9”

get_experiment_name(H, 1) ->
“l_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_m_0.9”



Solution：

By use of algorithm:TRIE (https://en.wikipedia.org/wiki/Trie) to solve the project.

Another way: use pygtrie (a Python library implementing a trie data structure).



Analysis: 

Some function still need optimization to reduce the executing time, for corner-cases possible problems, it may get slower if big dict dataset.



About time complexity:

The trie is a tree of nodes which supports Find and Insert operations. Find returns the value for a key string, and Insert inserts a string (the key) and a value into the trie. 
Both Insert and Find run in O(m) time (m is the length of the keys)  

