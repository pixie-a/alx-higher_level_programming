#include "lists.h"
#include <stdlib.h>

/**
*add_nodeint - add new node at the beginning of listint_t list
*@head: head of listint_t
*@n: constant int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - check if a singly-linked-list is palindrome
*@head: pointer to the head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *he = *head;
	listint_t *no = NULL, *de = NULL;

	if (*head == NULL || he->next == NULL)
		return (1);
	while (he != NULL)
	{
		add_nodeint(&no, he->n);
		he = he->next;
	}
	de = no;
	while (*head != NULL)
	{
		if ((*head)->n != de->n)
		{
			free_listint(no);
			return (0);
		}
		*head = (*head)->next;
		de = de->next;
	}
	free_listint(no);
	return (1);
}
