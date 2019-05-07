all: graf_ec4.png dat_ec4.dat sol_ec4.x

graf_ec4.png: dat_ec4.dat graf_ec4.py
	python3 graf_ec4.py

dat_ec4.dat: sol_ec4.x
	./sol_ec4.x

sol_ec4.x: sol_ec4.cpp
	g++ sol_ec4.cpp -o sol_ec4.x

clean:
	rm -rf *.x *.dat *.png
