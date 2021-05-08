import sys

sys.path.append('../')
from functions.main_countlignes import countNumberOfLinesInFolderWithMatch

print("All ext\t",countNumberOfLinesInFolderWithMatch("../../", "(.py$|.md$|.png$|.txt$|LICENCE|.json$)"), "\t Pour être plus précis: (.py$|.md$|.png$|.txt$|LICENCE|.json$)")
print("py$ md$\t",countNumberOfLinesInFolderWithMatch("../../", "(.py$|.md$)"))
print("py$\t",countNumberOfLinesInFolderWithMatch("../../", ".py$"))
