---
id: TC-AC-DN-E2E-027-role-matrix-positif-create-edit-per-capability
title: "Role Matrix Positif: Create dan Edit Berhasil per Capability"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-70
  - TC-AC-DN-107
  - TC-AC-DN-71
  - TC-AC-DN-161
coverage:
  web: automated
---

# Role Matrix Positif: Create dan Edit Berhasil per Capability

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Create-Only (Manage device master data: Create + Read) (Pre-setup #4); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #4 | Create-Only (Manage device master data: Create + Read) | (tanpa nama di TC) | `manageDeviceC_automated_{namaCompany}@qwertysystem.net` | `akunCreateOnly` | `Spectra.env.AC_DN_CREATE_PASSWORD` | TC-AC-DN-70, TC-AC-DN-107 |
| #5 | Update-Only (Manage device master data: Update + Read) | (tanpa nama di TC) | `manageDeviceU_automated_{namaCompany}@qwertysystem.net` | `akunUpdateOnly` | `Spectra.env.AC_DN_UPDATE_PASSWORD` | TC-AC-DN-71, TC-AC-DN-161 |

- Env var password: `Spectra.env.AC_DN_CREATE_PASSWORD`, `Spectra.env.AC_DN_UPDATE_PASSWORD`. `AC_DN_CREATE_PASSWORD`, `AC_DN_UPDATE_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Measurement Principal `Unit` (#13) dan Pohon Uji Kategori (#14) dibaca saja; Device Name inti (#16) tidak dipakai sebagai target tulis.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before` (disediakan tim FE/BE): `Door Antenna {runId}-027` dan `Door Antenna Dua {runId}-027` (Category `Antenna`, Measurement `Unit`) sebagai target Edit TC-AC-DN-71 dan TC-AC-DN-161.
- Data Dinamis yang dibuat langkah Create: `Wireless Gateway {runId}-027` dan `Create Only Antenna {runId}-027` (Category `Antenna`, Measurement `Unit`). Hasil Edit: `Door Antenna {runId}-027` menjadi `Door Antenna Pro {runId}-027` dan `Door Antenna Dua {runId}-027` menjadi `Door Update Only {runId}-027`. Hook `after` menghapus keempat record milik spec (`Wireless Gateway {runId}-027`, `Create Only Antenna {runId}-027`, `Door Antenna Pro {runId}-027`, `Door Update Only {runId}-027`) lewat fixture backend.

## Test Steps

### TC-AC-DN-70: Create-Only membuat Device Name baru sampai berhasil

1. Klik `[+ Device Name]`
2. Ketik `Wireless Gateway {runId}-027` pada field `Device Name` (placeholder "Enter device name")
3. Pilih `Unit` pada field `Measurement` (placeholder "Select measurement")
4. Pilih leaf `Antenna` pada field `Category` (placeholder "Select category")
5. Klik `[Submit]`
6. Verifikasi toast sukses: "Success, device name has been created."
7. Verifikasi popup form Create tertutup
8. Klik ikon Search, ketik Search `Wireless Gateway {runId}-027`, tekan Enter
9. Verifikasi hasil pencarian menampilkan baris `Wireless Gateway {runId}-027`
10. Verifikasi baris `Wireless Gateway {runId}-027` menampilkan Category `Antenna`
11. Verifikasi baris `Wireless Gateway {runId}-027` menampilkan Measurement `Unit`
12. Klik `(←)` pada kotak Search

### TC-AC-DN-107: Aktor Create-Only menyelesaikan Create Device Name sampai sukses

13. Klik tombol `+ Device Name` pada toolbar
14. Ketik `Create Only Antenna {runId}-027` pada field Device Name
15. Klik field Measurement lalu pilih `Unit`
16. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
17. Klik `[Submit]`
18. Verifikasi toast sukses: "Success, device name has been created."
19. Ketik Search `Create Only Antenna {runId}-027`, tekan Enter
20. Verifikasi List memuat baris `Create Only Antenna {runId}-027`
21. Klik `(←)` pada kotak Search

### TC-AC-DN-71: Update-Only mengubah nama Device Name sampai berhasil

22. Logout dari akun Create-Only
23. Login sebagai Update-Only (`Fixture.settings-device-name.akunUpdateOnly`, password dari `Spectra.env.AC_DN_UPDATE_PASSWORD`)
24. Buka halaman `Settings > Device > Device Name`
25. Ketik Search `Door Antenna {runId}-027`, tekan Enter
26. Klik ikon `⋯` pada baris `Door Antenna {runId}-027` lalu pilih `Edit`
27. Ubah nilai field `Device Name` menjadi `Door Antenna Pro {runId}-027`
28. Klik `[Save]`
29. Verifikasi toast sukses: "Success, device name has been updated."
30. Verifikasi popup form Edit tertutup
31. Ganti isi kotak search dengan `Door Antenna Pro {runId}-027`, tekan Enter
32. Verifikasi baris pada List menampilkan Device Name `Door Antenna Pro {runId}-027`
33. Verifikasi baris `Door Antenna Pro {runId}-027` menampilkan Category `Antenna`
34. Verifikasi baris `Door Antenna Pro {runId}-027` menampilkan Measurement `Unit`
35. Klik `(←)` pada kotak Search

### TC-AC-DN-161: Aktor Update-Only menyelesaikan Edit Device Name sampai sukses

36. Ketik Search `Door Antenna Dua {runId}-027`, tekan Enter
37. Buka menu aksi pada baris `Door Antenna Dua {runId}-027` lalu klik `Edit`
38. Kosongkan field Device Name lalu ketik `Door Update Only {runId}-027`
39. Klik `[Save]`
40. Verifikasi toast sukses: "Success, device name has been updated."
41. Ganti isi kotak search dengan `Door Update Only {runId}-027`, tekan Enter
42. Verifikasi List memuat baris `Door Update Only {runId}-027`
43. Klik `(←)` pada kotak Search

## Notes

- Spec Role Matrix positif (bagian 3a konvensi): aksi Create dan Edit berhasil oleh role yang berhak. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan data (S-06): target Edit TC-AC-DN-71 dan TC-AC-DN-161 (`Door Antenna` Pre-setup #16 di TC) diganti record milik spec bersuffix; nama hasil Edit mengikuti nilai TC dengan suffix. Kata kunci Search TC-AC-DN-70 ("Wireless") diganti nama lengkap bersuffix agar baris milik spec yang ditemukan.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16) pada langkah 25, 36, dan 19; mengosongkan Search lewat `(←)`; ganti akun eksplisit dan langkah "Buka halaman" setelah login (langkah 1 tidak login karena akun Create-Only login di hook `before`, S-07).
- Ukuran spec (43 langkah, di atas 35 langkah): dua blok role berdiri sendiri (Create-Only lalu Update-Only dengan ganti akun eksplisit), tiap Expected menjadi Verifikasi sendiri (S-01), satu kelas fungsional.
- Temuan untuk QA:
  - TC-AC-DN-70 dan TC-AC-DN-107 (Create-Only) serta TC-AC-DN-71 dan TC-AC-DN-161 (Update-Only) memiliki alur dan Expected yang tumpang tindih; tiap TC tetap satu spec.
