#include "lists.h"
/**
 * check_cycle - check if there is a cycle
 * @list: input list
 * Return: true, false
 */
int check_cycle(listint_t *list)
{
	listint_t *step, *multi;

	if (list == NULL)
		return (0);
	step = list;
	multi = list->next;
	while (1)
	{
		if (step == multi)
			return (1);
		if (multi == NULL)
			return (0);
		step = step->next;
		multi = multi->next;
		if (multi == NULL)
			return (0);
		multi = multi->next;
	}
	return (0);
}
