#include <stdio.h>
#include <stdlib.h>
struct Node {
int key;
struct Node* left, *right;
};
struct Node* createNode(int key) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->key = key;
newNode->left = newNode->right = NULL;
return newNode;
}
struct Node* insert(struct Node* root, int key) {
if (root == NULL) {
return createNode(key);
}
if (key < root->key) {
root->left = insert(root->left, key);
} else if (key > root->key) {
root->right = insert(root->right, key);
}
return root;
}
struct Node* search(struct Node* root, int key) {
if (root == NULL || root->key == key) {
return root;
}
if (key < root->key) {
return search(root->left, key);
}
return search(root->right, key);
}
struct Node* minValueNode(struct Node* node) {
struct Node* current = node;
while (current->left != NULL) {
current = current->left;
}
return current;
}
struct Node* deleteNode(struct Node* root, int key) {
if (root == NULL) {
return root;
}
if(key<root->key){
root->left=deletenode(root->left,key);
}
else if(key>root->key){
root->right=deletenode(root->,key);
}
return root;
}
struct node* search(struct node* root,int key){
if(root==null||root->key){
return root;
}
if(key<root->key){
return search(root->left,key);
}
return search(root->right,key);
}
return search(root->right,key);
}

