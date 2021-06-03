config:
   plugin_type: test
   entry_point: main.yml
   # roles_path: ../  # Optional, contains relative path to a role
subparsers:
    
   selenium-plugin:
        description: This is a Selenium plugin to run UI tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Group one
              options:
                  boolflag:
                      type: bool
                      help: "simple boolean option"
                      default: true

                  otherboolflag:
                      type: bool
                      help: "another boolean flag option"
                      default: true

