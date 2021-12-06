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
    void helper (TreeNode* root, int targetSum, vector<vector<int>>& paths, vector<int>& currpath){
        if (root == NULL) return;
        currpath.push_back(root->val);
        //leaf node
        if (root->left == NULL && root->right == NULL){
            if (targetSum == root->val){
                paths.push_back(currpath);
            }
        }
        if (root->left != NULL){
            helper(root->left, targetSum-root->val, paths, currpath);
        }
        if (root->right != NULL){
            helper(root->right, targetSum-root->val, paths, currpath);
        }
        currpath.pop_back();
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> paths;
        vector<int> path;
        helper(root, targetSum, paths, path);
        return paths;        
    }
};