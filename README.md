# Preparing
1. Install **podman** or **docker**
1. Save the customized **default.conf.env** as **config.env**
2. Run (for running via docker export **CONTAINER=docker**):
```bash
make init
```
3. Run migration
```bash
make app-migrate
```
