---
id: TC-AC-ACC-E2E-008-empty-state-genuinely-kosong-tiga-sub-tab
title: "Empty State Genuinely Kosong pada Tiga Sub-tab List Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-20
  - TC-AC-ACC-21
  - TC-AC-ACC-22
coverage:
  web: automated
---

# Empty State Genuinely Kosong pada Tiga Sub-tab List Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-GRP-3 | Active-Full + Archived-Read Kemang (Manage active client: C/R/U/D dan Manage archived client: Read, exact-match Cabang Kemang) | `activeFullArchivedReadKemang_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GRP3_PASSWORD` |

- Login di hook `before` spec ini (Active-Full + Archived-Read Kemang, A-GRP-3); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Group `Cabang Kemang` tidak memiliki Client berstatus Active, Suspended, maupun Archived pada view aktor ini (satu-satunya node assignment aktor; Tabel A3, populasi Cabang Kemang kosong). Spec read-only.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-20: Empty state genuinely kosong sub-tab Active

1. Klik sub-tab `Active`
2. Verifikasi empty state: ilustrasi dengan judul `No clients yet` dan deskripsi `Get started by creating your first client.`
3. Verifikasi tidak ada tombol atau CTA di dalam empty state
4. Verifikasi tombol `[+ New Client]` tetap ada di toolbar

### TC-AC-ACC-21: Empty state genuinely kosong sub-tab Suspended

5. Klik sub-tab `Suspended`
6. Verifikasi empty state: ilustrasi dengan judul `No suspended clients` dan deskripsi `Suspended clients will appear here.`
7. Verifikasi tidak ada tombol atau CTA di dalam empty state

### TC-AC-ACC-22: Empty state genuinely kosong sub-tab Archived

8. Klik sub-tab `Archived`
9. Verifikasi empty state: ilustrasi dengan judul `No archived clients` dan deskripsi `Archived clients will appear here.`
10. Verifikasi tidak ada tombol atau CTA di dalam empty state

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Ilustrasi, judul, dan deskripsi empty state ditulis satu `Verifikasi` karena Expected TC menyebutnya satu butir (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-20 sampai 22: precondition c menyebut Data Pre-setup C-01…C-14 tersedia tetapi tidak berpengaruh pada aktor ini (hanya Group `Cabang Kemang`); precondition d menjadi penentu dan dijamin oleh Tabel A3 (Cabang Kemang tanpa Client).
