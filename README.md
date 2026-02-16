# Home Server Configuration

This repository documents the architecture and configuration of my home server. It runs a variety of services orchestrated using Docker Compose.

## 🌐 Networking & Security

**Important Note:** This setup **does not use Nginx**. Instead, all external access and domain management are handled through **Cloudflare** (likely using Cloudflare Tunnels/Zero Trust) for enhanced security and ease of use.

*   **Cloudflare**: Manages the domain and provides secure access to services without opening ports manually.
*   **Tailscale**: A mesh VPN used for secure remote access to the home network.
*   **AdGuard Home**: Provides network-wide ad blocking and DNS services.

## 🐳 Services

The server hosts a suite of applications for media, productivity, and system management:

### Media Stack
*   **Plex**: The core media server for streaming content.
*   **Zurg + Rclone**: A specialized setup for mounting real-debrid content. Zurg acts as a WebDAV server which Rclone mounts to the filesystem, allowing Plex and Radarr to access it.
*   **Radarr**: Movie collection manager.
*   **Prowlarr**: Indexer manager for Radarr and other *arr apps.
*   **Overseerr**: Request management and media discovery tool.

### Productivity & Tools
*   **Glance**: A modern dashboard to monitor and access all services.
*   **Filebrowser**: Web-based file manager for managing files on the server.
*   **NocoDB**: An open-source Airtable alternative, backed by a **PostgreSQL** database.
*   **Koillection**: A service to manage collections (books, games, etc.).
*   **Vaultwarden**: An unofficial Bitwarden server implementation for password management.
*   **KV**: A custom lightweight key-value/notes application.

## 📂 Structure

The project is organized by service, with each directory containing its own `docker-compose.yml` and configuration files.

*(Note: The actual configuration files are primarily documented in `my_server_architecture.txt` and `folder_structure.txt`)*

## 🛠️ Maintenance & Debugging

The following commands can be used to generate the documentation files:

### Generate Server Architecture
This command finds all `docker-compose.yml` files and concatenates them into `my_server_architecture.txt`.

```bash
find . -name "docker-compose.yml" -print0 | xargs -0 -I {} sh -c 'echo "\n\n### FILE: {} ###"; cat "{}"' > my_server_architecture.txt
```

### Generate Folder Structure
This command generates a tree view of the directory structure, excluding common ignore patterns, and saves it to `folder_structure.txt`.

```bash
tree -L 3 -I 'node_modules|venv|.git' > folder_structure.txt
```
