---
id: TC-FA-GRP-E2E-003-loading-state-dan-error-load-groups-list-try-again
title: "Loading State dan Error Load Groups List dengan [Try Again]"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-7
  - TC-FA-GRP-8
coverage:
  web: automated
---

# Loading State dan Error Load Groups List dengan [Try Again]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk (a) menahan respons request daftar group (TC-FA-GRP-7, menahan respons hanya untuk mengamati Loading) dan (b) memaksa respons 5xx pada request daftar group pertama (TC-FA-GRP-8). Intercept dilepas segera setelah pemicunya selesai dan dilepas di hook `after` bila spec gagal di tengah. Fixture BE dan sesi API aktor disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-7: Loading state Groups List

1. Tahan respons request daftar group dengan intercept
2. Muat ulang halaman Settings > Groups dengan F5
3. Verifikasi Loading component tampil di area tabel
4. Lepas tahanan respons
5. Verifikasi Loading component hilang dan baris data tampil setelah data diterima

### TC-FA-GRP-8: Error load Groups List dan [Try Again]

6. Paksa respons 5xx pada request daftar group pertama dengan intercept
7. Muat ulang halaman Settings > Groups dengan F5
8. Verifikasi area tabel menampilkan `Unable to load this data.` beserta tombol [Try Again]
9. Verifikasi area tabel bukan empty state
10. Lepas intercept agar endpoint pulih
11. Klik [Try Again]
12. Verifikasi tabel memuat ulang dan tampil normal dengan baris data

## Notes

- Langkah penghubung (S-03): langkah 10 (melepas intercept sebagai pemulihan endpoint, S-09).
- Muat ulang F5 menggantikan "Buka Fixed Asset > Settings > Groups" karena layar awal sudah dibuka hook `beforeEach` suite.
- P-5 (butir b): TC-FA-GRP-8 adalah satu kegagalan 5xx sebagai objek uji ringan yang berada bersama TC loading (TC-FA-GRP-7) pada permukaan yang sama.
- Temuan untuk QA:
  - TC-FA-GRP-7 menyebut "network throttle" tanpa mekanisme; spec memakai intercept penahan respons (disediakan tim FE).
  - TC-FA-GRP-8 menyebut "Endpoint list disimulasikan 5xx" tanpa nama endpoint; spec tidak menyebut endpoint (S-13).
