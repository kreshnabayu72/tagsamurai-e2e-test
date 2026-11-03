---
id: TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download
title: "Resilience: Gagal Baca List, Detail, Log, dan Download"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-8
  - TC-AC-CS-50
  - TC-AC-CS-593
  - TC-AC-CS-402
  - TC-AC-CS-387
  - TC-AC-CS-430
coverage:
  web: automated
---

# Resilience: Gagal Baca List, Detail, Log, dan Download

## Prerequisites

- Mode: FE+BE. Spec memaksa sebagian respons lewat `Spectra.intercept()` di atas backend nyata (bagian 6); `Mode: mock` tidak dipakai karena modul ini tidak punya `openapi.yaml` maupun LLD sebagai sumber daftar endpoint (R-15, S-13).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data Pre-setup baca-saja (spec tidak menulis data): baris `SUBS-20260101-00001` (#61: Client PT Sejahtera, FAMS, Professional, Active, 01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama); dataset #82 (120 baris term tab Current dan 60 baris tab History); Changelog seed #84 (24 entri contoh).
- Kebutuhan intercept (parsial, disediakan tim FE; endpoint hanya yang dinamai TC dan path-nya tidak tertulis di TC, PRD, atau LLD): respons endpoint data List 500; endpoint Detail 500; endpoint Subscription Log lambat lalu 500; endpoint data Changelog 500; endpoint Download List 500; endpoint Download Changelog 500. Intercept dilepas segera setelah dipakai (S-09).
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan yang terunduh (hanya untuk memastikan ada atau tidaknya berkas, bukan isi sel).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-8: State error saat pengambilan List gagal dan pemulihan lewat Try Again

1. Paksa respons endpoint data List gagal dengan 500 lewat `Spectra.intercept()`
2. Klik menu `Allocation > Client Subscription`
3. Verifikasi area tabel menampilkan "Unable to load this data." dengan tombol `[Try Again]`
4. Verifikasi area tabel bukan empty state
5. Lepas intercept respons List
6. Klik `[Try Again]`
7. Verifikasi data List dimuat dan baris tampil

### TC-AC-CS-50: State error Detail dan pemulihan lewat Try Again

8. Paksa respons endpoint Detail gagal dengan 500 lewat `Spectra.intercept()`
9. Ketik Search `SUBS-20260101-00001`, tekan Enter
10. Klik baris `SUBS-20260101-00001`
11. Verifikasi Detail menampilkan "Unable to load this data." dengan tombol `[Try Again]`
12. Lepas intercept respons Detail
13. Klik `[Try Again]`
14. Verifikasi tiga SectionCard tampil
15. Klik menu `Client Subscription` di sidebar

### TC-AC-CS-593: State loading dan error Subscription Log serta pemulihan lewat Try Again

16. Perlambat respons endpoint Subscription Log lewat `Spectra.intercept()`
17. Ketik Search `SUBS-20260101-00001`, tekan Enter
18. Klik ikon `⋯` pada baris `SUBS-20260101-00001`, klik `Subscription Log`
19. Verifikasi modal Subscription Log menampilkan state Loading
20. Klik `[✕]`
21. Ganti intercept: paksa respons endpoint Subscription Log gagal dengan 500
22. Klik ikon `⋯` pada baris `SUBS-20260101-00001`, klik `Subscription Log`
23. Verifikasi modal menampilkan "Unable to load this data." dengan tombol `[Try Again]`
24. Verifikasi modal tidak tertutup
25. Lepas intercept respons Subscription Log
26. Klik `[Try Again]`
27. Verifikasi daftar log tampil tanpa menutup modal
28. Klik `[✕]`

### TC-AC-CS-402: Error load Modal Changelog

29. Paksa respons data Changelog gagal 500 lewat `Spectra.intercept()`
30. Klik ikon Changelog di toolbar
31. Verifikasi ErrorState menampilkan "Unable to load this data." dengan tombol `[Try Again]`
32. Lepas intercept respons Changelog
33. Klik `[Try Again]`
34. Verifikasi entri Changelog tampil
35. Klik `[✕]` pada modal Changelog

### TC-AC-CS-387: Download gagal menampilkan toast error tanpa ekstensi

36. Paksa respons Download List gagal 500 lewat `Spectra.intercept()`
37. Klik Download dan pilih `Download as CSV`
38. Verifikasi toast error "Error, failed to download Client-Subscription-Current." tanpa ekstensi berkas
39. Verifikasi tidak ada berkas terunduh
40. Lepas intercept respons Download List

### TC-AC-CS-430: Download Changelog gagal menampilkan toast error

41. Klik ikon Changelog di toolbar
42. Paksa respons Download Changelog gagal 500 lewat `Spectra.intercept()`
43. Klik Download dan pilih `Download as XLSX`
44. Verifikasi toast error "Error, failed to download Changelog-Client-Subscription." tanpa ekstensi
45. Lepas intercept respons Download Changelog
46. Klik `[✕]` pada modal Changelog

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 15 (kembali ke List), langkah 9 dan 17 (Search untuk menemukan baris target, R-16), langkah 20, 28, 35, 46 (menutup modal), langkah 21 (mengganti intercept dari lambat ke 500), dan langkah 5, 12, 25, 32, 40, 45 (melepas intercept segera setelah dipakai, S-09).
- Spec ini melewati ~35 langkah (46). Alasan: semua blok satu kelas harness (fault injection pada pembacaan data atau unduhan) dengan pola yang sama dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tidak ada langkah prefix identik yang dapat dihapus.
- Langkah 19 (state Loading) diasersi sebelum langkah yang mengubah state itu (bagian 8b butir 5). Perlambatan respons untuk mengamati Loading bukan kelas b; kegagalan 500 yang dipaksa pada langkah 21 sampai 23 adalah kelas b.
- Temuan untuk QA:
  - TC-AC-CS-8, 50, 402, 593 menyebut kode S-01, S-04, S-05, S-08 untuk pola state (ErrorState); spec mengasersi teks dan tombol yang disebut TC saja.
  - TC-AC-CS-8 langkah 2 menyebut menu `Allocation > Client Subscription` sebagai satu klik; spec mengikuti teksnya.
  - TC-AC-CS-593 Expected b menyebut "modal tidak tertutup" tanpa batas waktu pengamatan; spec mengasersinya sesudah error tampil.
  - TC-AC-CS-387 Expected b ("tidak ada berkas terunduh") mengandalkan kemampuan membaca unduhan; spec memakai toast error pada langkah 38 sebagai anchor positif (bagian 8b butir 11).
