# It's a tough universe out there... #
... so here's a collection of command-line utilities that I find handy. All of them should be pretty self-explanatory and can be executed with the --help flag if you need more information.

Feel free to contact me if you have any questions.

## StrRexx ##
A really simple Rexx interpreter, written in Rexx. This is handy if you want to interactively play around with Rexx commands.

## Killchar ##
Recursively remove spaces and other annoying characters from file names

## Photog ##
A simple photo renaming appplication
For each image file in the current folder, replaces the prefix of the file name with a ten character string representing the date the photo was taken.

## Macsen's Transitioning Background (MTB) ##
A simple wallpaper switcher for Gnome 3

### Before you begin ###
There is a bit of manual configuration/set-up that needs to be done before you can use this utility.

MTB looks for image files in subfolders of the ~/Pictures/Backgrounds. You can use up to 24 folders, named 00 to 23. The folder name represents the hour at which MTB will start for looking in that folder for images.

If, for example, you have two folders named 08 and 17, MTB will start using the images in folder 08 at 08:00 and then switch to using folder 17 at 17:00.

You will need to manually create these folders before the script can be run. You will also neet to put some images in them.

### Randomising the lock screen ###
MTB will also randomise the lock screen, if desired. This is not time sensitive - you just need to have a one or more pictures in ~/Pictures/Backgrounds/lock

### Using MTB ###
MTB can be set to change backgrounds at any interval (in minutes), but you do need to configure it first with the --wait switch.

For example:
mtb --wait=15
... will set a wait time of 15 minutes between background switches.

If no wait time is set, a default of 20 minutes is used.

The switcher can be started by executing mtb with no options. This call is best added in your gnome startup applications.

Other options can be displayed with mtb -h