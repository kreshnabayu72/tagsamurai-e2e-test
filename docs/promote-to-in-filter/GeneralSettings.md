# Usulan Naik ke "Di Dalam Filter": Global Settings > General Settings

Modul: Global Settings > General Settings (Form Pengaturan, Save Pertama, Session Idle Timeout, Plan, Changelog, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/GeneralSettings`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

General Settings mengatur nilai yang dipakai di seluruh modul (mata uang, zona waktu, format tanggal, dan idle timeout sesi), jadi bug di sini menyebar ke banyak tempat.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-045 | Dua admin | High | Dua admin menyimpan pengaturan yang sama, dan Save terakhir menimpa tanpa peringatan. Nilai ini dipakai di seluruh modul | Gagal: toast tidak tampil | tidak |
| E2E-051 | Bypass DOM A | Medium | Kontrol yang dinonaktifkan di UI bisa diubah lewat manipulasi client, misalnya Currency Code tanpa dialog konfirmasi | Lolos | tidak |
| E2E-052 | Bypass DOM B | Medium | Pola sama dengan E2E-051 untuk Date Format, Time Format, dan Session Idle Timeout | Lolos | tidak |
| E2E-025 | Multi-Konteks: Session Idle Timeout Tidak Mengubah Kebijakan Satu Sesi Web per Akun | Medium | Kebijakan sesi berdampak ke keamanan akun. Perubahan timeout tidak boleh mengubah aturan satu sesi web per akun | Lolos | tidak |
| E2E-006 | Record belum ada, Save pertama | Medium | Tenant baru yang belum punya record General Settings harus bisa menyimpan pengaturan pertama | Lolos | tidak |
| E2E-023 | State Tenant: General Settings Tersedia dan Identik di Semua Plan Tanpa Gating | Medium | Plan yang salah membatasi General Settings di satu tier | Lolos | tidak |

## Yang Tidak Dinaikkan

- E2E-009 dan E2E-010 (Guided Tooltip): tampilan, dampak rendah.
- E2E-012 dan E2E-013 (mobile): belum dijalankan.
- E2E-031, E2E-032, E2E-033, E2E-037, E2E-039, E2E-053, E2E-054 (Changelog General Settings: chip filter, pagination, sort, retensi, Setup Column): pola list yang seragam, dampak rendah.

## Catatan untuk FE/QA

- E2E-045 gagal karena toast `Success, general settings has been saved.` tidak tampil dalam 3 detik. Ini perlu dicek QA apakah toast memang tidak muncul atau asersinya yang salah. Spec tidak mengasersi Old Value baris Save kedua.
- E2E-006 dan E2E-023 bergantung pada penghapusan record lewat database dan perubahan plan. Mekanismenya belum didefinisikan di TC, PRD, atau LLD, jadi ditulis sebagai kemampuan tim BE dan FE.
- Daftar ini hanya mencakup 16 spek yang diajukan untuk General Settings. Beberapa spek punya judul yang sangat singkat (misalnya "Bypass DOM A" dan "Dua admin"), jadi penilaian dampaknya perlu diverifikasi dengan melihat `spec.md` lengkap sebelum keputusan final.
