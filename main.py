import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_V4qrJlVHjOQejE9hoSL@pg-2ddb00d3-mo-books.l.aivencloud.com:21804/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
