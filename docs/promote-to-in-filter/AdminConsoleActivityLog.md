# Usulan Naik ke "Di Dalam Filter": Admin Console > Activity Log

Modul: Admin Console > Activity Log
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/ActivityLog`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-017 | State Tenant: Entitas Suspended Tetap Dapat Membaca dan Aksi Tercatat | High | Write lockdown: aksi tulis pada tenant Suspended harus ditolak dan tercatat dengan benar | Belum dijalankan | tidak |
| E2E-018 | Perubahan Hubungan Entitas: Reassign Partner dan Pindah Staf | High | Jejak audit saat hubungan entitas berubah; log yang salah bisa menyembunyikan siapa yang memindahkan staf | Belum dijalankan | tidak |

## Yang Tidak Dinaikkan

- E2E-002, E2E-034, E2E-041, E2E-042, E2E-044: urutan default, filter tanggal, download besar, retensi tampilan, dan koneksi real-time. Dampaknya ke tampilan dan performa, bukan kebenaran data.
- E2E-005, E2E-036, E2E-038, E2E-049: tampilan sel, kontrol filter, bahasa, dan tooltip.

## Catatan untuk FE/QA

- Semua spek di modul ini belum dijalankan. Setelah dijalankan, daftar ini perlu dicek ulang terhadap hasil run.
