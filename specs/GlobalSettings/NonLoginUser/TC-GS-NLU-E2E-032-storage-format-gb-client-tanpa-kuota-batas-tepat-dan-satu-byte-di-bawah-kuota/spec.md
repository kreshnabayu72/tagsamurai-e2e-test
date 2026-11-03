---
id: TC-GS-NLU-E2E-032-storage-format-gb-client-tanpa-kuota-batas-tepat-dan-satu-byte-di-bawah-kuota
title: "Storage: format GB, client tanpa kuota, batas tepat, dan 1 byte di bawah kuota"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-510
  - TC-GS-NLU-511
  - TC-GS-NLU-515
  - TC-GS-NLU-516
  - TC-GS-NLU-517
coverage:
  web: automated
---

# Storage: format GB, client tanpa kuota, batas tepat, dan 1 byte di bawah kuota

## Prerequisites

- Mode: FE+BE (backend nyata; pengecekan Storage dilakukan server berdasarkan usage ledger dan kuota tiap client).
- Login di hook `before` spec ini sebagai akun aktor pertama (Client PT Storage Penuh GB); halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1 dan 19) dengan `{namaCompany}` = nama Client pada tabel berikut. Nama env baru yang diusulkan (belum terdaftar di `spectra.config.ts` dan `.env.example`; akun disediakan tim FE):

  | Client | Env password | Kuota / usage ledger | TC |
  |---|---|---|---|
  | PT Storage Penuh GB | `GS_STORAGEGB_TC_PASSWORD` | 2147483648 byte (2.0 GB) / 2576980378 byte (2.4 GB) | 511 |
  | PT Storage Tanpa Kuota | `GS_STORAGENOQUOTA_TC_PASSWORD` | Storage belum pernah dialokasikan | 510, 515 |
  | PT Storage Batas | `GS_STORAGEEDGE_TC_PASSWORD` | 2147483648 byte / 2147483648 byte | 516 |
  | PT Storage Hampir | `GS_STORAGENEAR_TC_PASSWORD` | 2147483648 byte / 2147483647 byte | 517 |

