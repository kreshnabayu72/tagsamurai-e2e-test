---
id: TC-FA-PREF-E2E-080-defense-in-depth-first-accounting-period-di-luar-rentang-v-09-v-10-lewat-request-langsung
title: "Defense-in-Depth: First Accounting Period di Luar Rentang, V-09 Versi Tax Depreciation Class, dan V-10 Transaksi Bertanggal Ditolak Lewat Request Langsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-236
  - TC-FA-PREF-237
  - TC-FA-PREF-522
  - TC-FA-PREF-523
  - TC-FA-PREF-524
  - TC-FA-PREF-525
coverage:
  web: automated
---

# Defense-in-Depth: First Accounting Period di Luar Rentang, V-09 Versi Tax Depreciation Class, dan V-10 Transaksi Bertanggal Ditolak Lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-236 dan 237 memakai PB-1 (First Accounting Period Mar 2026) dan PB-2; TC-524 dan 525 memakai PC-1 (First Accounting Period Mar 2026); TC-522 memakai PC-3 (Fiscal Year Start January, belum terkunci, Tax Depreciation Class memiliki versi kedua ber-Effective From); TC-523 memakai PC-4 (transaksi bertanggal paling awal 15 Mei 2026, First Accounting Period Mar 2026). PC-3 dan PC-4 dibentuk lewat seed BE, "disediakan tim FE" tanpa endpoint karangan (S-13).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP, baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10), baca daftar periode Accounting Period. Disediakan tim FE/BE.
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan; seed ulang hanya untuk berpindah seri fixture dan pemulihan akhir ke nilai awal di hook `after`.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-236: Permintaan langsung dengan First Accounting Period satu bulan setelah bulan berjalan ditolak

2. Kirim permintaan Save Preferences langsung (fixture BE) dengan First Accounting Period = Nov 2026; bulan berjalan Oktober 2026
3. Verifikasi server menolak permintaan dengan pesan "First accounting period must be between Jan 2000 and the current month"
4. Baca ulang Preferences dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
5. Verifikasi First Accounting Period tetap "Mar 2026"
6. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)

### TC-FA-PREF-237: Permintaan langsung dengan First Accounting Period satu bulan sebelum Jan 2000 ditolak

7. Kirim permintaan Save Preferences langsung (fixture BE) dengan First Accounting Period = Dec 1999; bulan berjalan Oktober 2026
8. Verifikasi server menolak permintaan dengan pesan "First accounting period must be between Jan 2000 and the current month"
9. Baca ulang Preferences dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
10. Verifikasi First Accounting Period tetap "Mar 2026"
11. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)
12. Seed ulang Preferences ke PC-1 lewat API dan catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-524: Request langsung First Accounting Period bulan di masa depan ditolak

13. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah First Accounting Period menjadi Nov 2026
14. Verifikasi server menolak permintaan dengan pesan "First accounting period must be between Jan 2000 and the current month"
15. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
16. Verifikasi nilai Preferences tersimpan tidak berubah (First Accounting Period tetap Mar 2026)
17. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-525: Request langsung First Accounting Period sebelum Januari 2000 ditolak

18. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah First Accounting Period menjadi Dec 1999
19. Verifikasi server menolak permintaan dengan pesan "First accounting period must be between Jan 2000 and the current month"
20. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
21. Verifikasi nilai Preferences tersimpan tidak berubah (First Accounting Period tetap Mar 2026)
22. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal
23. Seed ulang ke PC-3 lewat API (versi kedua Tax Depreciation Class ber-Effective From) dan catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-522: Request langsung mengubah Fiscal Year Start saat ada versi Tax Depreciation Class ber-Effective From ditolak

24. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah Fiscal Year Start menjadi April
25. Verifikasi server menolak permintaan dengan pesan "Fiscal year start cannot be changed because tax depreciation class versions already exist."
26. Baca ulang nilai Preferences tersimpan dan daftar periode di Accounting Period, lalu hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
27. Verifikasi Fiscal Year Start tetap January
28. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal
29. Verifikasi periode akuntansi tidak dibangun ulang
30. Seed ulang ke PC-4 lewat API (transaksi bertanggal paling awal 15 Mei 2026) dan catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-523: Request langsung mengubah First Accounting Period ke bulan setelah transaksi bertanggal ditolak

31. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengubah First Accounting Period menjadi Jun 2026
32. Verifikasi server menolak permintaan dengan pesan "First accounting period cannot be later than existing dated transactions."
33. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
34. Verifikasi First Accounting Period tetap Mar 2026
35. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API; kunci V-09 dan V-10 dibentuk lewat fixture BE (bagian 3 P-2). Request langsung tidak melewati browser; asersi penolakan ada pada langkah Verifikasi respons.
- Baseline log (langkah 1, 12, 23, 30) dicatat setelah tiap seed ulang dan dipakai sebagai pembanding hitung ulang TC sesudahnya, karena penolakan tidak mengubah jumlah baris log (S-12).
- Langkah penghubung (S-03): langkah 12, 23, 30 (seed ulang saat seri fixture berganti dari PB-1 ke PC-1, PC-3, PC-4).
- Post Condition semua TC ("tidak ada perubahan Preferences dan tidak ada entri log baru") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log. Frasa Expected butir b TC-524 dan 525 mengulang ketiga surface log; diasersi pada langkah jumlah baris.
- Temuan untuk QA:
  - TC-FA-PREF-236 dan 237 membaca ulang lewat tab Preferences pada konteks "Baca ulang Preferences", sedangkan Precondition tidak mencatat jumlah baris log padahal Post Condition meminta "tidak ada entri log baru"; spec menambah pencatatan baseline (S-12).
  - TC-FA-PREF-236, 237, 524, dan 525 menguji batas dan pesan yang sama pada seri PB dan PC; perbedaan hanya seri fixture.
  - TC-FA-PREF-522 dan 523 tidak menyebut kode respons HTTP; spec hanya mengasersi pesan penolakan.
