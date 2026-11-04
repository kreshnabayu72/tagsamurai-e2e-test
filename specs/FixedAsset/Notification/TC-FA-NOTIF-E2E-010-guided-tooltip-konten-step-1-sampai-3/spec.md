---
id: TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3
title: "Guided Tooltip fa-notification: Kunjungan Pertama, Konten Step 1 sampai 3, dan Back"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-45
  - TC-FA-NOTIF-46
  - TC-FA-NOTIF-47
  - TC-FA-NOTIF-49
  - TC-FA-NOTIF-53
coverage:
  web: automated
---

# Guided Tooltip fa-notification: Kunjungan Pertama, Konten Step 1 sampai 3, dan Back

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Notification Center, dan Guided Tooltip `fa-notification`.
- Akun aktor: Total Control Pre-setup #31 (`totalControlTour_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Pengecualian atas hook suite untuk flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-notification` sehingga hook `before` suite tidak menyetelnya true untuk akun #31. Fixture BE menghapus flag itu untuk akun #31 di hook `before` spec ini (keadaan Pre-setup #31: tanpa flag) dan hook `after` memulihkannya ke keadaan itu.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) tersedia untuk akun #31. Spec hanya membaca data; fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-45: Tour berjalan otomatis pada kunjungan pertama ke Notification Center

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center untuk pertama kali (flag seen belum ada)
2. Verifikasi overlay gelap dan tooltip box muncul otomatis dari Step 1
3. Verifikasi indikator `Step 1 of 3`

### TC-FA-NOTIF-46: Step 1 menyorot Bell icon

4. Verifikasi spotlight pada Bell icon
5. Verifikasi Title `Notifications`
6. Verifikasi Description `Get notified in real time about approvals, confirmations, and updates that need your attention.`
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil
8. Verifikasi tombol `[Back]` Hidden

### TC-FA-NOTIF-53: [Back] kembali ke step sebelumnya

9. Klik `[Next]`
10. Klik `[Back]`
11. Verifikasi Step 1 tampil dengan Title `Notifications`
12. Verifikasi tombol `[Back]` Hidden

### TC-FA-NOTIF-47: Step 2 menyorot area badge atau dot Bell icon

13. Klik `[Next]`
14. Verifikasi spotlight pada area Bell icon tempat badge atau dot berada
15. Verifikasi Title `Unread Count`
16. Verifikasi Description `A badge or dot on the bell shows when you have notifications you haven't read yet.`
17. Verifikasi indikator `Step 2 of 3`
18. Verifikasi tombol `[Back]` tampil

### TC-FA-NOTIF-49: Step 3 membuka Dropdown Panel otomatis dan menyorot [Show All]

19. Klik `[Next]`
20. Verifikasi Dropdown Panel terbuka otomatis
21. Verifikasi spotlight pada tautan `[Show All]`
22. Verifikasi Title `Notification Center`
23. Verifikasi Description `This dropdown only shows your 5 most recent notifications — see the full history in Notification Center.`
24. Verifikasi indikator `Step 3 of 3`
25. Verifikasi tombol `[Next]` berubah menjadi `[Done]`
26. Klik `[Done]`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelima TC berbagi satu tur yang berjalan terus dari kunjungan pertama; langkah "Buka Notification Center untuk pertama kali" TC-46, 47, 49, dan 53 dipenuhi oleh tur yang sedang berjalan dari langkah 1 (state sama: Step 1 tampil). Urutan blok: TC-45, 46, 53, 47, 49 supaya `[Back]` (TC-53) diuji dari Step 2 ke Step 1 sebelum tur maju ke Step 3; urutan menyimpang dari urutan nomor TC. TC-47 Langkah 2 "Klik `[Next]`" dan TC-49 Langkah 2 "Klik `[Next]` dua kali" dipenuhi oleh langkah 13 dan 19 (kumulatif dari Step 1 ke Step 3, setelah `[Next]` dan `[Back]` pada langkah 9 dan 10 yang kembali ke Step 1).
- Langkah penghubung (S-03): langkah 26 (`[Done]` menutup tur dan Dropdown Panel; hasilnya tidak diasersi karena diuji spec lain di suite ini, dan flag yang tersimpan dipulihkan hook `after`).
- Langkah 8 dan 12 (`[Back]` Hidden) memakai tombol `[Next]` yang tampil (langkah 7) dan Title Step 1 (langkah 11) sebagai anchor positif pada surface yang sama.
- Guided Tooltip dipisah menjadi tiga spec (010 konten Step 1 sampai 3 dan Back, 011 menutup tur dan flag seen, 012 keyboard, replay, dan varian tanpa notifikasi) walau berbagi akun #31 dan seed N-01 sampai N-07, karena blok yang menyimpan flag menghapus flag di awal blok dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-45 sampai TC-53 menulis "Buka Notification Center untuk pertama kali" tanpa menyebut jalur membuka (Bell icon lalu `[Show All]`, atau navigasi lain); spec memakai Bell icon lalu `[Show All]`.
  - TC-45 menulis flag "belum ada" sedangkan Pre-setup #31 menyebut "tanpa flag"; spec menyamakan keduanya sebagai keadaan tanpa flag.
