# version code 6adf56d2e064+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.





## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of
              - the senator's last name,
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example:
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    vote_record_dict = {}

    for string in strlist:
        data = string.split(' ')
        vote_record_dict[data[0]] = [int(x) for i, x in enumerate(data) if i > 3]

    return vote_record_dict


## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2

    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253

    You should definitely try to write this in one line.
    """
    return sum([x * y for (x, y) in zip(voting_dict.get(sen_a), voting_dict.get(sen_b))])



## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """
    current_most_similar = 0
    most_similar_sen = ''
    for sen_name in voting_dict.keys():
        if sen == sen_name:
            continue
        most_similar = policy_compare(sen, sen_name, voting_dict)
        if most_similar > current_most_similar:
            most_similar_sen = sen_name
            current_most_similar = most_similar
    return most_similar_sen



## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
        >>> least_similar('c', vd)
        'b'
    """
    current_least_similar = float('infinity')
    least_similar_sen = ''
    for sen_name in voting_dict.keys():
        if sen == sen_name:
            continue
        least_similar = policy_compare(sen, sen_name, voting_dict)
        if least_similar < current_least_similar:
            least_similar_sen = sen_name
            current_least_similar = least_similar
    return least_similar_sen



## 5: (Task 2.12.5) Chafee, Santorum
most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold'



## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    tot = 0
    for sen_name in sen_set:
        tot += sum([x * y for (x, y) in zip(voting_dict.get(sen), voting_dict.get(sen_name))])
    return tot / len(sen_set)


def create_senator_set(strlist):
    senator_set = set([])
    for string in strlist:
        data = string.split(' ')
        senator_set.add(data[0])
    return senator_set


def find_democrats(strlist):
    democrats = set([])
    for string in strlist:
        data = string.split(' ')
        if data[1] == 'D':
            democrats.add(data[0])
    return democrats


def find_greast_average(sen_set, sen_subset, voting_dict):
    greatest_avg = -float('infinity')
    greatest_avg_sen = ''
    for sen in sen_set:
        avg = find_average_similarity(sen, sen_subset, voting_dict)
        if avg > greatest_avg:
            greatest_avg = avg
            greatest_avg_sen = sen
    return greatest_avg_sen


most_average_Democrat = 'Biden' # give the last name (or code that computes the last name)



## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example:
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    averages = []
    for sen in sen_set:
        votes = voting_dict.get(sen, [])
        if not averages:
            averages = votes
        else:
            averages = [vote + avg for (vote, avg) in zip(votes, averages)]
            # [vote + averages[i] for (i, vote)  in enumerate(votes)]
    return [avg / float(len(sen_set)) for avg in averages]


average_Democrat_record = [-0.23255813953488372, 1.0, 0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116, -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]  # give the vector as a list



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example:
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    rivals = ()
    similarity = float('infinity')
    for i, sen_a in enumerate(list(voting_dict.keys())):
        for j, sen_b in enumerate(list(voting_dict.keys())[i+1:]):
            new_similarity = policy_compare(sen_a, sen_b, voting_dict)
            if new_similarity < similarity:
                similarity = new_similarity
                rivals = (sen_a, sen_b)

    return rivals
