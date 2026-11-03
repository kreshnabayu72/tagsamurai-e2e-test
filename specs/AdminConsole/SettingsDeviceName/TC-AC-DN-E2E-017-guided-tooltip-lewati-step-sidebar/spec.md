---
id: TC-AC-DN-E2E-017-guided-tooltip-lewati-step-sidebar
title: "Guided Tooltip: Step 2 Dilewati saat Sidebar Tertutup atau Tersembunyi pada 1279 px"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-653
  - TC-AC-DN-654
coverage:
  web: automated
---

# Guided Tooltip: Step 2 Dilewati saat Sidebar Tertutup atau Tersembunyi pada 1279 px

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Guided Fresh (Pre-setup #28) `Fixture.settings-device-name.guidedFresh` (email `guidedFresh_automated_{namaCompany}@qwertysystem.net`, nama tampil `Dewi Lestari`, Principal), password `Spectra.env.AC_DN_GUIDED_PASSWORD` (nama env berkode modul sesuai `suite.md`, didaftarkan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_DN_GUIDED_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name`; hook `before` suite menyetel flag `guided_tooltip_seen_ac-settings-device` ke `seen` untuk akun UI yang dipakai suite dan hook `after` suite memulihkannya. Spec ini memakai akun Pre-setup #28 dan mengatur flag sendiri sesudah hook (pengecualian bagian 4).
- Kemampuan teknis (disediakan tim FE/BE): menyetel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset sebelum tiap TC dan membaca nilainya; mengubah lebar viewport dan memulihkannya (minimal 1280 px pada awal tiap TC).
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16), baca-saja. Tidak ada data Dinamis. State global yang diubah: flag Guided Tooltip akun #28 (dipulihkan hook `after` suite).

## Test Steps

### TC-AC-DN-653: Walkthrough Guided Tooltip melewati Step 2 saat Category Sidebar tertutup dan tidak membuka Sidebar otomatis

1. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
2. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
3. Klik `[Skip]`
4. Klik Floating toggle `▶` di tepi kiri panel Sidebar
5. Klik tombol `[?]` di sebelah kanan Breadcrumb
6. Verifikasi Step 1 menampilkan indikator "Step 1 of 5" (indikator dihitung ulang dari step yang tampil karena Step 2 dilewati)
7. Klik `[Next]`
8. Verifikasi setelah `[Next]` pada Step 1 tampil langkah dengan Title "Search and Filter" (spotlight pada Search dan Filter di toolbar) dan indikator "Step 2 of 5"
9. Verifikasi langkah dengan Title "Category Tree" tidak tampil
10. Verifikasi Category Sidebar tetap tertutup selama walkthrough
11. Verifikasi Floating toggle tetap bertanda `◀` di tepi kanan layar (Sidebar tidak dibuka otomatis)
12. Klik `[Next]`
13. Verifikasi langkah "Changelog" tampil dengan indikator "Step 3 of 5"
14. Klik `[Next]`
15. Verifikasi langkah "Device List" tampil dengan indikator "Step 4 of 5"
16. Klik `[Next]`
17. Verifikasi langkah "Column Visibility" tampil dengan indikator "Step 5 of 5"
18. Verifikasi indikator dengan total 6 tidak tampil pada langkah mana pun
19. Verifikasi pada langkah "Step 5 of 5" tombol `[Next]` berubah menjadi `[Done]`
20. Klik `[Done]`
21. Verifikasi klik `[Done]` menutup walkthrough
22. Verifikasi walkthrough tidak memindahkan halaman dan tidak membuka dialog
23. Klik Floating toggle `◀` di tepi kanan layar

### TC-AC-DN-654: Walkthrough Guided Tooltip melewati Step 2 saat Category Sidebar tersembunyi pada viewport 1279 px

24. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
25. Atur lebar viewport 1279 px
26. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
27. Verifikasi Step 1 menampilkan indikator "Step 1 of 5" (indikator dihitung ulang dari step yang tampil karena Step 2 dilewati)
28. Klik `[Next]`
29. Verifikasi setelah `[Next]` pada Step 1 tampil langkah dengan Title "Search and Filter" dan indikator "Step 2 of 5"
30. Verifikasi langkah dengan Title "Category Tree" tidak tampil
31. Verifikasi Category Sidebar tetap tersembunyi
32. Verifikasi Floating toggle tetap bertanda `◀` di tepi kanan layar (Sidebar tidak dibuka otomatis)
33. Klik `[Next]`
34. Verifikasi langkah "Changelog" tampil dengan indikator "Step 3 of 5"
35. Klik `[Next]`
36. Verifikasi langkah "Device List" tampil dengan indikator "Step 4 of 5"
37. Klik `[Next]`
38. Verifikasi langkah "Column Visibility" tampil dengan indikator "Step 5 of 5"
39. Verifikasi indikator dengan total 6 tidak tampil pada langkah mana pun
40. Verifikasi pada langkah "Step 5 of 5" tombol `[Next]` berubah menjadi `[Done]`
41. Klik `[Done]`
42. Verifikasi klik `[Done]` menutup walkthrough
43. Verifikasi walkthrough tidak memindahkan halaman dan tidak membuka dialog
44. Pulihkan lebar viewport ke ukuran awal suite

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 1 dan 24 menyetel flag sebelum tiap TC (kemampuan disediakan tim FE/BE); langkah 23 membuka kembali Sidebar yang ditutup langkah 4 karena state collapsed tersimpan per user; langkah 44 memulihkan viewport.
- Langkah "Klik `[Next]` tiga kali" pada TC ditulis satu `Next` per langkah dengan `Verifikasi` tepat sesudahnya karena Expected butir d menyebut tiga langkah berurutan dan indikator masing-masing.
- Ukuran spec (44 langkah, di atas smell sekitar 35 langkah): alasan R3 (bagian 3 prinsip 13). Dua TC memakai satu topik (Step 2 walkthrough dilewati), satu akun, dan satu kelas harness; tiap TC memulai dari flag yang disetel ulang sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal. Langkah bertambah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
