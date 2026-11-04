---
id: TC-FA-LBL-E2E-007-role-independensi-gerbang-katalog-dan-penugasan-label
title: "Role: independensi gerbang katalog label dan penugasan label pada aset"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB-LOGIC-05a
  - FALB-LOGIC-05b
coverage:
  web: automated
---

# Role: independensi gerbang katalog label dan penugasan label pada aset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: `DU-19` (Manage Asset Master Data dengan Permission Create, Update, dan Delete, tanpa Permission Update pada "Manage Asset & TAG"), env `FA_AMDCRUD_EMAIL` dan `FA_AMDCRUD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun kedua: `DU-20` (Permission Update pada "Manage Asset & TAG" tanpa "Manage Asset Master Data", cakupan group hanya group pertama), env `FA_ATUPD_EMAIL` dan `FA_ATUPD_PASSWORD`, dipakai setelah ganti akun eksplisit (langkah 6). Hook `after` mengembalikan sesi ke `DU-01`.
- Data uji: `DU-18` (label seed milik spec, bersuffix `{runId}-007`, dibuat lewat API di hook `before`, dihapus di hook `after`); `DU-21` (satu aset Active milik spec di group pertama, dalam cakupan `DU-20`, dibuat lewat API di hook `before`, tanpa label, dihapus di hook `after`); `DU-46` (group, departemen, dan divisi kedua, di luar cakupan `DU-20`); `DU-48` (satu aset Active milik spec di group kedua `DU-46`, tanpa label, dibuat lewat API di hook `before`, dihapus di hook `after`).
- Kemampuan teknis: sesi API aktor (termasuk sesi API akun `DU-20`, token tidak dihitung sebagai sesi web) dan fixture BE untuk seeding label dan aset, klien HTTP untuk request langsung ke server, disediakan tim FE/BE. Halaman Asset List dan Asset Detail serta endpoint penugasan label dimiliki modul `asset/`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB-LOGIC-05a: Gerbang Global Role "Manage Asset Master Data" atas katalog Labels

1. Ketik Search `DU-18`, tekan Enter
2. Verifikasi baris label `DU-18` tampil pada Labels List
3. Verifikasi tombol `[+ Label]` tampil pada Table Tools
4. Klik `[⋯]` pada baris label `DU-18`
5. Verifikasi aksi `Edit` dan `Delete` tampil pada menu `[⋯]`
6. Ganti akun: logout, lalu login dengan akun `DU-20`
7. Buka Fixed Asset > Settings > Asset Master
8. Verifikasi tab `Labels` tidak tampil pada halaman Settings > Asset Master yang termuat

### FALB-LOGIC-05b: Penugasan dan pelepasan label pada aset dinaungi independen oleh Permission Update "Manage Asset & TAG" dalam cakupan group aset

9. Buka Asset Detail aset `DU-21` dari Asset List modul `asset/`
10. Pilih label `DU-18` dari dropdown label pada Asset Detail
11. Verifikasi chip label `DU-18` tampil pada Asset Detail aset `DU-21`
12. Klik `[✕]` pada chip label `DU-18`
13. Verifikasi nama aset `DU-21` tampil pada Asset Detail
14. Verifikasi chip label `DU-18` tidak tampil pada Asset Detail aset `DU-21`
15. Kirim request langsung penugasan label `DU-18` ke aset `DU-48` (group kedua `DU-46`) dengan sesi API `DU-20`
16. Verifikasi respons server menolak request
17. Verifikasi lewat fixture BE aset `DU-48` tidak memiliki relasi dengan label `DU-18`

## Notes

- Langkah penghubung: Search `DU-18` (langkah 1) menemukan baris target di Labels List; klik `[⋯]` membuka menu baris; langkah 6 adalah ganti akun eksplisit tanpa `Verifikasi`; langkah 7 dan 9 adalah navigasi umum.
- Anchor absence: baris label `DU-18` tampil (langkah 2) dan tab Settings > Asset Master dimuat sesudah langkah 7 menjadi anchor permukaan untuk tab `Labels` (langkah 8); nama aset `DU-21` tampil (langkah 13) mendahului asersi chip tidak tampil (langkah 14); chip `DU-18` tampil pada aset `DU-21` (langkah 11) membuktikan penugasan dalam cakupan group berhasil sebelum penolakan lintas group (langkah 16 dan 17).
- Pembagian klausa lintas spec: `FALB-LOGIC-05a` dikutip spec 005, 006, dan 007. Spec 005 mengasersi penolakan server Read Only, spec 006 mengasersi visibilitas per role, dan spec ini mengasersi bahwa `DU-19` memiliki aksi katalog dan `DU-20` tidak memiliki tab `Labels`.
- Pembagian klausa lintas spec: `FALB-LOGIC-05b` hanya dikutip spec ini; klausa "dalam cakupan group aset tersebut" diasersi lewat request langsung `DU-20` ke aset group kedua (langkah 15 sampai 17), perilaku FE untuk respons itu tidak diasersi (bagian 8b butir 1).
- Temuan PRD: PRD tidak menyatakan state kontrol penugasan label (Hidden atau Disabled) pada Asset Detail bagi pengguna tanpa Permission Update pada "Manage Asset & TAG", sehingga klausa "tanpa Update tidak dapat menugaskan atau melepas" `FALB-LOGIC-05b` tidak diasersi dengan akun `DU-19`.
- Temuan PRD: PRD tidak menyatakan apa yang tampil bila role tanpa "Manage Asset Master Data" membuka Settings > Asset Master dan tidak menyatakan elemen yang pasti tampil di halaman itu (tab `Asset Name` juga dinaungi "Manage Asset Master Data"), sehingga asersi tab `Labels` tidak tampil (langkah 8, `FALB-LOGIC-05a`) tidak punya anchor positif yang dinyatakan PRD; asersi tetap dipertahankan.
