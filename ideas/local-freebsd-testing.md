
$ mkdir -p vagrant/freebsd10
$ cd vagrant/freebsd10
# If using the libvirt provider
$ vagrant plugin install vagrant-mutate
$ vagrant box add --provider virtualbox freebsd/FreeBSD-10.3-RELEASE
$ vagrant mutate freebsd/FreeBSD-10.3-RELEASE libvirt
# Skip directly to here if using VirtualBox or VMWare
$ vagrant init -m freebsd/FreeBSD-10.3-RELEASE
# add 'config.ssh.shell = "sh"'
# add 'config.vm.hostname = "cpython.testing"'
$ vagrant up
$ vagrant ssh
# Following https://www.digitalocean.com/community/tutorials/how-to-install-git-on-freebsd-11-0
% sudo pkg tzsetup Australia/Brisbane
% sudo pkg install git
# Get the PR branch of interest
% git clone https://github.com/ncoghlan/cpython.git
% cd cpython
% git checkout -b ncoghlan-bpo-30647-skip-coercion-if-nl-langinfo-fails master
% git pull https://github.com/ncoghlan/cpython.git bpo-30647-skip-coercion-if-nl-langinfo-fails
# Build it (some optional modules won't build, but we don't care about those)
% ./configure && make


Configuration errors to figure out:

socket.gethostname() returns an empty string -> Set "config.vm.hostname" in Vagrantfile
test_create_tmp failure in test.test_mailbox -> Fixed by setting hostname
time.mktime() overflow error in test.test_email -> run 'sudo tzsetup Australia/Brisbane'
