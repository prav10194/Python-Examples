## LRU Cache

#### Problem Statment

We need to create 2 functions, get(key) and put(key, value)

get(key) will return the value of the key if found. 
Additional operations: update key as the most recently visited

put(key, value) will insert the key as most recently visited
Additional operations: Key might exist in the cache, in that case it needs to be updated. Also check the capacity and remove the least recently used key. 

#### Solution

To solve this problem we will save the keys as node of a Doubly Linked List. We will maintain a HashMap to save the nodes of the linked list. The left most node of the DLL will be the least recetly used key where as the right most node will be the most recently used key. 

Step 1: We need to create a ListNode class that will take key, value pair. The prev, next will be set as None by default. 

Step 2: In our LR Cache class, we need to initialize our HashMap <b>cache = {}</b> and our 2 starting nodes, left and right (which for now will be pointing to each other). 

Step 3: Define our 2 main functions, get and put. 

For get - we have to perform 2 actions. 
1. One of the main actions is to retrieve the value, if key exists in the cache map (value of the key can be accessed by retrieving the node and it's value). 
2. Then we would have to update the key as MR visited. This can be done by deleting the key and then creating a new key as MRU. 

For put - we have to perform 3 actions. 
1. Insert the key as MR visited. 
2. In case key exists, it needs to be updated with new value. (This can be done by deleting the key and then performing action 1)
3. In case length of the cache is greater than the capacity, delete the LR visited key. 

For performing the main 2 functions, we would need to create 2 more helpful functions. 

1. delete(key) - will delete the key from LL.
2. insert(key, value) - will insert the key as MR visited key. 
