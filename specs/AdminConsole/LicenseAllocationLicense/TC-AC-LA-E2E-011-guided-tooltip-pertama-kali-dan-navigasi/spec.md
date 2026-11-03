---
id: TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi
title: "Guided Tooltip: Walkthrough Pertama Kali, Replay, Navigasi, dan Skip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-47
  - TC-AC-LA-48
  - TC-AC-LA-49
  - TC-AC-LA-50
coverage:
  web: automated
---

# Guided Tooltip: Walkthrough Pertama Kali, Replay, Navigasi, dan Skip

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): baca, hapus, dan setel flag `guided_tooltip_seen_ac-license-allocation-license` per akun; atur ukuran viewport browser. Flag disimpan per akun dan dibaca lewat kemampuan itu.
- Akun UI kedua untuk TC-AC-LA-50 (`Ulangi dengan akun lain`) tidak tertulis di Pre-setup TC; disediakan tim FE beserta kredensialnya lewat fixture (lihat Temuan untuk QA).
- page_key walkthrough: `ac-license-allocation-license`. Flag diatur spec ini sendiri sesudah hook suite; hook `after` memulihkan nilai awal flag kedua akun.
- Tabel parameter Step 1 sampai 5 (langkah yang diulang per baris tabel pada TC-AC-LA-47):

| Step | Target | Title | Description |
|---|---|---|---|
| 1 | Tabs | `Current and History` | `Current shows allocations that are waiting for a decision, not started yet, or in effect. History keeps expired, rejected, and canceled ones.` |
| 2 | Table | `One Row per Allocation` | `Each row is a single allocation event. Final records stay as they are, so any correction is made with a new allocation.` |
| 3 | Breadcrumb | `License Allocation` | `This page lists every license allocation made to your clients. Open a row's menu to see its log or take action, or use the toolbar to start a new allocation.` |
| 4 | kolom Status | `Status Shows Where It's At` | `This column shows where each allocation stands, from approval through its license cycle.` |
| 5 | ikon Changelog | `Every Allocation Logged` | `Open this log to review who changed an allocation and when.` |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-license` diatur spec ini sendiri sesudah hook suite (kemampuan baca dan setel flag disediakan tim FE/BE); hook `after` memulihkan nilai awal flag.

## Test Steps

### TC-AC-LA-47: Walkthrough pertama kali: Step 1 sampai 5

1. Hapus flag `guided_tooltip_seen_ac-license-allocation-license` akun `totalControlLic` (keadaan belum ada)
2. Klik menu `License Allocation` di sidebar (membuka List untuk pertama kali)
3. Verifikasi walkthrough muncul otomatis dari Step 1 dengan indikator `Step 1 of 5`
4. Verifikasi walkthrough menyorot elemen pada kolom Target baris tabel Step yang aktif (langkah 4 sampai 7 diulang untuk Step 1 sampai 4)
5. Verifikasi Title Step yang aktif sama dengan kolom Title baris tabel Step itu
6. Verifikasi Description Step yang aktif sama dengan kolom Description baris tabel Step itu
7. Klik `[Next]`
8. Verifikasi Step 5 menyorot ikon Changelog
9. Verifikasi Title Step 5: `Every Allocation Logged`
10. Verifikasi Description Step 5: `Open this log to review who changed an allocation and when.`
11. Verifikasi tombol pada Step 5 berubah menjadi `[Done]`
12. Klik `[Done]`
13. Verifikasi walkthrough tertutup
14. Verifikasi flag seen tersimpan untuk akun `totalControlLic`

### TC-AC-LA-48: Tidak muncul otomatis pada kunjungan berikutnya dan replay

15. Klik menu `License Allocation` di sidebar (membuka kembali List)
16. Verifikasi walkthrough tidak muncul otomatis
17. Hover tombol `[?]` di sebelah kanan Breadcrumb
18. Verifikasi tooltip tombol `[?]`: `Show guide`
19. Klik tombol `[?]`
20. Verifikasi walkthrough dimulai dari Step 1
21. Verifikasi flag seen tidak direset oleh klik `[?]`

### TC-AC-LA-49: Navigasi walkthrough: Back, Next, dan Done

22. Verifikasi `[Back]` tidak tampil di Step 1
23. Klik `[Next]` ke Step 2
24. Verifikasi `[Back]` tampil di Step 2
25. Klik `[Back]`
26. Verifikasi walkthrough kembali ke Step 1
27. Klik `[Next]` sebanyak 4 kali hingga Step 5
28. Verifikasi tombol primer Step 5 berlabel `[Done]`

### TC-AC-LA-50: Skip dan klik overlay menyimpan flag seen

29. Hapus flag `guided_tooltip_seen_ac-license-allocation-license` akun `totalControlLic` dan muat ulang halaman hingga walkthrough tampil
30. Verifikasi walkthrough tampil dari Step 1
31. Klik `[Skip]`
32. Verifikasi walkthrough tertutup dan flag seen tersimpan untuk akun `totalControlLic`
33. Muat ulang halaman
34. Verifikasi Tabs List tampil
35. Verifikasi walkthrough tidak muncul lagi setelah muat ulang
36. Ganti akun: Logout lalu login sebagai akun UI kedua (disediakan tim FE; flag seen belum ada)
37. Klik menu `License Allocation` di sidebar hingga walkthrough tampil
38. Verifikasi walkthrough tampil dari Step 1
39. Klik overlay gelap
40. Verifikasi walkthrough tertutup dan flag seen tersimpan untuk akun UI kedua
41. Muat ulang halaman
42. Verifikasi Tabs List tampil
43. Verifikasi walkthrough tidak muncul lagi setelah muat ulang

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah hapus flag, langkah pasang dan lepas keadaan flag, langkah `Klik [Next]` yang berpindah Step, dan ganti akun eksplisit (S-07). Sesudah TC-AC-LA-47, `Klik menu License Allocation` membuka List dari dalam aplikasi karena hook `beforeEach` suite sudah membuka List sebelum walkthrough diaktifkan.
- Spec ini di atas 35 langkah dengan ekspansi (langkah 4 sampai 7 diulang empat kali). Alasannya: semua blok satu topik dan satu halaman (Guided Tooltip List License Allocation), berbagi satu flag, dan TC-AC-LA-48 sampai TC-AC-LA-50 bergantung pada flag yang dibangun TC-AC-LA-47; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC mengikuti TC sumber; TC-AC-LA-49 melanjutkan walkthrough yang dimulai lewat `[?]` pada akhir TC-AC-LA-48 (dependensi TC-AC-LA-49 ke TC-AC-LA-47).
- Step 5 ditulis eksplisit karena tombol berubah menjadi `[Done]` dan tidak ada `[Next]`.
- Temuan untuk QA:
  - TC-AC-LA-50 langkah 4 (`Ulangi dengan akun lain`) tidak menyebut akun lain; spec memakai akun UI kedua yang disediakan tim FE (S-13, S-11).
  - TC-AC-LA-47 Expected g (`flag seen tersimpan`) tidak memberi cara mengamati flag; spec memakai kemampuan baca flag yang disediakan tim FE/BE.
  - NC-19: Description Step 1 `Current and History` ditegaskan verbatim sesuai PRD; ketidaksesuaian dengan Aturan Terkunci #5 `guided-tooltip.md` sudah dicatat sebagai gap PRD owner dan TC tidak ditahan.
  - TC-AC-LA-49 Precondition menyebut walkthrough dimulai lewat `[?]`; spec melanjutkan walkthrough dari klik `[?]` TC-AC-LA-48 tanpa menutupnya.
