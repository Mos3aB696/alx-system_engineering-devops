#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie_pid);
			sleep(1);
		}
		else
			exit(0);
	}
	return (0);
}
