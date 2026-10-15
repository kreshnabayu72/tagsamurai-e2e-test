---
id: TC-AC-PP-E2E-050-log-snapshot-nama-aktor
title: "Snapshot Nama Aktor pada Published By dan Activity Log Setelah Akun Diganti Nama atau Dihapus"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-161
coverage:
  web: automated
---

# Snapshot Nama Aktor pada Published By dan Activity Log Setelah Akun Diganti Nama atau Dihapus

## Prerequisites

- Mode: FE+BE.
- Dua konteks browser berjalan bersamaan: sesi 1 untuk aktor Publish dan sesi 2 untuk Administrator.

| Sesi | Peran | Nama tampil | Email | Env var password |
|---|---|---|---|---|
| 1 (aktor Publish, akun sekali pakai, Pre-setup 17) | Total Control | `Andi Saputra` | `snapshotAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SNAP_PASSWORD` |
| 2 (Administrator, Pre-setup 1) | Total Control | `Andi Wijaya` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1; Published By `John Doe`, `John Doe`, `Jane Smith` dengan akun sudah dihapus), membuat ulang akun aktor Publish `Andi Saputra` (dibuat ulang per TC), lalu login sesi 1 sebagai akun itu (aktor pertama). Login Administrator di sesi 2 adalah langkah eksplisit di `## Test Steps`.
- Hook `after` (tetap jalan walau spec gagal di tengah): menghapus akun aktor Publish (termasuk bila sudah berganti nama menjadi `Andi Pratama` atau sudah di-soft-delete), mengembalikan dataset ke Riwayat A lewat Fixture BE, dan mengembalikan sesi browser ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Kemampuan teknis: dua konteks browser paralel; Fixture BE untuk seeding Riwayat A dan akun sekali pakai; akses Administrator ke Settings > User (Detail, ganti nama, hapus) dan ke Activity Log Admin Console.
- Data ganti nama: `Andi Saputra` menjadi `Andi Pratama`. Nama env `AC_SNAP_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`, belum terdaftar (`AC_TC_PASSWORD` sudah terdaftar); password tidak ditulis di spec atau fixture.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish `Version 4`, sehingga suite berjalan serial (`parallel: false`) dan dataset dipulihkan ke Riwayat A di hook `after`.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Langkah 1 |

## Test Steps

### TC-AC-PP-161: Nama aktor pada Published By dan entri log tidak berubah setelah akun diganti nama atau dihapus

1. Pada sesi 1 (akun `snapshotAdminConsole_automated_{namaCompany}@qwertysystem.net`, `Andi Saputra`), buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
2. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
3. Klik di akhir konten editor lalu ketik " Snapshot."
4. Klik `[Publish New Version]`
5. Klik `[Publish]` pada Dialog Publish Confirm sehingga `Version 4` terbentuk
6. Buka sesi 2 sebagai konteks browser terpisah dan login sebagai Administrator `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`)
7. Pada sesi 2, buka Activity Log (Admin Console) dan catat entri teratas dengan Object `Privacy Policy` (entri `Publish` untuk `Version 4` milik spec ini: Name, Old Value, New Value, Modified By, Date) sebagai baseline
8. Pada sesi 2, buka Settings > User lalu ganti nama user `Andi Saputra` menjadi `Andi Pratama`
9. Pada sesi 2, buka Settings > Privacy Policy dan amati baris `Version 4`
10. Verifikasi Published By pada baris `Version 4` tetap `Andi S`
11. Hover teks `Andi S` pada baris `Version 4`
12. Verifikasi tooltip `Andi Saputra` tampil
13. Pada sesi 2, hapus (soft-delete) akun `Andi Pratama` lewat Settings > User
14. Muat ulang halaman Settings > Privacy Policy pada sesi 2 dan amati baris `Version 4`
15. Verifikasi baris `Version 4` tetap menampilkan `Andi S`
16. Verifikasi baris `Version 4` tidak menampilkan `—`
17. Pada sesi 2, buka Activity Log (Admin Console) dan cari entri baseline yang dicatat di langkah 7 (penanda: Name `Version 4`, Date, dan posisi teratas dengan Object `Privacy Policy`)
18. Verifikasi Modified By pada entri baseline sama dengan nilai yang dicatat di langkah 7
19. Verifikasi entri baseline tidak menampilkan nama baru `Andi Pratama`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness c (multi-konteks): dua sesi browser dengan akun berbeda. Seluruh spec memakai satu TC sehingga tidak ada pemisahan kelas lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penghubung: login sesi 2 (langkah 6) adalah ganti konteks akun yang eksplisit. Langkah 7 (catat baseline entri) dan langkah 17 (cari entri baseline) adalah langkah baca beralasan S-12: log append-only dan reseed Riwayat A di spec lain menghasilkan banyak entri `Version 4`, jadi entri milik spec ini diidentifikasi sebagai entri teratas segera setelah Publish pada langkah 5 (suite serial) dan dibandingkan dengan catatan itu setelah rename dan hapus akun.
- Akun aktor mengikuti Pre-setup TC (Total Control). Akun `AC_PRINCIPAL_PP_PASSWORD` yang sudah terdaftar di config belum dipetakan ke Pre-setup; menunggu konfirmasi tim FE.
- Temuan untuk QA:
  - TC menyebut "ganti nama" dan "hapus (soft-delete)" lewat Settings > User tanpa merinci field, tombol, atau dialog di layar Settings > User; langkah 8 dan 13 mengikuti kalimat TC dan perincian layar diambil dari TC modul User.
  - Expected c ("tidak berubah mengikuti nama baru") tidak menyebut nilai kolom Modified By yang seharusnya tampil; langkah 18 mengasersi Modified By entri baseline sama dengan catatan langkah 7, dan langkah 19 mengasersi tidak adanya nama baru `Andi Pratama`.
  - Post Condition TC ("Snapshot nama aktor tetap `Andi Saputra`") tidak punya langkah observasi tambahan dan tidak diasersi di luar Expected a dan b.
