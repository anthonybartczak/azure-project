az postgres up --resource-group DjangoPostgres-blogAzure --location westeurope --sku-name B_Gen5_1 --server-name abazureblog --database-name blogdb --admin-user canadian --admin-password D5c8bf123. --ssl-enforcement Enabled --storage-size 5120

az webapp up --resource-group DjangoPostgres-blogAzure --location westeurope --plan DjangoPostgres-tutorial-plan --sku F1 --name abazureblog

az webapp config appsettings set --settings DBHOST="abazureblog" DBNAME="blogdb" DBUSER="canadian" DBPASS="D5c8bf123."