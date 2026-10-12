---
id: TC-GS-BRAND-E2E-068-defense-in-depth-bypass-server-dan-xss
title: "Defense-in-Depth Brand: Bypass UI ke Server, Emoji Lolos Filter FE, dan Payload Script"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-226
  - TC-GS-BRAND-227
  - TC-GS-BRAND-230
  - TC-GS-BRAND-231
coverage:
  web: automated
---

# Defense-in-Depth Brand: Bypass UI ke Server, Emoji Lolos Filter FE, dan Payload Script

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | System Role: Read saja (Tono Hartono) | `readCapability_automated_qaTeam1@qwertysystem.net` | `GS_READ_PASSWORD` |
  | 2 | Total Control Client A (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun 2).
- Environment variable: `GS_READ_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah karena request Delete ditolak, tanpa suffix `{runId}`): `Acme Corp` (in-use: FAMS Asset Name Forklift).
- Data dinamis: brand `<b>Bold</b> Co {runId}-068` (D-30), dibuat spec lewat UI pada TC-GS-BRAND-231 (nama dengan tag HTML literal). Input uji `Rogue Co` (TC-GS-BRAND-226) dan `Bad🌟Co` (TC-GS-BRAND-230) adalah input yang submit-nya diblokir sehingga dipakai literal dan tidak membuat data.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `<b>Bold</b> Co {runId}-068` dan `Rogue Co` bila ada.
- Kemampuan teknis: (a) mengirim request HTTP langsung ke server dari konteks browser yang login (console/fetch dengan token sesi) untuk TC-GS-BRAND-226 dan 227; (b) menyetel nilai field Brand Name langsung lewat DOM, melewati validasi FE, untuk TC-GS-BRAND-230.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-226: login sebagai System Role: Read saja. TC-GS-BRAND-227, 230, 231: login sebagai Total Control. Semua berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-226: Server menolak Create dari aktor tanpa capability Create walau UI di-bypass

1. Buka Global Settings > Master Reference > Brand
2. Kirim request Create Brand `Rogue Co` lewat console browser
3. Verifikasi toast error: "You don't have permission to do this."
4. Search `Rogue Co` pada tabel Brand
5. Verifikasi `Rogue Co` tidak ada di tabel

### TC-GS-BRAND-230: Emoji yang lolos filter FE ditolak server

6. Logout, lalu login sebagai Total Control Client A (`totalControl_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`
7. Buka Global Settings > Master Reference > Brand, klik [+ Brand]
8. Injeksi value `Bad🌟Co` langsung ke DOM field Brand Name (bypass validasi FE)
9. Klik [Submit]
10. Verifikasi pesan `Brand Name contains invalid characters`
11. Klik `✕` pada form Create Brand
12. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`
14. Search `Bad🌟Co` pada tabel Brand
15. Verifikasi record `Bad🌟Co` tidak dibuat (tidak ada di tabel)
16. Kosongkan Search

### TC-GS-BRAND-227: Server menolak Delete Brand in-use walau dialog dilewati (Expected Result a)

17. Kirim request Delete Acme Corp langsung ke server (tanpa melewati dialog)
18. Verifikasi Acme Corp tetap ada di tabel Brand

### TC-GS-BRAND-231: Payload script disimpan sebagai teks dan tidak dieksekusi

19. Klik [+ Brand], isi Brand Name `<b>Bold</b> Co {runId}-068`, klik [Submit]
20. Verifikasi nama tampil literal `<b>Bold</b> Co {runId}-068` di tabel
21. Buka Detail `<b>Bold</b> Co {runId}-068`
22. Verifikasi nama tampil literal `<b>Bold</b> Co {runId}-068` di Detail
23. Buka Changelog
24. Verifikasi nama tampil literal `<b>Bold</b> Co {runId}-068` di Changelog
25. Verifikasi tidak ada HTML yang dirender (tidak ada teks tebal dari tag `<b>`) di tabel, Detail, dan Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas defense-in-depth (prinsip 13a) tanpa harness eksternal.
- Urutan TC di spec berbeda dari urutan sumber: 226 (akun Read saja) lebih dulu, lalu satu kali ganti akun ke Total Control (langkah 6) untuk 230, 227, dan 231; aksi yang membuat data (231) paling akhir (prinsip 3.3 konvensi).
- TC-GS-BRAND-227 hanya memuat Expected Result a (Acme Corp tetap ada). Expected Result b ("Tidak ada entri Delete di Changelog") adalah asersi absence (kelas g) dan ada di spec `TC-GS-BRAND-E2E-075-log-absence-dua-sesi-dan-request-langsung`. Request Delete Acme Corp langsung ke server karenanya dikirim sekali di spec ini (langkah 17) dan sekali di spec 075, karena asersi absence dipisah dari asersi fungsional.
- TC-GS-BRAND-226 dan 227 berstatus `Manual Only` di TC sumber; sesuai bagian 2 konvensi, hambatan teknis bukan alasan mengeluarkan TC. Kemampuan teknis yang dibutuhkan dicatat di Prerequisites untuk tim FE.
- Urutan dalam TC-GS-BRAND-230: Verifikasi record tidak dibuat (langkah 15) dijalankan sesudah form ditutup (langkah 11 sampai 13) dan Search (langkah 14), karena tabel Brand tertutup modal selama form terbuka.
- Langkah penghubung: langkah 1 dan 7 (membuka halaman Brand), langkah 4, 14, dan 16 (Search nama brand yang diasersikan tidak ada, lalu mengosongkan Search), langkah 11 sampai 13 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`, sebagai pembersihan state antar TC). Verifikasi dialog pada langkah 12 adalah asersi tambahan yang tidak ada di TC; ditulis agar penutupan form deterministik (konvensi bagian 10 S-08).
