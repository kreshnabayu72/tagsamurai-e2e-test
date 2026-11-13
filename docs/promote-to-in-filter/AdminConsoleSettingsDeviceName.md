# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Device Name

Modul: Admin Console > Settings > Device Name (List, Create, Edit, Delete, Bulk Delete, Sidebar Category, Usage by Company, Changelog, Guided Tooltip, Mobile)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsDeviceName`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-078 | Bulk Delete: Selection Limit (Checkbox Disabled dan Select All Dipotong) | High | Bulk delete bisa melewati Selection Limit | Belum dijalankan | tidak |
| E2E-167 | Download di Atas 5.000 Baris dan Create Tidak Ikut Master Data Count Limit | High | Create bisa melewati Master Data Count Limit | Belum dijalankan | tidak |
| E2E-175 | Rename Device Name yang Memiliki Unit BYO Hardware atau TAG Tidak Memutus Relasi | High | Rename bisa memutus relasi unit yang sudah terdaftar | Gagal: dialog lain menutupi | tidak |
| E2E-179 | Konkurensi Create: Duplikat setelah Pengecekan Lolos dan Measurement Dihapus Admin Lain | High | Dua admin bisa membuat nama ganda | Gagal: TreeSelectDialog tidak ditemukan | belum jelas: perlu dicek apakah ini helper atau UI |
| E2E-180 | Konkurensi: Category Dihapus atau Mendapat Subcategory (Create) dan SKU Baru dari Sesi Lain saat Edit Category | High | Data relasi bisa tidak konsisten saat dua sesi bekerja bersamaan | Gagal: TreeSelectDialog tidak ditemukan | belum jelas: perlu dicek apakah ini helper atau UI |
| E2E-181 | Konkurensi Edit: Duplikat, Device Name Dihapus Admin Lain, dan Save setelah Device Name Terhapus | High | Edit bisa menimpa atau menulis ke data yang sudah dihapus | Gagal: pesan error duplikat tidak ditemukan | tidak |
| E2E-182 | Konkurensi Edit: Measurement atau Category Dihapus Admin Lain saat Form Edit Terbuka | High | Edit pada relasi yang sudah dihapus | Gagal: dialog lain menutupi | tidak |
| E2E-184 | Konkurensi Bulk Delete: Item Menjadi Berelasi atau Dihapus Admin Lain saat Dialog Terbuka | High | Bulk delete bisa menghapus item yang sudah berelasi | Gagal: modal tidak ditemukan | tidak |
| E2E-185 | Konkurensi Bulk Delete: Seleksi Campuran SKU dan Hapus dari Sesi Lain | High | Bulk delete bisa menghapus item yang sudah dihapus sesi lain | Gagal: modal tidak ditemukan | tidak |
| E2E-187 | Konkurensi Dua Sesi UI: Edit Record yang Sama, Save Kedua Menimpa Save Pertama | High | Save kedua bisa menimpa perubahan save pertama | Gagal: dialog lain menutupi | tidak |

## Yang Tidak Dinaikkan

- Mobile: E2E-020, E2E-021. Surface mobile belum dibangun.
- Tampilan, tooltip, dan aksesibilitas: E2E-002, E2E-006, E2E-010, E2E-014, E2E-015, E2E-016, E2E-022, E2E-023, E2E-054, E2E-055, E2E-074, E2E-086, E2E-128, E2E-139, E2E-173.
- Guided tooltip: E2E-017, E2E-023.
- Usage by Company: E2E-091, E2E-095, E2E-096, E2E-097, E2E-098. Dampak tampilan, dan fitur Usage by Company belum di-slicing (feature-gap:fe).
- Sort dan pagination: E2E-110, E2E-120.

## Catatan untuk FE/QA

- E2E-179 dan E2E-180 gagal karena TreeSelectDialog tree tidak ditemukan. Belum jelas apakah ini helper-gap atau UI. Perlu dicek.
- Banyak spek konkurensi gagal karena dialog lain menutupi halaman (dialog Edit Device Name masih terbuka). Ini mungkin masalah harness yang belum menutup dialog.
