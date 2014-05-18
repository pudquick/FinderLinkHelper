on open location theURL
	set newline to return
	set pythonScript to "
# Beginning of embedded python ... pretty evil, huh? #

import sys, urllib, os.path, subprocess

encoded_path = sys.argv[-1].rstrip().partition('finder://')[-1]
decoded_path = urllib.url2pathname(encoded_path).decode('UTF-8')
if decoded_path.startswith(u'~/'):
    homedir = os.path.expanduser('~').decode('UTF-8')
    relative_path = decoded_path.partition(u'~/')[-1]
    decoded_path = os.path.join(homedir, relative_path)
try:
    open_result = subprocess.check_call(['open', decoded_path.encode('UTF-8')])
except Exception:
    # Couldn't open the file
    # Return the decoded file path so we can pop an error dialog
    print decoded_path.encode('UTF-8'),

# End of python #
"
	set quotedScript to quoted form of pythonScript
	set filePath to do shell script "echo " & quotedScript & " | python - " & (quoted form of theURL)
	if (filePath is not equal to "") then
		--- We received a file path, indicating we couldn't open it
		display dialog ("Unable to open file:" & newline & newline & filePath) buttons {"OK"} default button "OK" with icon caution
	end if
end open location