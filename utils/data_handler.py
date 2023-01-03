import psycopg2
import psycopg2.extras
from psycopg2 import sql

class PostgreHandler:
    def __init__(self, database, host, user, password, debug = False):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.debug = debug
        self.connection = None
    
    def connect(self):
        self.connection = psycopg2.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host
        )
    
    def insert_data(self, table, data: dict):
        inserted = None
        if self.connection == None or self.connection.closed:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                insert_query = sql.SQL(
                    """
                    INSERT INTO {} ({})
                    VALUES ({})
                    RETURNING *;
                    """
                ).format(
                    sql.Identifier(table),
                    sql.SQL(',').join(map(sql.Identifier, data.keys())),
                    sql.SQL(',').join(map(sql.Literal,data.values()))   
                )
                cur.execute(insert_query)
                inserted = cur.fetchone()
                
            except Exception as e:
                print(f"Error during insert_data {e}")
        self.connection.close()       
        return inserted
    
    def get_data_all(self, table):
        result = []
        if self.connection == None or self.connection.closed:
            self.connect()
        try:
            with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                select_all = sql.SQL(
                    """
                        SELECT *
                        FROM {};
                    """
                ).format(
                    sql.Identifier(table)
                )
                cur.execute(select_all)
                result = cur.fetchall()
        except Exception as e:
            print(f"Error during get_all data {e}")
        self.connection.close()
        return result
                
    
    def get_data(self, table: str, columns:list, condition_column = None, condition_value = None):
        result = []
        if self.connection == None or self.connection.closed:
            self.connect()
        try:
            with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                if condition_column == None:
                    select_query = sql.SQL(
                        """
                        SELECT {}
                        FROM {}
                        """
                    ).format(
                        sql.SQL(',').join(map(sql.Identifier,columns)),
                        sql.Identifier(table)
                    )
                else:
                    select_query = sql.SQL(
                        """
                        SELECT {}
                        FROM {}
                        WHERE {} = {}
                        """
                    ).format(
                        sql.SQL(',').join(map(sql.Identifier,columns)),
                        sql.Identifier(table),
                        sql.Identifier(condition_column),
                        sql.Literal(condition_value)
                    )
                if self.debug == True:
                    print(select_query.as_string(cur))
                cur.execute(select_query)
                result = cur.fetchall()
        except Exception as e:
            print(f"Error during get_data {e}")
        self.connection.close()
        return result    
    
    def join_table_select_all(self, table_a, table_b, table_a_id, table_b_id = None, table_c = None, table_c_id = None):
        result = []
        if table_b_id == None:
            table_b_id = table_a_id
        
        if self.connection == None or self.connection.closed:
            self.connect()
        
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    if table_c == None:
                        join_query = sql.SQL(
                            """
                            SELECT *
                            FROM {}
                            JOIN {} ON {}.{} = {}.{}
                            """
                        ).format(
                            sql.Identifier(table_a),
                            sql.Identifier(table_b),
                            sql.Identifier(table_a),
                            sql.Identifier(table_a_id),
                            sql.Identifier(table_b),
                            sql.Identifier(table_b_id)
                        )
                        cur.execute(join_query)
                        result = cur.fetchall()
                    else:
                        if table_c_id == None:
                            table_c_id = table_b_id
                        join_query = sql.SQL(
                            """
                            SELECT *
                            FROM {}
                            JOIN {} ON {}.{} = {}.{}
                            JOIN {} ON {}.{} = {}.{}
                            """
                        ).format(
                            sql.Identifier(table_a),
                            sql.Identifier(table_b),
                            sql.Identifier(table_a),
                            sql.Identifier(table_a_id),
                            sql.Identifier(table_b),
                            sql.Identifier(table_b_id),
                            sql.Identifier(table_c),
                            sql.Identifier(table_b),
                            sql.Identifier(table_b_id),
                            sql.Identifier(table_c),
                            sql.Identifier(table_c_id)
                        )
                        cur.execute(join_query)
                        result = cur.fetchall()
                except Exception as e:
                    print(f"Error in join function {e}")
                
        self.connection.close()
        return result
    
    def update_item(self, table:str, set_column, set_value, condition_column:str, condition_value, ):
        if self.connection == None or self.connection.closed:
            self.connect()
        update_return = []    
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try: 
                
                update_query = sql.SQL(
                    """
                    UPDATE {}
                    SET {} = {}
                    WHERE {} = {}
                    RETURNING *
                    """
                ).format(
                    sql.Identifier(table),
                    sql.Identifier(set_column),
                    sql.Literal(set_value),
                    sql.Identifier(condition_column),
                    sql.Literal(condition_value)
                )
                if self.debug == True:
                    print(update_query.as_string(cur))
                cur.execute(update_query)
                update_return = cur.fetchone()
            except Exception as e:
                print(f"Error in update function {e}!")
                
        self.connection.close()
        return update_return
    
    def delete_item(self, table:str, condition_column:str, condition_value ):
        if self.connection == None or self.connection.closed:
            self.connect()
        delete_return = []    
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:  
                delete_query = sql.SQL(
                    """
                    DELETE FROM {}
                    WHERE {} = {}
                    RETURNING *
                    """
                ).format(
                    sql.Identifier(table),
                    sql.Identifier(condition_column),
                    sql.Literal(condition_value)
                )
                if self.debug == True:
                    print(delete_query.as_string(cur))
                cur.execute(delete_query)
                delete_return = cur.fetchone()
            except Exception as e:
                print(f"Error in update function {e}!")
                
        self.connection.close()
        return delete_return
        
        
        
    
