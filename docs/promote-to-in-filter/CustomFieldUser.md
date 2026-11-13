# Usulan Naik ke "Di Dalam Filter": Global Settings > Custom Field User

Modul: Global Settings > Custom Field User (Tabel Utama, Create, Edit, Toggle, Changelog, Download, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/CustomFieldUser`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-028 | Master Data Count Limit: 1.000 Field Memuat Field Inactive Tetap Menampilkan Dialog Limit Reached | High | Kuota field tidak ditegakkan berarti melewati batas lisensi | Gagal: gap helper BE terbuka | ya (limit tenant tidak bisa diatur lewat helper, BT-115) |
| E2E-029 | Multi-Konteks: Create Bersamaan Field Name Sama oleh Dua Admin dan Dua Admin Berebut Slot Terakhir Master Data Count Limit | High | Field ganda dan kuota terlewati saat dua admin bekerja bersamaan | Gagal: gap helper BE terbuka | ya (limit tenant tidak bisa diatur, BT-115) |
| E2E-038 | Multi-Konteks: Edit Bersamaan Last-Write-Wins, Form Edit Stale, Field Dihapus atau Dinonaktifkan Admin Lain di Tengah Edit | High | Edit dari form yang sudah basi bisa menimpa data atau mengubah tipe data field yang sudah dipakai | Lolos | tidak |
| E2E-043 | Selection Limit Bulk: Seleksi Manual ke-101 Diblok dan Select All Di-cap ke 100 dengan Toast Error Persist | High | Bulk action bisa melewati Selection Limit | Gagal: gap helper BE terbuka | ya (Selection Limit tidak bisa diatur, BT-115) |
| E2E-048 | Multi-Konteks Toggle Active: Record Sudah Dihapus atau Sudah Berubah Status oleh Admin Lain (Single dan Bulk) | High | Toggle pada record yang sudah berubah bisa mengaktifkan atau menonaktifkan field yang salah, dan memengaruhi form user | Lolos | tidak |
| E2E-066 | Download Changelog Custom Field CSV dan XLSX: Mengikuti Search dan Filter, Isi Sel, Seluruh Entri Lintas Halaman, dan Kolom Hidden | Medium | Export jejak audit yang tidak lengkap atau salah isi, misalnya entri Edit yang hilang | Gagal: nilai beda dari spec (satu entri Edit tidak ada di CSV) | tidak (perlu dipastikan QA: bug export atau mismatch spec) |
| E2E-076 | Multi-Tab: Submit Ganda Create Field Name Sama melalui Dua Tab pada Satu Sesi Tidak Menduplikasi Definisi | Medium | Definisi field ganda bisa merusak form user dan kuota | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-022 dan E2E-024 (validasi batas karakter dan numeric): validasi nilai, dampak sedang. Konsisten dengan keputusan di modul lain.
- E2E-025 (normalisasi numeric tersimpan): dampak sedang, pola validasi.
- E2E-045 (dialog konfirmasi, Esc, backdrop, toast): tampilan dan perilaku UI.
- E2E-005 dan E2E-006 (Guided Tooltip): tampilan, dampak rendah.
- E2E-058 (download di atas 5.000 baris): performa, dan belum ada helper untuk seed 5.001 field (BT-NEW-G1, G2).
- E2E-059 (filter dasar karena record dihapus sesi lain): tampilan tabel, dampak data tercakup oleh E2E-048.
- E2E-064 dan E2E-065 (Modal Changelog: pagination dan Setup Column): pola list yang seragam.
- E2E-071 (format tanggal General Settings pada Download CSV): tampilan format.
- E2E-046 (mobile Android): fitur mobile belum dibangun (feature-gap:fe, sprint-gap).
- E2E-075 (gating plan): prioritas Low.

## Catatan untuk FE/QA

- E2E-028 dan E2E-029 bergantung pada cara mengatur Master Data Count Limit tenant uji. Pre-setup belum menyediakannya, dan helper BE belum ada. Ada juga catatan bahwa keputusan NC-20 (dialog tampil saat klik `[+ Custom Field]`) belum selaras dengan API dan LLD. Lihat `## Notes` di spec 028.
- E2E-043 bergantung pada jumlah Custom Field tepat 1.000. Pre-setup hanya menyediakan 999 dan satu field tambahan diatur backend.
- E2E-066 gagal karena satu entri Edit tidak ditemukan di CSV. Perlu dicek QA apakah ini bug export (entri audit hilang) atau hanya perbedaan format. Spec juga mencatat perbedaan token sel kosong (`-` di TC, `—` di LLD).
- Daftar ini hanya mencakup 20 spek yang diajukan untuk Custom Field User. Spek lain di modul ini belum dinilai.
