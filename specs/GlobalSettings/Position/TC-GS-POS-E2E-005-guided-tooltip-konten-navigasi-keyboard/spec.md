---
id: TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard
title: "Guided Tooltip Tab Position: Konten Step, Navigasi Next/Back, Resize Viewport, Keyboard, dan Identik untuk Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-17
  - TC-GS-POS-22
  - TC-GS-POS-23
  - TC-GS-POS-24
coverage:
  web: automated
---

# Guided Tooltip Tab Position: Konten Step, Navigasi Next/Back, Resize Viewport, Keyboard, dan Identik untuk Read Only

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) untuk TC-GS-POS-17, 22, dan 23. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Read Only `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 3) untuk TC-GS-POS-24: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_RO_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: kunjungan ke tab Position adalah pemicu auto-open Guided Tooltip dan kunjungan ulang (klik sub-tab User List lalu Position) adalah aksi yang diuji, sehingga langkah buka ditulis di `## Test Steps` dan bukan di hook `beforeEach`.
- Data: tidak ada Data Pre-setup dan tidak ada Data Dinamis yang dipakai langkah.
- Guided Tooltip (page_key `gs-position`): spec ini menguji flag `guided_tooltip_seen_gs-position` sendiri, sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`); hook `before` mencatat nilai awal flag untuk akun Total Control dan akun Read Only lalu mereset keduanya ke belum ada (precondition "flag seen belum ada" TC-GS-POS-17, 22, 23, dan 24). Reset ulang flag akun Total Control dilakukan sebagai langkah penghubung sebelum TC-GS-POS-23 dan 22 karena TC sebelumnya menutup walkthrough dan menandai seen. Hook `after` memulihkan nilai awal kedua flag. Mekanisme baca, reset, dan pemulihan flag lewat API disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan flag kedua akun dan kembalikan viewport ke ukuran awal.
- Kemampuan teknis: mengubah ukuran viewport dan memulihkannya; input keyboard (Enter, panah kanan, panah kiri, Esc); pembacaan fokus keyboard pada kotak tooltip; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip dan viewport (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-17: Guided Tooltip, navigasi Next/Back dan konten tiap step

1. Buka Global Settings > User dari sidebar Global Settings
2. Klik sub-tab Position
3. Klik `[Next]`
4. Verifikasi Step 2 menyorot (spotlight) tabel Position
5. Verifikasi Step 2 Title "Position Table"
6. Verifikasi Step 2 Description "Browse and manage all positions in your organization from this table."
7. Verifikasi indikator "Step 2 of 3"
8. Verifikasi `[Back]` tampil
9. Klik `[Next]`
10. Verifikasi Step 3 menyorot (spotlight) ikon Changelog
11. Verifikasi Step 3 Title "Changelog Audit"
12. Verifikasi Step 3 Description "Review the history of changes made to positions."
13. Verifikasi indikator "Step 3 of 3"
14. Verifikasi tombol `[Next]` berubah menjadi `[Done]`
15. Klik `[Back]`
16. Verifikasi kembali ke Step 2 dengan indikator "Step 2 of 3"
17. Verifikasi Step 2 Title "Position Table"
18. Verifikasi Step 2 Description "Browse and manage all positions in your organization from this table."
19. Klik `[Skip]` untuk menutup walkthrough
20. Reset flag `guided_tooltip_seen_gs-position` akun Total Control ke belum ada

### TC-GS-POS-23: Accessibility Guided Tooltip, navigasi keyboard

21. Klik sub-tab User List
22. Klik sub-tab Position
23. Verifikasi tooltip box menerima fokus keyboard saat tampil
24. Tekan Enter
25. Verifikasi Enter berpindah ke Step 2 (indikator "Step 2 of 3")
26. Tekan panah kanan (→)
27. Verifikasi → berpindah ke Step 3 (indikator "Step 3 of 3")
28. Tekan panah kiri (←)
29. Verifikasi ← kembali ke Step 2 (indikator "Step 2 of 3")
30. Tekan Esc
31. Verifikasi Esc menutup walkthrough
32. Klik sub-tab User List
33. Klik sub-tab Position
34. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya (Esc setara Skip)
35. Reset flag `guided_tooltip_seen_gs-position` akun Total Control ke belum ada

### TC-GS-POS-22: Guided Tooltip, resize viewport di tengah walkthrough tidak menandai seen

36. Klik sub-tab User List
37. Klik sub-tab Position
38. Klik `[Next]` sampai Step 2 tampil
39. Ubah ukuran viewport
40. Verifikasi walkthrough tertutup saat resize
41. Kembalikan ukuran viewport ke ukuran awal
42. Klik sub-tab User List
43. Klik sub-tab Position
44. Verifikasi walkthrough muncul otomatis lagi pada kunjungan berikutnya
45. Verifikasi walkthrough dimulai dari Step 1 (indikator "Step 1 of 3")
46. Klik `[Skip]` untuk menutup walkthrough

### TC-GS-POS-24: Guided Tooltip identik untuk aktor Read Only

47. Ganti akun: logout dari akun Total Control
48. Login sebagai Read Only dengan `Spectra.env.GS_RO_PASSWORD`
49. Buka Global Settings > User dari sidebar Global Settings
50. Klik sub-tab Position
51. Amati step pertama
52. Verifikasi Step 1 menyorot (spotlight) Table Tools
53. Verifikasi Step 1 Title "Table Tools"
54. Verifikasi Step 1 Description "Search, filter, and download the positions in this list."
55. Verifikasi indikator "Step 1 of 3"
56. Klik `[Next]`
57. Verifikasi Step 2 Title "Position Table"
58. Verifikasi Step 2 Description sama dengan Description Step 2 aktor Total Control pada Langkah 6: "Browse and manage all positions in your organization from this table."
59. Verifikasi indikator "Step 2 of 3"
60. Klik `[Next]`
61. Verifikasi Step 3 Title "Changelog Audit"
62. Verifikasi Step 3 Description sama dengan Description Step 3 aktor Total Control pada Langkah 12: "Review the history of changes made to positions."
63. Verifikasi indikator "Step 3 of 3"
64. Verifikasi tombol `[Done]` tampil pada Step 3
65. Verifikasi urutan step Table Tools, Position Table, lalu Changelog Audit sama persis dengan aktor Total Control
66. Verifikasi jumlah step 3 sama persis dengan aktor Total Control
67. Klik `[Done]` untuk menutup walkthrough

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 17, 23, 22, 24. TC-GS-POS-17, 23, dan 22 memakai akun Total Control dan tiap TC membutuhkan flag seen belum ada, sehingga flag di-reset sebagai langkah penghubung di antara TC; TC-GS-POS-24 ditaruh terakhir karena butuh ganti akun. Urutan ini menyimpang dari urutan TC sumber (17, 22, 23, 24) demi urutan state (TC-GS-POS-22 mengubah viewport). Perilaku auto-open, Skip, Done, dan penyimpanan flag diuji di spec 006 (TC-GS-POS-16, 18, 19, 20, 21).
- TC-GS-POS-17 tidak mengasersi konten Step 1 (Expected hanya Step 2 dan Step 3). Konten Step 1 diasersi pada TC-GS-POS-24 langkah 54 sebagai Expected a TC itu (Description Step 1 mengikuti PRD position.md §4.7, karena Expected TC-GS-POS-24 hanya menyebut Title dan indikator).
- TC-GS-POS-22 langkah "Klik `[Next]` sampai Step 2 tampil" adalah langkah penghubung yang menjalankan prasyarat Expected ("saat Step 2 tampil"); TC sumber tidak menyebutnya. "Buka ulang tab Position" dilakukan dengan klik sub-tab User List lalu Position.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik `[Skip]` penutup walkthrough pada akhir TC-GS-POS-17 dan 22, reset flag di akhir TC-GS-POS-17 dan 23, pemulihan viewport pada TC-GS-POS-22, klik sub-tab User List lalu Position untuk memicu kunjungan ulang, ganti akun pada TC-GS-POS-24, dan klik `[Done]` penutup.
- Spec 005 (konten, navigasi, resize, keyboard, Read Only) dan spec 006 (flag seen dan dismiss) menguji Guided Tooltip tab Position yang sama dan sengaja dipisah: gabungannya 113 langkah (67 dan 46), jauh di atas sekitar 35 langkah, dan tiap blok mereset flag seen sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Spec melewati sekitar 35 langkah (67 langkah). Seluruhnya satu kelas (Guided Tooltip tab Position: konten dan navigasi), tiap blok TC berdiri sendiri karena flag di-reset sebelum tiap blok, dan kegagalan satu blok tidak menghilangkan makna blok lain; blok pada akun Read Only (TC-GS-POS-24) berada di akhir dengan langkah ganti akun eksplisit dan tetap bermakna walau blok akun Total Control gagal keras, karena hook `before` mereset flag akun Read Only sendiri.
- Temuan untuk QA:
  - TC-GS-POS-24 Expected d ("urutan, konten, dan jumlah step sama persis dengan aktor Total Control") membandingkan dengan Total Control, sedangkan TC-GS-POS-17 tidak mengasersi Step 1 untuk Total Control; spec membandingkan Step 2 dan Step 3 dengan langkah TC-GS-POS-17 dan Step 1 dengan PRD.
  - TC-GS-POS-22 tidak menyebut ukuran viewport yang dipakai; spec memakai ukuran berbeda dari ukuran awal lalu memulihkannya.
  - TC-GS-POS-23 Expected c menulis "→ → Step 3" (dua panah); langkah TC hanya satu kali tekan →, sehingga spec menekan → satu kali dari Step 2 menuju Step 3.
  - TC-GS-POS-17, 22, 23, dan 24 mensyaratkan "flag seen belum ada" tanpa menyebut cara mereset; mekanismenya disediakan tim FE/BE.
