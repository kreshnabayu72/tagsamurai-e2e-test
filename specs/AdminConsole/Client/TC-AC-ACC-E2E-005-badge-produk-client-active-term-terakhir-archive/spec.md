---
id: TC-AC-ACC-E2E-005-badge-produk-client-active-term-terakhir-archive
title: "Badge Produk Client Active untuk Produk dengan Term Live yang Sudah Tidak Ada"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-467
coverage:
  web: automated
---

# Badge Produk Client Active untuk Produk dengan Term Live yang Sudah Tidak Ada

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-15 | Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng) | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Login di hook `before` spec ini (Active-Full, A-15); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Data Pre-setup: fixture A3 C-FX19-2 `PT Badge Arsip Sebagian` (Active; Client Code `FX19-002`; Partner CV Mitra Sejati; Group Area Jakarta; FAMS satu-satunya term Active; SAMS satu-satunya term Archive; SIEM tidak pernah berlangganan; Residen). Hanya dibaca.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-467: Badge produk Client Active untuk produk dengan term live yang sudah tidak ada

1. Klik sub-tab `Active`
2. Ketik Search `PT Badge Arsip Sebagian`, tekan Enter
3. Lihat sel FAMS dan SAMS Client tersebut di sub-tab `Active`
4. Verifikasi sel FAMS adalah badge `Active` severity success
5. Verifikasi sel SAMS adalah badge `Archive` severity dark
6. Verifikasi sel SAMS bukan teks `No Subscription`
7. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: badge produk lain (Active, Grace, Expired, Archive, Purge, Deleted, No Subscription) ada di spec 004.
- Temuan untuk QA:
  - TC-AC-ACC-467: Expected "bukan 'No Subscription'" ditulis sebagai `Verifikasi` tersendiri atas sel SAMS yang sama (anchor: badge `Archive` tampil pada langkah sebelumnya).
