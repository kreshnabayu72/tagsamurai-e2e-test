---
id: TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip
title: "Active Sessions: Filter Panel Screening, Opsi Dropdown, OR dan AND, serta Chip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-273
  - TC-FA-LIC-274
  - TC-FA-LIC-275
  - TC-FA-LIC-276
  - TC-FA-LIC-277
coverage:
  web: automated
---

# Active Sessions: Filter Panel Screening, Opsi Dropdown, OR dan AND, serta Chip

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.*` (berkas fixture belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Filter dropdown" (parameter langkah 17 sampai 21):

  | Field | Opsi dropdown (DISTINCT dari tabel saat ini) | Opsi yang dipilih | Baris yang tampil |
  |---|---|---|---|
  | Position | Admin Aset, Staff Gudang, Staff Keuangan, Supervisor Gudang | `Staff Gudang` | Rudi Hartono |
  | Division | Divisi IT, Divisi Keuangan, Divisi Logistik | `Divisi Logistik` | Rudi Hartono, Budi Santoso |
  | Device / OS | Android, iOS, macOS, Windows | `Windows` | Dewi Lestari, Budi Santoso |
  | Browser | Chrome, Edge, Mobile App, Safari | `Safari` | Rudi Hartono, Siti Rahma |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26.

## Test Steps

### TC-FA-LIC-273: Screening Filter Panel, field, tipe komponen, label, dan placeholder

1. Klik tab Concurrent User
2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel Filter tampil di bawah toolbar
5. Verifikasi field berurutan (maksimal 4 per baris): Position, Division, Device / OS, Browser, Login Time, Last Activity, Activation Status, Temporary User, Temporary Until
6. Verifikasi field Position: dropdown multi-select searchable, placeholder `All positions`
7. Verifikasi field Division: dropdown multi-select searchable, placeholder `All divisions`
8. Verifikasi field Device / OS: dropdown multi-select searchable, placeholder `All devices`
9. Verifikasi field Browser: dropdown multi-select searchable, placeholder `All browsers`
10. Verifikasi field Login Time: date range picker, placeholder `Select date`
11. Verifikasi field Last Activity: date range picker, placeholder `Select date`
12. Verifikasi field Activation Status: dropdown multi-select searchable, placeholder `All statuses`
13. Verifikasi field Temporary User: dropdown multi-select searchable, placeholder `All options`
14. Verifikasi field Temporary Until: date range picker, placeholder `Select date`
15. Verifikasi tombol `[Clear Field]` di kiri (text)
16. Verifikasi tombol `[Apply]` di kanan (filled)

### TC-FA-LIC-274: Opsi dan penyaringan Filter per kelas dropdown

17. Untuk setiap baris tabel "Filter dropdown" (langkah 17 sampai 21): buka dropdown field pada baris itu
18. Verifikasi opsi dropdown sama dengan kolom "Opsi dropdown" untuk baris tabel itu
19. Pilih opsi pada kolom "Opsi yang dipilih", klik `[Apply]`
20. Verifikasi tabel menampilkan tepat baris pada kolom "Baris yang tampil"
21. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-275: Dua opsi dalam satu field memakai OR, antar-field memakai AND

22. Pada field `Position` centang `Admin Aset` dan `Staff Gudang`, klik `[Apply]`
23. Verifikasi `Position` = `Admin Aset` atau `Staff Gudang` (OR): tabel menampilkan Rudi Hartono, Dewi Lestari
24. Tambahkan field kedua `Division` = `Divisi Logistik`, klik `[Apply]`
25. Verifikasi dua field berbeda yang terisi sekaligus memakai irisan (AND): tabel menampilkan Rudi Hartono
26. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-276: Chip, hapus lewat tombol X pada chip menghapus centang di dropdown

27. Pada field `Position` pilih `Admin Aset` dan `Staff Gudang`
28. Klik `(×)` pada chip `Admin Aset` tanpa membuka dropdown
29. Verifikasi chip `Admin Aset` hilang
30. Buka dropdown `Position`
31. Verifikasi centang `Admin Aset` di dropdown ikut hilang
32. Verifikasi chip `Staff Gudang` tetap
33. Klik `[Apply]`
34. Verifikasi tabel menampilkan: Rudi Hartono
35. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-277: Chip, uncheck di dalam dropdown menghapus chip yang bersangkutan

36. Pada field `Position` pilih `Admin Aset` dan `Staff Gudang`
37. Buka dropdown `Position`, hapus centang `Admin Aset`
38. Verifikasi chip `Admin Aset` hilang dari field
39. Verifikasi chip `Staff Gudang` tetap
40. Klik `[Apply]`
41. Verifikasi perubahan berlaku pada hasil setelah `[Apply]` ditekan: tabel Active Sessions menampilkan Rudi Hartono
42. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: `[Clear Field]` lalu `[Apply]` di akhir tiap blok (S-09) dan menambahkan field kedua pada TC-FA-LIC-275.
- Blok ulang: langkah 17 sampai 21 dijalankan 4 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah screening Filter satu tabel dengan satu dataset dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-FA-LIC-275 langkah 4 ("Tambahkan field kedua") tidak menyebut field dan nilainya, dan butir b tidak menyebut hasil irisan. Spec memakai `Division` = `Divisi Logistik` dan menurunkan hasil Rudi Hartono dari oracle TC-FA-LIC-274 dan TC-FA-LIC-268 (Rudi Hartono berada di Divisi Logistik, Dewi Lestari tidak). TC-FA-LIC-277 butir b ("Perubahan berlaku pada hasil setelah Apply") tidak menyebut baris hasil; spec mengasersi Rudi Hartono dari oracle TC-FA-LIC-276.
