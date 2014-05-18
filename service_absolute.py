import sys, os.path, locale, urllib2
from subprocess import Popen, PIPE

clipboard_paths = []

for input_path in sys.argv[1:]:
    # This version assumes absolute paths
    # Convert to Unicode
    adjusted_path = input_path.decode('UTF-8')
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
