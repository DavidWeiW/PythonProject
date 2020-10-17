# Hyperparameter Naming project

# The project requires to train a machine learning model that accepts a set of tunable hyperparameters. The hyperparameters are specified in a Python dictionary as follows:
# H = {
#    “learning_rate”: 0.1,
#    “dropout_in”: 0.5,
#    “dropout_out”: 0.3,
#    “use_cutout”: True,
#    “use_skip”: False,
#    “momentum”: 0.9
# }

# The requirement is to serialize the hyperparameters into a string such that she can easily remember her experiments.
# for example, to create a function get_experiment_name(hyperparameters_dict, prefix_length=-1) that returns a string. prefix_length specifies the length of the hyperparameter prefix that will be reported in the experiment name string. In the case that two hyperparameters have the same prefix of length prefix_length, the function returns the minimum length prefix that can uniquely identify the hyperparameter.

# A few example usages are:
# get_experiment_name(H) -> “learningrate_0.1_dropoutin_0.5_dropoutout_0.3_usecutout_True_useskip_False_momentum_0.9”
# get_experiment_name(H, 3) ->
# “lea_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_mom_0.9”
# get_experiment_name(H, 1) ->
# “l_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_m_0.9”


# Solution:
# algorithm:TRIE https://en.wikipedia.org/wiki/Trie
# another way: use pygtrie (a Python library implementing a trie data structure).
# Following is my code:

g_leaf_ptrs = {}


class Node:
    def __init__(self):
        self.m_children_ptrs = {}
        self.m_parent_ptr = 0
        self.m_word_so_far = ''
        self.m_word = ''
        self.m_curr_index = 0

    def add_word(self, word, word_so_far='', curr_index=0, ptr=0):
        '''add_word is called upon the root'''
        try:
            self.m_word = word
            self.m_curr_index = curr_index
            self.m_parent_ptr = ptr
            if self.m_curr_index == len(self.m_word):
                self.m_word_so_far = word_so_far
                return
            else:
                ch = self.m_word[self.m_curr_index]
                self.m_word_so_far = word_so_far + ch

            if ch not in self.m_children_ptrs:
                self.m_children_ptrs.update({ch: Node()})
            self.m_children_ptrs.get(ch).add_word(self.m_word, \
                                                  self.m_word_so_far, self.m_curr_index + 1, self)
        except:
            print('{} : exception, please handle the error'.format('add_word'))

    def print_trie(self):
        ''''pass'''
        try:
            if self:
                if (len(self.m_children_ptrs) == 0):  # leaf node
                    g_leaf_ptrs.update({self.m_word_so_far: self})
                    print(self.m_word_so_far)
                else:
                    for i in self.m_children_ptrs:
                        self.m_children_ptrs.get(i).print_trie()
        except:
            print('{} : exception, please handle the error'.format('print_trie'))

    def find_unique_prefix(self, word):
        ''''pass'''
        try:
            if len(self.m_parent_ptr.m_children_ptrs) > 1:
                return self.m_word_so_far[0:-1]  # this is the unique prefix
            else:
                return self.m_parent_ptr.find_unique_prefix(word)
        except:
            print('{} : exception, please handle the error'.format('find_unique_prefix'))


def check_name(name_o, name_u, prefix_length):
    ''''pass'''
    if prefix_length <= 0:
        return name_o

    if len(name_u) > prefix_length:
        res = name_u
    else:
        res = name_o[:prefix_length]
    return res


hyperparameters_dict = {
    'learning_rate': 0.1,
    'dropout_in': 0.5,
    'dropout_out': 0.3,
    'use_cutout': True,
    'use_skip': False,
    'momentum': 0.9
}


def get_experiment_name(hp, prefix_length=-1):
    '''TRIE
        create a empty Node and invoke add_word on it
        thus populating the trie with the words'''
    try:
        removetable = str.maketrans('', '', '_')
        words_org = list(hp.keys())
        words = [s.translate(removetable) for s in words_org]
        words_unique = []
        # print(words)
        ####
        root = Node()
        for word in words:
            root.add_word(word)
        # print the trie
        root.print_trie()
        # for word in words:
        for i in range(len(words)):
            ptr = g_leaf_ptrs.get(words[i])
            unique_prefix = ptr.find_unique_prefix(words[i])
            words_unique.append(unique_prefix)
            name_final = check_name(words[i], unique_prefix, prefix_length)

            if words_org[i] in hp.keys():
                hp[name_final] = hp.pop(words_org[i])
        ####
        # print(words_unique)
        # output
        res_final = '_'.join([a + '_' + str(b) for (a, b) in hp.items()])
        # print(res_final)
        # print(hp)
        return res_final
    except:
        print('{} : exception, please handle the error'.format('get_experiment_name'))


result = get_experiment_name(hyperparameters_dict, 3)
print('Test Result: {}'.format(result))

