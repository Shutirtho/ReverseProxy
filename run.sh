echo "Building Image for the Reverse Proxy Server......"
echo  "................................................"
docker build -t techallenge ./ReverseProxy/challenge/
echo "Running Reverse Proxy Server mapping your machine’s port 9999 to the container’s published port 9999......"
echo  "................................................"
echo "Container ID : "
docker run -d -p 9999:9999 techallenge
echo "Running tests.sh"
echo  "................................................"
./ReverseProxy/tests.sh 
echo "==================Server is running at http://localhost:9999  ==================================="