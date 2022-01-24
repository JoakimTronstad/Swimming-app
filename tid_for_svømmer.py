import sqlite3
def main():
  conn = sqlite3.connect('swimmers.db')
  cur = conn.cursor()
  print('Data')
  cur.execute('SELECT * FROM Swimmers')
  for row in cur:
    print(row)
  conn.close()
if __name__ == '__main__': main()