PROJECT_NAME=dj_videos
PROJECT_PATH=/c/Users/AndreaHrelja/dj_videos/src
for dir in $(ls ${PROJECT_PATH}); do
    # Skip removing __pycache__ for `templates`
    # and all repositories containing a '.' (dot)
    if [[ ${dir} =~ templates|[\.]+ ]]; then continue; fi;
    
    rm ${PROJECT_PATH}/${dir}/__pycache__/ -r --dir
    if [ ${dir} = ${PROJECT_NAME} ]; then continue; fi;


    rm ${PROJECT_PATH}/${dir}/migrations/ -r --dir
    mkdir ${PROJECT_PATH}/${dir}/migrations
    touch ${PROJECT_PATH}/${dir}/migrations/__init__.py
done
