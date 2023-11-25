public_ip=$(curl -s ifconfig.me)
echo "Getting public ip.........: $(public_ip)"
sudo sed -i "s/server_name.*/server_name $public_ip;/" /etc/nginx/sites-available/hhcproject
sudo ln -s /etc/nginx/sites-available/hhcproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx