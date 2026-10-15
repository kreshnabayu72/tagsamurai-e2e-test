---
id: TC-AC-PP-E2E-009-role-matrix-visibilitas-elemen
title: "Role Matrix: Visibilitas Elemen Halaman Privacy Policy per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-13
  - TC-AC-PP-17
  - TC-AC-PP-18
  - TC-AC-PP-19
  - TC-AC-PP-21
  - TC-AC-PP-22
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman Privacy Policy per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-AC-PP-13, 17 | Total Control (Principal, Global Role "Manage privacy policy" Read dan Update) | Andi Wijaya | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-AC-PP-13, 18, 19, 22 | Read Only (Principal, "Manage privacy policy" Read saja) | Dewi Lestari | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |
| TC-AC-PP-13, 21 | Default User (tanpa Global Role "Manage privacy policy") | (tanpa nama di TC) | `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DU_PASSWORD` |

- Login akun aktor pertama (Total Control) dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login/logout eksplisit.
- Dataset Riwayat A (Version 3 Active, 10 Aug 2026 pukul 20:30 UTC `John Doe`; Version 2, 02 Jul 2026, `John Doe`; Version 1, 15 Jan 2026, `Jane Smith`, akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan dataset ke Riwayat A. Spec read-only, tidak membuat data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kemampuan teknis: Fixture BE. Tidak memakai intercept, jam server, atau klien HTTP.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_RO_PASSWORD` dan `AC_DU_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PP-13: Item sidebar Privacy Policy tampil untuk Total Control, Read Only, dan Default User dan halaman terbuka

1. Buka grup Settings pada sidebar (sesi Total Control dari hook `before`)
2. Verifikasi Total Control: item "Privacy Policy" tampil di grup Settings
3. Klik "Privacy Policy"
4. Verifikasi Total Control: halaman `Settings > Privacy Policy` terbuka dengan tabel Version History
5. Verifikasi Total Control: tabel menampilkan tiga baris Riwayat A (`Version 3` Active, `Version 2`, `Version 1`)
6. Verifikasi Total Control: tidak ada pembatasan baris per aktor
7. Logout dari akun Total Control
8. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
9. Buka grup Settings pada sidebar
10. Verifikasi Read Only: item "Privacy Policy" tampil di grup Settings
11. Klik "Privacy Policy"
12. Verifikasi Read Only: halaman terbuka dengan tabel Version History
13. Verifikasi Read Only: tabel menampilkan tiga baris Riwayat A yang sama (`Version 3` Active, `Version 2`, `Version 1`)
14. Logout dari akun Read Only
15. Login sebagai Default User (`defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`)
16. Buka grup Settings pada sidebar
17. Verifikasi Default User: item "Privacy Policy" tampil (tanpa syarat role "Manage privacy policy")
18. Klik "Privacy Policy"
19. Verifikasi Default User: halaman terbuka dengan tabel Version History
20. Verifikasi Default User: tabel menampilkan tiga baris Riwayat A yang sama (`Version 3` Active, `Version 2`, `Version 1`)

### TC-AC-PP-21: Default User melihat row action dan tombol yang sama dengan Total Control tanpa syarat role Manage privacy policy

21. Klik `[⋯]` pada baris `Version 3`
22. Verifikasi dropdown baris `Version 3` berisi `Detail`
23. Verifikasi dropdown baris `Version 3` berisi `Edit`
24. Pilih `Detail` dan tunggu konten termuat
25. Amati footer modal
26. Verifikasi footer Modal View menampilkan tombol `[Edit]`
27. Klik `[✕]` untuk menutup Modal View

### TC-AC-PP-18: Read Only melihat dropdown row action hanya berisi Detail pada baris Active dan Superseded

28. Logout dari akun Default User
29. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
30. Buka Settings > Privacy Policy lewat sidebar
31. Klik `[⋯]` pada baris `Version 3`
32. Verifikasi dropdown baris `Version 3` hanya berisi `Detail`
33. Verifikasi `Edit` Hidden (bukan disabled)
34. Tutup dropdown
35. Klik `[⋯]` pada baris `Version 2`
36. Verifikasi dropdown baris `Version 2` hanya berisi `Detail`
37. Tutup dropdown

### TC-AC-PP-19: Read Only membuka Modal View versi Active tanpa tombol [Edit] di footer

38. Klik teks tautan `Version 3`
39. Tunggu konten termuat
40. Verifikasi `Settings > Privacy Policy > Popup Privacy Policy Detail` terbuka dengan konten rendered
41. Verifikasi footer modal kosong: tombol `[Edit]` Hidden
42. Verifikasi tidak ada tombol Close di footer
43. Klik `[✕]` untuk menutup Modal View

### TC-AC-PP-22: Tabel tidak memiliki kolom checkbox dan Bulk Action Bar, dan kontrol baca tetap aktif untuk Read Only

44. Amati header dan baris tabel
45. Verifikasi tidak ada kolom checkbox seleksi baris
46. Verifikasi tidak ada Bulk Action Bar
47. Amati toolbar dan header kolom Column Visibility `(⋯)`
48. Verifikasi icon Search, Filter, dan Download tampil
49. Verifikasi icon Search, Filter, dan Download aktif
50. Verifikasi icon Sort pada header Version, Published At, dan Published By tampil
51. Verifikasi icon Sort pada header Version, Published At, dan Published By aktif
52. Verifikasi pagination tampil
53. Verifikasi pagination aktif
54. Verifikasi trigger Column Visibility `(⋯)` tampil
55. Verifikasi trigger Column Visibility `(⋯)` aktif
56. Verifikasi ikon `[⋯]` row action tampil pada tiap baris karena Detail tersedia

### TC-AC-PP-17: Total Control melihat row action Detail pada semua baris dan Edit hanya pada baris Active

57. Logout dari akun Read Only
58. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
59. Buka Settings > Privacy Policy lewat sidebar
60. Klik `[⋯]` pada baris `Version 3`, amati dropdown, lalu tutup
61. Verifikasi dropdown baris `Version 3` berisi `Detail` (icon FileInfoLine)
62. Verifikasi dropdown baris `Version 3` berisi `Edit` (icon Edit2Line)
63. Klik `[⋯]` pada baris `Version 2`, amati dropdown, lalu tutup
64. Verifikasi dropdown baris `Version 2` hanya berisi `Detail`
65. Amati toolbar
66. Verifikasi toolbar menampilkan `Search`, `Filter`, `Download`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Spec Role Matrix visibilitas (bagian 3a konvensi): satu daftar elemen, banyak role, hasil berbeda per role; polaritas tampil dan Hidden dicampur.
- Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-05): TC sumber 13, 17, 18, 19, 21, 22 diurutkan ulang menjadi 13 (Total Control, Read Only, Default User), 21 (Default User), 18, 19, 22 (Read Only), 17 (Total Control) agar jumlah ganti akun minimal dan setiap akun dipakai berurutan. TC-AC-PP-13 mengganti akun dua kali (langkah 7–8 dan 14–15, sesuai langkah TC); dua ganti akun berikutnya (langkah 28–29 dan 57–58) adalah langkah penghubung.
- Langkah penghubung (S-03): langkah 27, 43 (tutup Modal View), 28–30 dan 57–59 (ganti akun eksplisit dan buka halaman), 34, 37 (tutup dropdown). Langkah 1 tidak melakukan login karena akun aktor pertama sudah login di hook `before` (S-07).
- Pembagian TC lintas spec: Role Matrix positif eksekusi per capability di spec 012 dan 013; negatif di spec 010 dan 011.
- Temuan untuk QA:
  - TC-AC-PP-17, TC-AC-PP-18 (judul dan Data Uji), dan TC-AC-PP-23 melabeli `Version 2` sebagai "Superseded" sedangkan TC-AC-PP-02 menyatakan tidak ada badge Superseded; istilah hanya label data uji, tidak diasersi sebagai badge.
  - TC-AC-PP-13 precondition menyebut "user Principal untuk role Total Control, Read Only, dan Default User" tanpa email; spec memakai akun Pre-setup 1, 2, dan 3.
  - TC-AC-PP-19 Expected b menyebut footer kosong sekaligus "tidak ada tombol Close"; kedua klausa dipisah menjadi dua Verifikasi (langkah 41–42).
- Ukuran spec (66 langkah, melewati sekitar 35): langkah membengkak karena tiap klausa Expected menjadi satu Verifikasi (S-01) dan Role Matrix mengulang langkah untuk tiga role (bagian 3a). Satu dataset (Riwayat A), tanpa aksi tulis, dan tiap blok TC berdiri sendiri (login ulang eksplisit di awal blok akun) sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal; spec tidak dipecah (konvensi bagian 3, batas ukuran).
