How to install Google Chrome 28+ on Red Hat Enterprise Linux 6 ?

1. add repository
  # yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-el6/repo/epel-6/mosquito-myrepo-el6-epel-6.repo --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-dev/repo/epel-6/mosquito-myrepo-dev-epel-6.repo

2. add google's repository
  # echo -e "[google-chrome]\nname=google-chrome\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64\nenabled=1\ngpgcheck=0\ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" > /etc/yum.repos.d/google-chrome.repo

3. Install Chrome
  # yum update
  # yum-complete-transaction  # post script error
  # yum install google-chrome-unstable
