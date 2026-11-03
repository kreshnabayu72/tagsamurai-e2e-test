---
id: TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access
title: Masking Assigned Clients per Baris Group Role - Zero Access, Read Only, CRUD, dan Hak Parsial
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-99
  - TC-AC-PF-100
  - TC-AC-PF-101
  - TC-AC-PF-102
  - TC-AC-PF-103
  - TC-AC-PF-106
coverage:
  web: automated
---

# Masking Assigned Clients per Baris Group Role - Zero Access, Read Only, CRUD, dan Hak Parsial

## Prerequisites

- Mode: FE+BE
- Akun aktor: #8 `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` (Manage plans & licensing: Read dan Update; Group Role Manage active client: CRUD pada group client pemakai plan `Growth` kecuali Read Only pada group PT Bumi Sentosa, Zero Access pada group PT Timur Jaya dan PT Zona Nol, Read + Create pada group PT Hak Parsial Satu, Read + Delete pada group PT Hak Parsial Dua; password dari env `AC_PF_GM_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan D (`Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5, PT Wahana Nusantara Active v1 eligible, PT Karya Abadi Active v1 delta downgrade, PT Cahaya Mandiri Grace v5, PT Bumi Sentosa Active v1 Read Only, PT Timur Jaya Active v1 Zero Access, PT Zona Nol Active v5 Zero Access, PT Hak Parsial Satu Active v1, PT Hak Parsial Dua Active v1; kolom Clients list `Growth` bernilai 9). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup, capability dan Group Role) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-99: seluruh baris Assigned Clients dan kolom Clients

1. Verifikasi kolom Clients baris `Growth` pada list bernilai `9`.
2. Buka Plan Detail `Growth` (klik Plan Name).
3. Klik Tab Assigned Clients.
4. Verifikasi Tab Assigned Clients menampilkan kesembilan baris.

### TC-AC-PF-100: Zero Access pada PT Timur Jaya

5. Verifikasi Client Name `PT Timur Jaya` tampil sebagai teks statis (bukan link).
6. Buka Overlay Row Action pada `PT Timur Jaya`.
7. Verifikasi opsi `Detail` tampil tetapi Disabled.
8. Hover opsi `Detail`.
9. Verifikasi tooltip "You do not have permission to view or manage clients in this group."
10. Verifikasi opsi `Push Update` tampil tetapi Disabled.
11. Hover opsi `Push Update`.
12. Verifikasi tooltip "You do not have permission to view or manage clients in this group."

### TC-AC-PF-101: Zero Access dengan Push Update tidak memenuhi syarat bisnis

13. Buka Overlay Row Action pada `PT Zona Nol`.
14. Hover opsi `Detail` yang Disabled.
15. Verifikasi opsi `Detail` Disabled dengan tooltip "You do not have permission to view or manage clients in this group."
16. Verifikasi opsi `Push Update` tidak ada (Hidden) karena client sudah versi terbaru.

### TC-AC-PF-102: Read Only pada PT Bumi Sentosa

17. Verifikasi Client Name `PT Bumi Sentosa` berupa link aktif.
18. Buka Overlay Row Action pada `PT Bumi Sentosa`.
19. Verifikasi Overlay Row Action memuat `Detail` aktif dan tanpa `Push Update` (Hidden, tanpa tooltip).

### TC-AC-PF-103: CRUD pada PT Wahana Nusantara dan PT Karya Abadi

20. Buka Overlay Row Action pada `PT Wahana Nusantara`.
21. Verifikasi `Detail` dan `Push Update` aktif.
22. Buka Overlay Row Action pada `PT Karya Abadi`.
23. Verifikasi Overlay Row Action hanya memuat `Detail`; `Push Update` tidak ada.

### TC-AC-PF-106: hak Group parsial tanpa Update

24. Verifikasi Client Name `PT Hak Parsial Satu` dan `PT Hak Parsial Dua` berupa link aktif.
25. Buka Overlay Row Action pada `PT Hak Parsial Satu`.
26. Verifikasi Overlay Row Action memuat `Detail` aktif dan tanpa `Push Update` (Hidden, tanpa tooltip).
27. Buka Overlay Row Action pada `PT Hak Parsial Dua`.
28. Verifikasi Overlay Row Action memuat `Detail` aktif dan tanpa `Push Update` (Hidden, tanpa tooltip).

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (membuka Plan Detail dan Tab Assigned Clients yang dipakai semua TC berikutnya dalam spec ini; TC-AC-PF-100 sampai 106 mengulang langkah "Buka Plan Detail `Growth` → Tab Assigned Clients" yang sama).
- Langkah 17 dan 19 serta langkah 23 memuat anchor positif untuk absence `Push Update` (`Detail` aktif pada Overlay yang sama).
- Temuan untuk QA:
  - TC-AC-PF-99 precondition menyebut aktor "CRUD pada group 4 client", sedangkan Pre-setup #8 menyebut CRUD pada semua group pemakai `Growth` selain yang dikecualikan; spec mengikuti Pre-setup #8.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
