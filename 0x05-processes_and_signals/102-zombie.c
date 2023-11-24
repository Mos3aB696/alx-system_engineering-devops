#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_loop - infinite loop
 *
 * Return: 0
 */
int infinite_loop(void)
{
	while (1)
		sleep(1);
	return (0);
}

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
	infinite_loop();
	return (0);
}
