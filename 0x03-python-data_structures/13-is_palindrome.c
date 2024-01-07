#include "lists.h"
/**
 * add_front - add node at front
 * @head: input head
 * @n: input number
 * Return: the head
 */
listint_t *add_front(listint_t **head, int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return NULL;
	if (head == NULL)
		return NULL;
	new->n = n;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = *head;
		*head = new;
	}
	return (new);
}
/**
 * is_palindrome - check if palindrome
 * @head: input head
 * Return: true or false
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev_head = NULL;
	listint_t *current, *rev_curr;

	current = *head;
	while (current != NULL)
	{
		add_front(&rev_head, current->n);
		current = current->next;
	}
	current = *head;
	rev_curr = rev_head;
	while (current != NULL)
	{
		if (current->n != rev_curr->n)
		{
			free_listint(rev_curr);
			return (0);
		}
		current = current->next;
		rev_curr = rev_curr->next;
	}
	free_listint(rev_curr);
	return (1);
}
