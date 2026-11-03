---
id: TC-AC-SU-E2E-194-user-list-sort-3-state-kelas-teks
title: "User List Sort: Sort 3-State Kelas Teks dengan Nilai Kosong di Akhir dan di Awal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-294
coverage:
  web: automated
---

# User List Sort: Sort 3-State Kelas Teks dengan Nilai Kosong di Akhir dan di Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-194`):
| Nama | Email | Position | Division | Employee ID | TAG |
|---|---|---|---|---|---|
| `anisa rahma {runId}-194` | `d.anisa@{runId}-194.qwertysystem.net` | `Analyst` | `Operations` | `EMP-4-{runId}-194` | `E2801{runId}1` |
| `Budi Santoso {runId}-194` | `c.budi@{runId}-194.qwertysystem.net` | `Manager` | `Finance` | `EMP-3-{runId}-194` | `E2801{runId}2` |
| `Citra Dewi {runId}-194` | `b.citra@{runId}-194.qwertysystem.net` | `Clerk` | `Marketing` | `EMP-2-{runId}-194` | `E2801{runId}3` |
| `Dedi Kurnia {runId}-194` | `a.dedi@{runId}-194.qwertysystem.net` | (kosong) | `Audit` | (kosong) | (kosong) |
- Asersi urutan memakai urutan relatif antar keempat baris milik spec; baris Pre-setup ikut tampil dan tidak diasersi.
- Tabel urutan TC-294 (parameter langkah 7 sampai 12; nama baris disingkat dengan nama depan):
| No | Kolom | Urutan relatif klik 1 (A-Z, ikon ↑) | Urutan relatif klik 2 (Z-A, ikon ↓) |
|---|---|---|---|
| 1 | Name | anisa, Budi, Citra, Dedi | Dedi, Citra, Budi, anisa |
| 2 | Email | Dedi, Citra, Budi, anisa | anisa, Budi, Citra, Dedi |
| 3 | Position | anisa, Citra, Budi, Dedi (kosong `—` di akhir) | Dedi (kosong `—` di awal), Budi, Citra, anisa |
| 4 | Division | Dedi, Budi, Citra, anisa | anisa, Citra, Budi, Dedi |
| 5 | Employee ID | Citra, Budi, anisa, Dedi (kosong `—` di akhir) | Dedi (kosong `—` di awal), anisa, Budi, Citra |
| 6 | TAG | anisa, Budi, Citra, Dedi (kosong `—` di akhir) | Dedi (kosong `—` di awal), Citra, Budi, anisa |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-294: Sort 3-state kelas teks (Name default, Email, Position, Division, Employee ID, TAG)

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Centang kolom `TAG` pada Setup Column
4. Klik `[Save]`
5. Amati urutan awal tabel
6. Verifikasi urutan awal Name A-Z case-insensitive: baris `anisa rahma {runId}-194` sebelum `Budi Santoso {runId}-194`
7. Klik header kolom pada kolom "Kolom" tabel urutan TC-294 (klik 1)
8. Verifikasi urutan relatif baris pada kolom "Urutan relatif klik 1" tabel urutan TC-294
9. Klik header kolom yang sama (klik 2)
10. Verifikasi urutan relatif baris pada kolom "Urutan relatif klik 2" tabel urutan TC-294
11. Klik header kolom yang sama (klik 3)
12. Verifikasi urutan kembali ke default Name A-Z (anisa, Budi, Citra, Dedi)

## Notes

- Langkah 7 sampai 12 diulang untuk tiap baris tabel urutan TC-294 (8b butir 7); parameter ada di Prerequisites, `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): Setup Column menampilkan kolom TAG sebelum disortir (langkah 1 TC); konfigurasi kolom dipulihkan hook `after`.
- Alasan di atas ±35 langkah (ekspansi): satu TC dengan enam kolom yang langkahnya identik; berdiri sendiri.
- TC-295 sampai TC-297 dan TC-656 (sort lain) ada di spec 083.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-194` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-294 menyebut nilai kosong di akhir/awal untuk Position, Employee ID, dan TAG; spec mengasersi posisi relatif terhadap baris milik spec saja karena baris Pre-setup dengan nilai kosong juga ikut tampil.
