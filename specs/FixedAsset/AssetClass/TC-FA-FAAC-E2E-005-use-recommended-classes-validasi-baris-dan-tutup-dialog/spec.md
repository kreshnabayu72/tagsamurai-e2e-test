---
id: TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog
title: "Dialog Use Recommended Classes: Validasi Class Code dan Class Name per Baris, Class Code Duplikat, Klik Backdrop, dan Unsaved Changes"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-288
  - TC-FA-FAAC-289
  - TC-FA-FAAC-287
  - TC-FA-FAAC-699
  - TC-FA-FAAC-710
coverage:
  web: automated
---

# Dialog Use Recommended Classes: Validasi Class Code dan Class Name per Baris, Class Code Duplikat, Klik Backdrop, dan Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state client): client belum memiliki Asset Class (tabel kosong, EmptyState tampil) dan Tax Depreciation Class rekomendasi Active, disiapkan di hook `before` lewat fixture BE. Hook `after` menghapus Asset Class `HEAVY-EQ` bila masih ada dan memulihkan state client ke nilai awal. Seed disediakan tim FE/BE (lihat `suite.md`).
- Data masukan: Class Code `AB#`; Class Code 16 karakter `A`; Class Name 121 karakter `B`; Class Code ubahan `heavy-eq` (baris MACH) dan `HEQ-1` (baris HEAVY-EQ). Semua dimasukkan ke field dialog dan tidak pernah disimpan.
- Kemampuan teknis: sesi API aktor sebagai pelaku kedua yang hanya memicu perubahan state (TC-FA-FAAC-287), lihat `suite.md`; fixture BE untuk membaca jumlah Asset Class dan menghapus Asset Class `HEAVY-EQ`, disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini membuat satu Asset Class `HEAVY-EQ` (nama literal dari TC) lewat sesi API dan menghapusnya di langkah 32 serta hook `after`.

## Test Steps

### TC-FA-FAAC-288: Dua baris terpilih memiliki Class Code identik

1. Klik link `Use recommended classes` pada EmptyState tabel
2. Centang baris HEAVY-EQ dan MACH
3. Ubah Class Code baris MACH menjadi `heavy-eq`
4. Klik `Create`
5. Verifikasi baris HEAVY-EQ mendapat caption `Class code already exists`
6. Verifikasi baris MACH mendapat caption `Class code already exists`
7. Verifikasi tidak ada Asset Class dibuat (jumlah Asset Class pada client tetap 0 lewat fixture BE)
8. Klik `Cancel`

### TC-FA-FAAC-289: Class Code dan Class Name baris tunduk pada validasi V-01 sampai V-07

9. Klik link `Use recommended classes` pada EmptyState tabel
10. Centang baris HEAVY-EQ
11. Kosongkan Class Code baris HEAVY-EQ
12. Ketik Class Code `AB#`
13. Verifikasi caption `Class code contains invalid characters`
14. Ganti isi Class Code dengan 16 karakter `A`
15. Verifikasi caption `Max. 15 characters` pada Class Code
16. Kosongkan Class Name baris HEAVY-EQ
17. Ketik Class Name 121 karakter `B`
18. Verifikasi caption `Max. 120 characters` pada Class Name
19. Kosongkan Class Code dan Class Name baris HEAVY-EQ
20. Klik `Create` saat kosong
21. Verifikasi caption `Class code must not be empty`
22. Verifikasi caption `Class name must not be empty`
23. Verifikasi tidak ada Asset Class dibuat (jumlah Asset Class pada client tetap 0 lewat fixture BE)
24. Klik `Cancel`

### TC-FA-FAAC-287: Class Code baris sudah dipakai Asset Class lain

25. Klik link `Use recommended classes` pada EmptyState tabel
26. Centang baris HEAVY-EQ
27. Buat Asset Class dengan Class Code `HEAVY-EQ` lewat sesi API aktor hingga Asset Class tersimpan
28. Klik `Create` pada dialog
29. Verifikasi baris HEAVY-EQ mendapat caption `Class code already exists`
30. Verifikasi jumlah Asset Class pada client tetap 1 (hanya Asset Class dari sesi API) lewat fixture BE
31. Klik `Cancel`
32. Hapus Asset Class `HEAVY-EQ` dari sesi API lewat fixture BE hingga tersimpan

