```find . -name "docker-compose.yml" -print0 | xargs -0 -I {} sh -c 'echo "\n\n### FILE: {} ###"; cat "{}"' > my_server_architecture.txt```

```tree -L 3 -I 'node_modules|venv|.git' > folder_structure.txt```
