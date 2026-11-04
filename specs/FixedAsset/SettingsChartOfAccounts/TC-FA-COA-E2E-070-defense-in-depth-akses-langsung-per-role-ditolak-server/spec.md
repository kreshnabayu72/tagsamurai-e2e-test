---
id: TC-FA-COA-E2E-070-defense-in-depth-akses-langsung-per-role-ditolak-server
title: "Defense-in-Depth: Akses Langsung per Role Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-107
  - TC-FA-COA-108
  - TC-FA-COA-153
  - TC-FA-COA-269
  - TC-FA-COA-270
  - TC-FA-COA-271
coverage:
  web: automated
---

# Defense-in-Depth: Akses Langsung per Role Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI). Spec hanya mengasersi respons server dan state data (bagian 8b butir 1, `K-1`); asersi absence log tidak ada di spec ini (lihat Notes).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun UI: semua permintaan langsung memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Aktor permintaan langsung (sesi API aktor; email mengikuti tabel Pre-setup TC):

  | TC | Aktor | Email | Password |
  |---|---|---|---|
  | TC-FA-COA-107; TC-FA-COA-153 (permintaan sebagai Read Only) | Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
  | TC-FA-COA-108 | Manage accounting - Read | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_READ_PASSWORD` |
  | TC-FA-COA-153 (permintaan sebagai Group Manager) | Group Manager (tanpa Manage accounting) | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
  | TC-FA-COA-269 | Manage accounting - Create | `manageAccountingCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_CREATE_PASSWORD` |
  | TC-FA-COA-270 | Manage accounting - Update | `manageAccountingUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_UPDATE_PASSWORD` |
  | TC-FA-COA-271 | Manage accounting - Delete | `manageAccountingDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_DELETE_PASSWORD` |

- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_GM_PASSWORD`, `FA_MACC_READ_PASSWORD`, `FA_MACC_CREATE_PASSWORD`, `FA_MACC_UPDATE_PASSWORD`, dan `FA_MACC_DELETE_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE), pada client yang sama dengan akun aktor:
  - Akun target aktif: Code `DID070A`, Account Name `Akun Target Aktif {runId}-070`, Function Depreciation Expense, Active, Used By 0, belum pernah diekspor (padanan P1 pada TC-FA-COA-108, 269, 270, 271).
  - Akun target nonaktif: Code `DID070B`, Account Name `Akun Target Nonaktif {runId}-070`, Function Gain on Disposal, Inactive, Used By 0, belum pernah diekspor (padanan P3 pada TC-FA-COA-269, 270, 271).
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID070A` dan `DID070B` memuat nomor spec supaya unik per spec, sedangkan `5-6700`, `CAP-8300`, dan `CAP-8304` adalah nilai TC untuk permintaan Create yang selalu ditolak (tidak pernah tersimpan). `DID070A`, `DID070B`, `5-6700`, dan `CAP-8300` dibersihkan di hook `before` dan `after` (R-13); `CAP-8300` dan `CAP-8304` juga diketik spec 095 pada permintaan Create yang sama-sama selalu ditolak (Code hanya diketik pada Create yang tidak pernah tersimpan, pengecualian A-18), sehingga tidak bertabrakan; `CAP-8304` tidak dipakai data Pre-setup dan tidak pernah tersimpan sehingga tidak dibersihkan.
- Data Pre-setup yang hanya dibaca dan tidak diubah (TC-FA-COA-153): P1 `5-6001 - Depreciation Expense - Admin` dan P7 `4-7002 - Gain and Loss on Disposal` (Used By 2).
- Payload Create (TC-FA-COA-107, 270, 271) memakai Account Name bersuffix `{runId}-070` dan Function Depreciation Expense; TC hanya menyebut "Name valid, Function valid" (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (Create, Edit, Delete, Activate, Deactivate, baca daftar akun, baca daftar pemakai Used By, baca Changelog, Download) dengan sesi API aktor; pembacaan daftar akun dari server beserta Code, Account Name, Function, dan status.
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-107: Create oleh Read Only

1. Kirim permintaan Create akun Code `5-6700`, Account Name `Akun Bypass {runId}-070`, Function Depreciation Expense langsung ke server menggunakan sesi API aktor Read Only hingga respons diterima
2. Verifikasi respons server 403 (Forbidden)
3. Verifikasi daftar akun dari server memuat `DID070A`
4. Verifikasi daftar akun dari server tidak memuat akun Code `5-6700` (tidak ada akun dibuat)

### TC-FA-COA-108: Edit dan Delete oleh Manage accounting - Read

5. Kirim permintaan Edit Account Name `DID070A` menjadi `Akun Edit Bypass {runId}-070` langsung ke server menggunakan sesi API aktor Manage accounting - Read hingga respons diterima
6. Kirim permintaan Delete `DID070A` langsung ke server menggunakan sesi API aktor Manage accounting - Read hingga respons diterima
7. Verifikasi kedua permintaan pada langkah 5 dan 6 ditolak dengan 403
8. Verifikasi akun `DID070A` tidak berubah: Account Name tetap `Akun Target Aktif {runId}-070` dan akun masih ada pada daftar dari server

### TC-FA-COA-153: Permintaan baca langsung tanpa capability

9. Kirim permintaan baca daftar akun langsung ke server menggunakan sesi API aktor Group Manager hingga respons diterima
10. Kirim permintaan baca daftar pemakai (popup Used By) untuk akun P7 langsung ke server menggunakan sesi API aktor Group Manager hingga respons diterima
11. Kirim permintaan baca Changelog langsung ke server menggunakan sesi API aktor Group Manager hingga respons diterima
12. Kirim permintaan Download daftar akun langsung ke server menggunakan sesi API aktor Group Manager hingga respons diterima
13. Verifikasi keempat permintaan pada langkah 9 sampai 12 menerima respons 403 (Forbidden)
14. Verifikasi tidak ada data akun, daftar pemakai, riwayat, atau berkas yang dikembalikan pada keempat respons tersebut
15. Kirim permintaan baca daftar akun yang memuat akun P1 dan P7 langsung ke server menggunakan sesi API aktor Read Only hingga respons diterima
16. Kirim permintaan baca daftar pemakai (popup Used By) untuk akun P7 langsung ke server menggunakan sesi API aktor Read Only hingga respons diterima
17. Kirim permintaan baca Changelog langsung ke server menggunakan sesi API aktor Read Only hingga respons diterima
18. Kirim permintaan Download daftar akun langsung ke server menggunakan sesi API aktor Read Only hingga respons diterima
19. Verifikasi keempat permintaan pada langkah 15 sampai 18 diterima dan data dikembalikan (daftar akun memuat P1 dan P7, daftar pemakai P7, riwayat Changelog, dan berkas Download)

### TC-FA-COA-269: Manage accounting - Create

20. Kirim permintaan Edit Account Name `DID070A` menjadi `Akun Edit Bypass {runId}-070` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
21. Kirim permintaan Activate `DID070B` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
22. Kirim permintaan Deactivate `DID070A` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
23. Kirim permintaan Delete `DID070A` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
24. Verifikasi setiap permintaan pada langkah 20 sampai 23 ditolak server dengan 403

### TC-FA-COA-270: Manage accounting - Update

25. Kirim permintaan Create akun Code `CAP-8300`, Account Name `Akun Create {runId}-070`, Function Depreciation Expense langsung ke server menggunakan sesi API aktor Manage accounting - Update hingga respons diterima
26. Kirim permintaan Delete `DID070A` langsung ke server menggunakan sesi API aktor Manage accounting - Update hingga respons diterima
27. Verifikasi setiap permintaan pada langkah 25 dan 26 ditolak server dengan 403
28. Verifikasi daftar akun dari server memuat `DID070A`
29. Verifikasi daftar akun dari server tidak memuat akun Code `CAP-8300` (tidak dibuat)

### TC-FA-COA-271: Manage accounting - Delete

30. Kirim permintaan Create akun Code `CAP-8304`, Account Name `Akun Create {runId}-070`, Function Depreciation Expense langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
31. Kirim permintaan Edit Account Name `DID070A` menjadi `Akun Edit Bypass {runId}-070` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
32. Kirim permintaan Activate `DID070B` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
33. Kirim permintaan Deactivate `DID070A` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
34. Verifikasi setiap permintaan pada langkah 30 sampai 33 ditolak server dengan 403
35. Verifikasi daftar akun dari server memuat `DID070A`
36. Verifikasi daftar akun dari server tidak memuat akun Code `CAP-8304` (tidak dibuat)

## Notes

- `K-1`: TC-FA-COA-107, 108, 153, 269, 270, dan 271 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan kontrak API, karena TC granular tetap sumber.
- Tanpa langkah UI: semua aksi adalah permintaan langsung (bagian 8b butir 1), sehingga precondition TC-FA-COA-269, 270, 271 ("Login sbg Role" dan "User berada di ... tab `Chart of Accounts` aktif") dipenuhi oleh sesi API aktor, bukan login browser; tidak ada langkah Ganti akun; tiap langkah permintaan langsung menyebut sesi API aktornya secara eksplisit sehingga setara Step ganti akun (S-07).
- Spec melewati sekitar 35 langkah (36 langkah). Alasan: satu kelas harness (defense-in-depth per role) dan satu dataset; enam blok berdiri sendiri dengan aktor berbeda; Expected dipecah satu Verifikasi per butir (S-01) dan permintaan tiap TC disalin utuh; spec tidak dipecah lebih jauh.
- Langkah 3, 28, dan 35 memverifikasi `DID070A` pada daftar sebagai anchor positif sebelum asersi bahwa akun yang ditolak tidak dibuat (bagian 8b butir 2).
- TC memakai P1 dan P3 sebagai target tulis yang ditolak; spec memakai akun milik spec `DID070A` dan `DID070B` sebagai padanan (S-06) dengan state yang sama (Active dan Inactive, Used By 0, belum diekspor). P1 dan P7 hanya dibaca pada TC-FA-COA-153.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log" pada Post Condition TC-FA-COA-269, TC-FA-COA-270, dan TC-FA-COA-271 diasersi di spec 095, yang memuat permintaan langsung yang sama dengan baseline sendiri. Spec ini hanya mengasersi respons server dan state data.
- `A-18`: Account Code literal tanpa suffix menjadi objek asersi: `DID070A` (TC-FA-COA-107, 108, 270, 271: ada pada daftar akun dari server dan tidak berubah; langkah 3, 8, 28, 35), `5-6700` (TC-FA-COA-107: tidak ada akun dibuat; langkah 4), `CAP-8300` (TC-FA-COA-270; langkah 29), dan `CAP-8304` (TC-FA-COA-271; langkah 36). `DID070A` dan `DID070B` dibersihkan di hook `before` dan `after`; `5-6700`, `CAP-8300`, dan `CAP-8304` hanya diketik pada Create yang selalu ditolak 403 dan tidak pernah tersimpan.
- Temuan untuk QA:
  - TC-FA-COA-107 menyebut "Name valid, Function valid" tanpa nilai; spec memakai Account Name bersuffix `{runId}-070` dan Function Depreciation Expense.
  - TC-FA-COA-108, 269, dan 271 tidak menyebut payload Edit (Account Name baru); spec memakai `Akun Edit Bypass {runId}-070`.
  - TC-FA-COA-269, 270, 271: Post Condition "Data akun P1 dan P3 tidak berubah dan tidak ada log" tidak punya Expected padanan sehingga "data tidak berubah" tidak diasersi (S-01); khusus TC-FA-COA-269 tidak ada asersi state sesudah penolakan. Perlu butir Expected "data tidak berubah" bila state ingin dijaga. Klausa "tidak ada log" diasersi di spec 095.
  - TC-FA-COA-107 dan 108 ("Tidak ada akun dibuat", "P1 tidak berubah") butuh pembacaan state dari server; kemampuan disediakan tim FE/BE.
  - TC-FA-COA-153 langkah 5 hanya menyebut "diterima dan data dikembalikan"; spec mengasersi isi yang dikembalikan per jenis permintaan sesuai Expected c.
