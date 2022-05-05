# Fixes needed - All are a must prior to publishing the code to upstream

[] The code references the internal (first problem) old and now broken (second
problem) location for the rhos-release rpm inside 
roles/infrared-horizon-selenium/tasks/main.yml
That should not happen, there is a specialized rhos-release task provided by
infrared. Please use that. See for example
plugins/tripleo-overcloud/build_templates.yml
This change should allow you to cleanup all the code which calls rhos-release.

[] The code should not unconditionally enable the EPEL repository and keep it
enabled, but just enable it when installing the relevant packages.

[x] Please also don't include the .venv directory which is currently in the
repository.

# Future

[] Create a project and user for conducting the test. Clean up when done.
This should replace the existing mechanism which creates/deletes the demo user

[] With python 3 you don't need to use *virtualenv*, but just
create a venv with *python3 -m venv*.

[] Complement the above with: Use the 'pip' ansible task and thus replace a
good part of roles/infrared-horizon-selenium/tasks/run_selenium_tests.yml
See:
docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html
