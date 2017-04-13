# -*- coding: utf-8 -*-  
  
#导入日志及pg模块  
import logging  
import logging.config  
import pg  
  
#日志配置文件名  
LOG_FILENAME = 'logging.conf'  
  
#日志语句提示信息  
LOG_CONTENT_NAME = 'pg_log'  
  
def log_init(log_config_filename, logname):  
    ''''' 
    Function:日志模块初始化函数 
    Input：log_config_filename:日志配置文件名 
           lognmae:每条日志前的提示语句 
    Output: logger 
    author: socrates 
    date:2012-02-12 
    '''  
    logging.config.fileConfig(log_config_filename)  
    logger = logging.getLogger(logname)  
    return logger  
  
def operate_postgre_tbl_product():  
    ''''' 
    Function:操作pg数据库函数 
    Input：NONE 
    Output: NONE 
    author: socrates 
    date:2012-02-12 
    '''    
    pgdb_logger.debug("operate_postgre_tbl_product enter...")   
      
    #连接数据库    
    try:  
        pgdb_conn = pg.connect(dbname = 'ktjl', host = '127.0.0.1', user = 'postgres', passwd = 'admin')  
    except Exception, e:  
         print e.args[0]  
         pgdb_logger.error("conntect postgre database failed, ret = %s" % e.args[0])      
         return      
       
    pgdb_logger.info("conntect postgre database(kevin_test) succ.")   
                
    #查询表 1         
    sql_desc = "select * from users"  
    for row in pgdb_conn.query(sql_desc).dictresult():  
        print row  
        pgdb_logger.info("%s", row)      
       
    #关闭数据库连接       
    pgdb_conn.close()         
    pgdb_logger.debug("operate_sqlite3_tbl_product leaving...")   
  
if __name__ == '__main__':   
      
    #初始化日志系统  
    pgdb_logger = log_init(LOG_FILENAME, LOG_CONTENT_NAME)     
      
    #操作数据库  
    operate_postgre_tbl_product()  