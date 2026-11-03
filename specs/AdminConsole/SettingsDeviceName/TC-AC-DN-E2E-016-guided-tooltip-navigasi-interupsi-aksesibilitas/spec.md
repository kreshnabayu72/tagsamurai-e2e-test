---
id: TC-AC-DN-E2E-016-guided-tooltip-navigasi-interupsi-aksesibilitas
title: "Guided Tooltip: Siklus Navigasi, Interupsi, dan Aksesibilitas Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-647
  - TC-AC-DN-648
  - TC-AC-DN-649
coverage:
  web: automated
---

# Guided Tooltip: Siklus Navigasi, Interupsi, dan Aksesibilitas Keyboard

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

### TC-AC-DN-647: Siklus navigasi walkthrough: Back, Next, Done, dan Skip lewat tombol maupun klik overlay

1. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
2. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
3. Verifikasi Step 1 of 6: tombol `[Back]` Hidden
4. Verifikasi Step 1 of 6: tombol `[Skip]` dan `[Next]` tampil
5. Klik `[Next]`
6. Klik `[Back]`
7. Verifikasi `[Back]` pada Step 2 kembali ke Step 1 of 6
8. Klik `[Next]` lima kali
9. Verifikasi Step 6 of 6: tombol `[Next]` berubah menjadi `[Done]`
10. Klik `[Done]`
11. Verifikasi `[Done]` menutup walkthrough
12. Verifikasi flag `guided_tooltip_seen_ac-settings-device` bernilai true
13. Klik tombol `[?]`
14. Klik area overlay gelap
15. Verifikasi klik overlay gelap menutup walkthrough sama seperti `[Skip]`
16. Klik tombol `[?]`
17. Klik `[Skip]`
18. Verifikasi `[Skip]` menutup walkthrough

### TC-AC-DN-648: Walkthrough yang terputus oleh resize atau navigasi tidak menyetel flag dan muncul lagi pada kunjungan berikutnya

19. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
20. Atur lebar viewport 1440 px
21. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
22. Klik `[Next]` dua kali
23. Ubah lebar viewport dari 1440 px menjadi 1300 px (tetap ≥ 1280 px)
24. Verifikasi resize menutup walkthrough
25. Verifikasi resize tidak menyetel flag `guided_tooltip_seen_ac-settings-device`
26. Muat ulang halaman dengan F5
27. Verifikasi setelah F5 walkthrough muncul lagi dari Step 1 of 6
28. Klik `[Next]` sekali
29. Klik item sidebar navigasi menuju halaman lain
30. Verifikasi navigasi keluar di tengah walkthrough menutup walkthrough
31. Verifikasi navigasi keluar itu tidak menyetel flag `guided_tooltip_seen_ac-settings-device`
32. Kembali ke halaman `Settings > Device > Device Name`
33. Verifikasi pada kunjungan berikutnya walkthrough muncul lagi dari Step 1 of 6
34. Klik `[Skip]` dan pulihkan lebar viewport ke ukuran awal suite

### TC-AC-DN-649: Aksesibilitas walkthrough: fokus keyboard, Enter atau panah kanan, panah kiri, dan Esc

35. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
36. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
37. Verifikasi tooltip box menerima fokus keyboard saat aktif
38. Tekan `Enter`
39. Verifikasi `Enter` berfungsi sebagai `[Next]`: Step 2 of 6 tampil
40. Tekan panah kanan
41. Verifikasi panah kanan berfungsi sebagai `[Next]`: Step 3 of 6 tampil
42. Tekan panah kiri
43. Verifikasi panah kiri berfungsi sebagai `[Back]`: Step 2 of 6 tampil
44. Tekan `Esc`
45. Verifikasi `Esc` berfungsi sebagai `[Skip]`: walkthrough tertutup
46. Verifikasi flag `guided_tooltip_seen_ac-settings-device` bernilai true

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 19, dan 35 menyetel flag sebelum tiap TC (kemampuan disediakan tim FE/BE); langkah 34 menutup walkthrough dan memulihkan viewport.
- Urutan: pada TC-AC-DN-647, asersi `[Back]` tersembunyi di Step 1 ditulis sebelum `[Next]` pertama; asersi yang bergantung pada langkah ditulis tepat sesudah aksinya (R-03).
- Ukuran spec (46 langkah, di atas smell sekitar 35 langkah): alasan R3 (bagian 3 prinsip 13). Tiga TC memakai satu topik (walkthrough Guided Tooltip), satu akun, dan satu kelas harness; tiap TC memulai dari flag yang disetel ulang (langkah 1, 19, 35) sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal. Langkah bertambah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-DN-648 langkah 3 menyebut viewport 1440 px sebagai ukuran awal tetapi precondition hanya menyebut "viewport ≥ 1280 px"; spec mengatur 1440 px sebagai langkah penghubung sebelum membuka halaman.
