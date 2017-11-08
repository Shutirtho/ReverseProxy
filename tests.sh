#! /bin/bash
declare -a app_endpoints=( 

	                    http://localhost:9999/listroutes 
	                    http://localhost:9999/stats 
	                    http://localhost:9999/listroutes/E 
	                    http://localhost:9999/listroutes/F
	                    http://localhost:9999/listroutes/J
	                    http://localhost:9999/listroutes/KT
	                    http://localhost:9999/listroutes/8BX
	                    http://localhost:9999/listroutes/56
	                    http://localhost:9999/listroutes/57
	                    http://localhost:9999/listroutes/N_OWL
	                    http://localhost:9999/listroutes/T_OWL
	                    http://localhost:9999/listroutes/60


	                    )
echo "Performing health checks of the following endpoints"
for i in "${app_endpoints[@]}"
do
    echo $i
    if curl -sI $i | grep HTTP | grep -v 200 > /dev/null ; then
    	echo "the above endpoints is not ok"
    	exit 1
    fi     
done
echo "---------------------------------"
echo "all endpoints are ok" 