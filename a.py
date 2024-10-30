# Python script that will glob all files and folders in the currenct
# directory and print its structure with a tree format
def print_folder_tree():
    import glob
    import os
    from itertools import tee

    SEP = "|   "
    files = glob.glob("**", recursive=True)
    files.sort()
    files, files_orig = tee(
        files
    )  # saving original iterator to get total length of the files list
    files_len = sum(1 for _ in files_orig)  # getting length

    for idx, fpath in enumerate(files):  # noqa
        branches = ""
        segments = fpath.split(os.sep)

        for seg in segments[:-1]:
            branches += SEP if seg.strip() else "    "

        branch = "|-- " if segments[-1].strip() and idx != files_len - 1 else "`-- "
        branches += branch
        print(branches + segments[-1])


print_folder_tree()
