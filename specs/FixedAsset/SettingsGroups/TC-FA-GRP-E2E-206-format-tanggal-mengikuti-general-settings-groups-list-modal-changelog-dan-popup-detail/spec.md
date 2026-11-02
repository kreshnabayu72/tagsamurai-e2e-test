---
id: TC-FA-GRP-E2E-206-format-tanggal-mengikuti-general-settings-groups-list-modal-changelog-dan-popup-detail
title: "Format Tanggal Mengikuti General Settings: Groups List, Modal Changelog, Popup Detail Group (Tab Assets dan Tab Users)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-914
  - TC-FA-GRP-915
  - TC-FA-GRP-916
coverage:
  web: automated
---

# Format Tanggal Mengikuti General Settings: Groups List, Modal Changelog, Popup Detail Group (Tab Assets dan Tab Users)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- State global yang diubah spec: General Settings (Date Format, Time, Timezone). Awal: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta; perubahan: MM/DD/YYYY, 12-hour. Kemampuan mengubah General Settings (disediakan tim FE/BE lewat sesi API) dan pemulihannya ke nilai awal di hook `after`. Suite berjalan serial.
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; Tab Users memuat Temporary User dengan Temporary Until (kolom curated, ditampilkan lewat Column Visibility).

## Test Steps

### TC-914: Groups List (kolom Last Updated dan input filter)

1. Atur General Settings (Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta) lewat sesi API hingga tersimpan
2. Muat ulang halaman (F5)
3. Buka Filter Last Updated, pilih rentang
4. Verifikasi nilai tanggal-waktu kolom Last Updated dan teks input date picker mengikuti format DD/MM/YYYY, 24-hour, dan timezone Asia/Jakarta
5. Atur General Settings (Date Format MM/DD/YYYY, Time 12-hour) lewat sesi API hingga tersimpan
6. Muat ulang halaman (F5)
7. Buka Filter Last Updated, pilih rentang
8. Verifikasi nilai tanggal-waktu kolom Last Updated dan teks input date picker ikut berubah mengikuti MM/DD/YYYY dan 12-hour

### TC-915: Modal Changelog (kolom Date dan input filter)

9. Atur General Settings (Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta) lewat sesi API hingga tersimpan
10. Muat ulang halaman (F5)
11. Klik icon Changelog, buka filter Date
12. Verifikasi nilai tanggal-waktu kolom Date dan teks input date picker mengikuti format DD/MM/YYYY, 24-hour, dan timezone Asia/Jakarta
13. Tutup Modal Changelog
14. Atur General Settings (Date Format MM/DD/YYYY, Time 12-hour) lewat sesi API hingga tersimpan
15. Muat ulang halaman (F5)
16. Klik icon Changelog, buka filter Date
17. Verifikasi nilai tanggal-waktu kolom Date dan teks input date picker ikut berubah mengikuti MM/DD/YYYY dan 12-hour
18. Tutup Modal Changelog

### TC-916: Popup Detail Group (Tab Assets Last Updated dan Tab Users Temporary Until)

19. Atur General Settings (Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta) lewat sesi API hingga tersimpan
20. Muat ulang halaman (F5)
21. Buka Detail Warehouse A, klik Tab Assets
22. Verifikasi nilai Last Updated pada Tab Assets mengikuti format DD/MM/YYYY, 24-hour, dan timezone Asia/Jakarta
23. Klik Tab Users, tampilkan kolom Temporary Until via Column Visibility
24. Verifikasi nilai Temporary Until pada Tab Users mengikuti format DD/MM/YYYY
25. Atur General Settings (Date Format MM/DD/YYYY, Time 12-hour) lewat sesi API hingga tersimpan
26. Muat ulang halaman (F5)
27. Buka Detail Warehouse A, klik Tab Assets
28. Verifikasi nilai Last Updated pada Tab Assets ikut berubah mengikuti MM/DD/YYYY dan 12-hour
29. Klik Tab Users, tampilkan kolom Temporary Until via Column Visibility
30. Verifikasi nilai Temporary Until pada Tab Users ikut berubah mengikuti MM/DD/YYYY

## Notes

- Langkah penghubung (S-03): mengatur General Settings lewat sesi API, memuat ulang halaman agar format baru berlaku, dan menutup Modal Changelog. Kolom Temporary Until yang ditampilkan dipulihkan lewat hook `after` (hapus preferensi kolom).
- Temuan untuk QA:
  - TC-914 sampai 916 menulis "Ubah General Settings ... ulangi" tanpa menyebut cara mengubahnya; spec memakai sesi API (kemampuan disediakan tim FE/BE). Expected "timezone aktif" tidak punya nilai terukur selain format; spec mengasersi format dan timezone Asia/Jakarta sebagaimana precondition TC.
