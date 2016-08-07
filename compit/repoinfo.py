
import re

# Import tokens file
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__))))

import github3

from tmp.tokens import GITHUB_TOKEN
import exceptions



github = github3.login(token=GITHUB_TOKEN)

class RepoInfo:
    def __init__(self, user=None, repo=None, url=None):
        if user and repo:
            self._init_from_user_and_repo(user, repo)
        elif url:
            self._init_from_url(url)

        # If repo obj is not set by this time we have faield to init
        if not self._repo_obj:
            print("Failed!")
            return None


        self._url = url
    def _init_from_url(self, url):
        # init from url
        p = re.compile(r'(http[s]?:\/\/)?([^\/\s]+\/)(?P<username>[^(#|?|\/)]*)[+\/]?(?P<repository>[^(#|?|\/)]*)[+\/]?')
        m = p.search(url)
        user = m.group("username")
        repo = m.group("repository")
        print(user, repo)
        self._repo_obj = self._get_repo_obj(user, repo)


    def _init_from_user_and_repo(self, user, repo):
        # init from user, repo
        self._repo_obj = self._get_repo_obj(user, repo)


    def _get_repo_obj(self, user, repo):
        if not user:
            raise exceptions.URLInvalid("Could not decode user")
        if not repo:
            raise exceptions.URLInvalid("Could not decode repository")
        
        repo_obj = github.repository(user, repo)
        if not repo_obj:
            raise exceptions.RepositoryNotValid("Could not retrieve repository")
            
        return repo_obj



