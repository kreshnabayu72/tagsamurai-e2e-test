# Usulan Naik ke "Di Dalam Filter": Global Settings > File Manager

Modul: Global Settings > File Manager (Tabel Utama, Recycle Bin, Kartu Storage, Auto-Purge, Changelog, Setup Column, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/FileManager`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Modul ini menyangkut penghapusan permanen file, sehingga kesalahan di sini bisa menyebabkan kehilangan data yang tidak bisa dipulihkan.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-018 | Selection Limit: Checkbox Diblokir, Select All di-cap, dan Kosongkan Recycle Bin Beberapa Putaran | High | Bulk action bisa melewati Selection Limit, dan pengosongan Recycle Bin bisa menghapus file permanen di luar yang dipilih | Lolos | tidak |
| E2E-026 | Konflik Dua Admin: Delete dan Permanently Delete File yang Sama Bersamaan | High | Penghapusan permanen bisa terjadi dua kali atau pada file yang sudah diubah admin lain | Lolos | tidak |
| E2E-029 | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | High | Retensi yang salah berarti file dihapus permanen terlalu cepat atau terlalu lama disimpan | Gagal: gap helper terbuka | ya (tidak ada route untuk mengatur Deleted Date file dan memicu job reset countdown; retensi diatur lewat Lifecycle Settings Principal) |
| E2E-058 | Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User | Medium | Jejak audit file harus tetap menunjukkan siapa pelakunya, meski nama atau akunnya sudah berubah atau dihapus | Gagal: gap helper terbuka | ya (file milik user nyata belum bisa di-seed, BT belum ada) |
| E2E-061 | File Manager Identik pada Seluruh Tier Plan | Medium | Plan yang salah membatasi File Manager di satu tier | Lolos | tidak |
| E2E-064 | State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended | High | Auto-purge yang berhenti saat Suspended berarti file yang seharusnya dihapus tetap tersimpan. Cascade purge foto user yang dihapus juga harus tetap jalan | Gagal: gap helper terbuka | ya (job auto-purge harian tidak bisa dipicu lewat route uji; file Recycle Bin tidak bisa dibuat 31 hari lalu) |
| E2E-066 | Kartu Storage Usage: Laporan Terlama, Kuota Belum Dialokasikan, Melewati Kuota, dan Batas Persentase | High | Laporan storage yang salah bisa membuat tenant melewati kuota tanpa peringatan | Gagal: gap helper terbuka | ya (skenario laporan storage belum bisa di-seed, BT-60) |

## Yang Tidak Dinaikkan

- E2E-021 (Bulk Delete dan Bulk Permanently Delete 1.001 baris): volume, diblokir backend (BT-84). Dampak logika sudah tercakup oleh E2E-018.
- E2E-043 (pagination dan reset pada modal Recycle Bin dan Changelog): pola list, dan gagal karena opsi filter belum bisa dibuat (helper-gap).
- E2E-051 (Setup Column tiga surface): pola Setup Column yang seragam.
- E2E-054 (download tabel utama 5.001 baris): volume, helper-gap BT-84.
- E2E-063 (kartu Storage dan aksi baca saat Suspended atau Expired): akses baca, dampak lebih ke tampilan. Pola yang sama sudah diputuskan di modul Brand dan Role.
- E2E-069 dan E2E-070 (Guided Tooltip): tampilan, dampak rendah.

## Catatan untuk FE/QA

- E2E-029, E2E-064, dan E2E-058 membutuhkan route uji untuk mengatur tanggal hapus file, memicu job auto-purge, dan membuat file milik user nyata. Route itu belum ada, dan BT-nya belum tercatat di repo.
- E2E-066 bergantung pada BT-60 (skenario laporan storage). Skenario S2, S3, S4, S7, dan S8 belum bisa di-seed.
- E2E-029 juga menyentuh Lifecycle Settings platform-wide (PATCH `/v2/enterprise-management/lifecycle-settings/recycle-bin`). Spec ini mungkin tidak boleh mengubahnya tanpa tag khusus. Ini perlu diputuskan QA.
- Daftar ini hanya mencakup 14 spek yang diajukan untuk File Manager. Spek lain di modul ini belum dinilai.
