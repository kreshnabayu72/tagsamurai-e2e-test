---
id: TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama
title: "Overlay Column Visibility Tabel Position: Screening, Uncheck, Drag Reorder, dan Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-177
  - TC-GS-POS-178
  - TC-GS-POS-179
  - TC-GS-POS-180
coverage:
  web: automated
---

# Overlay Column Visibility Tabel Position: Screening, Uncheck, Drag Reorder, dan Kolom Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position); spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record). Dipakai sebagai precondition TC-GS-POS-177 sampai 180 (tabel berisi data populasi), tidak diasersi.
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.populationSeed031`): 13 Position `HR Business Partner {runId}-031`, `IT Support Specialist {runId}-031`, `Temporary Staff {runId}-031`, `iOS Developer {runId}-031`, `Legal Counsel {runId}-031`, `Marketing Executive {runId}-031`, `Quality Assurance Analyst {runId}-031`, `Data Engineer {runId}-031`, `Office Administrator {runId}-031`, `Logistics Coordinator {runId}-031`, `Payroll Specialist {runId}-031`, `Security Officer {runId}-031`, `Training Coordinator {runId}-031`. Seeding ini dipakai sebagai precondition TC, tidak diasersi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-031` yang masih ada; pulihkan preferensi visibilitas dan urutan kolom tabel Position di browser ke default (Name lalu Last Updated, keduanya tampil).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: drag-and-drop item daftar kolom; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka); pembacaan urutan dan keberadaan kolom tabel, state disabled checkbox, dan tooltip.
- State global: preferensi kolom tabel Position tersimpan di browser per pengguna (Post Condition TC-GS-POS-178); spec memulihkannya lewat langkah penghubung di akhir tiap TC dan hook `after` sebagai cadangan. Tidak ada state lain yang diubah.

## Test Steps

### TC-GS-POS-177: Screening Overlay Column Visibility tabel utama

1. Klik ikon `⋯` pada header kolom Actions
2. Verifikasi User > Position > Overlay Column Visibility terbuka
3. Verifikasi Overlay Column Visibility tampil tanpa backdrop
4. Verifikasi daftar kolom memuat `Name` dengan checkbox ☑
5. Verifikasi daftar kolom memuat `Name` dengan drag handle
6. Verifikasi daftar kolom memuat `Last Updated` dengan checkbox ☑
7. Verifikasi daftar kolom memuat `Last Updated` dengan drag handle
8. Verifikasi item `Setup Column...` tampil di bagian bawah panel
9. Verifikasi kolom Checkbox dan Actions tidak tercantum di daftar kolom
10. Tutup Overlay Column Visibility

### TC-GS-POS-178: Uncheck kolom langsung diterapkan

11. Klik ikon `⋯` pada header kolom Actions
12. Uncheck `Last Updated`
13. Verifikasi kolom Last Updated langsung hilang dari tabel
14. Verifikasi Overlay Column Visibility tidak memiliki tombol `[Save]`
15. Tutup Overlay Column Visibility
16. Tekan F5
17. Verifikasi kolom Name tampil di tabel
18. Verifikasi kolom Last Updated tetap tersembunyi
19. Klik ikon `⋯` pada header kolom Actions
20. Centang `Last Updated`
21. Tutup Overlay Column Visibility

### TC-GS-POS-179: Drag reorder langsung diterapkan

22. Klik ikon `⋯` pada header kolom Actions
23. Drag `Last Updated` ke atas `Name`
24. Verifikasi urutan kolom tabel langsung `Last Updated | Name`
25. Tekan F5
26. Verifikasi urutan kolom tabel tetap `Last Updated | Name`
27. Klik ikon `⋯` pada header kolom Actions
28. Drag `Name` ke atas `Last Updated`
29. Tutup Overlay Column Visibility

### TC-GS-POS-180: Kolom terakhir yang tampil tidak bisa di-uncheck

30. Klik ikon `⋯` pada header kolom Actions
31. Uncheck `Last Updated`
32. Hover checkbox `Name`
33. Verifikasi checkbox `Name` disabled
34. Verifikasi checkbox `Name` tetap tampil di daftar kolom
35. Verifikasi Tooltip "At least one column must remain visible."
36. Centang `Last Updated`
37. Tutup Overlay Column Visibility

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 37 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas (Overlay Column Visibility tabel utama), satu akun, tanpa mengubah data Position; tiap TC memulihkan preferensi kolom sebelum TC berikutnya (langkah 19 sampai 20, 27 sampai 28, dan 36), sehingga kegagalan satu TC tidak mengubah state awal TC berikutnya.
- Urutan TC dalam spec mengikuti urutan TC sumber (177, 178, 179, 180). Layar awal Global Settings > User > Position dibuka di hook `beforeEach` dan dipakai bersama keempat TC.
- Langkah penghubung (aksi tanpa `Verifikasi`; membersihkan atau memulihkan state sebelum TC berikutnya mengandalkannya): langkah 10, 15, 21, 29, dan 37 (menutup overlay), langkah 19 sampai 20 (centang kembali Last Updated sesudah TC-GS-POS-178), langkah 27 sampai 28 (urutan kolom dikembalikan ke `Name | Last Updated` sesudah TC-GS-POS-179), dan langkah 36 (centang kembali Last Updated sesudah TC-GS-POS-180).
- Hover dan tooltip pada langkah 32 sampai 35 diasersi sebelum langkah yang mengubah state-nya (centang kembali Last Updated pada langkah 36).
- Langkah 17 (kolom Name tampil di tabel sesudah F5) adalah asersi tambahan di luar Expected TC-GS-POS-178 (S-03). Fungsinya anchor positif bagi absence langkah 18 (kolom Last Updated tetap tersembunyi): halaman sudah termuat sesudah muat ulang, sehingga kolom yang hilang bukan karena tabel belum dimuat (konvensi bagian 8b butir 2).
- Pembagian TC lintas spec: Popup Setup Column tabel utama (TC-GS-POS-181 sampai 191) ada di spec 032.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-178 ("preferensi tersimpan di browser untuk tabel Position") tidak punya langkah observasi di TC selain F5 pada langkah 16; persistensi lewat F5 diasersi pada langkah 18 (Expected b), dan penyimpanan di browser per pengguna tidak diasersi terpisah.
  - TC-GS-POS-177 sampai 180 tidak menyebut cara menutup Overlay Column Visibility ("Tutup overlay" pada TC-GS-POS-178); spec menulis "Tutup Overlay Column Visibility" tanpa cara tertentu, dan cara persisnya ditentukan di tahap script.
