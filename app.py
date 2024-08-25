from flask import Flask, render_template
import sqlitecloud
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
	conn = sqlitecloud.connect('sqlitecloud://cjl2u0m3sz.sqlite.cloud:8860?apikey=rYWBLxxIeLLKj5McdY2xWs5WpWExR9aIphV005t6wQA')
	db = 'journalDB'
	sql = """
		SELECT * FROM tbl_journal
	"""
	conn.execute(f"USE DATABASE {db}")
	query = conn.execute(sql)
	result = query.fetchall()
	return render_template('result.html', rows = result)
'''
for test purposes
	# multi = ''

	# for row in result:
	# 	data = f"{row[0]}|{row[1]}|{row[2]}"
	# 	multi += f"<ul>{data}</ul>"

	# return multi
'''
	# return render_template('result.html', rows = result)

@app.route('/insert')
def insert():
	conn = sqlitecloud.connect('sqlitecloud://cjl2u0m3sz.sqlite.cloud:8860?apikey=rYWBLxxIeLLKj5McdY2xWs5WpWExR9aIphV005t6wQA')
	db = 'journalDB'
	query = """
		INSERT INTO tbl_journal(journalDate, journalEntry)
		VALUES("2024-08-25", "second entry")
	"""
	conn.execute(f"USE DATABASE {db}")
	cursor = conn.execute(query)
	return 'insert success!'

if __name__ == '__main__':
	# app.run(port = 5002, debug = True)
	serve(app, host = '0.0.0.0', port = 5002)