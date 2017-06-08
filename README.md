A while ago KiCad got a new footprint library system - all footprints are [github repositories](https://githtub.com/KiCad), great right? Yes, since then anybody can contribute and the times when everybody created their own libraries are mostly gone.

But the implementation in KiCad has a serious drawback, at least for me. For some bizarre reason KiCad does not download these libraries, but loads them from github on demand. If you want to work offline, say you are traveling or have bad internet access, you are trapped in the 21st century move-everything-to-cloud attitude.

Fortunately you can still clone the footprints and add them to KiCad. To automate the process of downloading and updating track of the github repositories I wrote following scripts.

In order to use them `git` and python3 package [`argpar`](https://pypi.python.org/pypi/argpar).

To clone the repos:
```sh
$ ./clone.sh [DIRECTORY]
$ ./gen_table.py -t ~/.config/kicad/fp-lib-table [DIRECTORY]
```
Note: `gen_table.py` accepts multiple directories.

To update the repos:
```sh
$ ./pull.sh [DIRECTORY]
$ ./gen_table.py [DIRECTORY]
```