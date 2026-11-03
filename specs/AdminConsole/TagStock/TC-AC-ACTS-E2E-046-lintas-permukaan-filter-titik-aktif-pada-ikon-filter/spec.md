---
id: TC-AC-ACTS-E2E-046-lintas-permukaan-filter-titik-aktif-pada-ikon-filter
title: "Lintas Enam Permukaan: Filter, Ikon Filter Menampilkan Titik Aktif"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-89
coverage:
  web: automated
---

# Lintas Enam Permukaan: Filter, Ikon Filter Menampilkan Titik Aktif

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
| 5 | Approvals > TAG Stock, Tab Active | Tutup modal Event Log dengan klik (X), lalu sidebar Approvals > TAG Stock, Tab Active |
| 6 | Approvals > TAG Stock, Tab History | Sidebar Approvals > TAG Stock, Tab History |

- Opsi uji: opsi pertama pada dropdown filter pertama permukaan itu.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Untuk setiap baris tabel "Permukaan yang diuji", lakukan langkah 2 sampai 11
2. Buka permukaan sesuai kolom "Cara membuka"
3. Klik icon Filter
4. Pilih opsi pertama di dropdown filter pertama, klik `[Apply]`
5. Verifikasi icon Filter menampilkan badge titik tanpa angka saat panel terbuka
6. Klik icon Filter untuk menutup panel
7. Verifikasi icon Filter menampilkan badge titik tanpa angka saat panel tertutup
8. Klik icon Filter untuk membuka panel
9. Klik `[Clear Field]`, klik `[Apply]`
10. Verifikasi badge titik hilang dari icon Filter
11. Klik icon Filter untuk menutup panel

## Notes

- Pengulangan per permukaan (8b butir 7): langkah 2 sampai 11 diulang untuk enam permukaan pada tabel "Permukaan yang diuji" (parameter tiap iterasi ada di tabel, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa). Dihitung dengan ekspansi, spec ini sekitar 56 langkah.
- Alasan di atas sekitar 35 langkah (8b butir 7): satu TC memuat enam permukaan ("pada setiap permukaan") dan satu TC tetap satu spec; langkah yang diulang identik per permukaan dan iterasi berdiri sendiri.
- Langkah penghubung (S-03): langkah 2 (membuka permukaan) dan langkah 11 (menutup panel). Untuk permukaan 5, kolom "Cara membuka" menutup modal Event Log permukaan 4 lebih dulu (modal menutupi sidebar; hook `afterEach` tidak berjalan antar iterasi).
- Urutan langkah mengikuti keadaan: asersi titik saat panel terbuka ditulis sebelum panel ditutup (8b butir 5).
- Temuan untuk QA: TC menulis langkah 2 dan 3 sebagai satu urutan (`Pilih satu opsi, klik [Apply], tutup panel`) tetapi Expected (a) meminta titik diamati pada dua keadaan panel; spec mengamati keduanya.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
