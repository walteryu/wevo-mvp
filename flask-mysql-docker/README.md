# WeVo Platform MVP

## Docker App with Flask and MySQL Tutorial

## Summary

Initial MVP with Docker app with Flask and MySQL; it will be developed into the full MVP based on customer interviews with additional features. User authentication, CRUD operations, voting feature and data visualization will be added soon.

### Installation

1. Verify that Docker and composer have been installed
* 1.1. For Windows, Docker toolbox may need to be installed
* 1.2. For Mac and Linux, run Docker with default installation
2. After Docker installation, git clone this repository
3. From within the root directory, run `./run_docker.sh`
4. App will open on Docker port, so visit it in the browser
* 4.1. For Windows, check port with `docker-machine ip default`
* 4.2. For Mac and Linux, Docker should open port on 5000

## Docker Cheatsheet

### OSX and Linux - Docker App

1. Install Docker for OSX or Linux
2. Docker should open in port as indicated in config files
* 2.1. Show Docker port with `docker-machine ip default`
* 2.2. Visit web browser and point to `<ip_address>:port`
3. From src dir, run docker-compose to spin up image
* 3.1. Image will need to be refreshed between edits
* 3.2. Run `docker-compose down -v` between runs to refresh SQL
* 3.3. Run `docker-compose up -d --no-dep --build` to rebuild
* 3.4. Finally, re-run `docker-compose up` to re-run image
* 3.5. All commands are stored in `run_docker.sh` script

### Windows - Docker Toolbox

1. Install Docker Toolbox for Windows 10 Home (non-Pro)
2. Virtualbox must be running before launching Toolbox
* 2.1. Toolbox uses Virtualbox to locate IP address
* 2.2. Show Docker port with `docker-machine ip default`
* 2.3. Visit web browser and point to `<ip_address>:port`
3. Toolbox will launch from its own Terminal window
* 3.1. Toolbox launches from its Program Files\Toolbox dir
* 3.2. So, it cannot find the repo dir; so need to navigate
* 3.3. Copy .bashrc file into Program Files\Toolbox dir
* 3.4. NOTE: DO NOT EDIT BASHRC IN WINDOWS; IT WILL CRASH!
* 3.5. Edit .bashrc in either Bash or text editor only
* 3.6. NOTE: DO NOT EDIT IN VISUAL STUDIO OR WINDOWS TOOLS
* 3.7. Execute .bashrc so that there is shortcut to src dir
4. From src dir, run docker-compose to spin up image
* 4.1. Image will need to be refreshed between edits
* 4.2. Run `docker-compose down -v` between runs to refresh SQL
* 4.3. Run `docker-compose up -d --no-dep --build` to rebuild
* 4.4. Finally, re-run `docker-compose up` to re-run image
* 4.5. All commands are stored in `run_docker.sh` script

### Citations

The Docker app is based on the tutorial and repository below:

* Medium article [tutorial](https://medium.com/@shamir.stav_83310/dockerizing-a-flask-mysql-app-with-docker-compose-c4f51d20b40d)
* Github [repository](https://github.com/stavshamir/docker-tutorial)
