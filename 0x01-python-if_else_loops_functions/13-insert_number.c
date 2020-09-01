#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts number in sorted list
 * @head: address of head
 * @number: number to insert
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *temp;
	listint_t *new = malloc(sizeof(listint_t));

	if (!head)
		return (NULL);

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		temp = *head;
		*head = new;
		new->next = temp;
		return (new);
	}

	while (current)
	{
		if (current->next == NULL)
		{
			current->next = new;
			return (new);
		}
		if (number < current->next->n)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			return (new);
		}
		current = current->next;
	}
	free(new);
	return (NULL);
}
