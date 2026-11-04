---
id: TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type
title: "Filter Panel: Screening dan Isi Opsi Event Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-196
  - TC-FA-NOTIF-197
  - TC-FA-NOTIF-198
  - TC-FA-NOTIF-199
  - TC-FA-NOTIF-200
  - TC-FA-NOTIF-393
coverage:
  web: automated
---

# Filter Panel: Screening dan Isi Opsi Event Type

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi, 11 event_type DISTINCT; `audit_task_started` dan `borrow_resolved` tanpa notifikasi Unread) milik akun aktor. TC-393 memakai N-41 (event_type `assignment_declined`, dibuat 11/06/26; Pre-setup #18) yang di-seed fixture BE penukar sebagai langkah penghubung. Seed dipulihkan fixture BE pemulih di hook `before` dan `after`. Nilai (label opsi, judul item) dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-196: Screening Filter Panel Notification Center

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Klik icon Filter
3. Verifikasi icon Filter menjadi gelap saat panel terbuka
4. Verifikasi field `Event Type` (dropdown multi-select searchable) tampil dengan placeholder `All event types`
5. Verifikasi field `Date` (date picker tunggal) tampil dengan placeholder `Select date`
6. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) tampil

### TC-FA-NOTIF-197: Isi opsi dropdown Event Type berasal dari event_type pada notifikasi user dengan label Title Case

7. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
8. Klik icon Filter lalu buka dropdown `Event Type`
9. Verifikasi dropdown memuat 11 opsi: `Access Total Control Removed`, `Assignment Waiting Approval`, `Audit Resolved`, `Audit Task Started`, `Borrow Confirmation Required`, `Borrow Resolved`, `Borrow Waiting Approval`, `Damaged Repaired`, `Disposal Reported`, `Missing Found`, `Transfer Waiting Approval`
10. Verifikasi label opsi berupa Title Case Bahasa Inggris (`borrow_waiting_approval` tampil `Borrow Waiting Approval`)

### TC-FA-NOTIF-198: Opsi Event Type pada Tab Unread hanya memuat event_type yang punya notifikasi Unread

11. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
12. Klik Tab `Unread`
13. Klik icon Filter lalu buka dropdown `Event Type`
14. Verifikasi opsi `Damaged Repaired` dan `Borrow Waiting Approval` tampil (event_type yang punya notifikasi Unread)
15. Verifikasi opsi `Audit Task Started` tidak tampil (event_type hanya Read)

### TC-FA-NOTIF-199: Opsi Event Type tidak dipersempit oleh Search

16. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
17. Ketik Search `repaired`, tekan Enter
18. Verifikasi item `Asset has been repaired` tampil pada list
19. Klik icon Filter lalu buka dropdown `Event Type`
20. Verifikasi opsi `Borrow Waiting Approval` dan `Missing Found` tetap tampil (event_type selain `damaged_repaired`)

### TC-FA-NOTIF-200: Search internal dropdown Event Type mempersempit opsi

21. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
22. Klik icon Filter lalu buka dropdown `Event Type`
23. Ketik `borrow` pada kotak cari dropdown
24. Verifikasi opsi `Borrow Confirmation Required`, `Borrow Resolved`, dan `Borrow Waiting Approval` tampil
25. Verifikasi opsi `Damaged Repaired` tidak tampil
26. Ganti isi kotak cari dropdown dengan `zzzz`
27. Verifikasi teks `No results found` tampil pada dropdown

### TC-FA-NOTIF-393: Opsi Event Type tidak dipersempit oleh Filter Date yang aktif

28. Pulihkan seed notifikasi lewat fixture BE pemulih, tambahkan N-41 lewat fixture BE penukar, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
29. Klik icon Filter, pilih tanggal 18/06/26 pada field `Date`, lalu klik `[Apply]`
30. Scroll sampai akhir list hingga seluruh item termuat
31. Verifikasi list memuat sedikitnya satu item
32. Verifikasi list hanya memuat notifikasi yang dibuat pada 18/06/26 dan N-41 tidak tampil
33. Buka dropdown `Event Type`
34. Verifikasi opsi `Assignment Declined` tampil walau event_type `assignment_declined` hanya punya notifikasi N-41 yang dibuat 11/06/26
35. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 11, 16, 21, 35 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 28 (pemulihan seed, penambahan N-41, dan muat ulang), 30 (memuat seluruh item agar asersi universal mencakup semua item).
- Asersi tambahan di luar Expected TC (S-03): langkah 18 (item pembanding yang membuktikan Search aktif), langkah 14 (anchor positif sebelum asersi absence langkah 15, 8b butir 2), langkah 24 (anchor positif sebelum langkah 25), langkah 31 (item pembanding sebelum asersi universal langkah 32).
- Spec ini 35 langkah.
- Temuan untuk QA:
  - TC-198 menyebut "opsi hanya event_type yang punya notifikasi Unread" tanpa daftar opsi lengkap; spec mengasersi dua opsi yang pasti ada (`Damaged Repaired`, `Borrow Waiting Approval`) dan satu yang pasti tidak ada (`Audit Task Started`).
  - TC-199 menyebut "event_type selain `damaged_repaired`" tanpa menyebut opsi; spec memakai `Borrow Waiting Approval` dan `Missing Found`.
  - TC-200 langkah 3 menulis "hanya opsi yang memuat `borrow`"; spec memakai ketiga opsi `Borrow ...` dari daftar 11 opsi TC-197 dan satu opsi pembeda (`Damaged Repaired`).
  - TC-393 butir b menyebut "event_type DISTINCT seluruh notifikasi pada Tab aktif" tanpa jumlah opsi sesudah N-41 ditambahkan; spec hanya mengasersi opsi `Assignment Declined`.
