#include "lists.h"

/**
* insert_node - function inserts node
* @head: pointer to the head node
* @number: number to be inserted
*
* Return: returns address of new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));

	if (temp == NULL)
		return (NULL);

	temp->n = number;
	temp->next = NULL;

	listint_t *temp1, *new = head;

	while (new != NULL)
	{
		if (new->n > number)
		{
			temp1 = new;
			new = temp;
			temp->next = temp1;
		}
		new = new->next;
	}
	return (temp);

