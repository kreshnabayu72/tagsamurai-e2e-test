---
id: TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access
title: "Edit User: Validasi Required, Batas 120 Karakter Real-Time, dan Uncheck Semua Access Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-164
  - TC-GS-USER-165
  - TC-GS-USER-166
  - TC-GS-USER-167
  - TC-GS-USER-168
  - TC-GS-USER-169
  - TC-GS-USER-170
  - TC-GS-USER-171
  - TC-GS-USER-172
coverage:
  web: automated
---

# Edit User: Validasi Required, Batas 120 Karakter Real-Time, dan Uncheck Semua Access Ditolak

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Position `Staff` (No. 22), Division `Finance` (No. 23), dan produk `Fixed Asset` (subscription Client, No. 26); hanya dibaca. Spec tidak mengubah atau menghapus data Pre-setup (Dewi Lestari No. 12 tidak dipakai sebagai target; pengganti milik spec di bawah, S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD):
  - U-1: First Name `Dewi`, Last Name `Lestari {runId}-033` (Name `Dewi Lestari {runId}-033`), Email `dewilestari+{runId}-033@qwertysystem.net`, Position `Staff`, Division `Finance`, Employee ID `EMP-{runId}-033`, Access `Fixed Asset` dan `Global Settings`, permanen, Active ON. Satu user dipakai untuk semua TC karena semua kasus diblokir validasi dan tidak mengubah data.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 lewat API.
- Nilai uji batas (TC-GS-USER-169 sampai 172): First Name, Last Name, dan Employee ID memakai 120 huruf `A`; Email memakai 103 huruf `a` diikuti `@qwertysystem.net` (total 120 karakter). Karakter ke-121 yang diketik adalah `a` (Email) atau `A` (field lain) di akhir isi field.
- Kemampuan teknis: mengisi dan mengosongkan field; membaca inline error; mendeteksi muncul tidaknya dialog dan toast; jeda pendek tidak diperlukan.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-USER-164: First Name dikosongkan lalu Save

1. Klik icon Search, ketik `Dewi Lestari {runId}-033`, tekan Enter
2. Buka row action baris `Dewi Lestari {runId}-033` lalu klik `Edit`
3. Kosongkan First Name
4. Klik `[Save]`
5. Verifikasi inline error `First name must not be empty`
6. Verifikasi Popup Edit tetap terbuka
7. Isi kembali First Name dengan `Dewi`

### TC-GS-USER-165: Last Name dikosongkan lalu Save

8. Kosongkan Last Name
9. Klik `[Save]`
10. Verifikasi inline error `Last name must not be empty`
11. Verifikasi Popup Edit tetap terbuka
12. Isi kembali Last Name dengan `Lestari {runId}-033`

### TC-GS-USER-166: Email dikosongkan lalu Save

13. Kosongkan Email
14. Klik `[Save]`
15. Verifikasi inline error `Email must not be empty`
16. Verifikasi Popup Edit tetap terbuka
17. Isi kembali Email dengan `dewilestari+{runId}-033@qwertysystem.net`

### TC-GS-USER-167: Division dikosongkan lalu Save

18. Kosongkan Division
19. Klik `[Save]`
20. Verifikasi inline error `Division must not be empty`
21. Verifikasi Popup Edit tetap terbuka
22. Pilih kembali Division `Finance`

### TC-GS-USER-168: Hapus semua pilihan Access lalu Save

23. Hapus pilihan Access `Fixed Asset` dan `Global Settings`
24. Klik `[Save]`
25. Verifikasi inline error `Access must not be empty`
26. Verifikasi dialog Remove Access tidak muncul
27. Pilih kembali Access `Fixed Asset` dan `Global Settings`

### TC-GS-USER-169: First Name 121 karakter

28. Ubah First Name menjadi 120 karakter (120 huruf `A`)
29. Verifikasi tidak ada error pada First Name
30. Ketik 1 karakter lagi (`A`) di akhir First Name sehingga menjadi 121 karakter
31. Verifikasi error `Max. 120 characters` langsung muncul pada First Name
32. Klik `[Save]`
33. Verifikasi `[Save]` tidak memproses form: Popup Edit tetap terbuka
34. Verifikasi `[Save]` tidak memproses form: tidak ada toast sukses
35. Isi kembali First Name dengan `Dewi`

### TC-GS-USER-170: Last Name 121 karakter

