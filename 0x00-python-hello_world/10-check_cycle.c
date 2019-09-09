#include "lists.h"

/**
 * check_cycle - check for a cycle in a linked list
 * @list: the list to check
 * Return: 1 if there is a cycle, 0 if there isn't a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	if ((list->next)->next == NULL)
		return (0);

	while (1)
	{
		x = x->next;
		if (x == y)
			return (1);
		if (x == NULL)
			return (0);
		x = x->next;
		if (x == y)
			return (1);
		if (x == NULL)
			return (0);

		y = y->next;
	}
}
