#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node into a sorted linked list
 * @head: the sorted linked list
 * @number: the number to add
 * Return: the address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *prevnode = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);
	prevnode = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	/* If the number goes on front */
	if (!prevnode || prevnode->n > number)
	{
		*head = new;
		new->next = prevnode;
		return (new);
	}

	/* If the number goes in the middle or on the end */
	while (1)
	{
		if (!(prevnode->next) || ((prevnode->next)->n > number))
			break;
		prevnode = prevnode->next;
	}

	temp = prevnode->next;
	prevnode->next = new;
	new->next = temp;
	return (new);
}
