# Usulan Naik ke "Di Dalam Filter": Global Settings > Position

Modul: Global Settings > Position (Tabel Utama, Create, Edit, Delete, Bulk, Changelog, Log, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Position`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-024 | Selection Limit Bulk Position: Checkbox ke-(Limit+1) Disabled dan Select All Dibatasi Limit | High | Bulk action bisa melewati Selection Limit yang ditetapkan | Lolos | tidak |
| E2E-046 | Tidak Ada Pencatatan Log untuk Edit No-Op dan untuk Position Hasil Import | High | Jejak audit Position: edit tanpa perubahan tidak boleh tercatat, dan Position dari Import harus tercatat | Gagal: gap helper terbuka | ya (import Position 500 di tenant uji, BT-GS-POS-6) |
| E2E-051 | Multi-Konteks: Create Position Bersamaan oleh Dua Admin dengan Nama Sama dan pada Slot Limit Terakhir | High | Dua admin bisa membuat Position ganda dan melewati Master Data Count Limit | Lolos | tidak |
| E2E-052 | Multi-Konteks: Edit Bersamaan Last-Write-Wins serta Record yang Dihapus atau Menjadi In-Use di Antara Dialog dan Konfirmasi (Single dan Bulk) | High | Position yang sudah in-use bisa terhapus, dan edit bersamaan bisa menimpa data tanpa jejak | Gagal: dialog lain menutupi | tidak |

## Yang Tidak Dinaikkan

- E2E-027 (Mobile Android: aturan card, screening toolbar, dan long-press bulk delete): belum ada skrip, dan surface mobile belum dibangun. Dampaknya sedang. Bisa diusulkan setelah skrip ada.
- E2E-042 (Popup Changelog: Overlay Column Visibility dan Setup Column): pola Setup Column yang seragam, dampak rendah.
- E2E-053 (Multi-konteks: record baru, terhapus, dan rename dari sesi lain tanpa muat ulang): tampilan tabel saja. Dampak data terjaga oleh E2E-052.
- E2E-056 (Popup Changelog: sumber opsi dropdown filter): tampilan filter, dampak rendah.

## Catatan untuk FE/QA

- E2E-046 dan E2E-024 bergantung pada hal di luar spec: E2E-046 pada jalur Import di tenant uji, E2E-024 pada cara menurunkan Selection Limit lewat hook `before`. Sumber catatannya ada di `## Notes` → "Temuan untuk QA" masing-masing spec.
- E2E-052 banyak memuat asersi Post Condition (entri Changelog dan Activity Log) yang belum punya langkah observasi di TC. Asersi itu belum diuji, jadi dampaknya di spec belum penuh.
- Daftar ini hanya mencakup 8 spek yang diajukan untuk Position. Spek lain di modul ini belum dinilai.
