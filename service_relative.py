import sys, os.path, locale, urllib2
from subprocess import Popen, PIPE

clipboard_paths = []

for input_path in sys.argv[1:]:
    # This version checks for relative paths
    # Convert to Unicode
    adjusted_path = input_path.decode('UTF-8')
    homedir = os.path.join(os.path.expanduser('~').decode('UTF-8'), u'')
    # Compare path to user's home directory
    if adjusted_path.startswith(homedir):
        # File was within user's home directory, change to tilde relative form
        adjusted_path = os.path.join(u'~', adjusted_path.partition(homedir)[-1])
    # Now we safely encode the results
    path_url = 'finder://' + urllib2.quote(adjusted_path.encode('UTF-8'), safe='/~')
    clipboard_paths.append(path_url)

# Now we pass the results to pbcopy
if clipboard_paths:
    if len(clipboard_paths) > 1:
        stdin_str = '\n'.join(clipboard_paths) + '\n'
    else:
        stdin_str = clipboard_paths[0]
    try:
        pb = Popen(['pbcopy'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = pb.communicate(stdin_str)
    except:
        pass

sys.exit(0)
