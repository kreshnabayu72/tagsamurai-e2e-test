---
id: TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp
title: "Popup New Client: Clear Field, Esc, Klik Backdrop, Muat Ulang, dan Tombol Back (Total Control)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-75
  - TC-AC-ACC-74
  - TC-AC-ACC-555
  - TC-AC-ACC-553
  - TC-AC-ACC-488
  - TC-AC-ACC-554
  - TC-AC-ACC-72
  - TC-AC-ACC-73
  - TC-AC-ACC-556
coverage:
  web: automated
---

# Popup New Client: Clear Field, Esc, Klik Backdrop, Muat Ulang, dan Tombol Back (Total Control)

## Prerequisites

- Mode: FE+BE. Tidak ada data yang dibuat.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Nilai uji: `PT Contoh`, Address `Jl. Contoh No. 1`, `PT Esc Uji`, `PT Revert`, `PT Muat Ulang`, `PT Pindah Halaman` (hanya diketik, tidak pernah disimpan).
- Kemampuan teknis: mengonfirmasi atau menolak dialog `beforeunload` bawaan browser pada F5, menekan Esc, menekan tombol Back browser, mengklik area di luar popup, dan mengamati fokus keyboard (butir S-08: kemampuan `beforeunload` tertulis di sini). Spec ini menutup form dengan `[✕]` atau Esc, dan hook `beforeEach` suite boleh mengonfirmasi `beforeunload` sebagai jaring pengaman.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-75 dan TC-74: Klik backdrop, lalu ✕ dan Esc pada form bersih

1. Klik `[+ New Client]`
2. Klik area di luar popup (backdrop)
3. Verifikasi popup tetap terbuka
4. Klik `[✕]` di header popup
5. Verifikasi popup tertutup langsung
6. Verifikasi tidak ada dialog Unsaved Changes
7. Klik `[+ New Client]`
8. Tekan Esc
9. Verifikasi popup tertutup langsung
10. Verifikasi tidak ada dialog Unsaved Changes

### TC-555: F5 pada popup kosong

11. Klik `[+ New Client]`
12. Tekan F5 tanpa mengisi field apa pun
13. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

### TC-553: Ketik lalu hapus kembali

14. Klik `[+ New Client]`
15. Ketik `PT Revert` di field Company Name
16. Hapus seluruh teks Company Name hingga kosong
17. Klik `[✕]` di header popup
18. Verifikasi popup tertutup langsung
19. Verifikasi dialog Unsaved Changes tidak muncul

### TC-488: Esc pada popup dengan perubahan

20. Klik `[+ New Client]`
21. Isi Company Name `PT Esc Uji`
22. Tekan Esc
23. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
24. Klik `[Cancel]`
25. Verifikasi dialog tertutup
26. Verifikasi popup tetap terbuka
27. Verifikasi Company Name tetap "PT Esc Uji"
28. Tekan Esc lagi
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
30. Klik `[Leave]`
31. Verifikasi popup tertutup tanpa menyimpan

### TC-554: F5 pada popup terisi

32. Klik `[+ New Client]`
33. Isi Company Name `PT Muat Ulang`
34. Tekan F5
35. Verifikasi konfirmasi bawaan browser muncul (teks dan tombol ditentukan browser)
36. Pilih tetap berada di halaman pada konfirmasi bawaan browser
37. Verifikasi popup Create tetap terbuka
38. Verifikasi Company Name masih "PT Muat Ulang"
39. Klik `[✕]` di header popup
40. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
41. Klik `[Leave]`

### TC-72 dan TC-73: Clear Field, lalu dialog Unsaved Changes

42. Klik `[+ New Client]`
43. Centang checkbox "Stay on this form after submitting"
44. Isi Company Name `PT Contoh` dan Address `Jl. Contoh No. 1`
45. Klik `[Submit]` tanpa field lain agar muncul pesan error
46. Verifikasi pesan error inline tampil pada field wajib yang masih kosong
47. Klik `[Clear Field]`
48. Verifikasi Company Name kosong
49. Verifikasi Address kosong
50. Verifikasi pesan error inline hilang
51. Verifikasi popup tetap terbuka
52. Verifikasi tidak ada dialog konfirmasi apa pun
53. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
54. Verifikasi kursor fokus berada di field input pertama form
55. Isi Company Name `PT Contoh`
56. Klik `[✕]` di header popup
57. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
58. Klik `[Cancel]`
59. Verifikasi dialog tertutup
60. Verifikasi form tetap terbuka dengan isian
61. Klik `[✕]` di header popup lagi
62. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
63. Klik `[Leave]`
64. Verifikasi popup tertutup tanpa menyimpan

### TC-556: Tombol Back browser pada popup terisi

65. Klik `[+ New Client]`
66. Isi Company Name `PT Pindah Halaman`
67. Tekan tombol Back browser
68. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
69. Klik `[Cancel]`
70. Verifikasi dialog tertutup
71. Verifikasi halaman tetap di Client
72. Verifikasi popup Create tetap terbuka
73. Verifikasi Company Name masih "PT Pindah Halaman"
74. Tekan tombol Back browser lagi
75. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
76. Klik `[Leave]`
77. Verifikasi navigasi Back berjalan
78. Verifikasi popup Create tertutup tanpa menyimpan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Urutan (prinsip 6): kasus bersih lebih dulu memakai satu popup bersama (TC-75 lalu TC-74 pertama, popup berikutnya TC-74 kedua), kasus dirty memakai popup baru; TC-556 di akhir karena Back meninggalkan halaman. Jumlah buka form sama dengan jumlah kejadian menutup.
- Alasan di atas 35 langkah (sekitar 80 langkah): satu popup, satu role, satu kelas (penutupan popup), tanpa data tercipta; tiap blok berdiri sendiri.
- Langkah penghubung (S-03): penutup `✕`, dialog, dan `[Leave]` pada TC-554 menutup form dirty setelah konfirmasi bawaan browser (S-08).
- Temuan untuk QA:
  - TC-72 butir e ("Kursor fokus berada di field input pertama form") tidak menyebut field mana (Photo atau Company Name); spec memakai redaksi TC.
  - TC-556 butir c ("navigasi Back berjalan") tidak menyebut halaman tujuan; spec hanya memverifikasi navigasi berjalan dan popup tertutup.
