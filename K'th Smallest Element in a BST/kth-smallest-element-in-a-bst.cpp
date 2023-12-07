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
class Solution {
public:
    int count;
    int data;

    int kthSmallest(TreeNode* root, int k) {
        count = k;
        inOrderTraversal(root);
        return data;
    }

    void inOrderTraversal(TreeNode* node){
        if(node->left) inOrderTraversal(node->left);
        if(--count == 0 ){
            data= node->val;
            return;
        }
        if(node->right) inOrderTraversal(node->right);
    }
};
