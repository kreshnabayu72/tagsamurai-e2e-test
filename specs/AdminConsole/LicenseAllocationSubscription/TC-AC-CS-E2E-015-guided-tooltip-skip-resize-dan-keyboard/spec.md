---
id: TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard
title: "Guided Tooltip: Skip, Resize, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-64
  - TC-AC-CS-65
  - TC-AC-CS-66
  - TC-AC-CS-67
  - TC-AC-CS-68
coverage:
  web: automated
---

# Guided Tooltip: Skip, Resize, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `readOnlySub_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`, Read Only, Principal PT ABC; Pre-setup #3), password `Spectra.env.AC_SUB_RO_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): membaca, menghapus, dan menyetel flag `guided_tooltip_seen_ac-license-allocation-subscription` per akun. Spec ini mengatur flag sendiri sesudah hook suite; hook `after` suite memulihkan nilai awal flag.
- Kemampuan teknis: mengubah ukuran viewport browser di tengah walkthrough (TC-AC-CS-66) dan memulihkannya sesudahnya.

## Test Steps

### TC-AC-CS-64: Skip lewat tombol menutup walkthrough dan menetapkan flag seen

1. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun aktor (flag belum ada)
2. Klik menu `Allocation > Client Subscription` dari sidebar
3. Klik `[Next]` ke Step 2
4. Klik `[Skip]`
5. Verifikasi walkthrough tertutup tanpa berpindah halaman
6. Verifikasi flag bernilai true
7. Buka menu lain di sidebar, lalu buka lagi menu `Allocation > Client Subscription`
8. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-AC-CS-65: Skip lewat klik overlay gelap menutup walkthrough

9. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun aktor (flag belum ada)
10. Klik menu `Allocation > Client Subscription` dari sidebar
11. Klik area overlay gelap di luar spotlight
12. Verifikasi walkthrough tertutup
13. Verifikasi flag bernilai true

### TC-AC-CS-66: Resize atau navigasi keluar di tengah walkthrough tidak menetapkan flag seen

14. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun aktor (flag belum ada)
15. Klik menu `Allocation > Client Subscription` dari sidebar
16. Klik `[Next]` ke Step 2
17. Ubah ukuran viewport browser
18. Verifikasi walkthrough tertutup saat viewport diubah ukurannya
19. Verifikasi flag belum ditetapkan
20. Pulihkan ukuran viewport browser
21. Klik menu `Allocation > Client Subscription` dari sidebar
22. Verifikasi walkthrough muncul otomatis lagi dari Step 1
23. Klik `[Skip]`

### TC-AC-CS-67: Interaksi keyboard pada walkthrough

24. Klik `[?]`
25. Verifikasi tooltip box mendapat keyboard focus saat Step 1 aktif
26. Tekan `Enter`
27. Verifikasi Step 2 tampil
28. Tekan panah kanan
29. Verifikasi Step 3 tampil
30. Tekan panah kiri
31. Verifikasi Step 2 tampil kembali
32. Tekan `Esc`
33. Verifikasi walkthrough tertutup seperti Skip

### TC-AC-CS-68: Walkthrough aktor tanpa tombol [+ Subscription] tetap menampilkan lima langkah termasuk Step 2 Toolbar

34. Logout lalu login sbg Role: Read Only (Principal) `Rina Wijaya`
35. Hapus flag `guided_tooltip_seen_ac-license-allocation-subscription` untuk akun Read Only (flag belum ada)
36. Klik menu `Allocation > Client Subscription` dari sidebar
37. Verifikasi tombol `[+ Subscription]` tidak ada di toolbar
38. Verifikasi Step 1 menyorot Tabs dengan indikator "Step 1 of 5"
39. Klik `[Next]`
40. Verifikasi Step 2 menyorot Toolbar dengan Title "Controls for the Whole List", Description "The toolbar holds the controls that work on the whole list instead of a single row. Starting a new subscription also begins here when your role allows it.", dan indikator "Step 2 of 5"
41. Klik `[Next]`
42. Verifikasi Step 3 menyorot header kolom Actions dengan indikator "Step 3 of 5"
43. Klik `[Next]`
44. Verifikasi Step 4 menyorot kolom Status dengan indikator "Step 4 of 5"
45. Klik `[Next]`
46. Verifikasi Step 5 menyorot ikon Changelog dengan indikator "Step 5 of 5"
47. Klik `[Done]`
48. Verifikasi flag bernilai true

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah menghapus flag, pemulihan viewport, dan langkah "Buka menu lain di sidebar" pada TC-AC-CS-64 (menu yang dipakai ditentukan penulis skrip; TC tidak menyebut nama menu). Ganti akun pada TC-AC-CS-68 punya langkah eksplisit (S-07). TC-AC-CS-67 memakai flag true dari akhir TC-AC-CS-66.
- Verifikasi indikator "Step [N] of 5" pada TC-AC-CS-68 digabung dengan Verifikasi target langkah yang sama.
- Spec ini 48 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (perilaku Guided Tooltip) dan berdiri sendiri; tiap blok mengatur ulang flag sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-CS-68 Expected c (urutan langkah sama dengan aktor yang punya capability Create) dan Expected d (indikator) tidak punya langkah pembanding terhadap akun Create; spec mengasersi urutan target dan indikator pada akun Read Only saja.
  - TC-AC-CS-67 Expected a menyebut tooltip box mendapat fokus; TC tidak menyebut cara mengamati fokus selain langkah sebelumnya.
  - TC-AC-CS-66 langkah 2 tidak menyebut ukuran viewport baru; spec menulis "Ubah ukuran viewport browser" dan memulihkannya sesudahnya (S-03).
