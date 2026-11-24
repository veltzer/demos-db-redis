# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `scripts/redis_start.sh:2` - every redis script (start, stop, status, enable, disable) acts on `mysql.service`, copied from demos-db-mysql. They never touch redis and do change the MySQL server instead. Point them at `redis-server.service` (the Debian/Ubuntu unit name); the same fix is needed in `scripts/redis_stop.sh:3`, `scripts/redis_status.sh:2`, `scripts/redis_enable.sh:2` and `scripts/redis_disable.sh:2`.

## Medium

- `README.md:1` - the repo is called "Demos for the redis database", but it holds no redis demo at all (no redis-cli scripts, no client code), only the service helpers in `scripts/`. Add actual demos, or describe the repo for what it is. The README also has no blank line after its heading and no layout section (compare demos-db-mysql `README.md`).

## Low

- `scripts/redis_stop.sh:2` - `sudo systemctl daemon-reload` before `stop` does nothing for stopping a service and appears only in this script. Remove it.
- `scripts/` - demos-db-mysql has an install script (`scripts/mysql_install.sh`), but there is no `redis_install.sh` (`sudo apt install redis-server redis-tools`), so the start/enable scripts fail on a fresh machine. Add one.
