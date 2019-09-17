#include "lists.h"

/**
 * is_palindrome - checks if a LL is a palindrome or not
 * @head: the head of a linked list
 * Return: 1 if is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = NULL;
	listint_t *new = NULL;
	listint_t *tmp = NULL;
	int len = 0, half = 0;
	int pali = 1;

	if (!head)
		return (0);
	if (!(*head))
		return (1);

	h = *head;
	for (len = 0; h; len++)
		h = h->next;
	if (len == 1)
		return (1);

	h = *head;
	for (half = len / 2; half; half--, h = h->next)
		add_nodeint_end(&new, h->n);

	h = *head;
	for (tmp = new; tmp; tmp = tmp->next, h = h->next)
		if (tmp->n != h->n)
		{
			pali = 0;
			break;
		}
	free_listint(new);
	return (pali);
}
