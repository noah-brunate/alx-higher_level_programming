#include "lists.h"

/**
* check_cycle - function checks for cycles
* @list: pointer to the head node
*
* Return: returns 0 if there is no cycle and 1 else
*/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}


