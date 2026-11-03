---
id: TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace
title: "List: Baris Aktif, Kedaluwarsa, dan Grace"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-11
  - TC-AC-CS-12
  - TC-AC-CS-13
  - TC-AC-CS-15
  - TC-AC-CS-16
coverage:
  web: automated
---

# List: Baris Aktif, Kedaluwarsa, dan Grace

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #69 `SUBS-20250815-00001` (Warung Kopi Senja, Active), #50 `SUBS-20250819-00002` (Bengkel Maju Jaya, Expired, Grace End 17/09/26), #51 `SUBS-20250801-00001` (CV Mitra Sejati, Custom Plan `Mitra Premium`, Grace), #60 `SUBS-20260810-00001` (PT Sejahtera, Trial Active), #54 `SUBS-20260201-00001` (Klinik Medika Jaya, Trial Expired). Tanggal acuan data `19/08/26`.
- Konfigurasi kolom Setup Column yang disimpan spec (kolom Grace End) dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### TC-AC-CS-11: Baris term paid Active di tab Current: badge success dan row action penuh

1. Ketik Search `SUBS-20250815-00001`, tekan Enter
2. Klik ikon `⋯` pada baris itu
3. Verifikasi kolom Status menampilkan badge "Active" severity success
4. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Renew, Cancel Subscription
5. Verifikasi Edit, Cancel Request, Resubmit, dan Convert tidak ada di menu

### TC-AC-CS-13: Baris Custom Plan berstatus Grace di tab Current

6. Ganti isi kotak search dengan `SUBS-20250801-00001`, tekan Enter
7. Klik ikon `⋯` pada baris itu
8. Verifikasi kolom Plan menampilkan nama Custom Plan `Mitra Premium` apa adanya dengan badge "Custom"
9. Verifikasi kolom Status menampilkan badge "Grace" severity warning
10. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Renew

### TC-AC-CS-15: Baris Trial Active di tab Current: row action Convert

11. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
12. Klik ikon `⋯` pada baris itu
13. Verifikasi kolom Plan menampilkan "Enterprise" dengan badge "Trial"
14. Verifikasi kolom Status menampilkan badge "Active" severity success
15. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Convert
16. Verifikasi Renew, Cancel Subscription, Edit, dan Cancel Request tidak ada di menu

### TC-AC-CS-16: Baris Trial Expired di tab Current: row action Convert

17. Ganti isi kotak search dengan `SUBS-20260201-00001`, tekan Enter
18. Klik ikon `⋯` pada baris itu
19. Verifikasi kolom Plan menampilkan "SIEM" dengan badge "Trial"
20. Verifikasi kolom Status menampilkan badge "Expired" severity danger
21. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Convert

### TC-AC-CS-12: Baris term paid Expired di tab Current: Grace End hanya setelah kolom Curated ditampilkan

22. Ganti isi kotak search dengan `SUBS-20250819-00002`, tekan Enter
23. Klik ikon `⋯` pada baris itu
24. Verifikasi kolom Status menampilkan badge "Expired" severity danger
25. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Renew
26. Klik header kolom `⋯`, centang kolom `Grace End`, lalu klik `[Save]`
27. Verifikasi baris `SUBS-20250819-00002` menampilkan Grace End `17/09/26`
28. Klik `(←)` pada kotak Search
29. Verifikasi sedikitnya satu baris tampil di tab `Current`
30. Verifikasi baris berstatus Expired atau Grace menampilkan tanggal Grace End
31. Verifikasi baris berstatus selain Expired dan Grace menampilkan "—" pada kolom Grace End

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16) dan langkah `Klik (←)` pada kotak Search sebelum asersi baris lain pada TC-AC-CS-12. TC-AC-CS-12 ditempatkan terakhir karena menyimpan konfigurasi kolom (S-10).
- Menu row action dibuka lewat ikon `⋯` baris; menu tertutup saat langkah Search berikutnya dimulai.
- Temuan untuk QA:
  - TC-AC-CS-12 langkah 3 menulis "centang kolom Grace End → kolom Grace End tampil" tanpa menyebut `[Save]`; modal/overlay Setup Column mengikuti PRD dengan footer `[Reset to Default]` dan `[Save]` (bagian 7 konvensi), sehingga spec menambah klik `[Save]` sebagai langkah penghubung. `suite.md` tidak mendaftarkan spec ini sebagai penyimpan konfigurasi kolom (hanya spec Setup Column List dan Changelog); pemulihan di hook `after` ditulis di Prerequisites spec ini.
  - TC-AC-CS-11 sampai TC-AC-CS-16 mengasersi baris yang tidak punya successor dan Client tanpa trial (Precondition); TC tidak menyebut cara memastikannya selain data Pre-setup.
