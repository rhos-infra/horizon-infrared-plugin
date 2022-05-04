---
config:
   plugin_type: test
   entry_point: main.yml
subparsers:
   selenium-plugin:
        description: This is a Selenium plugin to run UI tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Fetch repositories
              options:
                  geckodriver-base-url:
                      type: Value
                      help: "The download url for geckodriver"
                      default: "https://github.com/mozilla/geckodriver/releases/download/"

                  geckodriver-version:
                      type: Value
                      help: "The geckodriver version in format 0.nn.m to be downloaded"
                      default: "0.29.0"

                  horizon-selenium-repo:
                      type: Value
                      help: "The horizon repo containing selenium tests (required)"

                  horizon-selenium-branch:
                      type: Value
                      help: |
                          Currently this corresponds to the openstack version being tested
                          For example "rhos-16.1-trunk-patches

                  horizon-selenium-config:
                      type: Value
                      help: |
                          The location of the horizon.conf file to be used
                      default: "openstack_dashboard/test/integration_tests/local-horizon.conf"
     
