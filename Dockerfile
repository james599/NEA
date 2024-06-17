# specifies that there is a WSGI server running on port 8000
upstream app_server_flaskapp {
    server localhost:8000 fail_timeout=0;
}

# Nginx is set up to run on the standard HTTP port and listen for requests
server {
  listen 80;

  # nginx should serve static files and never send them to the WSGI server
  location /static {
    autoindex on;
    alias /static;
  }

  # requests that do not fall under /static are passed on to the WSGI
  # server that was specified above running on port 8000
  location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_redirect off;

    if (!-f $request_filename) {
      # port forwarding from 80 to 8000 (upstream function)
      proxy_pass http://app_server_flaskapp;
      break;
    }
  }
}