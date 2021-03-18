Set up Zephyr project for Windows side: https://docs.zephyrproject.org/latest/getting_started/index.html 
Set up wsl1 with Ubuntu: https://docs.microsoft.com/en-us/windows/wsl/install-win10
On Windows install nrf tools from https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download
Put this folder to yours /mnt/c/Users/Magda/zephyrproject/zephyr/

On wsl find your zephyrproject:
$ cd /mnt/c/Users/Magda/zephyrproject

and build fake JLinkExe:
cc ./zephyr/wsl_jlink/JLinkExe.c -o ./zephyr/wsl_jlink/JLinkExe -g
The name 'JLinkExe" must match with the name in ~/zephyrproject/zephyr/scripts/west_commands/runners/jlink.py:
DEFAULT_JLINK_EXE = 'JLink.exe' if sys.platform == 'win32' else 'JLinkExe'

On wsl add to PATH directory of your fake JLinkExe:
$ export PATH=$PATH:/mnt/c/Users/Magda/zephyrproject/zephyr/wsl_jlink/
You can add this command to ~/.bashrc

To flash run from yours /mnt/c/Users/Magda/zephyrproject:
$ west flash --runner jlink

If you have zephyrproject in other dir than ~/ , then you will need to adjust paths in JLinkExe.c to your case.

in JLinkExe.c:
//TODO: generated runner.jlink has wrong path to hex like: /mnt/c/... so I changed it manually to
// my C:/Users/Magda/zephyrproject/zephyr/build/zephyr/zephyr.hex
sprintf(cmd, "scp %s Magda@localhost:~/zephyrproject/runner.jlink", argv[i]);