---
id: TC-FA-ASTL-UI-057-tabel-sort
title: "Siklus Sort kolom tabel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRT-3@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  "EB-SRT-3@tabel-all-assets": [3, 5, 6, 8, 9, 11, 12, 16, 17, 18]
anchor: [2, 14]
coverage:
  web: automated
---
# Siklus Sort kolom tabel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Tabel All Assets
- Data:
  - DU-057-1: Aset pertama: Name `Printer Laser - 1`, Asset ID `AST-0031`, Brand `Epson`, Status `Not Paired Yet`.
  - DU-057-2: Aset kedua: Name `Kursi Kerja - 1`, Asset ID `AST-0072`, Brand `Ikea`, Status `Available`.
  - DU-057-3: Aset ketiga: Name `Laptop Dell - 1`, Asset ID `AST-0101`, Brand `Dell`, Status `Available`.
- Kondisi:
  - K1: tabel memuat DU-057-1 sampai DU-057-3 dengan urutan bawaan Name A–Z, yaitu `Kursi Kerja - 1`, `Laptop Dell - 1`, lalu `Printer Laser - 1`.

## Test Steps

### Siklus tiga klik pada satu kolom
1. Tampilkan Tabel All Assets dengan kondisi K1
2. Verifikasi urutan baris `Kursi Kerja - 1`, `Laptop Dell - 1`, lalu `Printer Laser - 1`
3. Verifikasi kolom Photo tidak memiliki ikon sort
4. Klik header kolom Asset ID
5. Verifikasi indikator sort naik `↑` aktif pada kolom Asset ID
6. Verifikasi urutan baris `Printer Laser - 1`, `Kursi Kerja - 1`, lalu `Laptop Dell - 1`
7. Klik header kolom Asset ID
8. Verifikasi indikator sort turun `↓` aktif pada kolom Asset ID
9. Verifikasi urutan baris `Laptop Dell - 1`, `Kursi Kerja - 1`, lalu `Printer Laser - 1`
10. Klik header kolom Asset ID
11. Verifikasi indikator sort pada kolom Asset ID hilang
12. Verifikasi urutan baris kembali `Kursi Kerja - 1`, `Laptop Dell - 1`, lalu `Printer Laser - 1`

### Klik kolom lain memindahkan indikator
13. Klik header kolom Asset ID
14. Verifikasi indikator sort naik `↑` aktif pada kolom Asset ID
15. Klik header kolom Brand
16. Verifikasi indikator sort pada kolom Asset ID netral
17. Verifikasi indikator sort naik `↑` aktif pada kolom Brand
18. Verifikasi urutan baris `Laptop Dell - 1`, `Printer Laser - 1`, lalu `Kursi Kerja - 1`
