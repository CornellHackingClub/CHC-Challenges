#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>  

const char *answers[] = {
        "Nope",
        "Haha. No.",
        "You wish.",
        "There's a chance.",
        "Yes!",
        "If you try, maybe.",
        "Well, I believe in you"
    };
const size_t answers_count = sizeof(answers) / sizeof(answers[0]);

int main(int argc, char *argv[]) {
	char question_buffer[100];
	if(argc < 2) {
		printf("Usage: %s <question>\n", argv[0]);
		exit(0);
	}
	if(argc > 1)                        
        strcpy(question_buffer, argv[1]);  
    else                                
        question_buffer[0] = 0;

	srand(time(NULL));
	int r = rand();
	printf("%d\n", r);
	r %= answers_count;
	printf("%d\n", r);
	
    printf("%s\n", answers[r]);
}