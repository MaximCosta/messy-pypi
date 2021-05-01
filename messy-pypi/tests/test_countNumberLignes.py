import sys
sys.path.append('../') # Revient à la racine pour puouvoir revenir sur les import et n'influe pas sur linsteInsideFolder
from function.main_countlignes import countNumberOfLinesInFolderWithMatch

print(countNumberOfLinesInFolderWithMatch("../../"))