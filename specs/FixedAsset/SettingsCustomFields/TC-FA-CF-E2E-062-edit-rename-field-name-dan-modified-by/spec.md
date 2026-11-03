---
id: TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by
title: "Edit: Rename Field Name, Trim Spasi, dan Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-206
  - TC-FA-CF-212
  - TC-FA-CF-219
  - TC-FA-CF-297
coverage:
  web: automated
---

# Edit: Rename Field Name, Trim Spasi, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Storage Capacity` (Numeric 0 Decimal Places, Scope {Generator, Pump}) dan `Asset Serial Tag` (Text, Required Yes). Nilai rename Dinamis bersuffix `{runId}-062`: `Capacity Trim {runId}-062` dan `Storage Capacity Renamed {runId}-062`. Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Storage Capacity`, `Asset Serial Tag`) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Waktu: jam server dan jam browser sinkron; Last Updated dibandingkan dengan waktu yang dicatat sesudah `[Save]` dengan toleransi satu menit (S-12). Format Date mengikuti General Settings Company Nilai (`dd/MM/yy`, 24 jam).
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-219: Save tanpa perubahan nilai adalah no-op dengan toast netral dan modal tertutup

2. Catat Modified By dan Last Updated baris `Storage Capacity`
3. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
4. Klik `[Save]` tanpa mengubah apa pun
5. Verifikasi modal tertutup
6. Verifikasi toast netral `No changes to save.` tampil
7. Verifikasi toast `Success, custom field has been updated.` tidak tampil
8. Verifikasi Modified By dan Last Updated baris `Storage Capacity` sama dengan nilai yang dicatat pada langkah 2

### TC-FA-CF-297: Edit yang mengubah nilai memperbarui Modified By ke aktor dan Last Updated ke waktu Save

9. Klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`
10. Ubah toggle Required ke No
11. Klik `[Save]`
12. Catat waktu sesudah `[Save]`
13. Verifikasi Modified By baris `Asset Serial Tag` menampilkan `Sarah J`
14. Verifikasi Last Updated baris `Asset Serial Tag` menampilkan waktu `[Save]` (toleransi satu menit) dengan format General Settings

### TC-FA-CF-212: Spasi di ujung Field Name Edit dipangkas saat disimpan

15. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
16. Ubah Field Name menjadi `  Capacity Trim {runId}-062  ` (spasi di kedua ujung)
17. Klik `[Save]`
18. Klik row action `⋯` > `Edit` pada baris `Capacity Trim {runId}-062`
19. Verifikasi Field Name tersimpan sebagai `Capacity Trim {runId}-062` tanpa spasi di ujung
20. Ganti isi Field Name dengan `Storage Capacity`
21. Klik `[Save]`

### TC-FA-CF-206: Rename Field Name tersimpan dan baris serta Last Updated dan Modified By diperbarui

22. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
23. Ubah Field Name menjadi `Storage Capacity Renamed {runId}-062`
24. Klik `[Save]`
25. Catat waktu sesudah `[Save]`
26. Verifikasi toast sukses `Success, custom field has been updated.` tampil
27. Verifikasi modal tertutup
28. Verifikasi baris menampilkan Field Name `Storage Capacity Renamed {runId}-062`
29. Verifikasi Modified By baris `Storage Capacity Renamed {runId}-062` menampilkan `Sarah J`
30. Verifikasi Last Updated baris `Storage Capacity Renamed {runId}-062` menampilkan waktu `[Save]` (toleransi satu menit)

## Notes

- Urutan TC di spec: 219, 297, 212, 206. Kasus no-op (219) berjalan lebih dulu pada `Storage Capacity` yang belum berubah; TC-FA-CF-297 memakai `Asset Serial Tag`; TC-FA-CF-212 dan 206 sama-sama mengubah nama `Storage Capacity`, sehingga nama dikembalikan ke `Storage Capacity` di antara keduanya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 2 (mencatat nilai Modified By dan Last Updated untuk pembanding Expected c TC-FA-CF-219), langkah 12 dan 25 (mencatat waktu Save untuk asersi Last Updated), langkah 20 dan 21 (mengembalikan nama `Storage Capacity` supaya TC-FA-CF-206 berjalan pada baris bernama baseline). Langkah 16 sampai 19 mengganti nama dengan `{runId}-062` agar nama hasil rename unik per run; Expected TC tetap pada hasil pemangkasan spasi.
- Last Updated pada langkah 14 dan 30 memakai satu cara waktu: dicatat sesudah aksi dan dibandingkan dengan toleransi satu menit.
- Temuan untuk QA:
  - Nilai Modified By dan Last Updated asli baris `Storage Capacity` tidak disebut pada Expected c TC-FA-CF-219 selain "tidak berubah"; spec membandingkan dengan nilai yang dicatat sebelum aksi.
  - TC-FA-CF-212 tidak menyebut toast untuk Save; spec tidak mengasersinya.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
