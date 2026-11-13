# Usulan Naik ke "Di Dalam Filter": Global Settings > Role & Permission

Modul: Global Settings > Role & Permission (Tab Total Control, Read Only, System, Detail, Popup Assign, Changelog, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Role`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Modul ini mengatur hak akses, jadi kriteria dampak diterapkan ketat pada konflik assign, remove, dan perlindungan Total Control.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-033 | Konflik Assign: Dua Admin Meng-Assign User yang Sama Secara Bersamaan | High | Dua admin meng-assign user yang sama bisa menghasilkan role ganda atau hak yang tidak diinginkan | Gagal: toast tidak ditemukan | tidak |
| E2E-045 | Selection Limit Detail: Volume Data Melewati Batas Seleksi | High | Bulk action bisa melewati Selection Limit | Gagal: kontrol halaman tidak ditemukan | tidak |
| E2E-048 | Bulk Remove Satu Baris: Dialog Single dan Klik Ganda pada [Remove] | High | Klik ganda bisa mencabut hak dua kali atau mencabut hak user yang salah | Gagal: toast tidak ditemukan | tidak |
| E2E-079 | Pencatatan Log Lama Tidak Berubah setelah Rename User serta Modified By dan Last Updated oleh Assign | Medium | Jejak audit: log lama tidak boleh berubah saat user di-rename, dan Modified By harus tepat | Lolos | tidak |
| E2E-082 | Pencatatan Changelog: User dan Changelog: User > Role | Medium | Jejak audit perubahan hak akses per user | Lolos | tidak |
| E2E-083 | Absence Log: Assign Total Control Tidak Menulis Entry ke Changelog: User > Role | Medium | Jejak audit: entri Total Control tidak boleh tercatat di tempat yang salah | Lolos | tidak |
| E2E-093 | Fitur Ber-Plan Tetap Muncul sebagai Role di Semua Plan | Medium | Plan yang salah membatasi atau membuka role | Gagal: toast tidak ditemukan | tidak |
| E2E-094 | Isolasi Akses Produk Lain pada Assign Total Control Global Settings | Medium | Assign Total Control bisa mengubah akses produk lain (misalnya Admin Console) | Gagal: dialog lain menutupi | ya (Admin Console route belum tersedia, BT-61) |
| E2E-102 | Default User Tetap Total Control Setelah Semua Total Control Lain Di-Remove | Medium | Tenant bisa kehilangan admin Total Control sama sekali, sehingga terkunci | Gagal: jumlah baris tidak sesuai | tidak |
| E2E-103 | Konflik Antar Admin pada Edit CRUD: Nilai Sama, Status Total Control Berubah, dan Baris Sudah Dihapus | High | Edit dari admin lain bisa menimpa hak tanpa peringatan | Gagal: baris tidak ditemukan | tidak |
| E2E-104 | Konflik Antar Admin pada Remove Baris Role: Sudah Dihapus Admin Lain atau Target Menjadi Total Control | High | Remove pada target yang sudah berubah bisa mencabut hak yang salah | Gagal: baris tidak ditemukan | tidak |
| E2E-105 | Konflik Antar Admin pada Remove Access Level: Target Sudah di-Remove atau Tier Berbeda dari Tab yang Dirender | High | Remove access level pada tier yang sudah berbeda bisa mencabut hak yang salah | Lolos | tidak |
| E2E-107 | Realtime: Auto-Revert Menghilangkan User dari Tab Total Control Sesi Admin Lain Tanpa Reload | High | Admin lain tetap melihat user yang sudah tidak punya hak, dan bisa mengambil aksi berdasar data basi | Gagal: modal tidak ditemukan | tidak |

## Yang Tidak Dinaikkan

- E2E-009, E2E-010, E2E-011 (Guided Tooltip dan hover tooltip): tampilan, dampak rendah.
- E2E-012, E2E-013, E2E-014 (mobile): belum ada skrip, dan surface mobile belum dibangun.
- E2E-020 dan E2E-021 (tooltip baris default user dan aksesibilitas keyboard): tampilan atau aksesibilitas, dampak data tidak berubah.
- E2E-027 (Popup Assign: kolom, sort, pagination): tampilan dan retensi seleksi. Ada helper-gap custom field Region, tapi dampak data rendah.
- E2E-053, E2E-056, E2E-057 (Custom Field Region, Setup Column): helper-gap custom field, dan tampilan kolom.
- E2E-067 (Modal Changelog: sort, Setup Column, pagination): pola list yang seragam.
- E2E-089 (sinkron rename Position dan status Custom Field): tampilan kolom. Sinkron datanya tercakup oleh spek lain di modul Position dan Custom Field.
- E2E-090 (format tanggal General Settings): tampilan.
- E2E-059 (download Total Control di atas 5.000 baris): prioritas Low, dan helper bulk seed belum ada.
- E2E-097 (State Tenant Suspended, tab dan detail tetap dapat dilihat): dampak lebih ke tampilan. Kontrol tulis Suspended sudah diuji di modul Global Settings lain. Hook teardown di spek ini juga gagal.

## Catatan untuk FE/QA

- E2E-094 bergantung pada Admin Console > Settings > Role & Permission, yang belum bisa diakses di backend nyata (BT-61). Asersi akses Admin Console saat ini ditulis sebagai kemampuan tim FE.
- E2E-102 mengubah sejumlah Total Control, dan Pre-setup memuat lebih banyak Total Control dari yang disebut TC. Spec memulihkannya di hook `after`. Ini perlu dicek QA.
- E2E-048 menulis counter `1 User selected` sesuai TC, sementara PRD menulis `1 user selected`. Perbedaan ini perlu diputuskan.
- Daftar ini hanya mencakup 27 spek yang diajukan untuk Role. Spek lain di modul ini belum dinilai.
