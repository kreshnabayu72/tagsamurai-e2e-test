---
id: TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama
title: "Guided Tooltip: Isi dan Kunjungan Pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-60
  - TC-AC-CS-61
  - TC-AC-CS-62
  - TC-AC-CS-63
coverage:
  web: automated
---

# Guided Tooltip: Isi dan Kunjungan Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): membaca, menghapus, dan menyetel flag `guided_tooltip_seen_ac-license-allocation-subscription` per akun. Spec ini mengatur flag sendiri sesudah hook suite; hook `after` suite memulihkan nilai awal flag.
- TC-AC-CS-61 bergantung pada keadaan TC-AC-CS-60, TC-AC-CS-62 pada TC-AC-CS-61, dan TC-AC-CS-63 pada TC-AC-CS-62 (kolom Dependensi); spec menjalankannya berurutan dan mengatur flag di awal tiap TC yang mensyaratkan flag belum ada.

## Test Steps

### TC-AC-CS-60: Isi lima langkah walkthrough Guided Tooltip

1. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun aktor (flag belum ada)
2. Klik menu `Allocation > Client Subscription` dari sidebar
3. Verifikasi Step 1 target Tabs: Title "Current and History", Description "Current shows subscriptions that are running or waiting for a decision. History keeps finished ones. Renewing or changing a plan always adds a new row instead of editing the old one."
4. Verifikasi indikator Step 1 berbentuk "Step 1 of 5"
5. Klik `[Next]`
6. Verifikasi Step 2 target Toolbar: Title "Controls for the Whole List", Description "The toolbar holds the controls that work on the whole list instead of a single row. Starting a new subscription also begins here when your role allows it."
7. Verifikasi indikator Step 2 berbentuk "Step 2 of 5"
8. Klik `[Next]`
9. Verifikasi Step 3 target header kolom Actions `⋯`: Title "Actions Follow the Term's Status", Description "Row actions depend on each term's status. Open a row's `⋯` menu to see what is available."
10. Verifikasi indikator Step 3 berbentuk "Step 3 of 5"
11. Klik `[Next]`
12. Verifikasi Step 4 target kolom Status: Title "Status Tells the Lifecycle Stage", Description "Status shows where each term is in its lifecycle."
13. Verifikasi indikator Step 4 berbentuk "Step 4 of 5"
14. Klik `[Next]`
15. Verifikasi Step 5 target ikon Changelog: Title "Full History, One Click Away", Description "Every change to subscriptions is logged here, including renewals applied automatically by the scheduled job."
16. Verifikasi indikator Step 5 berbentuk "Step 5 of 5"
17. Klik `[Done]`

### TC-AC-CS-61: Walkthrough muncul otomatis hanya pada kunjungan pertama

18. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun aktor (flag belum ada)
19. Klik menu `Allocation > Client Subscription` dari sidebar
20. Verifikasi walkthrough muncul otomatis dari Step 1 pada kunjungan pertama
21. Klik `[Skip]`
22. Verifikasi flag `guided_tooltip_seen_ac-license-allocation-subscription` bernilai true
23. Buka menu lain di sidebar, lalu buka lagi menu `Allocation > Client Subscription`
24. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-AC-CS-62: Tombol [?] memutar ulang walkthrough dari Step 1 tanpa mereset flag

25. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
26. Verifikasi tooltip tombol "Show guide"
27. Klik `[?]`
28. Verifikasi walkthrough mulai dari Step 1
29. Klik `[Next]` empat kali hingga Step 5 tampil
30. Klik `[Done]`
31. Muat ulang halaman
32. Verifikasi flag `guided_tooltip_seen_ac-license-allocation-subscription` tetap true
33. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-AC-CS-63: Navigasi Back, Next, dan Done pada walkthrough

34. Klik `[?]`
35. Verifikasi Step 1 tampil dan tidak menampilkan tombol `[Back]`
36. Klik `[Next]`
37. Verifikasi Step 2 tampil
38. Klik `[Back]`
39. Verifikasi Step 1 tampil kembali
40. Klik `[Next]` empat kali hingga Step 5 tampil
41. Verifikasi pada Step 5 tombol `[Next]` berubah menjadi `[Done]`
42. Klik `[Done]`
43. Verifikasi walkthrough tertutup
44. Verifikasi flag `guided_tooltip_seen_ac-license-allocation-subscription` bernilai true

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah menghapus flag, `[Done]` pada akhir TC-AC-CS-60 yang menutup walkthrough, dan langkah "Buka menu lain di sidebar" pada TC-AC-CS-61 (menu lain yang dipakai ditentukan penulis skrip; TC tidak menyebut nama menu).
- Rantai Dependensi TC-AC-CS-60, 61, 62, 63: tiap TC melanjutkan keadaan TC sebelumnya (walkthrough pertama, flag true, replay lewat `[?]`).
- Spec ini 44 langkah, di atas smell 35 langkah. Alasan: TC-AC-CS-60 sampai TC-AC-CS-63 berantai lewat kolom Dependensi dan keadaan flag; satu topik (Guided Tooltip) sehingga tidak dipecah tanpa mengulang setup flag.
- Temuan untuk QA:
  - TC-AC-CS-60 Expected f (indikator "Step [N] of 5") ditulis sebagai Verifikasi per langkah karena indikator berbeda tiap langkah.
  - TC-AC-CS-61 langkah 3 "Buka menu lain" tidak menyebut menu; spec menulisnya tanpa nama menu.
  - TC-AC-CS-61 dan TC-AC-CS-62 mengasersi nilai flag; TC tidak memberi cara membacanya selain sebutan flag. Kemampuan membaca flag ditulis disediakan tim FE/BE (S-11).
