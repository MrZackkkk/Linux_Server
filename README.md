# Home Server Configuration

This repository documents the architecture and configuration of my home server. It runs a variety of services orchestrated using Docker Compose.

## 🌐 Networking & Security

**Important Note:** This setup **does not use Nginx**. Instead, all external access and domain management are handled through **Cloudflare** (likely using Cloudflare Tunnels/Zero Trust) for enhanced security and ease of use.

*   **Cloudflare**: Manages the domain and provides secure access to services without opening ports manually.
*   **AdGuard Home**: Provides network-wide ad blocking and DNS services.

## 🐳 Services

The server hosts a suite of applications for media, productivity, and system management:

### Media Stack
*   **Plex**: The core media server for streaming content.
*   **Zurg + Rclone**: A specialized setup for mounting real-debrid content. Zurg acts as a WebDAV server which Rclone mounts to the filesystem, allowing Plex and Radarr to access it.

### Productivity & Tools
*   **Glance**: A modern dashboard to monitor and access all services.
*   **Filebrowser**: Web-based file manager for managing files on the server.
*   **NocoDB**: An open-source Airtable alternative, backed by a **PostgreSQL** database.
*   **Koillection**: A service to manage collections (books, games, etc.).
*   **Vaultwarden**: An unofficial Bitwarden server implementation for password management.

## 📂 Structure

The project is organized by service, with each directory containing its own `docker-compose.yml` and configuration files.

*(Note: The actual configuration files are primarily documented in `my_server_architecture.txt` and `folder_structure.txt`)*

## 📝 Generating Documentation

The documentation files `folder_structure.txt` and `my_server_architecture.txt` are generated using the following commands:

**Generate `folder_structure.txt`:**
```bash
tree -I 'node_modules|.git' > folder_structure.txt
```

**Generate `my_server_architecture.txt`:**
```bash
sudo find . -maxdepth 4 -not -path '*/.*' -name "docker-compose.yml" -print0 | sort -z | xargs -0 -I {} bash -c 'echo ""; echo "### FILE: {} ###"; cat "{}"' > my_server_architecture.txt
```

**Update Repository:**
```bash
git add my_server_architecture.txt folder_structure.txt
git commit -m "Update server documentation"
git pull origin main --no-rebase
git push origin main
```
