---
id: TC-AC-ACTS-E2E-040-lintas-permukaan-filter-chip-dan-hapus-lewat-x
title: "Lintas Enam Permukaan: Filter, Opsi Terpilih Tampil sebagai Chip dan Dihapus Lewat (X)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-83
coverage:
  web: automated
---

# Lintas Enam Permukaan: Filter, Opsi Terpilih Tampil sebagai Chip dan Dihapus Lewat (X)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Permukaan yang diuji (tabel parameter; sedikitnya 11 baris data seed per permukaan, dengan sedikitnya dua nilai distinct pada kolom dropdown filter pertama; N total dari seeding, 8b butir 10):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | halaman awal TAG > Stock (dibuka hook `beforeEach`) |
| 2 | Detail SKU, Tab Available | Search SKU `RFID-ASSET-CORE-R5`, klik Device Name, Tab Available |
| 3 | Detail SKU, Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, klik Tab In Use |
| 4 | Modal Event Log (Tab Add Stock) | Detail SKU `RFID-ASSET-CORE-R5`, klik `[Event Log]` |
| 5 | Approvals > TAG Stock, Tab Active | Tutup modal Event Log (permukaan 4), lalu Sidebar Approvals > TAG Stock, Tab Active |
| 6 | Approvals > TAG Stock, Tab History | Sidebar Approvals > TAG Stock, Tab History |

- Opsi uji: dua opsi pertama pada dropdown filter pertama permukaan itu.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Untuk setiap baris tabel "Permukaan yang diuji", lakukan langkah 2 sampai 13
2. Buka permukaan sesuai kolom "Cara membuka"
3. Klik icon Filter
4. Centang opsi pertama dan opsi kedua di dropdown filter pertama
5. Verifikasi opsi pertama tampil sebagai chip di dalam field
6. Verifikasi opsi kedua tampil sebagai chip di dalam field
7. Klik (X) pada chip opsi pertama
8. Verifikasi chip opsi pertama hilang dari field
9. Buka dropdown filter pertama
10. Verifikasi opsi pertama ter-uncheck di dropdown
11. Verifikasi chip opsi kedua tetap tampil di dalam field
12. Klik `[Clear Field]`
13. Klik icon Filter untuk menutup panel

## Notes

- Pengulangan per permukaan (8b butir 7): langkah 2 sampai 13 diulang untuk enam permukaan pada tabel "Permukaan yang diuji" (parameter tiap iterasi ada di tabel, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa). Dihitung dengan ekspansi, spec ini sekitar 68 langkah.
- Alasan di atas sekitar 35 langkah (8b butir 7): satu TC memuat enam permukaan ("pada setiap permukaan") dan satu TC tetap satu spec; langkah yang diulang identik per permukaan dan iterasi berdiri sendiri.
- Langkah penghubung (S-03): langkah 2 (membuka permukaan), `[Clear Field]` (membersihkan draft, S-09; tanpa `[Apply]` sehingga tidak ada filter ter-Apply tersisa), dan langkah 13 (menutup panel). Modal Event Log (permukaan 4) ditutup lewat kolom «Cara membuka» permukaan 5 sebelum pindah ke sidebar Approvals (S-09).
- Temuan untuk QA: TC tidak menyebut nama field dropdown dan opsi yang dicentang; spec memakai dropdown filter pertama dan dua opsi pertamanya. Modal Event Log diuji pada Tab Add Stock (TC tidak menyebut tab).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
