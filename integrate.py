az postgres up --resource-group DjangoPostgres-blogAzure --location westeurope --sku-name B_Gen5_1 --server-name abazureblog --database-name pollsdb --admin-user canadian --admin-password D5c8bf123. --ssl-enforcement Enabled --storage-size 5120

az webapp up --resource-group DjangoPostgres-blogAzure --location westeurope --plan DjangoPostgres-tutorial-plan --sku F1 --name abazureblog

az webapp config appsettings set --settings DBHOST="ab_azureblog" DBNAME="pollsdb" DBUSER="canadian" DBPASS="D5c8bf123."

az webapp create-remote-connection --subscription 9af68c87-0379-4b7b-9c88-57b4055db1e9 --resource-group DjangoPostgres-blogAzure -n abazureblog &


{
  "connectionStrings": {
    "ado.net": "Server=abazureblog.postgres.database.azure.com;Database=pollsdb;Port=5432;User Id=canadian@abazureblog;Password=D5c8bf123.;",
    "jdbc": "jdbc:postgresql://abazureblog.postgres.database.azure.com:5432/pollsdb?user=canadian@abazureblog&password=D5c8bf123.",
    "jdbc Spring": "spring.datasource.url=jdbc:postgresql://abazureblog.postgres.database.azure.com:5432/pollsdb  spring.datasource.username=canadian@abazureblog  spring.datasource.password=D5c8bf123.",
    "node.js": "var client = new pg.Client('postgres://canadian@abazureblog:D5c8bf123.@abazureblog.postgres.database.azure.com:5432/pollsdb');",
    "php": "host=abazureblog.postgres.database.azure.com port=5432 dbname=pollsdb user=canadian@abazureblog password=D5c8bf123.",
    "psql_cmd": "psql --host=abazureblog.postgres.database.azure.com --port=5432 --username=canadian@abazureblog --dbname=pollsdb",
    "python": "cnx = psycopg2.connect(database='pollsdb', user='canadian@abazureblog', host='abazureblog.postgres.database.azure.com', password='D5c8bf123.', port='5432')",
    "ruby": "cnx = PG::Connection.new(:host => 'abazureblog.postgres.database.azure.com', :user => 'canadian@abazureblog', :dbname => 'pollsdb', :port => '5432', :password => 'D5c8bf123.')",
    "webapp": "Database=pollsdb; Data Source=abazureblog.postgres.database.azure.com; User Id=canadian@abazureblog; Password=D5c8bf123."
  },
  "host": "abazureblog.postgres.database.azure.com",
  "password": "D5c8bf123.",
  "username": "canadian@abazureblog"
}

{
  "URL": "http://abazureblog.azurewebsites.net",
  "appserviceplan": "DjangoPostgres-tutorial-plan",
  "location": "westeurope",
  "name": "abazureblog",
  "os": "Linux",
  "resourcegroup": "DjangoPostgres-blogAzure",
  "runtime_version": "python|3.7",
  "runtime_version_detected": "-",
  "sku": "FREE",
  "src_path": "G:\\blogAzure"
}