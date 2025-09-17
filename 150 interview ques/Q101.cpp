//https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
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
    bool isMirror(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    if (p->val != q->val) return false;

    return isMirror(p->left, q->right) && isMirror(p->right, q->left);
    }

    bool isSymmetric(TreeNode* root) {
    if (!root) return true; 
    return isMirror(root->left, root->right);
     }

};