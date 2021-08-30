# Blokos.io

## App Structure

- Users
  - Profiles 
    - Base: Model and functionality common to all users.
    - Manager:
      - Generated when registering directly at the main website.
      - Manages workspaces and all related components.
    - Members:
      - Team members for specific projects.

- Workspaces
  - Each user has a personal workspace as starting point.
  - Users can create or join* existing projects from their workspaces.
  - 

## Roadmap

- [x] Profiles 
- [x] Include Django admin docs
- [x] User creation to trigger default profile creation.
- [ ] FIX extra profiles creation for user from admin area
- [ ] 
- [ ] Include Django debug toolbar

## Utils

### Package Utils

```shell
# install pip-check if not yet installed
pip install pip-check

# check package versions from time to time
pip-check

pip install <package> --upgrade
```
