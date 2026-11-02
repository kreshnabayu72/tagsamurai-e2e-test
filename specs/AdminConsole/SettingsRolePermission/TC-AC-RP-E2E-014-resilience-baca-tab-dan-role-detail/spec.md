---
id: TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail
title: "Resilience Baca: Loading dan Error Load Tab Total Control dan Role Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-56
  - TC-AC-RP-57
  - TC-AC-RP-58
  - TC-AC-RP-59
coverage:
  web: automated
---

# Resilience Baca: Loading dan Error Load Tab Total Control dan Role Detail

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; sebagian respons pengambilan data dipaksa lewat `Spectra.intercept()`, dan data Pre-setup dari backend nyata diasersi setelah intercept dilepas).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13 (pemegang tingkat akses), #23 (failure injection lewat intercept respons jaringan). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`):
  - TC-AC-RP-56: menahan respons pengambilan data Tab Total Control (penundaan respons).
  - TC-AC-RP-57: respons pengambilan data Tab Total Control dipaksa server error 5xx (500), lalu dilepas sebelum `[Try Again]`.
  - TC-AC-RP-58: menahan respons pengambilan data Role Detail (penundaan respons).
  - TC-AC-RP-59: respons pengambilan data Role Detail dipaksa server error 5xx (500), lalu dilepas sebelum `[Try Again]`.
  Endpoint yang dipanggil halaman tidak didefinisikan di TC; pemetaan intercept ke endpoint disediakan tim FE. Semua intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Spec tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-56: Loading state saat data Tab Total Control diambil

1. Tahan respons pengambilan data Tab Total Control (penundaan respons)
2. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
3. Verifikasi area tabel menampilkan Loading component selama respons tertunda
4. Lepaskan respons yang ditahan
5. Verifikasi Loading component hilang
6. Verifikasi baris Tab Total Control tampil

### TC-AC-RP-57: Error load Tab Total Control menampilkan pesan dan Try Again

7. Atur respons pengambilan data Tab Total Control menjadi server error 5xx
8. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
9. Verifikasi area tabel menampilkan "Unable to load this data."
10. Verifikasi area tabel menampilkan tombol `[Try Again]`
11. Verifikasi empty state tidak tampil
12. Lepas intercept respons 5xx
13. Klik `[Try Again]`
14. Verifikasi baris Tab Total Control tampil
15. Verifikasi pesan "Unable to load this data." hilang

### TC-AC-RP-58: Loading state saat data Role Detail diambil

16. Klik tab `System`
17. Tahan respons pengambilan data Role Detail (penundaan respons)
18. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
19. Verifikasi area tabel menampilkan Loading component selama respons tertunda
20. Lepaskan respons yang ditahan
21. Verifikasi Loading component hilang
22. Verifikasi baris tabel Role Detail `Manage language` tampil

### TC-AC-RP-59: Error load Role Detail menampilkan pesan dan Try Again

23. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
24. Atur respons pengambilan data Role Detail menjadi server error 5xx
25. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
26. Verifikasi area tabel menampilkan "Unable to load this data."
27. Verifikasi area tabel menampilkan tombol `[Try Again]`
28. Verifikasi empty state tidak tampil
29. Lepas intercept respons 5xx
30. Klik `[Try Again]`
31. Verifikasi baris tabel Role Detail `Manage language` tampil
32. Verifikasi pesan "Unable to load this data." hilang

## Notes

- Mode: FE+BE (intercept parsial di atas backend nyata). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness b (fault injection / resilience); satu spec untuk dua permukaan baca (Tab Total Control dan Role Detail) sesuai konvensi bagian 3 prinsip 13.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): mengatur, menahan, dan melepas intercept; membuka halaman lewat menu Settings pada TC-AC-RP-56 dan TC-AC-RP-57 karena intercept harus aktif sebelum halaman diminta; klik segmen "System" pada Breadcrumb mengembalikan Tab System sebelum TC-AC-RP-59.
- Intercept dilepas segera setelah pemicu selesai (S-09); langkah "Lepas intercept" pada TC-AC-RP-57 dan TC-AC-RP-59 mengikuti Langkah Uji "Nonaktifkan failure injection lalu klik `[Try Again]`".
- Asersi Loading component diletakkan sebelum respons dilepas (8b butir 5); asersi "Loading hilang" sesudah respons dilepas dan didahului anchor berupa baris tampil sesudahnya.
- Temuan untuk QA:
  - TC-AC-RP-57 dan TC-AC-RP-59 menyebut "failure injection 5xx" tanpa kode status tertentu; spec memakai 500.
  - TC-AC-RP-56 dan TC-AC-RP-58 tidak menyatakan lama penundaan respons; spec menahan respons sampai dilepas eksplisit.
  - Endpoint pengambilan data Tab Total Control dan Role Detail tidak disebut TC; pemetaan intercept ke endpoint disediakan tim FE (S-13).
