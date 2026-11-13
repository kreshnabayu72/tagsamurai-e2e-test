# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Device Category

Modul: Admin Console > Settings > Device Category (Tree Category, Add Subcategory, Edit, Delete, Hierarchy Depth Limit, Changelog, Absence Log)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsDeviceCategory`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-028 | Add Subcategory: State Submitting, Klik Ganda Submit, dan Pencarian Tree Aktif | High | Klik ganda bisa membuat subcategory ganda | Gagal: toast sukses tidak tampil | tidak |
| E2E-038 | Edit Category: Perubahan Huruf Besar-Kecil Saja, State Submitting, dan Klik Ganda Save | High | Klik ganda dan perubahan kapitalisasi bisa menimbulkan nama ganda | Lolos | tidak |
| E2E-051 | Dua Admin: Add Subcategory saat Parent Dihapus, Node Hasil Pencarian Dihapus, dan Hierarchy Depth Limit Turun | High | Subcategory bisa dibuat di bawah parent yang sudah dihapus | Lolos | tidak |
| E2E-052 | Dua Admin: Edit saat Node Dihapus dan Edit Bersamaan pada Node yang Sama | High | Edit bersamaan bisa menimpa perubahan admin lain | Lolos | tidak |
| E2E-053 | Dua Admin: Nama Sama pada Parent yang Sama dan Family Dihapus saat Edit Descendant | High | Nama ganda pada parent yang sama, atau edit pada family yang sudah dihapus | Lolos | tidak |
| E2E-055 | Dua Admin: Delete pada Node yang Sudah Dihapus Admin Lain dan Permintaan Delete Kedua dari Tab Lain | High | Delete ganda dari dua tab | Lolos tak lengkap | tidak (ui-gap D-096 pada step 22, bukan gap helper) |
| E2E-087 | Hierarchy Depth Limit: Penurunan Tidak Menghapus Node dan Kenaikan Langsung Berlaku pada Add | High | Penurunan batas kedalaman tidak boleh menghapus node yang sudah ada | Gagal: dialog lain menutupi | tidak |
| E2E-094 | Dua Admin: Edit ke Nama yang Baru Dibuat Admin Lain di Parent yang Sama | High | Nama ganda pada parent yang sama lewat dua admin | Lolos | tidak |
| E2E-097 | Absence Log: Aksi pada Satu Node Tidak Menghasilkan Entri untuk Node Lain | Medium | Jejak audit harus tepat per node | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-004, E2E-069, E2E-074, E2E-078, E2E-089, E2E-096: aksesibilitas, changelog, setup column, dan sidebar. Tampilan.
- E2E-006, E2E-012, E2E-036, E2E-041, E2E-063, E2E-090, E2E-093: pencarian tree, tri-state, unsaved changes, dan validasi 120 karakter. Tampilan atau validasi format.
- E2E-031: batas 120 karakter dan auto-trim. Validasi format.

## Catatan untuk FE/QA

- E2E-028 gagal karena toast sukses tidak muncul dalam 3 detik. Perlu dicek apakah ini timing harness atau perilaku UI.
- E2E-041 gagal karena node "Pemindai Pro" tidak ditemukan. Tidak ada tanda helper-gap, jadi ini perlu dicek QA.
