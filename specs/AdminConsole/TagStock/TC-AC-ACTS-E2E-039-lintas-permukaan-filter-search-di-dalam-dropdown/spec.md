---
id: TC-AC-ACTS-E2E-039-lintas-permukaan-filter-search-di-dalam-dropdown
title: "Lintas Enam Permukaan: Filter, Search di Dalam Dropdown Mempersempit Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-82
coverage:
  web: automated
---

# Lintas Enam Permukaan: Filter, Search di Dalam Dropdown Mempersempit Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Permukaan yang diuji (tabel parameter; sedikitnya 11 baris data seed per permukaan, dengan sedikitnya dua nilai distinct pada kolom dropdown filter pertama; N total dari seeding, 8b butir 10):

| No | Permukaan | Cara membuka | Dropdown filter pertama |
|---|---|---|---|
| 1 | Stock List | halaman awal TAG > Stock (dibuka hook `beforeEach`) | `Device Name` |
| 2 | Detail SKU, Tab Available | Search SKU `RFID-ASSET-CORE-R5`, klik Device Name, Tab Available | `Status` |
| 3 | Detail SKU, Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, klik Tab In Use | `Client` |
| 4 | Modal Event Log (Tab Add Stock) | Detail SKU `RFID-ASSET-CORE-R5`, klik `[Event Log]` | `Activity` |
| 5 | Approvals > TAG Stock, Tab Active | Tutup modal Event Log (permukaan 4), lalu Sidebar Approvals > TAG Stock, Tab Active | `Type` |
| 6 | Approvals > TAG Stock, Tab History | Sidebar Approvals > TAG Stock, Tab History | `Type` |

- Potongan nilai opsi: tiga karakter pertama salah satu opsi pada dropdown filter pertama permukaan itu, ditulis dengan huruf besar-kecil dibalik dari opsi aslinya (TC menyebut tiga karakter pertama salah satu opsi). Nilai yang tidak ada: `zzqxyz`.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Untuk setiap baris tabel "Permukaan yang diuji", lakukan langkah 2 sampai 12
2. Buka permukaan sesuai kolom "Cara membuka"
3. Klik icon Filter
4. Buka dropdown filter pertama sesuai kolom «Dropdown filter pertama»
5. Verifikasi dropdown memiliki kotak pencarian internal
6. Ketik potongan nilai opsi di kotak pencarian internal
7. Verifikasi daftar opsi menyempit sesuai substring yang diketik
8. Verifikasi penyaringan opsi tidak case-sensitive
9. Ganti isi kotak pencarian internal dengan `zzqxyz`
10. Verifikasi teks `No results found` tampil
11. Verifikasi hasil kosong dropdown berupa teks saja, tanpa ilustrasi
12. Tekan Esc untuk menutup dropdown, lalu klik icon Filter untuk menutup panel

## Notes

- Pengulangan per permukaan (8b butir 7): langkah 2 sampai 12 diulang untuk enam permukaan pada tabel "Permukaan yang diuji" (parameter tiap iterasi ada di tabel, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa). Dihitung dengan ekspansi, spec ini sekitar 62 langkah.
- Alasan di atas sekitar 35 langkah (8b butir 7): satu TC memuat enam permukaan ("pada setiap permukaan") dan satu TC tetap satu spec; langkah yang diulang identik per permukaan dan iterasi berdiri sendiri.
- Langkah penghubung (S-03): langkah 2 (membuka permukaan) dan 12 (menutup dropdown dan panel Filter). Modal Event Log (permukaan 4) ditutup lewat kolom «Cara membuka» permukaan 5 sebelum pindah ke sidebar Approvals (S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-82 menyebut dropdown filter pertama per permukaan (kolom tabel) dan potongan tiga karakter pertama salah satu opsi; spec membalik huruf besar-kecil potongan itu untuk mengasersi butir b (tidak case-sensitive).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
