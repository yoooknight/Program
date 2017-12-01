# /bin/bash
# YoooKnight

while true
do
    python /home/Python/STE_Class/STE_Class.py 1 >/dev/null 2 >&1
    
    res=`echo $?`
    if [ res=9 ]
    then
        exit
    fi

    sleep 1
done
