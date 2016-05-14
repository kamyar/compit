import github3

from tokens import GITHUB_TOKEN

github = github3.login(token=GITHUB_TOKEN)


class RepoInfo:
  def __init__(self, addr):
    self._addr = addr
    
