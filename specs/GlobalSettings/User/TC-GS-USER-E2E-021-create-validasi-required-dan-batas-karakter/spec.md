---
id: TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter
title: "Create User: Validasi Required dan Batas 120 Karakter First Name, Last Name, Employee ID, dan Email"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-91
  - TC-GS-USER-92
  - TC-GS-USER-93
  - TC-GS-USER-94
  - TC-GS-USER-95
  - TC-GS-USER-96
  - TC-GS-USER-97
  - TC-GS-USER-98
  - TC-GS-USER-99
  - TC-GS-USER-100
coverage:
  web: automated
---

# Create User: Validasi Required dan Batas 120 Karakter First Name, Last Name, Employee ID, dan Email

## Prerequisites

- Mode: mock.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). Pada mode mock, status flag ini disajikan oleh data mock yang disediakan tim FE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Pada mode mock, sesi login Total Control disajikan oleh mock; password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (akun default suite; didaftarkan di `executionConfig.environmentVariables`).
- Kebutuhan mock: seluruh API di-mock (spec dijalankan tim FE sebagai integration test tanpa backend nyata). API yang di-mock mengacu `global-settings/user/API/user-crud.yaml` (API pendukung disediakan tim FE):
  | method path (yaml:baris) | respons dipaksa |
  |---|---|
  | `POST /v2/iam/users/check-availability` (277) | jawaban V-07/V-08: "belum dipakai" untuk semua nilai yang diketik spec |
  | `POST /v2/iam/users` (334) | Create; dipantau, nol request diterima |

  Sumber opsi dropdown Division, Access, dan Custom Field form Create disediakan tim FE, sesuai data yang disajikan mock di bawah.

  Data yang disajikan mock:
  - Opsi dropdown Division memuat `Finance`.
  - Opsi Access memuat `Fixed Asset`, `Global Settings`, dan `Supply Asset`.
  - Custom Field user disajikan tanpa field Required (TC tidak mengisi Custom Field).
  - Pengecekan duplikat Email dan Employee ID (V-07 dan V-08 di PRD) dijawab "belum dipakai" untuk semua nilai yang diketik spec.
  - Mock mencatat setiap request yang diterima; dipakai untuk Verifikasi "user tidak dibuat" dan "`[Submit]` tidak memproses form" (tidak ada request pembuatan user yang diterima).
- Data Dinamis: tidak ada; seluruh `[Submit]` diblokir validasi FE dan tidak ada data tercipta. Nilai yang diketik memakai nilai TC apa adanya karena tidak ada data yang disimpan.
- Data karakter batas: 120 karakter berupa huruf `a` berulang; untuk Email, 103 huruf `a` diikuti `@qwertysystem.net` (total 120 karakter, format valid); karakter ke-121 berupa satu huruf `a` yang diketik di akhir nilai.
- State global yang diubah: tidak ada.
- Kemampuan teknis: mengetik 120 dan 121 karakter pada satu field; mock mencatat request masuk.

## Test Steps

### Pembukaan Popup

1. Klik `[+ User]` di Table Tools

### TC-GS-USER-96: Semua field wajib kosong memunculkan seluruh error required sekaligus

2. Klik `[Submit]` langsung tanpa mengisi apa pun
3. Verifikasi inline error di bawah First Name: `First name must not be empty`
4. Verifikasi inline error di bawah Last Name: `Last name must not be empty`
5. Verifikasi inline error di bawah Division: `Division must not be empty`
6. Verifikasi inline error di bawah Email: `Email must not be empty`
7. Verifikasi inline error di bawah Access: `Access must not be empty`
8. Klik `✕` di header Popup
9. Klik `[+ User]` di Table Tools

### TC-GS-USER-91: First Name kosong

