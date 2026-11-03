---
id: TC-FA-COA-E2E-062-modal-changelog-setup-column-reorder-pin-reset-dan-tutup
title: "Modal Changelog: Setup Column Reorder, Pin, Reset, dan Tutup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-209
  - TC-FA-COA-210
  - TC-FA-COA-211
  - TC-FA-COA-212
coverage:
  web: automated
---

# Modal Changelog: Setup Column Reorder, Pin, Reset, dan Tutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat perubahan ada (minimal satu baris): riwayat Changelog P41 (asumsi pre-setup, bukan data PRD) atau entri lain yang dihasilkan spec lain; spec tidak mengasersi isi baris.
- Kolom tabel Changelog untuk langkah berulang 3 sampai 4 dan 8 sampai 11:

  | Kolom |
  |---|
  | `Date` |
  | `Action` |
  | `Account Code` |
  | `Field` |
  | `Old Value` |
  | `New Value` |
  | `Modified By` |

- Konfigurasi kolom awal tabel Changelog: default modul (tujuh kolom, tanpa kolom terpin).
- State yang diubah spec: konfigurasi kolom tabel Changelog tersimpan lewat `[Save]` pada langkah 16 dan 24; dipulihkan ke default modul pada langkah 22 sampai 24 (`Reset to Default` lalu `[Save]`, langkah TC-211). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-209: Reorder kolom Changelog

1. Klik ikon Changelog di toolbar
2. Klik header kolom Actions ⋯ > `Setup Column...`
3. Seret baris kolom `Date` ke posisi paling bawah daftar popup
4. Verifikasi kolom `Date` menjadi kolom data terakhir sebelum kolom Actions pada pratinjau tabel
5. Ulangi langkah 3 dan 4 untuk setiap kolom lain pada tabel Prerequisites (`Action`, `Account Code`, `Field`, `Old Value`, `New Value`, `Modified By`)
6. Tutup popup dengan ikon ✕

### TC-FA-COA-210: Pin dan unpin kolom Changelog

7. Klik header kolom Actions ⋯ > `Setup Column...`
8. Klik ikon Pin pada baris kolom `Date`, lalu gulir tabel horizontal ke kanan
9. Verifikasi kolom `Date` tetap di posisinya saat tabel digulir horizontal
10. Klik ikon Pin pada baris kolom `Date` untuk unpin, lalu gulir tabel horizontal ke kanan
11. Verifikasi kolom `Date` ikut bergeser setelah unpin
12. Ulangi langkah 8 sampai 11 untuk setiap kolom lain pada tabel Prerequisites (`Action`, `Account Code`, `Field`, `Old Value`, `New Value`, `Modified By`)
13. Tutup popup dengan ikon ✕

### TC-FA-COA-211: Reset to Default sebagai pratinjau, permanen setelah Save

14. Klik header kolom Actions ⋯ > `Setup Column...`
15. Hapus centang kolom Old Value dan New Value
16. Klik `[Save]`
17. Klik header kolom Actions ⋯ > `Setup Column...`
18. Klik `Reset to Default`
19. Verifikasi pratinjau tabel menampilkan tujuh kolom berurutan Date, Action, Account Code, Field, Old Value, New Value, Modified By tanpa kolom terpin
20. Tutup popup dengan ikon ✕
21. Verifikasi tabel kembali ke konfigurasi tersimpan (Old Value dan New Value hidden) karena reset belum disimpan
22. Klik header kolom Actions ⋯ > `Setup Column...`
23. Klik `Reset to Default`
24. Klik `[Save]`
25. Verifikasi tabel menampilkan ketujuh kolom default
26. Tutup modal Changelog dengan ikon ✕
27. Klik ikon Changelog di toolbar
28. Verifikasi tabel Changelog menampilkan ketujuh kolom default (konfigurasi tersimpan kembali ke default)

### TC-FA-COA-212: Tutup popup dengan ikon ✕ tanpa Save

29. Klik header kolom Actions ⋯ > `Setup Column...`
30. Hapus centang kolom Field
31. Seret baris kolom Date ke posisi paling bawah daftar popup
32. Pin kolom Action
33. Verifikasi pratinjau tabel mengikuti perubahan
34. Tutup popup dengan ikon ✕
35. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (default modul: ketujuh kolom, urutan default, tanpa pin)
36. Tutup modal Changelog dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (36 langkah nominal, sekitar 76 dengan ekspansi langkah 5 dan 12): langkah 3 sampai 4 dan 8 sampai 11 diulang untuk tujuh kolom (idiom 8b.7, parameter pada tabel Prerequisites, tanpa langkah bersyarat, `Verifikasi` tetap satu per klausa); seluruh blok memakai satu modal Changelog, satu popup Setup Column, dan satu kelas harness (fungsional Setup Column), dan tiap blok berdiri sendiri sehingga kegagalan satu kolom tidak membuat blok lain kehilangan makna.
- Langkah 5 mengulang langkah 3 dan 4 untuk enam kolom lain; langkah 12 mengulang langkah 8 sampai 11 untuk enam kolom lain. Tujuh seretan berurutan pada TC-209 membuat urutan kembali ke urutan awal.
- Pada langkah 8 dan 10, aksi Pin atau unpin lalu gulir ditulis satu langkah karena gulir adalah bagian dari satu tindakan pengamatan TC-210 (pin, gulir, unpin, gulir).
- Langkah penghubung (S-03): langkah 6, 13, 20, dan 34 (menutup popup tanpa `[Save]`), langkah 14 sampai 16 (menyiapkan konfigurasi tersimpan, langkah TC-211), langkah 22 sampai 24 (pemulihan Setup Column eksplisit, R-24 dan 8b.13), langkah 26 dan 27 (menutup dan membuka ulang modal untuk mengamati konfigurasi tersimpan), langkah 36 (menutup modal).
- Quick panel, popup, checkbox, dan guard satu kolom tabel Changelog ada di spec 061.
- Temuan untuk QA:
  - TC-211 butir c ("konfigurasi tersimpan kembali ke default") tidak menyebut cara mengamati; spec menutup lalu membuka ulang modal Changelog (langkah 26 sampai 28).
  - TC-210 tidak menyebut sisi beku kolom pada tabel Changelog; spec mengasersi "tetap di posisinya" untuk semua kolom.
