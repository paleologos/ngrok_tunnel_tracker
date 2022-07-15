
echo "========================================================="
echo "Updating system"
echo "========================================================="
read -p "Press enter to continue / Pritisnite Enter da bi ste nastavili:  "
sleep 1 
sudo apt update -y
sudo apt upgrade -y

echo "========================================================="
echo "Installing curl "
echo "========================================================="
read -p "Press enter to continue / Pritisnite Enter da bi ste nastavili:  "
sleep 1 
sudo apt install curl -y
sleep 1 
read -p "Press enter to continue / Pritisnite Enter da bi ste nastavili:  "
