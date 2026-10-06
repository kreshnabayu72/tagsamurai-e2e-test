---
id: TC-AC-ACAL-E2E-041-multi-field-edit-pencatatan-entri-terpisah
title: "Tab User Action — Mutasi multi-field menghasilkan N entri baris terpisah dengan timestamp identik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-241
coverage:
  web: automated
---

# Tab User Action — Mutasi multi-field menghasilkan N entri baris terpisah dengan timestamp identik

## Prerequisites

- Login sebagai Role: Principal Total Control
- Akses ke form edit di salah satu modul Admin Console (misal: Edit Distributor atau Edit Setting)

## Test Steps

1. Buka modul edit target (contoh: Edit Distributor)
2. Ubah 3 field sekaligus dalam satu kali submit:
   - Ubah `Company Name` dari "PT Maju" menjadi "PT Maju Bersama"
   - Ubah `Phone Number` dari "0812345678" menjadi "0819999888"
   - Ubah `Address` dari "Jl. Mawar 1" menjadi "Jl. Mawar 10"
3. Klik tombol `[Save]` untuk menyimpan perubahan
4. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
5. Verifikasi sistem mencatat tepat 3 baris entri log terpisah:
   - Baris 1: Field `Company Name`, Old Value `"PT Maju"`, New Value `"PT Maju Bersama"`
   - Baris 2: Field `Phone Number`, Old Value `"0812345678"`, New Value `"0819999888"`
   - Baris 3: Field `Address`, Old Value `"Jl. Mawar 1"`, New Value `"Jl. Mawar 10"`
6. Verifikasi nilai timestamp pada kolom `Date` dari ketiga baris tersebut identik presisi (tercatat dalam satu transaksi atomik)

## Notes

- Setiap perubahan field dicatat per-baris atomik untuk transparansi granularitas per field.
