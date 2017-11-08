echo "Building Image for the Reverse Proxy Server......"
echo  "................................................"
docker build -t techallenge ./ReverseProxy/challenge/>/dev/null
echo "Starting Reverse Proxy Server and mapping your machine’s port 9999 to the container’s published port 9999......"
echo  "................................................"
docker run -d -p 9999:9999 techallenge>/dev/null
echo "Running tests.sh"
echo  "................................................"
./ReverseProxy/tests.sh 
echo "==================Server is running at http://localhost:9999  ==================================="