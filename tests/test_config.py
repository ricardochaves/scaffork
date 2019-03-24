import unittest

from scaffork.load_config import load_config_yaml


class TestConfig(unittest.TestCase):
    def test_load_config_yaml(self):

        config = load_config_yaml("./tests/data/.scaffork.yml")

        self.assertEqual(config.dict_["project_source"], "url to clone")
        self.assertEqual(config.dict_["project_name"], "my_project_name")
        self.assertEqual(config.dict_["project_dir"], "./tmp")
        self.assertEqual(config.dict_["use_github"], True)
        self.assertEqual(config.dict_["github_repo"], "repository name")
        self.assertEqual(config.dict_["github_is_private"], True)
        self.assertEqual(config.dict_["github_description"], "repository description")
        self.assertEqual(config.dict_["github_owner"], "user_account")
        self.assertEqual(config.dict_["github_is_organization"], True)
        self.assertEqual(config.dict_["github_has_issues"], True)
        self.assertEqual(config.dict_["github_has_projects"], True)
        self.assertEqual(config.dict_["github_has_wiki"], True)
        self.assertEqual(config.dict_["github_token"], "my personal github token")
        self.assertEqual(config.dict_["use_travis"], True)
        self.assertEqual(len(config.dict_["travis_envs"]), 1)
        self.assertEqual(config.dict_["use_codeclimate_maintainability"], True)
        self.assertEqual(config.dict_["use_codeclimate_coverage"], True)
        self.assertEqual(config.dict_["codeclimate_token"], "my code climate token")
