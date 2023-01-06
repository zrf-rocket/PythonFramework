# airflow framework
### AirFlow介绍
    airflow 是一个编排、调度和监控workflow的平台，由Airbnb开源，现在在Apache Software Foundation 孵化。airflow 将workflow编排为由tasks组成的DAGs(有向无环图)，调度器在一组workers上按照指定的依赖关系执行tasks。同时，airflow 提供了丰富的命令行工具和简单易用的用户界面以便用户查看和操作，并且airflow提供了监控和报警系统。
    Airflow的调度依赖于crontab命令，与crontab相比airflow可以直观的看到任务执行情况、任务之间的逻辑依赖关系、可以设定任务出错时邮件提醒、可以查看任务执行日志。

crontab命令管理的方式存在以下几方面的弊端：
1. 在多任务调度执行的情况下，难以理清任务之间的依赖关系；
2. 不便于查看当前执行到哪一个任务；
3. 任务执行失败时不便于查看执行日志，也即不方便定位报错的任务和错误原因；
4. 不便于查看调度流下每个任务执行的起止消耗时间，这对于优化task作业是非常重要的；
5. 不便于记录历史调度任务的执行情况，而这对于优化作业和错误排查是很重要的；








