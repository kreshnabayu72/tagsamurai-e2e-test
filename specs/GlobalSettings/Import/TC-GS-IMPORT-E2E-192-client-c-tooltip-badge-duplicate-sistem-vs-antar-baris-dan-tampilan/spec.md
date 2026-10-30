---
id: TC-GS-IMPORT-E2E-192-client-c-tooltip-badge-duplicate-sistem-vs-antar-baris-dan-tampilan
title: "Client C: tooltip badge duplicate (sistem vs antar-baris) dan tampilan nilai Tab User Login (Access, Phone, tanggal mentah, strip) hasil unggah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-476
  - TC-GS-IMPORT-769
coverage:
  web: automated
---

# Client C: tooltip badge duplicate (sistem vs antar-baris) dan tampilan nilai Tab User Login (Access, Phone, tanggal mentah, strip) hasil unggah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client C; Sub-Tab User Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Pre-setup: Client C tanpa draft Tab Brand dan Tab User Login (Kontrak Fixture R1; reset oleh hook `beforeEach` suite). Brand `Samsung` ada di Client C. Custom Field Active Client C: Shift (Dropdown), Shift Notes (Text Area), Overtime Hours (Numeric), Emergency Phone (Phone), Join Date (Date), dan Tax ID (Text, opsional). Division `Engineering`, `Marketing` dan Position `Senior Developer` ada di Client C (R4).
- Berkas uji (pembuat data lewat upload UI): `brand-tooltip.csv` (header `Brand Name`; 4 baris berurutan `Samsung`, `Pioneer`, `Nexus`, `Pioneer`); `user-login-display.csv` (header First Name; Last Name; Email; Division; Position; Employee ID; Access; Active Period; Shift; Shift Notes; Overtime Hours; Emergency Phone; Join Date; 2 baris: (1) Gita, Permata, `gita.permata.disp@example.com`, Engineering, Senior Developer, EMP-9001, `Global Settings;Fixed Asset`, Active Period tanggal besok, Shift `Pagi`, Shift Notes `Handles night shift`, Overtime Hours `7.5`, Emergency Phone `+6281234567890`, Join Date 30 hari sebelum hari uji; (2) Hadi, Pranoto, `hadi.pranoto.disp@example.com`, Marketing, Access `Global Settings`, kolom lain kosong; tanpa kolom Tax ID). Tanggal dihitung saat berkas dibuat dalam bentuk `YYYY-MM-DD`. Email berkas diberi suffix per run `+{runId}-192` sebelum `@` bila hook mengizinkan; bila tidak, email literal dibersihkan di hook `before` (draft tidak di-commit).
- Cleanup (hook `after`): draft Brand dan draft User Login Client C dibuang lewat skrip reset. Tidak ada commit, sehingga tidak ada record master data baru.
- Kemampuan teknis: hover badge, pemilihan berkas pada dialog unggah.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Tooltip badge duplicate (TC-GS-IMPORT-476)

1. Klik `[Upload File]` dan pilih berkas `brand-tooltip.csv`
2. Klik `[Confirm Mapping]`
3. Hover badge `duplicate` baris 1 (`Samsung`)
4. Verifikasi tooltip "Brand name already exists. This row will be skipped automatically."
5. Hover badge `duplicate` baris 2 (`Pioneer` pertama)
6. Verifikasi tooltip "This row duplicates another row in this draft. It will be skipped automatically."

### Tampilan nilai Tab User Login (TC-GS-IMPORT-769)

7. Pindah ke Sub-Tab User Login
8. Klik `[Upload File]` dan pilih berkas `user-login-display.csv`
9. Klik `[Confirm Mapping]`
10. Verifikasi header: Checkbox, #, First Name, Last Name, Email, Division, Position, Employee ID, Access, Active Period, diikuti Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes, dan Tax ID, lalu Status dan Actions
11. Verifikasi Row # 1: sel Tax ID tampil `—`
12. Verifikasi Row # 1: Access tampil `Global Settings;Fixed Asset` dengan pemisah `;`
13. Verifikasi Row # 1: Emergency Phone tampil `+62 81234567890` (satu spasi antara kode negara dan nomor)
14. Verifikasi Row # 1: Join Date tampil tanggal 30 hari sebelum hari uji persis seperti isi berkas dalam bentuk `YYYY-MM-DD`
15. Verifikasi Row # 1: Active Period tampil tanggal besok dalam bentuk `YYYY-MM-DD`
16. Verifikasi Row # 2: sel Position, Employee ID, Active Period, Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes, dan Tax ID menampilkan `—`
17. Verifikasi kedua baris berstatus `pending`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec pembuat data (upload UI) tanpa commit; draft dibuang di hook `after`.
- Pindah Sub-Tab pada langkah 7 adalah langkah penghubung (S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-769 Data Uji menulis Email `gita.permata.disp@example.com` dan `hadi.pranoto.disp@example.com` tanpa suffix per run; spec memakai suffix per run bila hook mengizinkan, dan asersi tidak memuat teks Email.
  - TC-GS-IMPORT-769 Expected a menyebut Tax ID sebagai kolom Custom Field Active tetapi berkas tidak memuat kolomnya; spec mengikuti TC (kolom tampil `—`).
  - TC-GS-IMPORT-476 dan 769 tidak memuat Post Condition.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