### TC-FA-FAAC-699: Klik backdrop pada dialog form Use Recommended Classes (D-21)

33. Klik link `Use recommended classes` pada EmptyState tabel
34. Ubah Class Code baris HEAVY-EQ menjadi `HEQ-1`
35. Klik area backdrop di luar dialog
36. Verifikasi dialog `Use Recommended Classes` tetap terbuka
37. Verifikasi Class Code baris HEAVY-EQ tetap `HEQ-1`
38. Verifikasi dialog `Unsaved Changes` tidak muncul
39. Klik `[Cancel]` pada dialog
40. Verifikasi dialog `Use Recommended Classes` menutup tanpa dialog `Unsaved Changes`
41. Verifikasi tidak ada Asset Class yang dibuat dan EmptyState `No asset class yet` tetap tampil

### TC-FA-FAAC-710: Ikon ✕ dan Esc pada dialog form yang Class Code-nya sudah diubah

42. Klik link `Use recommended classes` pada EmptyState tabel
43. Ubah Class Code baris HEAVY-EQ menjadi `HEQ-1`
44. Klik ikon `[✕]` di header dialog `Use Recommended Classes`
45. Verifikasi dialog `Unsaved Changes` tampil di atas dialog `Use Recommended Classes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
46. Klik `Cancel` pada dialog `Unsaved Changes`
47. Verifikasi dialog `Unsaved Changes` menutup
48. Verifikasi dialog `Use Recommended Classes` tetap terbuka dengan Class Code baris HEAVY-EQ tetap `HEQ-1`
49. Tekan tombol Esc
50. Verifikasi dialog `Unsaved Changes` tampil lagi dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
51. Klik `Leave` pada dialog `Unsaved Changes`
52. Verifikasi dialog `Unsaved Changes` dan dialog `Use Recommended Classes` menutup
53. Verifikasi tidak ada Asset Class yang dibuat dan EmptyState `No asset class yet` tetap tampil
54. Verifikasi tidak ada toast

## Notes

- Spec melewati sekitar 35 langkah (54 langkah): semua blok memakai dialog yang sama (Use Recommended Classes) pada dataset awal yang sama (client tanpa Asset Class), tiap blok berdiri sendiri dan hanya blok TC-FA-FAAC-287 membuat satu data (dihapus di langkah 32), dan memisahnya hanya menggandakan login, hook, dan pemulihan state. Langkah bertambah karena `Verifikasi` dipecah per klausa (S-01).
- Langkah penghubung (S-03): langkah 8, 24, dan 31 (`Cancel` menutup dialog sebelum blok berikutnya; perilaku `Cancel` tanpa konfirmasi diasersi di langkah 40), langkah 32 (menghapus Asset Class yang dibuat sesi API agar tabel kosong kembali). Langkah 27 memicu perubahan state lewat sesi API (R-20; rujukan butir "Sesi API aktor" di `suite.md`).
- Urutan TC dalam spec: 288, 289, 287, 699, 710 (validasi diblokir lebih dulu, kasus menutup dialog di akhir; S-10). TC-FA-FAAC-287 diletakkan setelah dua blok validasi karena membuat data.
- Nama literal `HEAVY-EQ` pada TC-FA-FAAC-287 dipakai tanpa suffix: Class Code maksimum 15 karakter dan kolom Class Code baris rekomendasi adalah isi tetap dialog; seeding Asset Class `HEAVY-EQ` hanya dilakukan sesi API di langkah 27, cleanup hanya menghapus yang dibuat spec ini (langkah 32 dan hook `after`), suite serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAC-289 langkah 4 ("Klik Create saat kosong") tidak menyatakan kapan field dikosongkan sesudah diisi; spec mengosongkan Class Code dan Class Name lebih dulu (langkah 19) lalu mengklik `Create` (langkah 20), sehingga caption "must not be empty" diasersi sesudah submit.
