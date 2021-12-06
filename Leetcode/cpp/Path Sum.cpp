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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == NULL) return false;
        if (root->left == NULL && root->right == NULL){
            return targetSum == root->val;
        }
        bool retval = false;
        if (root->left != NULL){
            retval = hasPathSum(root->left, targetSum-root->val);
        }
        if (retval == false && root->right != NULL){
            retval = hasPathSum(root->right, targetSum-root->val);
        }
        return retval;
    }
};