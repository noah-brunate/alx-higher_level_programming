#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* is_palindrome - function checks if list is palindrone
* @head: pointer to the head node
*
* Return: 1 if its plaindrone else 0
*/
int is_palindrome(listint_t **head)
{
	int len, flag, mid;
	listint_t *val = head;
	int *list;

	while (val != NULL)
	{
		list.append(val->n);
		len++;
		val = val->next;
	}
	mid = floor(len / 2);
	for (i = 0; i < mid; i++)
	{
		if (list[mid - 1] == list[mid + 1])
			flag++;
	}
	if (flag == mid)
		return (1);
	else
		return (0);
}


