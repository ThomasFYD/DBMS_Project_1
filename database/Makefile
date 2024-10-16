
opendbms:
	sqlite3 ./schoolFacts.sqlite

drop:
	sqlite3 ./schoolFacts.sqlite < sql/drop_tables.sql

build:
	sqlite3 ./schoolFacts.sqlite < sql/buildTables.sql

clean:
	rm -f schoolFacts.sqlite

check:
	sqlite3 ./schoolFacts.sqlite < sql/dev.sql