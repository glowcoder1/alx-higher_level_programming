#include "lists.h"

/**
 * print_dlistint - function that prints all the elements of a dlistint_t list
 * @h: pointer to head of the list
 * Return: counts of the elements in list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *curr = h;

	while (curr != NULL)
	{
		printf("%i\n", curr->n);
		count++;
		curr = curr->next;
	}
	return (count);
}
