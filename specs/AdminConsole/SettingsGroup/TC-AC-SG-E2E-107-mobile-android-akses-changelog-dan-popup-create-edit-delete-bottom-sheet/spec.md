---
id: TC-AC-SG-E2E-107-mobile-android-akses-changelog-dan-popup-create-edit-delete-bottom-sheet
title: "Mobile Android: Akses Changelog dari Header dan Popup Create, Edit, serta Delete sebagai Bottom Sheet"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-55
  - TC-AC-SG-56
coverage:
  web: unsupported
  mobile: automated
---

# Mobile Android: Akses Changelog dari Header dan Popup Create, Edit, serta Delete sebagai Bottom Sheet

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android TAG Samurai (PRD §4.6). Spec hanya membuka dan menutup popup; tidak ada group yang dibuat, diubah, atau dihapus.
- Perangkat atau emulator Android dengan aplikasi terpasang (Pre-setup #37), serta kemampuan tap, ketik, dan mengetuk elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Pre-setup #37 menyebut "akun Total Control Principal uji" tanpa email; spec memakai akun Pre-setup #1 (lihat Temuan untuk QA). Login di aplikasi Android dilakukan di hook `before` spec ini.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini. Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` untuk akun aktor disetel `seen` oleh hook suite (kemampuan disediakan tim FE/BE; lihat `suite.md`).
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group; Card List memuat `Region A`); `Region A` memiliki 4 entitas yang menempel (Pre-setup #19) sehingga Delete hanya menampilkan dialog blok D-03 yang ditutup dengan `[OK]`; tidak ada group yang terhapus dan Last Updated tidak berubah (S-06). Riwayat Changelog Group entitas Principal sudah ada di environment (tidak di-seed spec ini).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-107`, maupun cleanup.

## Test Steps

### TC-AC-SG-55: Akses Changelog di mobile lewat ikon di header halaman

1. Buka menu `Settings > Group` di aplikasi mobile
2. Ketuk ikon Changelog pada header halaman
3. Verifikasi Changelog terbuka lewat ikon di header halaman
4. Verifikasi isi Card List Changelog sama dengan web: Date, Action, Group Name, Field, Old Value, New Value, Modified By
5. Periksa Filter pada Changelog
6. Verifikasi filter Field tidak tersedia
7. Tutup Changelog
8. Ketuk ikon `⋯` pada toolbar mobile
9. Verifikasi bottom sheet toolbar `⋯` memuat Column Visibility
10. Verifikasi Changelog tidak ada di bottom sheet toolbar
11. Tutup bottom sheet `⋯`

### TC-AC-SG-56: Popup Create, Edit, dan Delete pada mobile berupa bottom sheet dengan field dan dialog yang sama

12. Ketuk ikon tree pada toolbar mobile
13. Ketuk `[+] Group` di bottom sheet tree
14. Verifikasi popup Create tampil sebagai bottom sheet
15. Verifikasi field Group Name dengan placeholder "Enter group name"
16. Verifikasi tombol footer `[Submit]` dan `[Clear Field]`
17. Tutup bottom sheet Create lewat `✕`
18. Ketuk ikon pencarian `[🔍]`, ketik "Region A", lalu submit
19. Ketuk `⋯` pada card `Region A` lalu "Edit"
20. Verifikasi popup Edit tampil sebagai bottom sheet
21. Verifikasi field Group Name pada popup Edit
22. Verifikasi tombol footer `[Save]` dan `[Clear Field]`
23. Tutup bottom sheet Edit lewat `✕`
24. Ketuk `⋯` pada card `Region A` lalu "Delete"
25. Verifikasi dialog blok D-03 tampil dengan Title "Cannot Delete Group"
26. Verifikasi dialog memuat bullet `Region A`
27. Verifikasi body dialog "This group or its subgroups still have members. Remove all members before deleting."
28. Verifikasi dialog hanya memiliki satu tombol `[OK]`
29. Ketuk `[OK]` pada dialog
30. Ketuk `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03, S-09, R-16): langkah 5 mengamati tanpa asersi sendiri; langkah 7, 11, 17, 23, dan 29 menutup popup atau dialog; langkah 18 (Search untuk menemukan card `Region A`) dan langkah 30 (menutup input Search dan mereset tabel tanpa sisa saringan Search). Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web.
- Urutan TC-AC-SG-55 mengikuti state (bagian 8b butir 5): akses Changelog dari header diasersi lebih dulu, lalu bottom sheet toolbar diperiksa tidak memuat Changelog dengan Column Visibility sebagai anchor positif (langkah 9).
- Form Create dan Edit ditutup tanpa perubahan field (bukan form dirty), sehingga tidak ada dialog `Unsaved Changes` (S-08).
- Label tombol footer mengikuti `prd-conventions.md` §24.1 (`[Submit]` dan `[Clear Field]` untuk Create, `[Save]` dan `[Clear Field]` untuk Edit); TC hanya menulis "tombol footer yang sama dengan web".
- Temuan untuk QA:
  - TC-AC-SG-56 Expected a menyebut placeholder "Enter group name" untuk Create dan Edit; field Edit terisi nama `Region A` sehingga placeholder tidak teramati dan hanya diasersi pada Create (langkah 15). Delete `Region A` memunculkan dialog blok D-03 karena entitas menempel (Pre-setup #19); spec mengasersi Title, bullet, body, dan satu tombol `[OK]` sesuai Expected b.
  - TC-AC-SG-55 tidak menyebut data Changelog yang harus ada; spec mengandalkan riwayat Changelog Group entitas Principal yang sudah ada di environment.
  - Pre-setup #37 tidak menyebut email akun Total Control Principal untuk mobile, dan TC-AC-SG-53 sampai 56 tidak menyebut nomor Pre-setup di precondition; spec memakai akun Pre-setup #1.
  - TC-AC-SG-55 dan 56 bertanda `Manual Only`; spec tetap ditulis dengan perangkat Android yang dibutuhkan dicatat di Prerequisites.
