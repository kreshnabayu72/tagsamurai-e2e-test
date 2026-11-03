---
id: TC-AC-ACC-E2E-014-pindah-group-distributor-memindahkan-group-client-langsung
title: "Pindah Group Distributor Otomatis Memindahkan Group Client Distributor-langsung (Resolve Runtime)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-38
coverage:
  web: automated
---

# Pindah Group Distributor Otomatis Memindahkan Group Client Distributor-langsung (Resolve Runtime)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Distributor `PT Distribusi Nusantara` (D1, Group `Area Jakarta`, Pre-setup) adalah target aksi tulis sesuai TC (S-06: Group Distributor memang data bersama yang dibaca viewer lain); efek: Group D1 diubah ke `Area Surabaya` lalu dipulihkan ke `Area Jakarta` oleh langkah spec; Modified By, Last Updated, dan Changelog Distributor bertambah. Hook `after` memulihkan Group D1 ke `Area Jakarta` lewat Fixture BE bila spec gagal di tengah.
- State global bersama: tidak ada spec lain yang membaca node Group `Area Jakarta`, `Area Surabaya`, atau Group jaringan D1 saat spec ini berjalan (suite serial); precondition d TC-AC-ACC-38 menyebut TC-AC-ACC-6 sebagai contoh.
- Kemampuan teknis: akses ke Admin Console > Distributor oleh Total Control (Edit Distributor, Select Group) pada sesi yang sama.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-38: Pindah Group Distributor otomatis memindahkan Client Distributor-langsung di mata Principal

1. Ketik Search `PT Sinar Distributor`, tekan Enter
2. Lihat sel Group baris `PT Sinar Distributor`
3. Verifikasi Group `PT Sinar Distributor` adalah `Area Jakarta`
4. Buka Admin Console > Distributor, ketik Search `PT Distribusi Nusantara`, tekan Enter, buka `⋯` baris `PT Distribusi Nusantara`, lalu klik `Edit`
5. Ganti Select Group dari `Area Jakarta` ke `Area Surabaya`, lalu klik `[Save]`
6. Tunggu aksi `[Save]` selesai (popup Edit tertutup)
7. Muat ulang Admin Console > Client, ketik Search `PT Sinar Distributor`, tekan Enter
8. Lihat sel Group baris `PT Sinar Distributor`
9. Verifikasi Group `PT Sinar Distributor` berubah ke `Area Surabaya` tanpa edit per Client (Derived, bukan salinan tersimpan)
10. Buka Admin Console > Distributor, ketik Search `PT Distribusi Nusantara`, tekan Enter, buka `⋯` baris `PT Distribusi Nusantara`, klik `Edit`, kembalikan Select Group ke `Area Jakarta`, klik `[Save]`, lalu tunggu popup Edit tertutup

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 10. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Langkah 4 dan 5 memakai modul Distributor (Edit Distributor) hanya sebagai pemicu perubahan Group Distributor; perilaku Edit Distributor bukan objek uji spec ini.
- Temuan untuk QA:
  - TC-AC-ACC-38: Expected tidak menyebut toast hasil `[Save]` di Admin Console > Distributor; spec memakai langkah penghubung "Tunggu aksi selesai" sebelum berpindah ke List.
