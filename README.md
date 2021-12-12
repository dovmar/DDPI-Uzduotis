# DDPI-Uzduotis
Individuali didžiųjų duomenų programinių įrankių užduotis.


Programa suranda visus Hamiltono kelius grafe arba išveda žinutę kad tokie keliai grafe neegzistuoja.


Paleidimas:

```
sbatch -n branduoliu_kiekis batch.sh failo_pavadinimas 
```

Nepasirinkus `branduoliu_kiekis` programa bus paleidžiama su 20 branduolių.    



Pateikiami pavyzdiniai duomenų failai:

- small.csv 5 nodes 5 edges
- medium.csv 15 nodes 30 edges
- large.csv 40 nodes 58 edges
- small_no_paths.csv 5 nodes 5 edges and no Hamiltonian paths
