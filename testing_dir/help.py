def print_git_commands():
        git_commands = [
        ("git init", "Initializes a new Git repository."),
        ("git clone [repository URL]", "Creates a local copy of a remote repository."),
        ("git status", "Displays the current status of your local repository."),
        ("git add [file] or git add .", "Stages changes for the next commit."),
        ("git commit -m 'Commit message'", "Records staged changes in the repository."),
        ("git push origin [branch]", "Uploads local commits to the remote repository."),
        ("git pull origin [branch]", "Fetches and merges changes from the remote repository."),
        ("git checkout -b [new-branch-name]", "Creates a new branch and switches to it."),
        ("git checkout [branch-name]", "Changes to an existing branch."),
        ("git merge [branch]", "Combines changes from one branch into another."),
        ("git log", "Displays a log of all commits."),
        ("git reset [file] or git reset --hard HEAD", "Removes changes from the staging area or discards all changes."),
        ("touch .gitignore", "Creates a file to specify which files and directories to ignore."),
        ("git checkout [commit-hash]", "Moves the repository to a specific commit."),
        ("git push origin [new-branch]", "Uploads a new branch to the remote repository."),
        ("git ls-tree -r main", "Displays a recursive tree of files in the 'main' branch."),
        ("git branch","Lists all local branches."),
        ("git branch -m <branch>","Renames a local branch ."),
        ("git tag","Lists all tags."),
        ("git tag -a <tag name>","Creates an annotated tag."),
        ("git log --follow <file>","Shows the commit history of a file, including renames."),
        ("git reset --soft <commit>","Resets the HEAD pointer to the specified commit without changing files."),
        ("git ls-tree", ["List files in a commit/tree",
                             "-r - Recurse into subdirectories",
                             "-l - List blob object names instead of file paths",
                             "-t - Show object type"]),

        ("git branch", "Lists all local branches."),

        ]
        for command, function in git_commands:
            print(f"{command.ljust(40)} {function}")

# Call the function to print the table
print_git_commands()

