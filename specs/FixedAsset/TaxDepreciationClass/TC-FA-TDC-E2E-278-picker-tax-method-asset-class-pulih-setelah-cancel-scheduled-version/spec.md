---
id: TC-FA-TDC-E2E-278-picker-tax-method-asset-class-pulih-setelah-cancel-scheduled-version
title: "Picker Tax Method Asset Class: Metode yang Semula Disabled Dapat Dipilih Lagi Setelah Cancel Scheduled Version"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-967
sourceRules: ["S-13e", "F-FATDC-03.k10", "E-FATDC-95", "D-10"]
smoke: []
dependsOn: []
trace:
  "S-13e": [5, 21, 22, 23]
  "F-FATDC-03.k10": [10, 12, 13, 14]
  "E-FATDC-95": [10, 12, 13, 14]
  "D-10": [10, 11]
coverage:
  web: automated
---

# Picker Tax Method Asset Class: Metode yang Semula Disabled Dapat Dipilih Lagi Setelah Cancel Scheduled Version

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class, versi Current dan Scheduled, dan Asset Class pemakai lewat API; pemulihan data lewat API; mengarahkan kursor pada opsi dropdown untuk tooltip (langkah 22); tombol `Esc` (langkah 6 dan 24).
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat):

| Kunci fixture (usulan) | Class Code | Keterangan |
|---|---|---|
| `khsV20` | `KHS-V20` | Non-building, Useful Life 8; versi Current Straight Line dan Declining Balance; versi Scheduled Jan 2027 Straight Line saja; Used By 1: Asset Class `AC-SCH6 – Mesin Kompresor` memakai Straight Line (kunci `assetClassMesinKompresor`, disediakan tim FE/BE) |

- Tabel memuat tujuh class seed bawaan dan satu class milik spec (8 baris dalam satu halaman) sehingga baris target dibuka tanpa Search (8b.13, R-23).
- State global yang diubah: jam server dan jam browser (hook `before`, dipulihkan di `after`) dan versi Scheduled Jan 2027 `KHS-V20` (dibatalkan langkah 11, dipulihkan lewat seeding ulang di hook `after`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-967: Cancel Scheduled Version membuat metode yang semula Disabled dapat dipilih lagi pada picker Tax Method Asset Class

1. Klik tab Asset Class
2. Ketik Search `AC-SCH6`, tekan Enter
3. Buka Drawer Edit Asset Class AC-SCH6
4. Klik dropdown Tax Method
5. Verifikasi opsi `Declining Balance` Disabled
6. Tekan `Esc` untuk menutup dropdown Tax Method
7. Klik `[×]` pada header Drawer Edit Asset Class
8. Klik tab Tax Depreciation Class
9. Klik link Class Code `KHS-V20` pada tabel
10. Klik `[Cancel scheduled version]` pada Alert
11. Klik `[Cancel version]` pada dialog D-10
12. Klik tautan View versions
13. Verifikasi versi `Jan 2027` berstatus `Cancelled`
14. Tutup modal Versions
15. Klik `[×]` pada header Drawer
16. Klik tab Asset Class
17. Ganti isi kotak search dengan `AC-SCH6`, tekan Enter
18. Buka Drawer Edit Asset Class AC-SCH6
19. Klik dropdown Tax Method
20. Verifikasi opsi `Straight Line` dapat dipilih
21. Verifikasi opsi `Declining Balance` dapat dipilih
22. Arahkan kursor ke opsi `Declining Balance`
23. Verifikasi opsi `Declining Balance` tidak Disabled
24. Verifikasi tidak ada tooltip pada opsi `Declining Balance`
25. Tekan `Esc` untuk menutup dropdown Tax Method
26. Klik `[×]` pada header Drawer Edit Asset Class

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 8 (membaca keadaan awal picker lalu kembali ke tab Tax Depreciation Class), langkah 14 dan 15 (menutup modal Versions dan Drawer), langkah 16 (berpindah tab), langkah 2 dan 17 (Search `AC-SCH6` untuk menemukan baris target; R-16; langkah 17 menulis "ganti isi kotak search" karena Search dipertahankan lintas pindah tab, 8b.9), langkah 6, 7, 25, 26 (menutup dropdown dan Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Asersi tambahan di luar Expected TC (S-03): langkah 1 sampai 5 membuktikan precondition e TC (opsi `Declining Balance` Disabled sebelum Cancel) sebagai anchor positif supaya asersi "tidak Disabled" langkah 23 tidak lulus semu (8b.2); langkah 10 dan 11 adalah langkah TC 2; langkah 12 sampai 14 mengamati Expected a lewat Modal Versions (TC tidak menyebut tempat mengamati; Drawer tetap terbuka setelah Cancel Version).
- Pemilik perilaku picker (Disabled, tooltip `Not allowed from [MMM YYYY].`) adalah modul Asset Class (FAAC-LOGIC-02f); spec ini menguji pengaruh Cancel Scheduled Version pada picker tersebut seperti TC-967.
- Langkah 20 sampai 24 memecah Expected b TC-967 per klausa (S-01); langkah 24 (absence tooltip) didahului hover langkah 22 dan opsi tampil dapat dipilih (langkah 20, 21) sebagai anchor positif (8b.2).
- TC-966 (picker Disabled setelah versi Scheduled terbentuk) ada di spec 277.
- Temuan untuk QA:
  - TC-967 tidak menyebut cara membuka Drawer Edit Asset Class dan menutup dropdown; spec menulis "Buka Drawer Edit" tanpa label tombol, perlu dilengkapi dari PRD Asset Class, dan memakai `Esc` serta `[×]` tanpa perubahan.
  - TC-967 langkah 2 menyebut "konfirmasi pada dialog D-10" tanpa label tombol; spec memakai `[Cancel version]` seperti spec lain.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
