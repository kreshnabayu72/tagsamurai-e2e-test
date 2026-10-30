---
id: TC-GS-ROLE-E2E-093-tanpa-gating-plan-role-tampil-di-semua-plan
title: "Fitur Ber-Plan Tetap Muncul sebagai Role di Semua Plan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-246
coverage:
  web: automated
---

# Fitur Ber-Plan Tetap Muncul sebagai Role di Semua Plan

## Prerequisites

- Mode: FE+BE.
- Kelas harness: state tenant (kelas h), perbedaan plan antar Client. Spec tidak mengubah plan; keempat Client sudah berada di plan masing-masing (Pre-setup #16).
- Role yang diuji (Total Control, Ahmad Fauzi, pada Client masing-masing plan; email dan kandidat disediakan tim FE karena tidak ada di Tabel Data Uji Pre-setup TC):

| Plan | Akun Total Control | Kandidat Assign Role | Env var password |
|---|---|---|---|
| Starter | Ahmad Fauzi, Client plan Starter | satu user kandidat tanpa baris role di Client Starter | `Spectra.env.GS_PLANSTARTER_TC_PASSWORD` |
| Growth | Ahmad Fauzi, Client plan Growth | satu user kandidat tanpa baris role di Client Growth | `Spectra.env.GS_PLANGROWTH_TC_PASSWORD` |
| Professional | Ahmad Fauzi, Client plan Professional | satu user kandidat tanpa baris role di Client Professional | `Spectra.env.GS_PLANPRO_TC_PASSWORD` |
| Enterprise | Ahmad Fauzi, Client plan Enterprise | satu user kandidat tanpa baris role di Client Enterprise | `Spectra.env.GS_PLANENT_TC_PASSWORD` |

- Login akun plan Starter (aktor pertama) dilakukan di hook `before`; plan lain memakai langkah ganti akun eksplisit (logout lalu login). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`. Env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data: keempat kandidat dibuat atau disediakan tim FE sebagai user Active dengan Access Global Settings, tanpa access level dan tanpa baris role. Langkah Assign Role meng-assign baris Manage TAG; hook `after` menghapus baris itu pada keempat Client lewat API (sesi API Total Control tiap Client).
- Kemampuan teknis: empat Client pada plan berbeda dengan akun Total Control masing-masing; login ganti akun lintas Client; seeding dan pemulihan baris role lewat API per Client.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite), termasuk untuk akun keempat plan; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada pada plan (hanya baris role kandidat, dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### Plan Starter

1. Buka Global Settings > Role & Permission > Tab System
2. Verifikasi keenam role (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) tampil di Tab System
3. Buka Detail "Manage TAG", klik `[+ Assign]`
4. Centang kandidat Client plan Starter
5. Klik `[Assign]`
6. Verifikasi toast sukses: "Success, role has been assigned."

### Plan Growth

7. Logout, lalu login sebagai Total Control Client plan Growth
8. Buka Global Settings > Role & Permission > Tab System
9. Verifikasi keenam role (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) tampil di Tab System
10. Buka Detail "Manage TAG", klik `[+ Assign]`
11. Centang kandidat Client plan Growth
12. Klik `[Assign]`
13. Verifikasi toast sukses: "Success, role has been assigned."

### Plan Professional

14. Logout, lalu login sebagai Total Control Client plan Professional
15. Buka Global Settings > Role & Permission > Tab System
16. Verifikasi keenam role (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) tampil di Tab System
17. Buka Detail "Manage TAG", klik `[+ Assign]`
18. Centang kandidat Client plan Professional
19. Klik `[Assign]`
20. Verifikasi toast sukses: "Success, role has been assigned."

### Plan Enterprise

21. Logout, lalu login sebagai Total Control Client plan Enterprise
22. Buka Global Settings > Role & Permission > Tab System
23. Verifikasi keenam role (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) tampil di Tab System
24. Buka Detail "Manage TAG", klik `[+ Assign]`
25. Centang kandidat Client plan Enterprise
26. Klik `[Assign]`
27. Verifikasi toast sukses: "Success, role has been assigned."

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke plan; semua langkah berasal dari TC-GS-ROLE-246.
- Spec berbentuk empat blok per plan (bukan perulangan atas tabel) karena akun login tiap plan berbeda dan login aktor pertama harus berada di hook `before`; isi tiap blok identik (langkah 1 sampai 6 diulang pada langkah 8 sampai 13, 15 sampai 20, 22 sampai 27).
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti akun (langkah 7, 14, 21); membuka Tab System dan Detail "Manage TAG" (langkah 1, 3, 8, 10, 15, 17, 22, 24).
- Verifikasi keenam role memakai satu `Verifikasi` untuk enam role karena Expected a TC menyebut "Keenam role tampil" sebagai satu klausa.
- Temuan untuk QA:
  - TC-GS-ROLE-246 tidak menyebut akun Total Control, email, dan kandidat Assign Role di tiap Client plan; spec menulisnya "disediakan tim FE" dan memakai satu kandidat per Client.
  - TC-GS-ROLE-246 Langkah Uji 2 ("Assign Role Manage TAG ke 1 user") tidak menyebut kandidat; spec memakai kandidat tanpa baris role yang disediakan tim FE.
  - TC-GS-ROLE-246 tidak menyebut cara memulihkan baris Manage TAG yang dibuat pada tiap plan; spec memulihkannya di hook `after`.