10. Isi Last Name `Santoso`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset` (First Name dikosongkan)
11. Klik `[Submit]`
12. Verifikasi inline error di bawah First Name: `First name must not be empty`
13. Verifikasi Popup tetap terbuka
14. Verifikasi user tidak dibuat: API mock tidak menerima request pembuatan user
15. Verifikasi tidak ada toast

### TC-GS-USER-92: Last Name kosong

16. Klik `[Clear Field]`
17. Isi First Name `Budi`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset` (Last Name dikosongkan)
18. Klik `[Submit]`
19. Verifikasi inline error di bawah Last Name: `Last name must not be empty`
20. Verifikasi Popup tetap terbuka
21. Verifikasi user tidak dibuat: API mock tidak menerima request pembuatan user
22. Verifikasi tidak ada toast

### TC-GS-USER-93: Email kosong

23. Klik `[Clear Field]`
24. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, pilih Access `Fixed Asset` (Email dikosongkan)
25. Klik `[Submit]`
26. Verifikasi inline error di bawah Email: `Email must not be empty`
27. Verifikasi Popup tetap terbuka
28. Verifikasi user tidak dibuat: API mock tidak menerima request pembuatan user
29. Verifikasi tidak ada toast

### TC-GS-USER-94: Division kosong

30. Klik `[Clear Field]`
31. Isi First Name `Budi`, Last Name `Santoso`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset` (Division dikosongkan)
32. Klik `[Submit]`
33. Verifikasi inline error di bawah Division: `Division must not be empty`
34. Verifikasi Popup tetap terbuka
35. Verifikasi user tidak dibuat: API mock tidak menerima request pembuatan user
36. Verifikasi tidak ada toast

### TC-GS-USER-95: Access kosong

37. Klik `[Clear Field]`
38. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso@qwertysystem.net` (Access tidak dipilih)
39. Klik `[Submit]`
40. Verifikasi inline error di bawah Access: `Access must not be empty`
41. Verifikasi Popup tetap terbuka
42. Verifikasi user tidak dibuat: API mock tidak menerima request pembuatan user
43. Verifikasi tidak ada toast

### TC-GS-USER-97: First Name 121 karakter

44. Klik `[Clear Field]`
45. Isi Last Name `Santoso`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset`
46. Ketik 120 karakter di First Name
47. Verifikasi tidak ada error di bawah First Name
48. Ketik 1 karakter lagi di First Name (121 karakter)
49. Verifikasi inline error di bawah First Name: `Max. 120 characters` muncul langsung tanpa `[Submit]`
50. Klik `[Submit]`
51. Verifikasi `[Submit]` tidak memproses form: API mock tidak menerima request pembuatan user

### TC-GS-USER-98: Last Name 121 karakter

52. Klik `[Clear Field]`
53. Isi First Name `Budi`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset`
54. Ketik 120 karakter di Last Name
55. Verifikasi tidak ada error di bawah Last Name
56. Ketik 1 karakter lagi di Last Name (121 karakter)
57. Verifikasi inline error di bawah Last Name: `Max. 120 characters` muncul langsung tanpa `[Submit]`
58. Klik `[Submit]`
59. Verifikasi `[Submit]` tidak memproses form: API mock tidak menerima request pembuatan user

### TC-GS-USER-99: Employee ID 121 karakter

