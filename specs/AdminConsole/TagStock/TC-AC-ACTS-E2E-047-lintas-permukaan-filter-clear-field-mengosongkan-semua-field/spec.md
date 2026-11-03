---
id: TC-AC-ACTS-E2E-047-lintas-permukaan-filter-clear-field-mengosongkan-semua-field
title: "Lintas Enam Permukaan: Filter, Tombol Clear Field Mengosongkan Semua Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-90
coverage:
  web: automated
---

# Lintas Enam Permukaan: Filter, Tombol Clear Field Mengosongkan Semua Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Permukaan yang diuji (tabel parameter; sedikitnya 11 baris data seed per permukaan, dengan sedikitnya dua nilai distinct pada kolom dropdown filter pertama; N total dari seeding, 8b butir 10):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | halaman awal TAG > Stock (dibuka hook `beforeEach`) |
| 2 | Detail SKU, Tab Available | Search SKU `RFID-ASSET-CORE-R5`, klik Device Name, Tab Available |
| 3 | Detail SKU, Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, klik Tab In Use |
| 4 | Modal Event Log (Tab Add Stock) | Detail SKU `RFID-ASSET-CORE-R5`, klik `[Event Log]` |
| 5 | Approvals > TAG Stock, Tab Active | Tutup modal Event Log dengan klik (X), lalu sidebar Approvals > TAG Stock, Tab Active |
| 6 | Approvals > TAG Stock, Tab History | Sidebar Approvals > TAG Stock, Tab History |

- N total baris tiap permukaan diturunkan dari seeding (sedikitnya 11 baris) dan dicatat sebagai baseline jumlah baris tabel tanpa filter sebelum uji (8b butir 10).
- Field uji: dua dropdown pertama pada panel Filter diisi dengan opsi pertama masing-masing ("isi beberapa field").
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Untuk setiap baris tabel "Permukaan yang diuji", lakukan langkah 2 sampai 10
2. Buka permukaan sesuai kolom "Cara membuka"
3. Catat jumlah baris tabel tanpa filter sebagai baseline
4. Klik icon Filter
5. Isi dua dropdown pertama dengan opsi pertama masing-masing
6. Klik `[Clear Field]`
7. Verifikasi seluruh field kembali kosong dengan placeholder
8. Klik `[Apply]`
9. Verifikasi jumlah baris tabel sama dengan baseline (tabel menampilkan semua data)
10. Klik icon Filter untuk menutup panel

## Notes

- Pengulangan per permukaan (8b butir 7): langkah 2 sampai 10 diulang untuk enam permukaan pada tabel "Permukaan yang diuji" (parameter tiap iterasi ada di tabel, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa). Dihitung dengan ekspansi, spec ini sekitar 50 langkah.
- Alasan di atas sekitar 35 langkah (8b butir 7): satu TC memuat enam permukaan ("pada setiap permukaan") dan satu TC tetap satu spec; langkah yang diulang identik per permukaan dan iterasi berdiri sendiri.
- Langkah penghubung (S-03): langkah 2 (membuka permukaan), pencatatan baseline, dan langkah 10 (menutup panel). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi).
- Temuan untuk QA: TC tidak menyebut jumlah field yang diisi dan nilainya; spec memakai dua dropdown pertama. Expected (b) "semua data" ditulis relatif terhadap baseline jumlah baris.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