36. Ubah Last Name menjadi 120 karakter (120 huruf `A`)
37. Verifikasi tidak ada error pada Last Name
38. Ketik 1 karakter lagi (`A`) di akhir Last Name sehingga menjadi 121 karakter
39. Verifikasi error `Max. 120 characters` langsung muncul pada Last Name
40. Klik `[Save]`
41. Verifikasi `[Save]` tidak memproses form: Popup Edit tetap terbuka
42. Verifikasi `[Save]` tidak memproses form: tidak ada toast sukses
43. Isi kembali Last Name dengan `Lestari {runId}-033`

### TC-GS-USER-171: Employee ID 121 karakter

44. Ubah Employee ID menjadi 120 karakter (120 huruf `A`)
45. Verifikasi tidak ada error pada Employee ID
46. Ketik 1 karakter lagi (`A`) di akhir Employee ID sehingga menjadi 121 karakter
47. Verifikasi error `Max. 120 characters` langsung muncul pada Employee ID
48. Klik `[Save]`
49. Verifikasi `[Save]` tidak memproses form: Popup Edit tetap terbuka
50. Verifikasi `[Save]` tidak memproses form: tidak ada toast sukses
51. Isi kembali Employee ID dengan `EMP-{runId}-033`

### TC-GS-USER-172: Email 121 karakter

52. Ubah Email menjadi 120 karakter (103 huruf `a` diikuti `@qwertysystem.net`)
53. Verifikasi tidak ada error pada Email
54. Ketik 1 karakter lagi (`a`) di akhir Email sehingga menjadi 121 karakter
55. Verifikasi error `Max. 120 characters` langsung muncul pada Email
56. Klik `[Save]`
57. Verifikasi `[Save]` tidak memproses form: Popup Edit tetap terbuka
58. Verifikasi `[Save]` tidak memproses form: tidak ada toast sukses

### Penutupan form dan data tidak berubah (butir "data tidak berubah" TC-GS-USER-164 sampai 168)

59. Klik `[✕]`
60. Verifikasi dialog `Unsaved Changes` tampil
61. Klik `[Leave]`
62. Verifikasi Popup Edit tertutup
63. Verifikasi baris `Dewi Lestari {runId}-033` di tabel tidak berubah: Name, Email, Position, Division, Access (`Fixed Asset` dan `Global Settings`), dan Employee ID sama dengan data seed

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-164 sampai 172). Mode FE+BE; kelas harness: validasi form Edit (satu kelas, tanpa aksi sukses).
- Semua TC memakai satu pembukaan Edit dengan field dikembalikan ke nilai seed di antara kasus (bagian 3 prinsip 13, halaman yang sama dipakai berulang); tiap kasus diakhiri `[Save]` yang diblokir. Kasus terakhir (TC-GS-USER-172) tidak mengembalikan Email, sehingga form tetap dirty dan ditutup deterministik lewat `[✕]`, `Unsaved Changes`, `[Leave]` (S-08).
- Butir "data tidak berubah" (TC-GS-USER-164 sampai 168) dan "Save tidak memproses form" (169 sampai 172) diasersi di tempat: Popup tetap terbuka dan tidak ada toast sukses per kasus, lalu satu `Verifikasi` data baris tabel pada langkah 63 setelah form ditutup.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (membuka form), 7, 12, 17, 22, 27, 35, 43, 51 (mengembalikan field ke nilai seed), 59 dan 61 (penutupan form). `Verifikasi` dialog `Unsaved Changes` (langkah 60) dan Popup tertutup (langkah 62) adalah asersi tambahan sebagai bagian penutupan deterministik S-08; tidak ada di Expected TC sumber.
- Pembagian TC lintas spec: TC-GS-USER-164 sampai 172 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-164 sampai 167 butir "data tidak berubah" tidak menyebut cara memeriksa; spec memeriksa baris tabel setelah form ditutup.
  - TC-GS-USER-167 ("Kosongkan Division") tidak menyebut cara mengosongkan dropdown Division; spec menulis "Kosongkan Division".
  - TC-GS-USER-169 sampai 172 butir c ("`[Save]` tidak memproses form") tidak menyebut indikator selain form tidak diproses; spec memakai Popup tetap terbuka dan tidak ada toast sukses.
  - TC-GS-USER-172 tidak menyebut format 120 karakter Email yang valid; spec memakai 103 huruf `a` diikuti `@qwertysystem.net`.
- Spec melewati sekitar 35 langkah (63 langkah) karena memuat satu kelas (validasi form Edit), satu layar, satu user seed, satu pembukaan form yang dipakai bersama, dan tiap blok validasi berdiri sendiri (kegagalan satu blok field tidak membuat blok field lain kehilangan makna).
