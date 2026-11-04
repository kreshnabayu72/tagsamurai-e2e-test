---
id: TC-FA-PREF-E2E-079-defense-in-depth-request-langsung-mengubah-field-terkunci-ditolak
title: "Defense-in-Depth: Request Langsung Mengubah Fiscal Year Start dan First Accounting Period yang Terkunci Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-249
  - TC-FA-PREF-250
  - TC-FA-PREF-519
  - TC-FA-PREF-520
  - TC-FA-PREF-521
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Mengubah Fiscal Year Start dan First Accounting Period yang Terkunci Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-249 dan 250 memakai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026), PB-2 (akun Chart of Accounts tersedia), dan PB-7a (posting penyusutan pertama: Last Posted Period terisi pada Asset Class `IT Equipment`). TC-519 sampai 521 memakai PC-2 (posting penyusutan pertama ada; satu periode berstatus Soft Closed). Kunci dibentuk lewat seed BE; dipasang di hook `before` dan di langkah 15, "disediakan tim FE" tanpa endpoint karangan (S-13).
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP, baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10), dan seed ulang penguncian. Disediakan tim FE/BE.
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. TC-521 menyimpan In-service Date Source "Manual by Accounting"; pemulihan ke nilai awal dilakukan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-249: Permintaan langsung mengubah Fiscal Year Start saat terkunci ditolak server

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
2. Kirim request langsung Save Preferences (fixture BE) dengan Fiscal Year Start = July
3. Verifikasi server menolak permintaan
4. Buka kembali Settings > Accounting > Preferences
5. Verifikasi Fiscal Year Start tetap "January" pada tab Preferences
6. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
7. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)

### TC-FA-PREF-250: Permintaan langsung mengubah First Accounting Period saat terkunci ditolak server

8. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
9. Kirim request langsung Save Preferences (fixture BE) dengan First Accounting Period = Jan 2026
10. Verifikasi server menolak permintaan
11. Buka kembali Settings > Accounting > Preferences
12. Verifikasi First Accounting Period tetap "Mar 2026" pada tab Preferences
13. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
14. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)
15. Seed ulang penguncian ke PC-2 lewat API (Fiscal Year Start January, First Accounting Period Mar 2026, posting penyusutan pertama ada, satu periode Soft Closed)

### TC-FA-PREF-519: Request langsung mengubah Fiscal Year Start yang terkunci ditolak server

16. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
17. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah Fiscal Year Start menjadi April
18. Verifikasi server menolak permintaan
19. Baca ulang nilai Preferences tersimpan
20. Verifikasi Fiscal Year Start tetap January
21. Hitung ulang jumlah baris log di tiga surface
22. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal

### TC-FA-PREF-520: Request langsung mengubah First Accounting Period yang terkunci ditolak server

23. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
24. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah First Accounting Period menjadi Jan 2026
25. Verifikasi server menolak permintaan
26. Baca ulang nilai Preferences tersimpan
27. Verifikasi First Accounting Period tetap Mar 2026
28. Hitung ulang jumlah baris log di tiga surface
29. Verifikasi jumlah baris Changelog, System Log, dan Activity Log sama dengan jumlah awal

### TC-FA-PREF-521: Request langsung mengubah field lain saat Fiscal Year Start dan First Accounting Period terkunci tidak mengubah nilai terkunci

30. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, hanya mengubah In-service Date Source menjadi Manual by Accounting dengan Fiscal Year Start January dan First Accounting Period Mar 2026 tetap
31. Verifikasi permintaan berhasil
32. Baca ulang nilai Preferences tersimpan
33. Verifikasi In-service Date Source tersimpan Manual by Accounting
34. Verifikasi Fiscal Year Start tetap January
35. Verifikasi First Accounting Period tetap Mar 2026

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API; kunci dibentuk lewat fixture BE (bagian 3 P-2). Asersi "ditolak" ada pada langkah Verifikasi respons; pesan penolakan tidak tertulis di TC sehingga tidak diasersi.
- Langkah penghubung (S-03): langkah 4 dan 11 (membuka kembali halaman agar nilai tersimpan dibaca dari server, aksi TC), langkah 15 (seed ulang penguncian karena seri fixture berganti dari PB-7a ke PC-2).
- TC-521 menyimpan In-service Date Source "Manual by Accounting"; Post Condition ("hanya In-service Date Source yang berubah") diasersi pada langkah 33 sampai 35. Pemulihan nilai awal oleh hook `after` (R-08).
- Temuan untuk QA:
  - TC-FA-PREF-249, 250, 519, 520, dan 521 hanya menyebut "server menolak permintaan" tanpa kode respons atau pesan; spec tidak menetapkan angka status.
  - TC-FA-PREF-521 tidak mensyaratkan pencatatan jumlah baris log pada Expected; spec tidak menambah asersi log untuk TC itu.
  - TC-FA-PREF-249 dan 250 membaca ulang lewat tab Preferences (UI), sedangkan TC-519 sampai 521 lewat "baca ulang"; spec memakai pembacaan API untuk 519 sampai 521.
