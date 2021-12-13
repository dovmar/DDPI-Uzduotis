# DDPI-Uzduotis
Individuali didžiųjų duomenų programinių įrankių užduotis.


Programa suranda visus Hamiltono kelius grafe arba išveda žinutę kad tokie keliai grafe neegzistuoja.


Paleidimas:

```
sbatch -n branduoliu_kiekis batch.sh failo_pavadinimas 
```

Nepasirinkus `branduoliu_kiekis` programa bus paleidžiama su 20 branduolių.    



Pateikiami pavyzdiniai duomenų failai kartu su jų rezultatais:

- [small.csv](https://github.com/dovmar/DDPI-Uzduotis/blob/main/results.981301.out) 5 nodes 5 edges
- [medium.csv](https://github.com/dovmar/DDPI-Uzduotis/blob/main/results.981306.out) 15 viršūnių 30 briaunų
- [large.csv](https://github.com/dovmar/DDPI-Uzduotis/blob/main/results.981374.out) 20 viršūnių 57 briaunos
- [small_no_paths.csv](https://github.com/dovmar/DDPI-Uzduotis/blob/main/results.981302.out)) 5 viršūnės 5 briaunos ir nėra Hamiltono kelių
- [large_no_paths.csv]( 40 viršūnės 58 briaunos ir nėra Hamiltono kelių
