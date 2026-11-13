# Usulan Naik ke "Di Dalam Filter": Global Settings > Measurement

Modul: Global Settings > Measurement (Tabel Utama, Create, Edit, Delete, Bulk, Import, Unit Detail, Changelog, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Measurement`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-005 | Used By (Items): Item Type Nama Sama di FAMS dan Supply (Tote) dan Angka Besar 1250 (Mass) | High | Hitungan Used By yang salah bisa membuat unit dianggap tidak dipakai, lalu terhapus | Lolos | tidak |
| E2E-022 | Master Data Count Limit: Create di Batas, Dialog Cannot Add Unit, dan Form Tetap Terbuka | High | Kuota Master Data Count Limit melewati batas | Gagal: dialog lain menutupi | tidak |
| E2E-032 | Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap | Medium | Bulk action bisa melewati Selection Limit | Lolos | tidak |
| E2E-059 | Konflik Create dan Edit Unit oleh Dua Admin | High | Unit ganda dan edit yang menimpa perubahan admin lain | Lolos | tidak |
| E2E-060 | Konflik Delete, Bulk Delete, dan Buka Detail pada Unit yang Dihapus Admin Lain | High | Unit yang sudah dihapus admin lain bisa tercatat dihapus dua kali atau dibuka dari data basi | Lolos | tidak |
| E2E-061 | Konflik Unit Menjadi In-Use Saat Confirm Delete (Single dan Bulk) | High | Unit yang sedang dipakai bisa terhapus | Lolos | tidak |
| E2E-062 | Master Data Count Limit: Dua Admin Rebutan Slot Terakhir | Medium | Dua admin bisa melewati kuota Master Data Count Limit | Lolos | tidak |
| E2E-068 | Unit Hasil Import Type Measurement Dapat Diedit dan Dihapus seperti Unit Manual | Medium | Unit hasil import harus mengikuti aturan edit dan hapus yang sama dengan unit manual | Lolos | tidak |
| E2E-073 | Measurement Tidak Digate Plan: Create, Edit, Delete di Starter dan Enterprise serta Upgrade dan Downgrade | Medium | Plan yang salah membatasi atau membuka fitur Measurement, dan upgrade atau downgrade bisa mengubah data | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-006 (format tanggal General Settings): tampilan.
- E2E-010, E2E-011 (Guided Tooltip): tampilan, dampak rendah.
- E2E-012 (retensi state tab): tampilan.
- E2E-043 (Setup Column tabel): pola Setup Column yang seragam.
- E2E-046 (download Changelog dan Item Type List): spek ini lolos, dan pola download sudah dinilai di modul Brand.
- E2E-049, E2E-050, E2E-051, E2E-052 (Changelog Measurement: chip filter, sort, Setup Column): pola list yang seragam.
- E2E-075 (mobile Android): belum dijalankan.
- E2E-044 (state hover, fokus, focus trap): prioritas Low, dan gagal karena dialog menutupi.
- E2E-056, E2E-057 (Setup Column Unit Detail): prioritas Low.

## Catatan untuk FE/QA

- E2E-022 gagal karena dialog `Unit` ditutup overlay dialog lain. Ini masalah selector atau penanganan dialog di skrip, bukan spek. Asersi dialog `Cannot Add Unit` juga belum sesuai (`hasConfirmButton` bernilai `true`).
- E2E-062 mengasumsikan 1.000 unit, sedangkan Pre-setup menyebut 999 unit (`Lim 001` sampai `Lim 999`). Spec men-seed unit ke-1.000 sendiri. Perlu dicek QA.
- E2E-068 dan E2E-073 bergantung pada mekanisme Import dan perubahan plan yang belum didefinisikan di TC, PRD, atau LLD, jadi ditulis sebagai kemampuan tim FE/BE.
- Daftar ini hanya mencakup 23 spek yang diajukan untuk Measurement. Spek lain di modul ini belum dinilai.
