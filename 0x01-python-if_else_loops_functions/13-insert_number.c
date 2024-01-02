#include "lists.h"
/**
 * insert_node - insert new node
 * @head: input head
 * @number: input value
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL)
	{
		free(new);
		return (NULL);
	}
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	if (current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		if (current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
