all: graf_ec4(1).png graf_ec4(2).png dat_ec4.dat sol_ec4.x

graf_ec4(1).png: dat_ec4.dat graf_ec4_1.py
	python3 graf_ec4_1.py

graf_ec4(2).png: dat_ec4.dat graf_ec4_2.py
	python3 graf_ec4_2.py

dat_ec4.dat: sol_ec4.x
	./sol_ec4.x

sol_ec4.x: sol_ec4.cpp
	g++ sol_ec4.cpp -o sol_ec4.x

clean:
	rm -rf *.x *.dat *.png
