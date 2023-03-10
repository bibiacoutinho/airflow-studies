# Repo for Airflow studies
## Setup:
In docker-compose.yml, define where your output directory is going to be. This can be set in the first line of "volumes".

## Demo 1:
When trigger_dag is executed and finished with success, target_dag starts. Files:
- target_dag
- trigger_dag

## Demo 2:
update_file_dag updates a file (some_file.txt), when this file is updated, this triggers consumer_dag. Files:
- update_file_dag
- consumer_dag

obs: Demo 1 creates directory and file that it's needed to Demo 2 to work.

## Demo 3:
Example: trigger manually update_file_dag to update some_file.txt, consumer2_dag will waits until update_file2_dag updates another_file.txt to be executed. consumer2_dag will only be triggered when both files gets updated. Files:
- update_file_dag
- update_file2_dag
- consumer2_dag

obs: Demo 1 creates directory and file that it's needed to Demo 3 to work.

## Demo 4:
TaskGroup structure. Files:
- group_dag.py
- groups/group_downloads.py
- groups/group_transforms.py

TaskGroup Structure: "transforms" task is open to show subtasks:

![](/imgs/taskgroup.png)

## Demo 5:
Branching example. Files:
- branching_dag.py

![](/imgs/branching.png)
