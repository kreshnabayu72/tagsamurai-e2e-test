---
id: TC-AC-PP-E2E-006-first-time-publish-pertama-dan-log
title: "Publish Pertama pada First-time Setup Menghasilkan Version 1 Active dan Entri Log Publish"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-35
  - TC-AC-PP-156
coverage:
  web: automated
---

# Publish Pertama pada First-time Setup Menghasilkan Version 1 Active dan Entri Log Publish

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Dataset Riwayat C (0 versi). Hook `before` men-seed dataset ini lewat Fixture BE; riwayat append-only sehingga spec menyiapkan ulang Riwayat C lewat Fixture BE di antara TC-AC-PP-35 dan TC-AC-PP-156 (langkah penghubung); hook `after` mengembalikan dataset ke Riwayat A. Spec ini membuat satu versi (Version 1) per TC; versi tidak bernama sehingga tidak memakai suffix per run.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kemampuan teknis: Fixture BE (membuat ulang Riwayat C); akses ke Activity Log Admin Console untuk membaca entri teratas dengan Object `Privacy Policy`.
- State global: dokumen Privacy Policy dan Activity Log bersifat platform-wide; suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-PP-35: Publish pertama pada first-time setup menghasilkan Version 1 yang langsung Active

1. Klik menu Settings > Privacy Policy di sidebar
2. Klik [Create Privacy Policy]
3. Klik area editor lalu ketik "Initial privacy policy for the platform."
4. Klik [Publish New Version]
5. Verifikasi Dialog Publish Confirm terbuka
6. Klik [Publish]
7. Verifikasi muncul toast sukses: "Success, Privacy Policy has been published."
8. Verifikasi Dialog Publish Confirm tertutup
9. Verifikasi Modal tertutup
10. Verifikasi kembali ke tabel Version History
11. Verifikasi tabel menampilkan 1 baris: `Version 1` + badge `Active`
12. Verifikasi Published At baris `Version 1` bernilai tanggal hari ini sesuai Date Format `dd MMM yy`
13. Verifikasi Published By baris `Version 1` bernilai `Andi W`
14. Verifikasi empty state tidak tampil lagi
15. Verifikasi button [Create Privacy Policy] tidak tampil lagi

### TC-AC-PP-156: Publish pertama pada first-time setup mencatat Old Value kosong dan New Value Version 1

16. Kembalikan dataset ke Riwayat C (0 versi) lewat Fixture BE, lalu muat ulang Settings > Privacy Policy
17. Buka Activity Log (Admin Console) dan catat jumlah entri dengan Object `Privacy Policy` sebagai baseline
18. Klik menu Settings > Privacy Policy di sidebar
19. Klik [Create Privacy Policy], ketik "First policy.", klik [Publish New Version] lalu klik [Publish]
20. Buka Activity Log dan cari entri teratas dengan Object `Privacy Policy`
21. Verifikasi jumlah entri dengan Object `Privacy Policy` bertambah dibanding baseline sehingga entri teratas adalah entri hasil Publish ini
22. Verifikasi entri teratas: Action `Publish`
23. Verifikasi entri teratas: Object `Privacy Policy`
24. Verifikasi entri teratas: Field `Content`
25. Verifikasi entri teratas: New Value `Version 1`
26. Verifikasi entri teratas: Name `Version 1`
27. Verifikasi entri teratas: Old Value `—`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Verifikasi langkah 5 (Dialog Publish Confirm terbuka) diturunkan dari tanda "→" di kolom Langkah Uji TC-AC-PP-35, bukan dari kolom Expected Result; ditambahkan sebagai penanda state sebelum klik [Publish] (S-03).
- Langkah penghubung (S-03, S-12): langkah 16 (reset dataset ke Riwayat C karena riwayat append-only; TC-AC-PP-156 mensyaratkan Riwayat C), langkah 17 dan 21 (baseline jumlah entri log agar entri baru dapat diidentifikasi tanpa mengandalkan data log sebelumnya; asersi pertambahan jumlah ditambahkan sebagai identifikasi baseline, bukan Expected TC), langkah 18.
- Post Condition TC-AC-PP-35 (Published By snapshot `Andi Wijaya`; satu record audit dengan Old Value `—` dan New Value `Version 1`) tidak punya langkah observasi di TC-AC-PP-35. Rincian record audit diobservasi lewat TC-AC-PP-156 (Name, Old Value, New Value); snapshot lengkap nama `Andi Wijaya` diverifikasi lewat tooltip di spec lain (TC-AC-PP-155) dan tidak diasersi di sini.
- Pembagian TC lintas spec: entri log Publish di dua surface (System Log dan Activity Log) untuk versi berikutnya ada di spec 049; asersi absence log di spec 051.
- Temuan untuk QA:
  - TC-AC-PP-35 Expected c menyebut "tanggal hari ini" tanpa menyatakan zona waktu/format perbandingan; spec membandingkan dengan tanggal hari ini pada Time Zone General Settings (UTC).
  - TC-AC-PP-156 Expected tidak menyebut kolom Date entri log; tidak diasersi.
