# Usulan Naik ke "Di Dalam Filter": Admin Console > Hardware Stock

Modul: Admin Console > Hardware Stock (Stock List, Stock Detail, Approvals, Add Stock, Sync, Download, Setup Column)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/HardwareStock`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Semua spek di modul ini berstatus "Belum ada skrip". Penilaian sepenuhnya dari dampak bisnis.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-248 | Batas Register Asset Bulk Limit pada Add Stock Manual | High | Batas register massal bisa terlampaui | Belum ada skrip | tidak |
| E2E-250 | State Saving dan Klik Ganda Submit Add Stock Manual | High | Klik ganda bisa menambah stok dua kali | Belum ada skrip | tidak |
| E2E-258 | Batas 100 Synced Units pada Add Stock Sync | High | Batas sync terlampaui | Belum ada skrip | tidak |
| E2E-272 | Multi-Konteks: Race Add Stock dan Delete | High | Stok bisa bertambah pada item yang sudah dihapus | Belum ada skrip | tidak |
| E2E-244 | Tidak Ada Plan Gating: Add Stock Identik pada Tiap Tier Plan | Medium | Plan gating yang salah bisa membatasi atau membuka add stock | Belum ada skrip | tidak |
| E2E-262 | Sync: Klik Ganda Submit dan Badge Basi Akibat Sesi Lain | Medium | Sync ganda dan badge basi bisa menyesatkan jumlah stok | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- E2E-004: loading state. Tampilan.
- E2E-005, E2E-125, E2E-135, E2E-165, E2E-166, E2E-185, E2E-205, E2E-225: setup column, pin, reset, dan pagination. Tampilan.
- E2E-103, E2E-105, E2E-138, E2E-168, E2E-188, E2E-208, E2E-228, E2E-284, E2E-286: download dan transformasi sel. Dampak format berkas.
- E2E-283: lintas modul dengan Device Allocation dan asersi negatif. Dampak rendah untuk modul ini.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya hasil run. Setelah dijalankan, daftar ini perlu dicek ulang.
