FinderLinkHelper
================

This is a combination of tools that allow you to create / open links with a "finder://" URI scheme, including "relative to your home directory" links

Opening the links require the helper application to be installed on the Mac where someone attempts to click the link.

How to use:

The important files are the .workflows and the .applescript.

The .workflows are used to create OS X services which are available when you right-click on a file/files in the Finder.

If you double-click the .workflows in the Finder, they will prompt to install (and end up in ~/Library/Services).

They add two right-click menu choices (under the 'Services' section at the bottom:
* "Finder Link - Relative"
* "Finder Link - Absolute"

Using Relative will generate links that if the original file is contained within your home directory (normally at /Users/yourname), the link you share with someone will open one located at a similar path in *their* home directory.

Using Absolute will instead always start from the root directory (/). So if your username is "mike", a link to a file on your Desktop named "example.txt" will include: /Users/mike/example.txt. Such a link would only open for the person you send it to if they also have a "/Users/mike/example.txt" (that exact file path) on their computer.

If you choose Relative but the file is located outside of your user home, it will generate an Absolute-style link.

If the file is not available, you'll get an error dialog showing what it attempted to open.
