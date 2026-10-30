---
id: TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard
title: "Guided Tooltip Tab Custom Field: Konten 3 Step, Navigasi Keyboard, Fokus Tooltip Box, Aktor Read Only, dan Resize atau Navigasi Keluar"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-22
  - TC-GS-UCF-26
  - TC-GS-UCF-27
  - TC-GS-UCF-28
  - TC-GS-UCF-29
  - TC-GS-UCF-403
coverage:
  web: automated
---

# Guided Tooltip Tab Custom Field: Konten 3 Step, Navigasi Keyboard, Fokus Tooltip Box, Aktor Read Only, dan Resize atau Navigasi Keluar

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor (urutan pemakaian dalam spec):
  - Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-UCF-22, 27, 29, dan 403: login di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; flag seen sudah true (precondition TC-GS-UCF-22 dan 403).
  - Read Only (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-UCF-28: login lewat langkah ganti akun dengan `Spectra.env.GS_RO_PASSWORD`; flag seen sudah true.
  - Total Control Client A (First Visit C, Indah Lestari) `totalControlFirstVisitC_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-UCF-26: login lewat langkah ganti akun dengan `Spectra.env.GS_FVC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field untuk akun Total Control; setelah ganti akun, tab Custom Field dibuka oleh langkah spec.
- Guided Tooltip (page_key `gs-custom-field-user`): hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Total Control dan Read Only (precondition TC-GS-UCF-22, 27, 28, 29, 403) dan hook `after` memulihkannya (lihat `suite.md`). Spec ini menguji akun First Visit C sendiri sehingga dikecualikan dari penyetelan itu: hook `before` mencatat nilai awal flag akun First Visit C lalu mereset flag ke belum ada (precondition TC-GS-UCF-26), dan hook `after` memulihkan nilai awal itu. Mekanisme baca, reset, penyetelan, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Data Pre-setup: Custom Field Client A tersedia (dibaca saja; tidak diubah). Tidak ada Data Dinamis.
- Kemampuan teknis: tombol keyboard (panah kiri, panah kanan, Enter, Esc); pembacaan elemen yang menerima fokus keyboard; mengubah lebar viewport; tombol Back dan Forward browser; muat ulang halaman (tidak ada form terbuka sehingga tidak ada dialog `beforeunload`); ganti akun (logout lalu login).
- State global: flag Guided Tooltip akun First Visit C dan lebar viewport. Hook `after` memulihkan keduanya walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-22: Konten 3 step Guided Tooltip tab Custom Field sesuai urutan

1. Klik `[?]` di sebelah kanan Breadcrumb
2. Verifikasi Step 1 tampil dengan indikator `Step 1 of 3`
3. Verifikasi Step 1 menyorot Table Tools
4. Verifikasi Step 1 Title `Find and manage fields`
5. Verifikasi Step 1 Description `Find records and review changes from here — available actions depend on your access level.`
6. Verifikasi `[Back]` Hidden pada Step 1
7. Klik `[Next]`
8. Verifikasi Step 2 menyorot header kolom `Data Type`
9. Verifikasi Step 2 Title `Review data types`
10. Verifikasi Step 2 Description `Each field's data type is shown in this column.`
11. Klik `[Next]`
12. Verifikasi Step 3 menyorot header kolom `Required`
13. Verifikasi Step 3 Title `Required fields`
14. Verifikasi Step 3 Description `Shows whether a field must be filled in on user forms.`
15. Verifikasi `[Next]` berganti `[Done]` pada Step 3
16. Klik `[Done]`

### TC-GS-UCF-27: Keyboard pada walkthrough, panah kanan, panah kiri, Enter, dan Esc

17. Klik `[?]` di sebelah kanan Breadcrumb
18. Tekan panah kanan
19. Verifikasi walkthrough pindah ke Step 2
20. Tekan panah kiri
21. Verifikasi walkthrough kembali ke Step 1
22. Tekan Enter
23. Verifikasi walkthrough pindah ke Step 2
24. Tekan Esc
25. Verifikasi walkthrough tertutup

### TC-GS-UCF-29: Walkthrough tidak berpindah halaman dan tidak membuka dialog selama berjalan

26. Klik `[?]` di sebelah kanan Breadcrumb
27. Verifikasi pada Step 1 halaman tetap tab Custom Field
28. Verifikasi pada Step 1 tidak ada dialog, modal, atau route yang terbuka otomatis
29. Klik `[Next]`
30. Verifikasi pada Step 2 halaman tetap tab Custom Field
31. Verifikasi pada Step 2 tidak ada dialog, modal, atau route yang terbuka otomatis
32. Klik `[Next]`
33. Verifikasi pada Step 3 halaman tetap tab Custom Field
34. Verifikasi pada Step 3 tidak ada dialog, modal, atau route yang terbuka otomatis
35. Klik `[Done]`
36. Verifikasi setelah `[Done]` halaman tetap tab Custom Field

### TC-GS-UCF-403: Accessibility Guided Tooltip, tooltip box walkthrough menerima fokus keyboard

37. Klik `[?]` di sebelah kanan Breadcrumb
38. Verifikasi Step 1 tampil
39. Verifikasi tooltip box walkthrough menerima fokus keyboard
40. Tutup walkthrough dengan menekan Esc

### TC-GS-UCF-28: Walkthrough identik untuk aktor Read Only

41. Ganti akun: logout, lalu login sebagai Read Only
42. Buka Global Settings > User > Custom Field
43. Klik `[?]`
44. Verifikasi Step 1 menyorot Table Tools
45. Verifikasi `[+ Custom Field]` Hidden pada Table Tools
46. Verifikasi indikator Step 1 `Step 1 of 3`
47. Klik `[Next]`
48. Verifikasi Step 2 menyorot header kolom `Data Type`
49. Klik `[Next]`
50. Verifikasi Step 3 menyorot header kolom `Required`
51. Verifikasi total 3 step (indikator Step 3 `Step 3 of 3`)
52. Klik `[Done]`

### TC-GS-UCF-26: Resize viewport atau navigasi keluar di tengah walkthrough menutupnya tanpa menyimpan flag

53. Ganti akun: logout, lalu login sebagai Total Control Client A (First Visit C)
54. Buka Global Settings > User > Custom Field
55. Verifikasi Step 1 tampil
56. Ubah lebar viewport
57. Verifikasi walkthrough tertutup
58. Muat ulang halaman
59. Verifikasi walkthrough muncul lagi dari Step 1
60. Tekan tombol Back browser saat Step 1 tampil
61. Verifikasi walkthrough tertutup saat berpindah halaman
62. Tekan tombol Forward browser untuk kembali ke tab Custom Field
63. Verifikasi walkthrough muncul lagi dari Step 1
64. Kembalikan lebar viewport ke ukuran awal

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 22, 27, 29, 403 (akun Total Control), 28 (Read Only), 26 (First Visit C). Pengelompokan per akun menyimpang dari urutan daftar sumber (22, 26, 27, 28, 29, 403) supaya ganti akun hanya dua kali; TC-GS-UCF-26 ditaruh terakhir karena mengubah flag dan viewport. Pemulihan flag First Visit C dilakukan hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan 52 (`[Done]` menutup walkthrough sebelum TC berikutnya), langkah 40 (Esc menutup walkthrough), langkah 41 dan 53 (ganti akun), langkah 42 dan 54 (membuka tab Custom Field setelah ganti akun), dan langkah 64 (memulihkan viewport, S-09).
- Langkah 55 (Step 1 tampil) adalah asersi tambahan di luar Expected TC-GS-UCF-26 yang membuktikan walkthrough benar-benar terbuka sebelum langkah 57 mengasersi tertutup (anchor positif, S-03). Langkah 46 dan 51 memakai indikator `Step N of 3` dari Expected a TC-GS-UCF-22 sebagai padanan "Total 3 step" TC-GS-UCF-28 c, karena TC itu tidak menyebut cara membuktikan jumlah step.
- Pembagian TC lintas spec: auto-open kunjungan pertama, `[Skip]`, `[Done]` pada kunjungan pertama, klik overlay gelap, `Esc` kunjungan pertama, dan replay lewat `[?]` ada di spec 006 (TC-GS-UCF-23, 24, 25, 401, 402).
- Spec melewati sekitar 35 langkah (64 langkah). Seluruhnya satu kelas (Guided Tooltip tab Custom Field: konten dan navigasi), tiap blok TC berdiri sendiri dan blok setelah ganti akun (TC-GS-UCF-28 dan 26) tetap bermakna walau blok sebelumnya gagal; langkah ganti akun eksplisit ada di awal tiap blok akun baru.
- Temuan untuk QA:
  - TC-GS-UCF-26 langkah 1 ("Buka tab Custom Field hingga Step 1 tampil") tidak punya Expected untuk kemunculan awal; spec menambah `Verifikasi` Step 1 tampil (langkah 55) agar asersi tertutup tidak lolos tanpa walkthrough.
  - TC-GS-UCF-26 tidak menyebut halaman tujuan tombol Back browser; spec mengikuti TC (Back dan Forward) tanpa menyebut halaman sebelumnya.
  - TC-GS-UCF-26 langkah 2 ("Ubah lebar viewport") tidak menyebut ukuran; spec mengubah lebar viewport tanpa nilai tertentu.
  - TC-GS-UCF-22 b dan c tidak menyebut indikator `Step 2 of 3` dan `Step 3 of 3`; spec hanya mengasersi indikator Step 1 pada TC-GS-UCF-22.
  - Email dan env var akun First Visit C tidak ada di `.env.example`; `GS_FVC_TC_PASSWORD` adalah nama usulan.
