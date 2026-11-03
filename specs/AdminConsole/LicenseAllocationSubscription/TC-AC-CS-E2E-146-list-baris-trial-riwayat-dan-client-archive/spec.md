---
id: TC-AC-CS-E2E-146-list-baris-trial-riwayat-dan-client-archive
title: "List: Baris Trial Riwayat dan Client Archive di Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-22
  - TC-AC-CS-19
coverage:
  web: automated
---

# List: Baris Trial Riwayat dan Client Archive di Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`, capability Create saja, Partner CV Karya Mandiri; Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: Client `PT Abadi Jaya` (binaan langsung CV Karya Mandiri; #36) dengan term Archive `SUBS-20260101-00002` (#58) dan `SUBS-20240101-00001` (#94), Purge (#78), Deleted (#79), dan Canceled `SUBS-20241201-00001` (#93); baris tab History: `SUBS-20260501-00001` (#62 Trial Converted), Trial Rejected `Klinik Gigi Ceria` (#80), Trial Canceled `Optik Cahaya` (#81, requester original `Rina Pratama` #12).

## Test Steps

### TC-AC-CS-22: Client dan Product yang semua termnya Archive hanya muncul di History dan kembali tersedia di dropdown + Subscription

1. Ketik Search `PT Abadi Jaya`, tekan Enter
2. Verifikasi EmptyState "No results found" tampil dan tab `Current` tidak memuat baris PT Abadi Jaya
3. Klik `(←)` pada kotak Search
4. Klik tab `History`
5. Ketik Search `PT Abadi Jaya`, tekan Enter
6. Verifikasi tab `History` memuat baris Archive, Purge, Deleted, dan Canceled PT Abadi Jaya
7. Klik tab `Current`
8. Klik `[+ Subscription]`
9. Buka dropdown Client
10. Verifikasi dropdown Client memuat `PT Abadi Jaya`
11. Pilih Client `PT Abadi Jaya` lalu buka dropdown Product
12. Verifikasi dropdown Product memuat FAMS dan SAMS
13. Klik `✕` pada modal `Add Subscription`
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-AC-CS-19: Baris Trial Converted, Rejected, dan Canceled di tab History

16. Klik tab `History`
17. Ketik Search `SUBS-20260501-00001`, tekan Enter
18. Klik ikon `⋯` pada baris Trial Converted
19. Verifikasi badge Status Converted severity primary
20. Verifikasi kolom Plan menampilkan badge "Trial"
21. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
22. Ganti isi kotak search dengan `Klinik Gigi Ceria`, tekan Enter
23. Klik ikon `⋯` pada baris Trial Rejected (kolom Plan berbadge "Trial")
24. Verifikasi badge Status Rejected severity danger
25. Verifikasi kolom Plan menampilkan badge "Trial"
26. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
27. Logout lalu login sbg Role: Create-Only (Partner) `Rina Pratama`
28. Buka menu `Allocation > Client Subscription`
29. Klik tab `History`
30. Ketik Search `Optik Cahaya`, tekan Enter
31. Klik ikon `⋯` pada baris Trial Canceled (kolom Plan berbadge "Trial")
32. Verifikasi badge Status Canceled severity danger
33. Verifikasi kolom Plan menampilkan badge "Trial"
34. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Resubmit

## Notes

- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik tab, dan klik `(←)` pada kotak Search sebelum pindah ke tab `History` (mengosongkan kotak supaya Search berikutnya tidak bergantung pada status kotak sesudah pindah tab, bagian 8b butir 9). TC-AC-CS-22 ditempatkan lebih dulu karena memakai akun Total Control Principal tanpa pindah akun; TC-AC-CS-19 pindah akun sekali. Ganti akun punya langkah eksplisit (S-07).
- Form `Add Subscription` pada TC-AC-CS-22 ditutup deterministik: `✕`, Verifikasi dialog `Unsaved Changes`, `[Leave]` (S-08).
- Temuan untuk QA:
  - TC-AC-CS-19 tidak menyebut Subscription ID baris Trial Rejected dan Trial Canceled (hanya Client dan nomor Pre-setup #80 dan #81); spec mencarinya lewat Search nama Client dan mengenali baris Trial dari badge pada kolom Plan.
  - TC-AC-CS-19 Expected d ("Ketiga baris menampilkan badge Trial pada kolom Plan") tersebar per baris di spec karena ketiga baris tidak tampil bersamaan setelah Search per baris.
  - TC-AC-CS-22 tidak menyebut apakah form `Add Subscription` dirty setelah memilih Client; spec menutupnya dengan alur `Unsaved Changes` karena Client dipilih lebih dulu.
