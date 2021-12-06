/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

//accepted

class Solution {
public:
    int count = 0;
    vector<int> x = {0};
    vector<int> pathsums;
    
    void printv(vector<int>& v){
        for (int& elem: v){
            cout << elem << " ";
        }
        cout << endl;
    }
    
    void helper(TreeNode* root, int targetSum){
        if (root == NULL) return;
        
        pathsums.push_back(0);  //for the current element
                
        for(int &elem : pathsums){
            elem = elem + root->val;
            if (elem == targetSum) count++;
        }

        if (root->left != NULL){
            helper(root->left, targetSum);
        }
        if (root->right != NULL){
            helper(root->right, targetSum);
        }
        
        pathsums.pop_back();    
        for(int &elem : pathsums){
            elem = elem - root->val;
        }
    }
    int pathSum(TreeNode* root, int targetSum) {
        helper(root, targetSum);        
        return count;        
    }
};