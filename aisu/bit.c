#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100
typedef struct {
    unsigned char bits[MAX_SIZE];
    int size;
} BitSet;
void initializeSet(BitSet *set) {
    for (int i = 0; i < MAX_SIZE; i++) {
        set->bits[i] = 0;
    }
    set->size = 0;
}
void addToSet(BitSet *set, int element) {
    if (element < MAX_SIZE && element >= 0) {
        set->bits[element] = 1;
        set->size++;
    }
}
void removeFromSet(BitSet *set, int element) {
    if (element < MAX_SIZE && element >= 0 && set->bits[element] == 1) {
        set->bits[element] = 0;
        set->size--;
    }
}
void unionSets(BitSet *result, const BitSet *set1, const BitSet *set2) {
    for (int i = 0; i < MAX_SIZE; i++) {
        result->bits[i] = set1->bits[i] | set2->bits[i];
    }
    result->size = set1->size + set2->size;
}
void intersectionSets(BitSet *result, const BitSet *set1, const BitSet *set2) {
    for (int i = 0; i < MAX_SIZE; i++) {
        result->bits[i] = set1->bits[i] & set2->bits[i];
    }
    result->size = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        if (result->bits[i] == 1) {
            result->size++;
        }
    }
}
void displaySet(const BitSet *set) {
    for (int i = 0; i < MAX_SIZE; i++) {
        printf("%d", set->bits[i]);
    }
    printf("\n");
}
int main() {
    BitSet setA, setB, resultSet;
    int element;
    initializeSet(&setA);
    initializeSet(&setB);
    initializeSet(&resultSet);
    printf("Enter elements for Set A (0-99, -1 to exit):\n");
    while (1) {
        scanf("%d", &element);
        if (element == -1) break;
        addToSet(&setA, element);
    }
    printf("Enter elements for Set B (0-99, -1 to exit):\n");
    while (1) {
        scanf("%d", &element);
        if (element == -1) break;
        addToSet(&setB, element);
    }
    printf("Set A: ");
    displaySet(&setA);
    printf("Set B: ");
    displaySet(&setB);

    unionSets(&resultSet, &setA, &setB);
    printf("Union (A | B): ");
    displaySet(&resultSet);

    intersectionSets(&resultSet, &setA, &setB);
    printf("Intersection (A & B): ");
    displaySet(&resultSet);
    return 0;
}

