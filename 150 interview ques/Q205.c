/*https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define TABLE_SIZE 256

typedef struct Node {
    char key;
    char value;
    struct Node* next;
} Node;

// Corrected hash function to take char
unsigned int hash(char c) {
    return (unsigned char)c % TABLE_SIZE;
}

bool insert(Node* table[], char key, char value) {
    unsigned int h = hash(key);
    Node* temp = table[h];

    while (temp) {
        if (temp->key == key) {
            if (temp->value != value) return false; // inconsistent mapping
            else return true; // mapping already exists
        }
        temp = temp->next;
    }

    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->key = key;
    new_node->value = value;
    new_node->next = table[h];
    table[h] = new_node;
    return true;
}

bool isIsomorphic(char* s, char* t) {
    Node* s_to_t[TABLE_SIZE] = {0};
    Node* t_to_s[TABLE_SIZE] = {0};

    for (int i = 0; s[i] && t[i]; i++) {
        if (!insert(s_to_t, s[i], t[i])) return false;
        if (!insert(t_to_s, t[i], s[i])) return false;
    }

    return s[strlen(s)] == t[strlen(t)];
}
/*
===============================
  Isomorphic Strings in C
===============================

This code checks whether two strings are isomorphic.
Two strings are isomorphic if there’s a one-to-one character mapping 
between them such that each character from string `s` consistently maps 
to a character in string `t`, and vice versa.

Since C does not have built-in dictionaries or hashmaps, 
a custom hashmap is implemented using an array of linked lists.

----------------------------------
 Structures & Functions Explained:
----------------------------------

1. Node:
   - Represents a key-value pair in the hashmap.
   - Includes: key, value, and pointer to next node (for collision handling).

2. hash(char c):
   - Hashes the character using modulo with TABLE_SIZE (256).
   - Casts to unsigned char to avoid negative values.

3. insert(Node* table[], char key, char value):
   - Inserts a key-value mapping.
   - Checks if the key is already mapped inconsistently.
   - Returns false if conflict, true if valid.

4. isIsomorphic(char* s, char* t):
   - Uses two hash tables:
       - s_to_t: mapping from s → t
       - t_to_s: mapping from t → s
   - Validates character-by-character bijection.
   - Returns false if any conflict is found.

*/

///////////////////////////////////////////////////////////////
////////////////////     RAGE MODE 🔥     //////////////////////
///////////////////////////////////////////////////////////////
/*
 "BRO I BUILT A HASHMAP FROM SCRATCH 💥
  I FOUGHT SEGFAULTS ⚔️ 
  I GOT LOST IN POINTER HELL 😩 
  AND THEN I SEE PYTHON USERS SOLVE IT IN 1 LINE 😭
  
  3ms runtime. Beats 20%. Where's my medal?? 🥲

  And LeetCode said... no C solution in the 'optimum' section. 
  I'm fighting bosses out here while Python kids playing sudoku.

  I NEED A HUG AND A DEBUGGER 💀"
*/
