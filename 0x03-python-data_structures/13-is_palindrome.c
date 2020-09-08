
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: double pointer to address of head of linked list
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *current = *head;
	listint_t *reverse = NULL;

	if (head)
	{
		while (fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		reverse = reverse_list(&slow);

		while (reverse)
		{
			if (current->n != reverse->n)
				return (0);
			reverse = reverse->next;
			current = current->next;
		}
	reverse_list(&slow);
	}
	return (1);
}

/**
 *  reverse_list - reverses linked list
 *  @head: double pointer to address of head
 *  Return: pointer to first node of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *reverse = NULL;
	listint_t *prev = *head;
	listint_t *next = *head;

	while (prev)
	{
		next = next->next;
		prev->next = reverse;
		reverse = prev;
		prev = next;
	}
	return (reverse);
}
