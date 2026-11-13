# Usulan Naik ke "Di Dalam Filter": Global Settings > Activity Log

Modul: Global Settings > Activity Log (Tab Session, Tab User Action, Filter Date, Download, Setup Column, Retensi Log, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/ActivityLog`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Modul ini adalah jejak aktivitas, jadi yang paling penting adalah integritas dan kelengkapan log.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-016 | Snapshot Beku Setelah Data Diubah | High | Entri log harus tetap sama setelah data sumbernya berubah, jika tidak jejak aktivitas menjadi tidak bisa dipercaya | Lolos | tidak |
| E2E-062 | Filter Aktif dan Snapshot Setelah Sumber Dihapus | High | Entri log harus tetap tampil setelah sumbernya dihapus. Kalau hilang, jejak aktivitas terhapus bersama datanya | Lolos | tidak |
| E2E-056 | Aksi Sistem File Manager: Modified By System | Medium | Penghapusan permanen oleh sistem harus tercatat sebagai System. Kalau salah atribusi, pelaku penghapusan tidak terlihat | Gagal: gap helper terbuka | ya (job auto-purge File Manager tidak bisa dipicu dan file tidak bisa dibuat lewat umur hapus, BT belum ada) |
| E2E-059 | State Tenant: Client Suspended atau Expired | Medium | Auto-purge yang berjalan saat Suspended harus tetap tercatat | Gagal: gap helper terbuka | ya (job auto-purge File Manager tidak bisa dijalankan sebagai proses sistem di client Suspended) |
| E2E-060 | Perilaku Identik di Tiap Tier Plan | Medium | Log aktivitas yang berbeda per plan berarti jejak hilang di tier tertentu | Lolos | tidak |
| E2E-061 | Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner | Medium | Log lama yang terpotong menghilangkan jejak audit | Gagal: gap helper terbuka | ya (Principal membutuhkan tenant tag khusus, BT belum ada); feature-gap:fe (Distributor dan Partner belum di-slice) |

## Yang Tidak Dinaikkan

- E2E-002 (urutan default, tie-break, entri tiba tidak berurutan): urutan tampilan. Dampak data tidak berubah.
- E2E-018, E2E-023, E2E-032, E2E-039, E2E-041 (Search, Sort, Filter Date, kombinasi): pola list dan filter yang seragam.
- E2E-050 (download di atas dan tepat 5.000 baris): volume, pola yang sama dengan download besar di modul lain.
- E2E-049 (download gagal dengan toast): pesan error.
- E2E-003, E2E-005, E2E-006 (tooltip dan Guided Tooltip): tampilan. E2E-005 juga gagal karena dialog menutupi.
- E2E-008 (ganti bahasa, kolom verbatim dan translatable): tampilan.
- E2E-026, E2E-035 (Setup Column): pola Setup Column yang seragam.
- E2E-044 (opsi filter dan indikator loading): tampilan filter.
- E2E-007 (mobile): surface mobile belum dibangun, dikecualikan.

## Catatan untuk FE/QA

- E2E-056 dan E2E-059 bergantung pada job auto-purge File Manager yang tidak bisa dipicu lewat route uji. Ini sama dengan gap di modul File Manager (E2E-064).
- E2E-061 membutuhkan tenant Principal, yang tidak ditandai di spec. Distributor dan Partner belum di-slice.
- Daftar ini hanya mencakup 16 spek yang diajukan untuk Activity Log. Spek lain di modul ini belum dinilai.
