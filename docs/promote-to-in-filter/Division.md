# Usulan Naik ke "Di Dalam Filter": Global Settings > Division

Modul: Global Settings > Division (Tabel Utama, Create, Edit, Delete, Bulk, Changelog, Log, Import, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Division`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-028 | Edit Division: Code Dikosongkan, Auto-Generate, dan Save Tanpa Perubahan | High | Code dipakai sebagai identitas Division. Auto-generate yang salah bisa menimpa Code dengan nilai ganda atau salah | Lolos | tidak |
| E2E-030 | Konflik Edit vs Delete dan Bulk Delete: Record Dihapus Pihak Lain | High | Edit bisa menyimpan data pada Division yang sudah dihapus, tanpa jejak | Lolos | tidak |
| E2E-033 | Konflik Delete: Berubah In-Use Saat Confirm dan Sudah Dihapus Pihak Lain | High | Division yang sedang dipakai user bisa terhapus | Gagal: asersi toast error tidak sesuai | tidak |
| E2E-034 | Delete Division: Katalog Tidak Pernah Turun ke Nol | High | Katalog Division kosong membuat form User dan Non-Login User tidak bisa dipakai | Lolos | tidak |
| E2E-036 | Selection Limit: Checkbox Disabled dan Select All Dibatasi | High | Bulk action bisa melewati Selection Limit | Lolos tak lengkap | ui-defect (toast error persisten tidak tampil saat Select All dibatasi) |
| E2E-040 | Bulk Delete Race: Item Menjadi In-Use Setelah Pre-Check dan Saat Confirm | High | Bulk delete bisa menghapus Division yang sedang dipakai | Lolos | tidak |
| E2E-066 | Pencatatan Changelog: Modified By Mencatat Aktor Pelaksana | Medium | Jejak audit: perubahan Division harus mencatat siapa pelakunya | Lolos | tidak |
| E2E-067 | Absence Log: Edit Tanpa Perubahan dan Division In-Use Dilewati Tidak Menghasilkan Entri | High | Jejak audit: edit tanpa perubahan dan aksi yang dilewati tidak boleh mencatat entri palsu | Lolos | tidak |
| E2E-070 | Form User dan Non-Login User: Division Terpilih Dihapus Pihak Lain | High | User bisa tersimpan dengan Division yang sudah tidak ada | Lolos | tidak |
| E2E-071 | Import Create Missing Divisions: Edit, Delete In-Use, dan Pencatatan Create | Medium | Division hasil import harus punya jejak Create dan mengikuti aturan Edit dan Delete yang sama | Lolos tak lengkap | feature-gap:be (BT-114, endpoint belum dibangun) |
| E2E-078 | Tanpa Gating Plan: Create, Edit, dan Delete Identik di Semua Tier | Medium | Plan yang salah membatasi atau membuka fitur Division | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-044 (Search aktif terhadap Create dan Edit): prioritas Low, dampak rendah.
- E2E-077 (Realtime: Create dan Rename dari admin lain tampil otomatis): tampilan tabel saja. Dampak data tercakup oleh E2E-030.
- E2E-080 (Mobile: Create dan Edit Division): belum ada skrip, dan surface mobile belum dibangun.
- E2E-005 dan E2E-006 (Guided Tooltip): tampilan, dampak rendah.
- E2E-049 (Isolasi konfigurasi kolom Tabel dan Modal Changelog): pola Setup Column yang seragam.
- E2E-052 (Format tanggal General Settings pada filter dan Changelog): tampilan.
- E2E-058, E2E-060, E2E-061, E2E-062 (Modal Changelog: chip filter, pagination, Setup Column): pola list yang seragam, dampak rendah.

## Catatan untuk FE/QA

- E2E-071 bergantung pada fitur Import Create Missing Divisions, yang belum dibangun di backend.
- E2E-033 gagal karena asersi toast error (`expected queryToast("Error") to find nothing`), bukan karena fiturnya bug. Perlu dicek QA apakah asersinya benar.
- E2E-036 dan E2E-067 mengandung temuan QA di `## Notes` masing-masing spec.
- Daftar ini hanya mencakup 22 spek yang diajukan untuk Division. Spek lain di modul ini belum dinilai.
