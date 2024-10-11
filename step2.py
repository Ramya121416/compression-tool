import heapq
from collections import defaultdict, Counter

# Step 1: Node class for Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char        # Character
        self.freq = freq        # Frequency of the character
        self.left = None        # Left child (0)
        self.right = None       # Right child (1)
    
    # Comparison function for priority queue (based on frequency)
    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Function to build the Huffman Tree
def build_huffman_tree(frequency):
    # Priority queue (min-heap) to store nodes
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    # Continue combining the two smallest nodes until only one remains
    while len(heap) > 1:
        node1 = heapq.heappop(heap)  # Smallest node
        node2 = heapq.heappop(heap)  # Second smallest node
        
        # Create a new internal node with combined frequency
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
    
    # Return the root of the Huffman Tree
    return heapq.heappop(heap)

# Step 3: Function to generate Huffman Codes by traversing the tree
def generate_codes(root, current_code, codes):
    if root is None:
        return
    
    # If it's a leaf node, assign the current code
    if root.char is not None:
        codes[root.char] = current_code
        return
    
    # Traverse left and right children
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Step 4: Function to encode data using the Huffman codes
def huffman_encode(data, codes):
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    return encoded_data

# Step 5: Function to decode the encoded data using the Huffman Tree
def huffman_decode(encoded_data, root):
    decoded_output = []
    current_node = root
    
    for bit in encoded_data:
        # Traverse left for '0' and right for '1'
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # If we reach a leaf node, append the character to the output
        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root  # Start from the root for the next character
    
    return ''.join(decoded_output)

# Main Function to perform Huffman Coding
def huffman_coding(data):
    # Step 1: Calculate frequency of each character
    frequency = Counter(data)
    
    # Step 2: Build the Huffman Tree
    huffman_tree_root = build_huffman_tree(frequency)
    
    # Step 3: Generate Huffman codes
    codes = {}
    generate_codes(huffman_tree_root, "", codes)
    
    # Step 4: Encode the data
    encoded_data = huffman_encode(data, codes)
    
    # Step 5: Decode the data to verify it works
    decoded_data = huffman_decode(encoded_data, huffman_tree_root)
    
    return encoded_data, decoded_data, codes

# Test the implementation
if __name__ == "__main__":
    # Example input data
    data = "huffman coding is fun!"
    
    # Perform Huffman Coding
    encoded_data, decoded_data, codes = huffman_coding(data)
    
    # Output results
    print("Original Data:", data)
    print("Encoded Data:", encoded_data)
    print("Decoded Data:", decoded_data)
    print("Huffman Codes:", codes)
