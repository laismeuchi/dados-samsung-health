# Databricks notebook source
# dbutils.secrets.listScopes()
# dbutils.secrets.list(scope='samsung-health')

# COMMAND ----------

client_id = dbutils.secrets.get(scope='samsung-health', key='databrics-app-id')
client_secret = dbutils.secrets.get(scope='samsung-health', key='databricks-secret')
tenant_id = dbutils.secrets.get(scope='samsung-health', key='tenant-id')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://attachments@stshealthreader.dfs.core.windows.net/",
  mount_point = "/mnt/stshealthreader/attachments",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://bronze@stshealthreader.dfs.core.windows.net/",
  mount_point = "/mnt/stshealthreader/bronze",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://silver@stshealthreader.dfs.core.windows.net/",
  mount_point = "/mnt/stshealthreader/silver",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://gold@stshealthreader.dfs.core.windows.net/",
  mount_point = "/mnt/stshealthreader/gold",
  extra_configs = configs)

# COMMAND ----------

# display(dbutils.fs.ls("/mnt/stshealthreader/attachments/shealth"))

# COMMAND ----------

display(dbutils.fs.ls('/mnt/stshealthreader/attachments/shealth'))
