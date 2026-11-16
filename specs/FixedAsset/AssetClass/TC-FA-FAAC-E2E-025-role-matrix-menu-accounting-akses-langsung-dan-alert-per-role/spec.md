---
id: TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role
title: "Role Matrix: Menu Accounting, Akses Langsung ke Tab Asset Class, dan Alert Dependensi Akun per Role"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-69
  - TC-FA-FAAC-70
  - TC-FA-FAAC-589
  - TC-FA-FAAC-682
  - TC-FA-FAAC-683
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#b2", "§3.10#p1", "§2.1#r4", "E-FAAC-79", "§4.1.8#p2", "F-FAAC-16.k2", "§4.8#r2", "FAAC-LOGIC-20b", "FI-15"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": 2
  "§2.1#r2": 4
  "§2.1#r5": [6, 8, 10, 12]
  "§2.1#b2": [6, 8, 10, 12]
  "§3.10#p1": [15, 18]
  "§2.1#r4": [15, 18]
  "E-FAAC-79": [21, 22, 25, 26]
  "§4.1.8#p2": [29, 35]
  "F-FAAC-16.k2": [29, 35]
  "§4.8#r2": [29, 30, 35, 36]
  "FAAC-LOGIC-20b": [30, 36]
  "FI-15": [32, 38]
anchor: [14, 17]
coverage:
  web: automated
---

# Role Matrix: Menu Accounting, Akses Langsung ke Tab Asset Class, dan Alert Dependensi Akun per Role

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-FAAC-69 |
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-69, TC-FA-FAAC-682 |
| Manage accounting (Read) | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_R_PASSWORD` | TC-FA-FAAC-69, TC-FA-FAAC-683 |
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-69 |
| Manage accounting (Read, Update) | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RU_PASSWORD` | TC-FA-FAAC-69 |
| Manage accounting (Read, Delete) | `manageAccountingReadDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RD_PASSWORD` | TC-FA-FAAC-69 |
| Group Manager | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_GM_PASSWORD` | TC-FA-FAAC-70, TC-FA-FAAC-589 |

- Env var: `FA_TC_PASSWORD`, `FA_AC_RO_PASSWORD`, `FA_AC_MA_R_PASSWORD`, `FA_AC_MA_RC_PASSWORD`, `FA_AC_MA_RU_PASSWORD`, `FA_AC_MA_RD_PASSWORD`, `FA_AC_GM_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: akun fixture di tabel Role yang diuji (dibaca, tidak diubah). Akun role lain tanpa capability Manage accounting untuk TC-FA-FAAC-70 dan TC-FA-FAAC-589 tidak ada di Tabel Data Uji Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA).
- Data untuk TC-FA-FAAC-682 dan TC-FA-FAAC-683: Chart of Accounts tidak memiliki akun Active ber-Account Function Asset Cost; akun Active untuk Accumulated Depreciation dan Depreciation Expense tersedia (seed Pre-setup, disediakan tim FE/BE lewat fixture BE).
- State global yang diubah: Chart of Accounts (akun Active Asset Cost dikosongkan oleh fixture BE di hook `before`, dipulihkan di hook `after`) dan flag Guided Tooltip (dipulihkan hook suite). Spec ini menyatakan suite serial.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: ganti akun (logout lalu login), mengetik URL langsung di address bar, membaca toast, fixture BE untuk Chart of Accounts.

## Test Steps

### TC-FA-FAAC-69

1. Lihat sidebar
2. Verifikasi item Accounting tampil (Total Control)
3. Ganti akun: logout, lalu login sebagai Read Only
4. Verifikasi item Accounting tampil (Read Only)
5. Ganti akun: logout, lalu login sebagai Manage accounting (Read)
6. Verifikasi item Accounting tampil (Manage accounting (Read))
7. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Create)
8. Verifikasi item Accounting tampil (Manage accounting (Read, Create))
9. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Update)
10. Verifikasi item Accounting tampil (Manage accounting (Read, Update))
11. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Delete)
12. Verifikasi item Accounting tampil (Manage accounting (Read, Delete))

### TC-FA-FAAC-70

13. Ganti akun: logout, lalu login sebagai Group Manager
14. Verifikasi sedikitnya satu item menu lain pada sidebar tampil
15. Verifikasi item Accounting Hidden (tidak muncul di daftar menu) untuk Group Manager
16. Ganti akun: logout, lalu login sebagai role lain tanpa capability Manage accounting (akun disediakan tim FE)
17. Verifikasi sedikitnya satu item menu lain pada sidebar tampil
18. Verifikasi item Accounting Hidden (tidak muncul di daftar menu) untuk role lain tanpa Manage accounting

