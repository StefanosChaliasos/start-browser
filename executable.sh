startbrowserpath=$PWD
touch openbrowser
chmod +rwx openbrowser
exec 3<> openbrowser
    echo "#!/bin/bash" >&3
    #echo "python $startbrowserpath/startbrowser">&3
    #echo "python $startbrowserpath/startbrowser $@">&3
    echo "python $startbrowserpath/startbrowser --browser chrome">&3
exec 3>&-

sudo mv openbrowser /usr/local/bin/openbrowser
