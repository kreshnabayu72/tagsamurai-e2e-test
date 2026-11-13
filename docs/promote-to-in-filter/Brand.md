# Usulan Naik ke "Di Dalam Filter": Global Settings > Brand

Modul: Global Settings > Brand (Tabel Utama, Create, Edit, Delete, Bulk, Import, Detail Principal, Changelog, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Brand`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-025 | Konflik Create dan Edit Brand oleh Dua Admin | High | Brand ganda dan edit yang menimpa perubahan admin lain | Lolos | tidak |
| E2E-026 | Konflik Delete dan Bulk Delete Brand oleh Dua Admin | High | Brand yang sudah dihapus admin lain bisa tercatat hapus dua kali atau menghapus data yang salah | Lolos | tidak |
| E2E-027 | Konflik Brand Menjadi In-Use Saat Confirm Delete | High | Brand yang sudah dipakai bisa terhapus | Lolos tak lengkap | ui-gap (copy daftar dampak pada dialog belum sesuai UI) |
| E2E-031 | Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap | High | Bulk action bisa melewati Selection Limit | Lolos | tidak |
| E2E-033 | Master Data Count Limit: Dua Admin Rebutan Slot Terakhir | High | Dua admin bisa melewati kuota Master Data Count Limit | Lolos | tidak |
| E2E-066 | Stale Reference: Submit Form Konsumen dengan Brand yang Baru Dihapus Admin Lain | High | Form konsumen bisa tersimpan dengan Brand yang sudah tidak ada | Gagal: gap helper terbuka | ya (Device SKU tidak bisa dibuat karena Admin Console belum bisa dibuka di stack uji, BT-61); feature-gap:fe (Asset Name dan TAG BYO belum di-slice) |
| E2E-067 | Brand Hasil Import Dapat Diedit dan Dihapus seperti Brand Manual | Medium | Brand hasil import harus mengikuti aturan edit dan hapus yang sama dengan brand manual | Lolos | tidak |
| E2E-072 | Write Lockdown Brand saat Client Suspended atau Expired: Create, Edit, Delete, dan Bulk Delete Ditolak | High | Client suspended atau expired masih bisa menulis data Brand | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-007 dan E2E-008 (Guided Tooltip): tampilan, dampak rendah.
- E2E-041 (Setup Column tabel Brand): pola Setup Column yang seragam.
- E2E-045 dan E2E-046 (angka Used By, format tanggal General Settings): tampilan.
- E2E-048 (download Changelog dan Item Type List): isi file, dan spek ini lolos.
- E2E-049 (download Device SKU List pada Principal): helper-gap BT-61 (Device SKU tidak bisa dibuat di stack uji). Dampak data tercakup di spek lain.
- E2E-052 dan E2E-053 (Changelog Brand: chip filter, sort, pagination): pola list yang seragam.
- E2E-059 (chip filter Category pada Device SKU List): helper-gap BT-61, dampak tampilan filter.
- E2E-073 (baca data Brand saat Client Suspended): akses baca, dampak lebih ke tampilan. Penulisan saat Suspended sudah tercakup oleh E2E-072.
- E2E-074 (mobile Android): belum dijalankan.
- E2E-034 (tanpa gating plan): prioritas Low.

## Catatan untuk FE/QA

- E2E-066 bergantung pada Admin Console Device SKU (BT-61) dan slice Fixed Asset (Asset Name dan TAG BYO). Sebagian langkah belum bisa dijalankan sampai dependensi ini tersedia.
- E2E-027 gagal di satu langkah kecil karena copy `- Fixed Asset (1 asset name)` ditandai ui-gap (D-096, UI sebagai acuan). Ini perlu dicek QA.
- E2E-033 hanya 9 langkah dan mengandalkan slot kuota yang diatur di tenant uji. Sumber pengaturan kuota belum didefinisikan di spec.
- Daftar ini hanya mencakup 21 spek yang diajukan untuk Brand. Spek lain di modul ini belum dinilai.