### TC-FA-FAAC-589

19. Ganti akun: logout, lalu login sebagai Group Manager
20. Ketik URL halaman Settings > Accounting tab Asset Class langsung di address bar, tekan Enter
21. Verifikasi toast error "You don't have permission to do this." tampil (Group Manager)
22. Verifikasi UI di-refresh sehingga halaman tab Asset Class tidak tampil (Group Manager)
23. Ganti akun: logout, lalu login sebagai role lain tanpa capability Manage accounting (akun disediakan tim FE)
24. Ketik URL halaman Settings > Accounting tab Asset Class langsung di address bar, tekan Enter
25. Verifikasi toast error "You don't have permission to do this." tampil (role lain tanpa Manage accounting)
26. Verifikasi UI di-refresh sehingga halaman tab Asset Class tidak tampil (role lain tanpa Manage accounting)

### TC-FA-FAAC-682

27. Ganti akun: logout, lalu login sebagai Read Only
28. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
29. Verifikasi Alert warning "No active account for Asset Cost in Chart of Accounts. Add one so asset classes can map their accounts." tampil di atas tabel: Show
30. Verifikasi link [Go to Chart of Accounts] pada Alert: Show
31. Klik link [Go to Chart of Accounts] pada Alert
32. Verifikasi tab Chart of Accounts aktif pada halaman Settings > Accounting

### TC-FA-FAAC-683

33. Ganti akun: logout, lalu login sebagai Manage accounting (Read)
34. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
35. Verifikasi Alert warning "No active account for Asset Cost in Chart of Accounts. Add one so asset classes can map their accounts." tampil di atas tabel: Show
36. Verifikasi link [Go to Chart of Accounts] pada Alert: Show
37. Klik link [Go to Chart of Accounts] pada Alert
38. Verifikasi tab Chart of Accounts aktif pada halaman Settings > Accounting

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, 16, 19, 23, 27, dan 33 (ganti akun, ditambah ganti akun pada TC-FA-FAAC-69), langkah 28 dan 34 (membuka tab Asset Class sesudah login ulang, S-07).
- Satu spec memuat topik menu Accounting, akses langsung, dan Alert dependensi akun per role dalam satu kelas (Role Matrix); polaritas positif (menu tampil, Alert tampil) dan negatif (menu Hidden, akses ditolak) dicampur karena ketiganya matriks visibilitas atau akses per role (bagian 3a).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas (Role Matrix) dan satu topik (akses per role ke Accounting), tiap blok role berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah ganti akun saja memakai 13 langkah.
- Asersi Hidden item Accounting didahului asersi sedikitnya satu item menu lain pada sidebar yang sama tampil sebagai anchor positif (bagian 8b butir 2). Asersi tab Asset Class tidak tampil pada TC-FA-FAAC-589 memakai toast error sebagai anchor positif.
- Chart of Accounts tanpa akun Active ber-Account Function Asset Cost adalah state yang disiapkan fixture BE di hook `before` dan berlaku sepanjang spec; state itu dipulihkan di hook `after` dan tidak memengaruhi asersi TC-FA-FAAC-69, TC-FA-FAAC-70, dan TC-FA-FAAC-589.
- Temuan untuk QA:
  - TC-FA-FAAC-70 dan TC-FA-FAAC-589 menyebut "role lain yang tidak memiliki capability Manage accounting" tanpa menyebut role atau akunnya, dan Tabel Data Uji Pre-setup tidak memuat akun itu; spec menulis "akun disediakan tim FE" (S-11, S-13) tanpa nama env.
  - TC-FA-FAAC-69 dan TC-FA-FAAC-70 tidak menyebut aplikasi atau halaman tempat sidebar dilihat; spec mengasersi sidebar yang tampil sesudah login dan tidak menambah langkah membuka halaman tertentu.
  - Item menu lain pada sidebar untuk anchor TC-FA-FAAC-70 tidak disebut TC; spec memakai asersi umum "sedikitnya satu item menu lain".
  - TC-FA-FAAC-69 dan TC-FA-FAAC-70 tidak menyebut langkah login sebagai Total Control; Total Control login di hook `before`.
