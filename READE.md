#Repo for Airflow studies

##Setup:
In docker-compose.yml, define where your output directory is going to be. This can be set in the first line of "volumes".

##Demo 1:
When trigger_dag is executed and finished with success, target_dag starts. Files:
- target_dag
- trigger_dag

##Demo 2:
update_file_dag updates a file (some_file.txt), when this file is updated, this triggers consumer_dag. Files:
- update_file_dag
- consumer_dag
obs: Demo 1 creates directory and file that it's needed to Demo 2 to work.