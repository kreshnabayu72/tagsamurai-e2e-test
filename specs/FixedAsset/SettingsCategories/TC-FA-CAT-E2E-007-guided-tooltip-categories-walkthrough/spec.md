---
id: TC-FA-CAT-E2E-007-guided-tooltip-categories-walkthrough
title: "Guided Tooltip Categories: Kunjungan Pertama, Navigasi, dan Flag Seen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-27
  - TC-FA-CAT-28
  - TC-FA-CAT-29
  - TC-FA-CAT-30
  - TC-FA-CAT-31
coverage:
  web: automated
---

# Guided Tooltip Categories: Kunjungan Pertama, Navigasi, dan Flag Seen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`.
- Pengecualian atas butir Flag Guided Tooltip di `suite.md`: spec ini mengatur flag `guided_tooltip_seen_fa-settings-categories` sendiri sesudah hook (menghapus flag dengan langkah eksplisit); kemampuan mengatur dan menghapus flag disediakan tim FE/BE. Hook suite `after` memulihkan flag ke true.
- Kemampuan teknis: mengubah ukuran viewport browser (TC-FA-CAT-30); keyboard (Enter, panah kiri, Esc) untuk TC-FA-CAT-31.
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-27: Guided Tooltip otomatis muncul pada kunjungan pertama dan memuat tiga step verbatim

1. Hapus flag `guided_tooltip_seen_fa-settings-categories`
2. Buka Fixed Asset > Settings > Categories
3. Verifikasi walkthrough muncul otomatis dari Step 1 dengan indikator `Step 1 of 3`
4. Verifikasi Step 1 menyorot Sidebar Category Tree dengan Title `Category Tree` dan Description `Use this tree to navigate the category hierarchy and add new categories.`
5. Klik `[Next]`
6. Verifikasi Step 2 menyorot tabel direct children dengan Title `Categories Table` dan Description `This table shows the direct subcategories of the currently selected node.`
7. Klik `[Next]`
8. Verifikasi Step 3 menyorot header kolom Actions (⋯) pemicu Setup Column dengan Title `Setup Column` dan Description `Arrange and toggle table columns to match your workflow.`
9. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada step terakhir
10. Klik `[Done]`

### TC-FA-CAT-28: Kunjungan berikutnya tidak memunculkan walkthrough otomatis dan replay [?] memulai dari Step 1

11. Buka Fixed Asset > Settings > Categories
12. Verifikasi Breadcrumb `Settings > Categories` tampil
13. Verifikasi walkthrough tidak muncul otomatis
14. Hover tombol `[?]` di sebelah kanan Breadcrumb
15. Verifikasi tooltip tombol `Show guide`
16. Klik tombol `[?]`
17. Verifikasi walkthrough dimulai dari Step 1
18. Klik overlay gelap
19. Verifikasi walkthrough tertutup
20. Tekan F5
21. Verifikasi Breadcrumb `Settings > Categories` tampil
22. Verifikasi walkthrough tidak muncul otomatis (flag seen tidak di-reset oleh replay)

### TC-FA-CAT-29: Navigasi walkthrough: Back Hidden di Step 1, Skip, dan Done menyimpan flag seen

23. Hapus flag `guided_tooltip_seen_fa-settings-categories`
24. Buka Fixed Asset > Settings > Categories
25. Verifikasi tombol `[Back]` Hidden pada Step 1
26. Klik `[Next]` dua kali
27. Klik `[Back]`
28. Verifikasi walkthrough kembali ke Step 2 (`Step 2 of 3`)
29. Klik `[Skip]`
30. Verifikasi walkthrough tertutup
31. Muat ulang halaman
32. Verifikasi Breadcrumb `Settings > Categories` tampil
33. Verifikasi walkthrough tidak muncul (flag seen tersimpan oleh `[Skip]`)

### TC-FA-CAT-30: Resize viewport saat walkthrough menutupnya tanpa menyimpan flag seen

34. Hapus flag `guided_tooltip_seen_fa-settings-categories`
35. Buka Fixed Asset > Settings > Categories
36. Klik `[Next]` sehingga walkthrough Step 2 tampil
37. Ubah ukuran viewport menjadi lebar 1000px
38. Verifikasi walkthrough tertutup saat resize
39. Kembalikan viewport ke lebar 1400px
40. Muat ulang halaman
41. Verifikasi walkthrough muncul lagi dari Step 1 (flag seen tidak tersimpan)

### TC-FA-CAT-31: Walkthrough dapat dioperasikan dengan keyboard

42. Hapus flag `guided_tooltip_seen_fa-settings-categories`
43. Buka Fixed Asset > Settings > Categories
44. Verifikasi tooltip box walkthrough mendapat fokus keyboard
45. Tekan `Enter`
46. Verifikasi walkthrough menuju Step 2
47. Tekan panah kiri
48. Verifikasi walkthrough kembali ke Step 1
49. Tekan `Esc`
50. Verifikasi walkthrough tertutup (setara `[Skip]`)
51. Muat ulang halaman
52. Verifikasi Breadcrumb `Settings > Categories` tampil
53. Verifikasi walkthrough tidak muncul (flag seen tersimpan oleh `Esc`)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Pengecualian atas hook suite: spec ini membuka halaman sendiri sesudah mengatur flag (langkah 1, 23, 34, 42 menghapus flag; langkah "Buka Fixed Asset > Settings > Categories" sesudahnya).
- Urutan (S-10): TC-FA-CAT-27 diselesaikan dengan `[Done]` (langkah 10) sehingga flag seen bernilai true, yang menjadi prasyarat TC-FA-CAT-28 (walkthrough sudah pernah diselesaikan user ini). TC-FA-CAT-29, 30, dan 31 masing-masing diawali penghapusan flag.
- Langkah penghubung (S-03): langkah 39 (mengembalikan viewport). Langkah "Muat ulang halaman" dan "Tekan F5" sesudah penutupan walkthrough adalah langkah observasi flag seen; flag tidak dibaca langsung (S-13).
- Temuan untuk QA:
  - TC-FA-CAT-30 butir "Ubah ukuran viewport" tidak menyebut ukuran; spec memakai lebar 1000px lalu mengembalikan 1400px.
  - TC-FA-CAT-29 dan TC-FA-CAT-31 menyebut penyimpanan flag seen tanpa cara membaca flag; spec mengamati lewat muat ulang halaman.
- Ukuran spec 53 langkah, melewati sekitar 35 karena Expected dipecah per klausa (S-01). Seluruh blok satu topik (Guided Tooltip halaman Categories), satu kelas harness, satu dataset (CatMain) tanpa aksi tulis, dan tiap blok berdiri sendiri lewat penghapusan flag di awal blok; spec tidak dipecah (konvensi bagian 3, batas ukuran).
- Spec melewati 35 langkah (53 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
