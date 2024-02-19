#1st Question 
#Using Apply Min-Max

tree = {
    'A': {
        'B': {'D': {'H': -1, 'I': 4}, 'E': {'J': 2, 'K': 6}},
        'C': {'F': {'L': -3, 'M': -5}, 'G': {'N': 0, 'O': 7}}
    }
}

# Min-Max Algorithm
def minimax(node, maximizing_player):
    if isinstance(node, int):
        return node

    if maximizing_player:
        best_value = float('-inf')
        for child in node.values():
            value = minimax(child, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node.values():
            value = minimax(child, True)
            best_value = min(best_value, value)
        return best_value


best_value = minimax(tree['A'], True)
print("The best value for the maximizer (A) is:", best_value)

# Define the tree structure based on the given problem
tree = {
    'value': None,
    'children': [
        {
            'value': None,
            'children': [
                {'value': -1, 'children': []},  # H
                {'value': 4, 'children': []}    # I
            ]
        },  # D
        {
            'value': None,
            'children': [
                {'value': 2, 'children': []},  # J
                {'value': 6, 'children': []}   # K
            ]
        },  # E
        {
            'value': None,
            'children': [
                {'value': -3, 'children': []},  # L
                {'value': -5, 'children': []}   # M
            ]
        },  # F
        {
            'value': None,
            'children': [
                {'value': 0, 'children': []},  # N
                {'value': 7, 'children': []}   # O
            ]
        }   # G
    ]
}

#2nd Question
# Using Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if 'children' not in node or not node['children']:
        return node['value']

    if maximizing_player:
        value = float('-inf')
        for child in node['children']:
            value = max(value, alpha_beta_pruning(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  
        return value
    else:
        value = float('inf')
        for child in node['children']:
            value = min(value, alpha_beta_pruning(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  
        return value


best_value = alpha_beta_pruning(tree, float('-inf'), float('inf'), True)
print("The best value for the maximizer (A) is:", best_value)