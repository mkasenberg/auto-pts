#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    int change_name = 0;
    if(argc <= 1)
        printf("This program should be run by \'west flash --runner jlink\' command, which will provie arguments");

    // for(int i = 0; i < argc; i++) {
    //     fprintf(stderr, "argv[%d]%s\n", i, argv[i]);
    // }

    //Cheat checking version of JLink. JLink runner parses output to take version.
    if(strcmp(argv[1], "-bogus-argument-that-does-not-exist") == 0) {
        fprintf(stdout, "SEGGER J-Link Commander V6.88 (Compiled Nov 18 2020 16:08:22)\nDLL version V6.88, compiled Nov 18 2020 16:08:10\n");
        fflush(stdout);
        sleep(2);
        exit(0);
    }

    char cmd[1000];
    char sshcmd[800];
    sprintf(sshcmd, "JLink.exe ");
    for(int i = 1; i < argc; i++) {
        if(change_name == 1) {
            sprintf(sshcmd + strlen(sshcmd), "runner.jlink ");
            //TODO: it has wrong path to hex like: /mnt/c/... so I changed it manually to
            // my C:/Users/Magda/zephyrproject/zephyr/build/zephyr/zephyr.hex
            sprintf(cmd, "scp %s Magda@localhost:~/zephyrproject/runner.jlink", argv[i]);
            system(cmd);
        } else {
            sprintf(sshcmd + strlen(sshcmd), "%s ", argv[i]);
            change_name = 0;
            if(strcmp(argv[i], "-CommanderScript") == 0) {
                change_name = 1;
            }
        }
    }
    sprintf(cmd, "ssh Magda@localhost \"cd ~/zephyrproject/zephyr/wsl_jlink && %s\"", sshcmd);
    system(cmd);
}
