//https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
struct TreeNode {
    int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
            if(root == nullptr) return root;
        
            TreeNode* t = 0;
            t =  root -> left ;
            root -> left = root ->  right ;
            root -> right  = t;
            invertTree(root -> left);
            invertTree(root -> right);
            return root;

        
    }
};