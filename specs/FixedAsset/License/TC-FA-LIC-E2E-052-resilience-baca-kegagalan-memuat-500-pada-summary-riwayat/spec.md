---
id: TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat
title: "Resilience Baca: Kegagalan Memuat 500 pada Summary, Riwayat, Allocation Quota, Concurrent User, dan Banner"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-22
  - TC-FA-LIC-32
  - TC-FA-LIC-60
  - TC-FA-LIC-69
  - TC-FA-LIC-462
  - TC-FA-LIC-463
coverage:
  web: automated
---

# Resilience Baca: Kegagalan Memuat 500 pada Summary, Riwayat, Allocation Quota, Concurrent User, dan Banner

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #1 dan #12 (client Paid, PT Sejahtera); Pre-setup #14 untuk tab Concurrent User; Pre-setup #15 untuk blok banner (term live Active PT Sejahtera, Plan Owner `PT Maju Bersama`, End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1, Grace End 30/01/27; tanggal "hari ini" fixture 01/12/26 diatur fixture BE penyetel pada langkah yang disebut).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata memaksa respons 500 pada GET data ledger, GET riwayat subscription, GET data node Allocation Quota, GET sesi, dan GET daftar subscription; intercept dilepas segera setelah asersi tiap blok (S-09). Asersi memuat state backend (data tampil setelah `[Try Again]`), sehingga `Mode: FE+BE`, bukan `mock`.
- Kemampuan teknis: Jam browser/klien dimajukan lebih dari 60 detik untuk blok TC-FA-LIC-463 (pilihan spec; tidak menunggu waktu nyata); jam dipulihkan di hook `after`. Sesi UI tetap valid selama jam digeser (dinyatakan di `suite.md`).
- Spec tidak mengubah data Pre-setup; fixture BE penyetel tanggal banner dipulihkan di hook `after` (efek: tanggal "hari ini" fixture).

## Test Steps

### TC-FA-LIC-22: Kegagalan memuat License Summary

1. Pasang intercept jaringan: GET data ledger digagalkan 500
2. Muat ulang halaman License
3. Verifikasi area tabel menampilkan `Unable to load this data.` bersama tombol `[Try Again]` inline
4. Verifikasi tidak ada empty state
5. Verifikasi tidak ada toast
6. Lepas intercept jaringan
7. Klik `[Try Again]`
8. Verifikasi tabel License Summary menampilkan data

### TC-FA-LIC-32: Kegagalan memuat Subscription History

9. Pasang intercept jaringan: GET riwayat subscription digagalkan 500
10. Klik sub-tab `Subscription History`
11. Verifikasi area tabel riwayat menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
12. Verifikasi License Summary tetap tampil
13. Verifikasi tidak ada toast
14. Lepas intercept jaringan

### TC-FA-LIC-60: Kegagalan memuat data node Allocation Quota

15. Pasang intercept jaringan: GET data node digagalkan 500
16. Klik tab `Allocation Quota`
17. Verifikasi area section menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
18. Verifikasi bukan empty state
19. Verifikasi tidak ada toast
20. Lepas intercept jaringan

### TC-FA-LIC-69: Empty state Tab Concurrent User dan kegagalan memuat

21. Klik tab `Concurrent User`
22. Ketik Search `zzzz`, tekan Enter
23. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
24. Klik `(←)` pada kotak Search
25. Pasang intercept jaringan: GET sesi digagalkan 500
26. Muat ulang halaman License, lalu klik tab `Concurrent User`
27. Verifikasi `Unable to load this data.` dengan tombol `[Try Again]`
28. Lepas intercept jaringan

### TC-FA-LIC-462: Banner tidak dirender saat baca subscription gagal pada muat pertama

29. Jalankan fixture BE penyetel: tanggal "hari ini" 01/12/26 pada term live Pre-setup #15 hingga tersimpan
30. Pasang intercept jaringan: GET daftar subscription digagalkan 500
31. Muat ulang halaman License
32. Klik tiap tab pada Tabs Bar secara berurutan
33. Verifikasi halaman dan semua tab tetap berfungsi
34. Verifikasi banner tidak dirender
35. Verifikasi tidak ada toast
36. Lepas intercept jaringan

### TC-FA-LIC-463: Muat ulang otomatis banner gagal saat banner sudah tampil

37. Muat ulang halaman License
38. Verifikasi banner Notice tampil
39. Pasang intercept jaringan: request banner berikutnya digagalkan 500
40. Majukan jam klien lebih dari 60 detik
41. Klik tab `Allocation Quota`
42. Verifikasi banner Notice tetap tampil
43. Verifikasi tidak ada toast
44. Lepas intercept jaringan
45. Jalankan fixture BE penyetel: tanggal "hari ini" 24/12/26 hingga tersimpan
46. Majukan jam klien lebih dari 60 detik
47. Klik tab `All License`
48. Verifikasi banner diperbarui sesuai hasil terbaru

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): `Muat ulang halaman License` memuat ulang data di bawah intercept; `Klik tiap tab` membuktikan tab tetap berfungsi; fixture BE penyetel tanggal dan `Majukan jam klien` menyiapkan blok banner.
- Urutan TC: kegagalan baca tabel (TC-FA-LIC-22, TC-FA-LIC-32, TC-FA-LIC-60, TC-FA-LIC-69), lalu banner (TC-FA-LIC-462 dan TC-FA-LIC-463) dengan fixture tanggal (S-10).
- Temuan untuk QA:
  - TC-FA-LIC-463: klausa b (`diperbarui bila hasil berubah`) bersyarat; spec mengubah tanggal "hari ini" fixture ke 24/12/26 (7 hari sebelum End Date) agar hasil banner berubah, nilai itu bukan dari TC. Teks banner stage berikutnya tidak diasersi karena TC tidak menyebutnya.
  - TC-FA-LIC-463: `pindah Tab License setelah lebih dari 60 detik` dipenuhi dengan memajukan jam klien (R-10); TC tidak menyebut jam mana yang dibaca penghitung 60 detik.
  - TC-FA-LIC-462: `semua tab tetap berfungsi` diasersi dengan membuka tiap tab pada Tabs Bar; TC tidak merinci kriteria berfungsi.
- Alasan di atas sekitar 35 langkah (48 langkah): semua blok satu kelas harness (resilience baca, intercept 500) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya memasang dan melepas intercept.