- Env var: `GS_STORAGEGB_TC_PASSWORD`, `GS_STORAGENOQUOTA_TC_PASSWORD`, `GS_STORAGEEDGE_TC_PASSWORD`, `GS_STORAGENEAR_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk keempat akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 12 dan 19, hanya dibaca): Division `Operations`, Login User `Ahmad Fauzi` (pool Represented By) pada tiap client. Kuota dan usage ledger diatur lewat seed atau API (disediakan tim FE/BE); usage ledger PT Storage Hampir naik melewati kuota sesudah TC-GS-NLU-517 dan dipulihkan di hook `after`.
- Berkas uji di perangkat uji: gambar JPG 500 KB.
- Data Dinamis milik spec (Tabel Data Uji Dinamis No. 8 dan 9), First Name `Foto`, Division `Operations`, Represented By `Ahmad Fauzi`:
  - PT Storage Penuh GB: `Foto Format GB` (Last Name `Format GB`) Email `fotoformatgb+{runId}-032@qwertysystem.net` (tidak tersimpan).
  - PT Storage Tanpa Kuota: `Foto Tanpa Kuota {runId}-032` (Last Name `Tanpa Kuota {runId}-032`) Email `fototanpakuota+{runId}-032@qwertysystem.net` (tersimpan). `Storage Tanpa Kuota Satu {runId}-032` (First Name `Storage`, Last Name `Tanpa Kuota Satu {runId}-032`, berfoto, Division `Operations`, Represented By `Ahmad Fauzi`) Email `storagetanpakuotasatu+{runId}-032@qwertysystem.net` di-seed lewat API di hook `before` sebagai padanan Pre-setup No. 19 (Pre-setup tidak diubah; S-06).
  - PT Storage Batas: `Foto Batas Satu {runId}-032` (Last Name `Batas Satu {runId}-032`) Email `fotobatassatu+{runId}-032@qwertysystem.net` (tidak tersimpan).
  - PT Storage Hampir: `Foto Batas Dua {runId}-032` (Last Name `Batas Dua {runId}-032`) Email `fotobatasdua+{runId}-032@qwertysystem.net` (tersimpan).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-032` pada keempat client lewat API dan pulihkan usage ledger awal (mekanisme disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` (dirujuk sebagai `Fixture.nonLoginUser.<key>`) belum ada dan dibuat di tahap script.
- State global yang diubah: usage ledger PT Storage Hampir (lihat di atas). Suite berjalan serial.

## Test Steps

### Client PT Storage Penuh GB (login di hook before)

#### TC-GS-NLU-511: Toast Storage penuh berformat GB

1. Klik `[+ Non-Login User]`
2. Isi First Name `Foto`, Last Name `Format GB`, Email `fotoformatgb+{runId}-032@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
3. Klik `[Submit]`
4. Verifikasi toast error persisten: `Error, failed to upload photo. Storage is full (2.4 GB of 2.0 GB used).`
5. Verifikasi nilai terpakai `2.4 GB` ditampilkan apa adanya walau melebihi kuota `2.0 GB`
6. Verifikasi nilai pada toast berformat satu desimal dengan satuan `GB`
7. Tutup toast error secara manual
8. Klik `✕`
9. Verifikasi dialog Unsaved Changes tampil
10. Klik `[Leave]`

### Client PT Storage Tanpa Kuota

11. Ganti akun: logout, lalu login sebagai Total Control @ PT Storage Tanpa Kuota dengan password `Spectra.env.GS_STORAGENOQUOTA_TC_PASSWORD`
12. Buka Global Settings > User > User List > sub-tab Non-Login User

#### TC-GS-NLU-510: Create dengan foto pada client tanpa kuota tidak diblokir

13. Klik `[+ Non-Login User]`
14. Isi First Name `Foto`, Last Name `Tanpa Kuota {runId}-032`, Email `fototanpakuota+{runId}-032@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
15. Klik `[Submit]`
16. Verifikasi popup menutup
17. Verifikasi toast sukses `Success, non-login user has been created.`
18. Verifikasi tidak ada toast Storage penuh
19. Ketik Search `Foto Tanpa Kuota {runId}-032`, tekan Enter
20. Verifikasi baris `Foto Tanpa Kuota {runId}-032` muncul di tabel dengan foto sebagai avatar

#### TC-GS-NLU-515: Edit mengganti foto pada client tanpa kuota tidak diblokir

21. Ganti isi kotak search dengan `Storage Tanpa Kuota Satu {runId}-032`, tekan Enter
22. Klik `⋯` pada baris `Storage Tanpa Kuota Satu {runId}-032` > `Edit`
23. Unggah berkas JPG 500 KB pada avatar
24. Klik `[Save]`
25. Verifikasi popup menutup
26. Verifikasi toast sukses `Success, non-login user has been updated.`
27. Verifikasi tidak ada toast Storage penuh
28. Verifikasi avatar baris `Storage Tanpa Kuota Satu {runId}-032` menampilkan foto baru

### Client PT Storage Batas

29. Ganti akun: logout, lalu login sebagai Total Control @ PT Storage Batas dengan password `Spectra.env.GS_STORAGEEDGE_TC_PASSWORD`
30. Buka Global Settings > User > User List > sub-tab Non-Login User

#### TC-GS-NLU-516: Usage ledger tepat sama dengan kuota diblokir

31. Klik `[+ Non-Login User]`
32. Isi First Name `Foto`, Last Name `Batas Satu {runId}-032`, Email `fotobatassatu+{runId}-032@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
33. Klik `[Submit]`
34. Verifikasi toast error persisten: `Error, failed to upload photo. Storage is full (2.0 GB of 2.0 GB used).`
35. Verifikasi Popup Create tetap terbuka
36. Tutup toast error secara manual
37. Klik `✕`
38. Verifikasi dialog Unsaved Changes tampil
39. Klik `[Leave]`
40. Ketik Search `Foto Batas Satu {runId}-032`, tekan Enter
41. Verifikasi kolom header tabel Non-Login User tampil
42. Verifikasi tabel menampilkan `No results found` (tidak ada record `Foto Batas Satu {runId}-032` dibuat)

### Client PT Storage Hampir

43. Ganti akun: logout, lalu login sebagai Total Control @ PT Storage Hampir dengan password `Spectra.env.GS_STORAGENEAR_TC_PASSWORD`
44. Buka Global Settings > User > User List > sub-tab Non-Login User

#### TC-GS-NLU-517: Usage ledger 1 byte di bawah kuota tidak diblokir

45. Klik `[+ Non-Login User]`
46. Isi First Name `Foto`, Last Name `Batas Dua {runId}-032`, Email `fotobatasdua+{runId}-032@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
47. Klik `[Submit]`
48. Verifikasi popup menutup
49. Verifikasi toast sukses `Success, non-login user has been created.`
50. Verifikasi tidak ada toast Storage penuh
51. Ketik Search `Foto Batas Dua {runId}-032`, tekan Enter
52. Verifikasi baris `Foto Batas Dua {runId}-032` muncul di tabel dengan foto sebagai avatar

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` dan `####` memetakan langkah ke client dan id TC granular. Kelas blokir kondisi data (prinsip 12): tiap client mewakili satu kondisi Storage (penuh dalam GB, tanpa kuota, tepat di batas, 1 byte di bawah kuota). TC-GS-NLU-508, 509, dan 512 sampai 514 (Client PT Storage Penuh MB) ada di spec 030 dan 031.
- Alasan di atas sekitar 35 langkah: spec ini 52 langkah. Keempat blok client berdiri sendiri, satu kelas harness (blokir kondisi data), dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun tiap client (langkah 11, 12, 29, 30, 43, 44) adalah syarat tiap blok, bukan langkah tambahan yang dapat dihilangkan.
- Ganti akun eksplisit di langkah 11, 29, dan 43 karena tiap client punya akun Total Control sendiri (S-07); langkah 12, 30, dan 44 membuka layar awal karena hook `beforeEach` hanya membukanya untuk akun pertama.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 dan 36 (menutup toast error persisten; R-12), langkah 8 sampai 10 dan 37 sampai 39 (menutup form dirty secara deterministik; S-08), langkah 19, 21, 40, dan 51 (Search Name bersuffix untuk menemukan baris target karena Email bukan kolom Search; R-16).
- Langkah 42 memakai empty state `No results found` hasil Search sebagai asersi absence; anchor positif: header tabel Non-Login User tetap tampil (langkah 41; 8b.2).
- Temuan untuk QA:
  - TC-GS-NLU-511 Expected b menyebut "format satu desimal dengan satuan otomatis mengikuti kolom Size File Manager" tanpa aturan konversi; spec mengasersi `2.4 GB` dan `2.0 GB` dari teks toast.
  - TC-GS-NLU-510, 515, 516, dan 517 menyebut akun Total Control tiap client tanpa email dan password; spec memakai pola Pre-setup No. 1 dengan nama client sebagai `{namaCompany}` dan env baru yang diusulkan.
  - TC-GS-NLU-515 menyebut `Storage Tanpa Kuota Satu` sebagai record Pre-setup; spec memakai padanan milik spec dengan Email unik.
  - TC-GS-NLU-517 membuat usage ledger melewati kuota (1 byte di bawah kuota ditambah foto 500 KB); pemulihan ledger awal disediakan tim FE/BE.
