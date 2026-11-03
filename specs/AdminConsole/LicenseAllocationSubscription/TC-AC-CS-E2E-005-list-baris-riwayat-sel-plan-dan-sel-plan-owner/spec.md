---
id: TC-AC-CS-E2E-005-list-baris-riwayat-sel-plan-dan-sel-plan-owner
title: "List: Baris Riwayat, Sel Plan, dan Sel Plan Owner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-25
  - TC-AC-CS-26
  - TC-AC-CS-17
coverage:
  web: automated
---

# List: Baris Riwayat, Sel Plan, dan Sel Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #61 `SUBS-20260101-00001` (PT Sejahtera, Professional, Active), #51 `SUBS-20250801-00001` (Custom Plan `Mitra Premium`), #60 `SUBS-20260810-00001` (Trial Enterprise), #50 `SUBS-20250819-00002` (Plan Owner CV Karya Mandiri), #53 `SUBS-20260303-00001` (Plan Owner PT ABC); baris tab History: #62 `SUBS-20250101-00001` (Renewed), #52 `SUBS-20260812-00001` (Rejected), #58 `SUBS-20260101-00002` (Archive), #78 (Purge, PT Abadi Jaya FAMS Growth), #79 (Deleted, PT Abadi Jaya SAMS Starter).

## Test Steps

### TC-AC-CS-25: Sel Plan: nama biasa, Custom Plan berbadge Custom, dan Trial berbadge Trial

1. Ketik Search `SUBS-20260101-00001`, tekan Enter
2. Verifikasi kolom Plan baris Paid `Professional` menampilkan nama plan saja tanpa badge
3. Ganti isi kotak search dengan `SUBS-20250801-00001`, tekan Enter
4. Verifikasi kolom Plan Custom Plan menampilkan nama verbatim `Mitra Premium` dengan badge "Custom"
5. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
6. Verifikasi kolom Plan baris Trial menampilkan "Enterprise" dengan badge "Trial" severity primary di samping nama

### TC-AC-CS-26: Sel Plan Owner berformat [Nama] (Type)

7. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
8. Verifikasi kolom Plan Owner `PT Maju Bersama (Distributor)`
9. Ganti isi kotak search dengan `SUBS-20250819-00002`, tekan Enter
10. Verifikasi kolom Plan Owner `CV Karya Mandiri (Partner)`
11. Ganti isi kotak search dengan `SUBS-20260303-00001`, tekan Enter
12. Verifikasi kolom Plan Owner `PT ABC (Principal)`
13. Verifikasi teks Plan Owner berupa plain text, bukan badge atau link
14. Klik `(←)` pada kotak Search

### TC-AC-CS-17: Baris History berstatus data mati hanya punya row action Detail dan Subscription Log

15. Klik tab `History`
16. Ketik Search `SUBS-20250101-00001`, tekan Enter
17. Klik ikon `⋯` pada baris itu
18. Verifikasi badge Status Renewed severity primary
19. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
20. Verifikasi Start Date `01/01/25` dan End Date `31/12/25`
21. Ganti isi kotak search dengan `SUBS-20260812-00001`, tekan Enter
22. Klik ikon `⋯` pada baris itu
23. Verifikasi badge Status Rejected severity danger
24. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
25. Verifikasi Start Date dan End Date menampilkan "—"
26. Ganti isi kotak search dengan `PT Abadi Jaya`, tekan Enter
27. Klik ikon `⋯` pada baris berstatus Archive (`SUBS-20260101-00002`)
28. Verifikasi badge Status Archive severity dark
29. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
30. Klik ikon `⋯` pada baris berstatus Purge
31. Verifikasi badge Status Purge severity dark
32. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
33. Klik ikon `⋯` pada baris berstatus Deleted
34. Verifikasi badge Status Deleted severity dark
35. Verifikasi menu row action berisi tepat dua item: Detail, Subscription Log
36. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16) dan `Klik (←)` pada kotak Search di akhir TC-AC-CS-26 dan akhir spec. Urutan TC: 25, 26 (tab `Current`), lalu 17 (tab `History`) supaya pindah tab hanya sekali (S-10).
- Baris Purge dan Deleted PT Abadi Jaya ditemukan lewat satu Search `PT Abadi Jaya` karena TC tidak memberi Subscription ID keduanya.
- Spec ini 36 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (isi sel dan row action baris pada List) pada data Pre-setup baca-saja yang sama, dan berdiri sendiri; TC-AC-CS-17 mengasersi lima baris dengan status berbeda sehingga langkah Search dan menu tidak bisa dilebur.
- Temuan untuk QA:
  - TC-AC-CS-17 langkah 1 menyebut baris Purge dan Deleted tanpa Subscription ID (hanya Client, Product, Plan, tanggal, dan nomor Pre-setup #78 dan #79); spec mencarinya lewat Search `PT Abadi Jaya` dan mengenali baris dari Status.
  - TC-AC-CS-17 menulis "Menu row action tiap baris berisi tepat dua item" satu butir untuk lima baris; spec memisahkannya per baris sebagai Verifikasi menu (S-01) dan tidak menambah asersi baru.