60. Klik `[Clear Field]`
61. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset`
62. Ketik 120 karakter di Employee ID
63. Verifikasi tidak ada error di bawah Employee ID
64. Ketik 1 karakter lagi di Employee ID (121 karakter)
65. Verifikasi inline error di bawah Employee ID: `Max. 120 characters` muncul langsung tanpa `[Submit]`
66. Klik `[Submit]`
67. Verifikasi `[Submit]` tidak memproses form: API mock tidak menerima request pembuatan user

### TC-GS-USER-100: Email 121 karakter

68. Klik `[Clear Field]`
69. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, pilih Access `Fixed Asset`
70. Ketik Email 120 karakter berformat valid
71. Verifikasi tidak ada error di bawah Email
72. Ketik 1 karakter lagi di Email (121 karakter)
73. Verifikasi inline error di bawah Email: `Max. 120 characters` muncul langsung tanpa `[Submit]`
74. Klik `[Submit]`
75. Verifikasi `[Submit]` tidak memproses form: API mock tidak menerima request pembuatan user

### Penutup

76. Klik `✕` di header Popup
77. Verifikasi dialog `Unsaved Changes` tampil
78. Klik `[Leave]`

## Notes

- Mode: mock. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: TC-GS-USER-96, 91, 92, 93, 94, 95, 97, 98, 99, 100. TC-GS-USER-96 (semua field kosong) dikerjakan pertama pada Popup yang masih bersih, lalu Popup ditutup dan dibuka ulang, supaya error required dari TC-GS-USER-96 tidak tersisa dan membuat Verifikasi error TC-GS-USER-91 sampai 95 lolos karena sisa error. TC-GS-USER-91 sampai 95 berurutan sebagai kasus required satu field, lalu kasus batas karakter.
- Spec melewati sekitar 35 langkah (78 langkah) karena seluruh blok berada di satu kelas harness (validasi field Create tanpa data tercipta), memakai satu layar dan satu pembukaan Popup dengan field dikosongkan lewat `[Clear Field]` di antara kasus (prinsip 13, halaman yang dipakai berulang), dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah besar karena Expected dipecah per klausa (S-01).
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): `✕` dan `[+ User]` sesudah TC-GS-USER-96 (Popup kosong tidak dirty, tidak ada dialog); `[Clear Field]` di awal tiap blok sesudah TC-GS-USER-91; pengisian field wajib lain pada TC-GS-USER-97 sampai 100 supaya satu-satunya penyebab penolakan adalah error batas karakter.
- Penutup Popup memakai alur form dirty deterministik (`✕`, dialog `Unsaved Changes`, `[Leave]`) sesuai S-08. Verifikasi dialog di langkah penutup bukan dari Expected TC dan merupakan prosedur penutupan form dirty (S-08).
- Kasus TC-GS-USER-91 sampai 95 masing-masing mengosongkan field yang berbeda, sehingga error sisa dari kasus sebelumnya tidak menjadi satu-satunya bukti Verifikasi.
- Temuan untuk QA:
  - Access pada Create adalah multi dropdown (placeholder `Select access`, TC-GS-USER-88); TC-GS-USER-91 sampai 100 menulis "centang Access" dan "Access tidak dicentang"; spec memakai "pilih Access" dan "Access tidak dipilih".
  - TC-GS-USER-91 sampai 95 menyebut "Tidak ada toast" dan "user tidak dibuat" tanpa menyebut cara memeriksa user tidak dibuat pada mode mock; spec memakai pencatatan request di mock (disediakan tim FE).
  - TC-GS-USER-97 sampai 100 menyebut "`[Submit]` tidak memproses form" tanpa Data Uji field wajib lain; spec mengisi field wajib lain dengan nilai valid supaya Verifikasi bermakna.
  - TC-GS-USER-97 sampai 100 tidak menyebut karakter yang diketik; spec memakai huruf `a` berulang (Email: 103 huruf `a` + `@qwertysystem.net`).
  - TC-GS-USER-96 Expected tidak menyebut posisi error (di bawah field); spec mengikuti pola TC-GS-USER-91 sampai 95 (di bawah field).
  - Tabel Pre-setup No. 24 mendefinisikan Custom Field `Emergency Phone` sebagai Required, sedangkan TC-GS-USER-91 sampai 100 tidak mengisi Custom Field dan Expected TC-GS-USER-96 tidak memuat error `Emergency phone must not be empty`; pada mode mock, data Custom Field disajikan tanpa field Required (disediakan tim FE) dan spec hanya mengasersi error yang disebut TC.
  - Sumber opsi dropdown form tidak disebut di TC dan PRD; endpoint `POST /v2/iam/users/options` adalah opsi filter User List, bukan sumber dropdown form, sehingga tidak dipakai di spec ini dan sumber opsi disediakan tim FE (inferensi, diterima 2026-11-03; temuan sumber untuk pemilik PRD §4.1.3).
