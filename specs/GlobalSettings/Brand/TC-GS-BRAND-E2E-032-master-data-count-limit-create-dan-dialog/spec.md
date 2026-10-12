---
id: TC-GS-BRAND-E2E-032-master-data-count-limit-create-dan-dialog
title: "Master Data Count Limit: Create di Batas, Dialog Limit Reached, dan Tabel Tersaring"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-233
  - TC-GS-BRAND-232
  - TC-GS-BRAND-293
coverage:
  web: automated
---

# Master Data Count Limit: Create di Batas, Dialog Limit Reached, dan Tabel Tersaring

## Prerequisites

- Mode: FE+BE. Spec membuat satu brand (`Lim 1000 {runId}-032`) sampai jumlah brand mencapai 1.000.
- Akun: Total Control Client Limit, `Wulan Sari`, `totalControl_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_LIMIT_TC_PASSWORD` dan `GS_TC_PASSWORD` (pemulihan sesi di hook `after`). Password tidak ditulis di spec atau fixture.
- Fixture yang perlu disiapkan tim FE (belum ada): Client Limit dengan Master Data Count Limit 1.000 dan Selection Limit 100, berisi tepat 999 brand `Lim 001` sampai `Lim 999` (D-26) yang dibuat lewat Import Type Brand. Hook `before` memastikan jumlah brand 999 dan Master Data Count Limit 1.000.
- State global bersama: spec 031, 032, dan 033 memakai tenant Client Limit yang sama dengan jumlah brand sebagai syarat. Ketiganya dijalankan serial (tidak paralel satu sama lain); spec ini mensyaratkan 999 brand saat mulai dan menaikkannya menjadi 1.000 di tengah spec.
- Cleanup: hook `after` menghapus `Lim 1000 {runId}-032` dan `Lim 1001 {runId}-032` (bila ada) lewat API sehingga jumlah brand kembali 999, tanpa berasumsi langkah spec berhasil penuh.
- Kemampuan teknis: pemantauan request jaringan (status respons Submit `409 Conflict`; daftar request yang terkirim saat klik [+ Brand]; isi respons List yang memuat jumlah seluruh Brand entitas dan ceiling limit).
- TC-GS-BRAND-233: Master Data Count Limit 1.000, 999 brand (D-26); data uji `Lim 1000 {runId}-032` dan `Lim 1001 {runId}-032`.
- TC-GS-BRAND-232: jumlah brand 1.000 (dipenuhi oleh `Lim 1000 {runId}-032` dari TC-GS-BRAND-233 di spec yang sama; dependensi TC-GS-BRAND-233).
- TC-GS-BRAND-293: jumlah brand 1.000 (dependensi TC-GS-BRAND-233); data uji Search `Lim 001`.

## Test Steps

### TC-GS-BRAND-233: Create ke-N tepat di batas berhasil lalu ke-N+1 ditolak dengan Stay on form

1. Klik [+ Brand]
2. Centang checkbox `Stay on this form after submitting`
3. Isi Brand Name `Lim 1000 {runId}-032`
4. Klik [Submit]
5. Verifikasi toast sukses: "Success, brand has been created."
6. Verifikasi form tetap terbuka
7. Isi Brand Name `Lim 1001 {runId}-032`
8. Klik [Submit]
9. Verifikasi respons Submit `409 Conflict`
10. Verifikasi Dialog `Limit Reached` (warning) tampil dengan teks `You've reached the platform limit of 1000 brands. Contact support if you need a higher limit.` dan tombol `[OK]` saja
11. Klik [OK]
12. Verifikasi form Create tetap terbuka
13. Verifikasi Brand Name `Lim 1001 {runId}-032` dipertahankan di form
14. Klik `✕` di header form
15. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
16. Klik [Leave]
17. Klik icon Search
18. Ketik `Lim 1001 {runId}-032` di input Search
19. Tekan Enter
20. Verifikasi `Lim 1001 {runId}-032` tidak dibuat: empty state `No results found`
21. Klik `(←)` untuk menutup Search

### TC-GS-BRAND-232: Klik [+ Brand] saat Master Data Count Limit tercapai

22. Verifikasi tombol `[+ Brand]` tampil dan enabled
23. Mulai pemantauan request jaringan
24. Klik [+ Brand]
25. Verifikasi Dialog `Limit Reached` (warning) tampil dengan teks `You've reached the platform limit of 1000 brands. Contact support if you need a higher limit.` (`1000` angka polos tanpa pemisah ribuan) dan tombol `[OK]` saja, tanpa CTA upgrade
26. Verifikasi request jaringan sejak klik [+ Brand] hanya request List, tanpa request pre-check limit terpisah
27. Verifikasi Dialog tampil dari jumlah seluruh Brand entitas dan ceiling pada respons List
28. Klik [OK]
29. Verifikasi dialog tertutup tanpa membuka form Create

### TC-GS-BRAND-293: Klik [+ Brand] saat limit tercapai dan tabel sedang tersaring

30. Klik icon Search
31. Ketik `Lim 001` di input Search
32. Tekan Enter
33. Verifikasi tabel hanya memuat hasil Search (kurang dari 1.000 baris)
34. Klik [+ Brand]
35. Verifikasi Dialog `Limit Reached` tampil dengan `1000` sebagai limit dan tombol `[OK]` saja
36. Verifikasi form Create tidak terbuka
37. Verifikasi Dialog ditentukan dari jumlah seluruh Brand entitas pada respons List, bukan dari jumlah hasil tersaring
38. Klik [OK]
39. Klik `(←)` untuk menutup Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber (233, 232, 293) dipertahankan karena TC-GS-BRAND-232 dan TC-GS-BRAND-293 bergantung pada jumlah brand 1.000 yang tercapai di TC-GS-BRAND-233.
- Langkah penghubung (aksi tanpa `Verifikasi`): 14 sampai 16 (menutup form dirty secara deterministik lewat `✕`, dialog `Unsaved Changes`, dan [Leave]), 17 sampai 19 dan 21 (Search `Lim 1001` untuk memeriksa brand tidak dibuat, lalu menutup Search), 23 (memulai pemantauan jaringan), 38 (menutup Dialog `Limit Reached` pada TC-GS-BRAND-293 yang di TC sumber tidak ditutup), dan 39 (menutup Search). Langkah 15 mengasersi dialog `Unsaved Changes` sebagai bagian penutupan form dirty (S-08), bukan Expected Result TC.
- Langkah 17 sampai 21 (verifikasi `Lim 1001` tidak dibuat) diturunkan dari Expected Result d TC-GS-BRAND-233.
- Langkah 9: Expected Result TC menyebut respons Submit `409 Conflict`; dicek lewat pemantauan jaringan.
- Brand yang dibuat spec memakai suffix `{runId}-032` (nomor spec) karena spec lain (TC-GS-BRAND-234 pada spec `TC-GS-BRAND-E2E-033-master-data-count-limit-race-slot-terakhir`) memakai nama dasar yang sama.
- Kelas harness: volume data (999 brand, prinsip 13e).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
