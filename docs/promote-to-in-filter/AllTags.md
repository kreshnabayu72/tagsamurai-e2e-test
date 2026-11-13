# Usulan Naik ke "Di Dalam Filter": Global Settings > All Tags

Modul: Global Settings > All Tags (Registri TAG, Activate TAG, Commit, Audit, Delete, Approve/Reject, Event Log, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/AllTags`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper, fitur, atau hardware yang belum tersedia, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Modul ini mengatur inventaris TAG, sehingga kesalahan commit, kuota, atau delete bisa membuat stok dan kepemilikan TAG tidak akurat.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-033 | Commit Sebagian/Semua Gagal: Failed T-06/T-07, Evaluasi Ulang Submit Berikutnya, Waiting for Approval Client Lain, dan Toast T-25 | High | Commit yang gagal sebagian bisa membuat inventaris TAG tidak sesuai dengan yang tercatat | Gagal: gap lain terbuka | ya (helper TC-GS-TAG-102) |
| E2E-034 | Commit: Kuota Pool Kurang Saat Submit dan Kuota Habis oleh Sesi Paralel (Rollback Penuh, Dialog 1 Varian Commit) | High | Kuota TAG bisa terlewati, dan commit yang setengah berhasil bisa menyisakan data yang salah | Gagal: gap lain terbuka | ya (kuota tenant uji, TC-GS-TAG-106) |
| E2E-039 | Konflik Dua Client: Aktivasi Identifier Self-Purchased Baru yang Sama Bersamaan | High | Dua client bisa mengaktifkan identifier yang sama, sehingga satu TAG tercatat milik dua client | Gagal: tombol tidak ditemukan | tidak |
| E2E-044 | Audit: Dialog Keep Auditing/Discard, Refresh, Submit Gagal Server T-03, dan Tag Dihapus atau Tidak Eligible di Tengah Sesi T-13 | High | Hasil audit bisa tercatat untuk TAG yang sudah dihapus atau tidak eligible | Lolos tak lengkap | hardware-gap (TC-GS-TAG-135, D-097) |
| E2E-045 | Konflik Dua Admin: Delete Tag yang Sama dan Submit Audit Tipe yang Sama Bersamaan | High | Delete dan audit bersamaan bisa menghapus atau mengaudit TAG yang sudah tidak ada | Gagal: gap lain terbuka | ya (helper BT-GS-TAG-1, TC-GS-TAG-327) |
| E2E-048 | Selection Limit: Checkbox ke-(L+1) Diblokir dan Select All Lintas Halaman di-Cap | High | Bulk action bisa melewati Selection Limit | Gagal: gap lain terbuka | ya (helper BT-GS-TAG-1, TC-GS-TAG-157) |
| E2E-053 | Delete: Tag Di-pair Sebelum Commit T-34, Gagal Server T-23/T-24, Sudah Dihapus Admin Lain, dan Klik Ganda | High | TAG yang sedang di-pair bisa terhapus, dan delete ganda bisa mencatat dua kali | Gagal: nilai atau state beda dari spec (daftar TAG menjawab 422, diharapkan 200) | ya (BT-GAP-H8, TC-GS-TAG-146) |
| E2E-064 | Approve/Reject Kolisi Ditolak saat Tag Sudah Dihapus tetapi Event Delete Belum Diproses | High | Approve atau reject bisa diterapkan pada TAG yang sudah tidak ada | Gagal: gap lain terbuka | ya (helper BT-GS-TAG-1, TC-GS-TAG-352) |
| E2E-098 | Delete: Tag To be Returned Keluar dari Tab To Be Returned FAMS (Single dan Bulk) | High | TAG yang sudah dihapus masih muncul di daftar pengembalian FAMS | Gagal: gap lain terbuka | ya (helper, aktor Admin FAMS, TC-GS-TAG-144) |

## Yang Tidak Dinaikkan

- E2E-015 (Mobile: tanpa bulk delete, resolve, remove, dan visibilitas tombol per tab dan role): High, tetapi belum ada skrip dan surface mobile belum dibangun. Perlu dinilai ulang setelah skrip ada.
- E2E-011 (Plan Free: audit atas tipe terkunci dan delete by scan atas TAG terkunci): Medium, belum ada skrip.
- E2E-062 (Un-Retire ditolak saat kuota tipe penuh): Medium, belum ada skrip. Kalau skripnya sudah ada, layak dinilai ulang karena menyangkut kuota.
- E2E-005 dan E2E-037 (Guided Tooltip): tampilan, dampak rendah, belum ada skrip.
- E2E-077, E2E-079, E2E-080, E2E-085, E2E-100, E2E-101 (Setup Column, download, dan kolom Event Log): tampilan dan download, dampak rendah, belum ada skrip.

## Catatan untuk FE/QA

- Hampir semua spek yang dinaikkan bergantung pada helper BT-GS-TAG-1 atau BT-GAP-H8, atau pada aktor Admin FAMS. Helper-helper itu belum ada, jadi spek-spek ini belum bisa lulus.
- E2E-053 gagal dengan jawaban daftar TAG 422, bukan 200. Ini bisa jadi bug backend, bukan hanya kekurangan helper. Perlu dicek QA.
- E2E-039 gagal karena tombol `Self-Purchased` tidak ditemukan. Perlu dicek apakah ini selector atau tombolnya memang belum ada.
- E2E-044 bergantung pada hardware TAG (D-097). Sebagian langkah tidak bisa dijalankan tanpa hardware.
- Daftar ini hanya mencakup 20 spek yang diajukan untuk All Tags. Spek yang belum ada skripnya tidak saya nilai ulang sekarang.
