---
id: TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada
title: "State Tenant: Approve Trial, Cancel Request, dan Resubmit pada Client Suspended"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-305
  - TC-AC-CS-279
  - TC-AC-CS-530
  - TC-AC-CS-612
coverage:
  web: automated
---

# State Tenant: Approve Trial, Cancel Request, dan Resubmit pada Client Suspended

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Additional Approver Manage allocation Principal PT ABC, Maya Tanjung (Pre-setup #4), `approverSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_APPROVER_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): capability Create saja Partner CV Karya Mandiri, Rina Pratama (Pre-setup #12), `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A sampai E): Client `Toko Rejeki Suspended+{runId}-056` (binaan langsung PT Maju Bersama, status Suspended; padanan Pre-setup #45) dengan pengajuan Trial Waiting for Approval (Subscription ID seed A; Plan Owner PT Maju Bersama (Distributor), FAMS plan Starter; padanan #119) dan pengajuan Waiting for Approval (Subscription ID seed B; SAMS plan Growth, milik `Fajar N`; padanan #118); Trial Canceled (Subscription ID seed C) Client `Bengkel Suspended Mitra+{runId}-056` (Suspended, Plan Owner CV Karya Mandiri (Partner), milik `Rina Pratama`; padanan #106); term SAMS Canceled (Subscription ID seed D) Client `Toko Resubmit Suspended+{runId}-056` (Suspended, padanan #138) dan (Subscription ID seed E) Client `Toko Resubmit Expired+{runId}-056` (Expired, padanan #139) milik `Fajar N`.
- Data Pre-setup (keadaan global, hanya dibaca dan tidak diubah spec): Toggle Require Approval for Allocation ON (#23); Main Pocket saldo tersedia $25,000.00 (#20).
- Data Dinamis: Hasil Edit, Cancel Request, Resubmit, dan perubahan status Client hanya mengenai data seed milik spec ini; fixture backend pemulihan state (disediakan tim FE/BE) memulihkan status Client di hook `before`, `after`, dan sebagai langkah penghubung, dan seed dihapus di hook `after`. Record baru hasil Resubmit ikut dihapus bersama Client seed. Efeknya (Last Updated dan entri audit trail Client seed) dicatat di sini.
- Kemampuan teknis (disediakan tim FE/BE): mengatur status Client (Suspended, Expired) lewat fixture backend; seed per spec lewat API dan pemulihan state lewat fixture backend.

## Test Steps

### TC-AC-CS-305: Approve Trial atas Client yang berubah menjadi Suspended ditolak

1. Buka Approvals > Client Subscription
2. Ketik Search `Toko Rejeki Suspended+{runId}-056`, tekan Enter
3. Approve pengajuan Trial `Subscription ID seed A` lalu klik `[Submit]`
4. Verifikasi toast error baku "Changes can't be saved while this workspace is suspended or expired." dan bukan pesan V-19
5. Buka Allocation > Client Subscription tab Current, ketik Search `Toko Rejeki Suspended+{runId}-056`, tekan Enter
6. Verifikasi pengajuan Trial `Subscription ID seed A` tetap berstatus Waiting for Approval
7. Buka Detail pengajuan Trial
8. Verifikasi License Quota tidak menampilkan kuota yang diinisialisasi
9. Ubah status Client `Toko Rejeki Suspended+{runId}-056` menjadi Expired lewat fixture backend, buka Approvals > Client Subscription, ketik Search `Toko Rejeki Suspended+{runId}-056`, tekan Enter, Approve pengajuan Trial `Subscription ID seed A`, lalu klik `[Submit]`
10. Verifikasi toast error baku "Changes can't be saved while this workspace is suspended or expired." juga muncul untuk Client Expired

### TC-AC-CS-279: Cancel Request dan Edit atas pengajuan sendiri tetap berjalan pada Client Suspended

11. Ganti akun: Logout lalu login sebagai Create-Only Distributor (`Fajar Nugroho`); pulihkan Client `Toko Rejeki Suspended+{runId}-056` ke status Suspended lewat fixture backend, lalu buka Allocation > Client Subscription tab Current
12. Ketik Search `Toko Rejeki Suspended+{runId}-056`, tekan Enter, klik ikon `⋯` pada baris `Subscription ID seed B` lalu pilih `Edit`
13. Ubah Duration menjadi `2` lalu klik `[Save]`
14. Verifikasi toast sukses "Success, subscription has been updated."
15. Klik ikon `⋯` pada baris `Subscription ID seed B`, pilih `Cancel Request`, lalu klik `[Cancel Request]` pada dialog
16. Verifikasi toast sukses "Success, your request has been canceled."
17. Verifikasi tidak ada toast error "Changes can't be saved while this workspace is suspended or expired." pada kedua aksi

### TC-AC-CS-612: Resubmit term Canceled pada Client Suspended dan Client Expired berjalan normal

18. Klik tab `History`, ketik Search `Toko Resubmit`, tekan Enter, klik ikon `⋯` pada baris `Subscription ID seed D` lalu pilih `Resubmit`
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, your request has been submitted for approval."
21. Klik ikon `⋯` pada baris `Subscription ID seed E` lalu pilih `Resubmit`
22. Klik `[Submit]`
23. Verifikasi toast sukses "Success, your request has been submitted for approval."
24. Klik tab `Current`
25. Verifikasi record baru Client `Toko Resubmit Suspended+{runId}-056` berstatus Waiting for Approval
26. Verifikasi record baru Client `Toko Resubmit Expired+{runId}-056` berstatus Waiting for Approval

### TC-AC-CS-530: Resubmit baris Trial pada Client Suspended diblok

27. Ganti akun: Logout lalu login sebagai Create-Only Partner (`Rina Pratama`) dan buka Allocation > Client Subscription tab History
28. Ketik Search `Bengkel Suspended Mitra+{runId}-056`, tekan Enter, klik ikon `⋯` pada baris `Subscription ID seed C` lalu pilih `Resubmit`
29. Klik `[Submit]`
30. Verifikasi toast error baku "Changes can't be saved while this workspace is suspended or expired." dan bukan pesan V-19
31. Klik tab `Current`
32. Verifikasi baris lain milik Client `Bengkel Suspended Mitra+{runId}-056` atau hasil pencarian tab `Current` dimuat
33. Verifikasi tidak ada trial baru untuk Client `Bengkel Suspended Mitra+{runId}-056`

## Notes

- Urutan akun menyimpang dari urutan TC sumber (S-10): TC-AC-CS-305 (Additional Approver), TC-AC-CS-279 dan TC-AC-CS-612 (Create-Only Distributor), lalu TC-AC-CS-530 (Create-Only Partner) supaya ganti akun hanya dua kali.
- Pemicu perubahan status Client lewat fixture backend adalah pemicu kelas h (P-2); tidak ada konteks UI kedua.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); Search di Approvals sebelum Approve pada baris seed (R-16); pemulihan status Client dan data lewat fixture; ganti akun eksplisit (S-07).
- Anchor absence (bagian 8b butir 2): ketiadaan trial baru pada TC-AC-CS-530 didahului Verifikasi hasil pencarian tab `Current` dimuat pada surface yang sama.
- Temuan untuk QA: (1) TC-AC-CS-305 butir c (Requester tetap dapat Cancel Request atau menunggu Timeout Auto-Cancel) tidak diasersi karena tidak punya langkah di TC; kasus Client Expired diasersi lewat pengulangan Approve. (2) TC-AC-CS-279 Expected c adalah kesimpulan dari butir a dan b; spec mengasersinya sebagai tidak adanya toast error baku. (3) TC-AC-CS-530 tidak menyebut posisi pengamatan "tidak ada trial baru"; spec mengamatinya di tab `Current`. (4) Approvals tidak jelas punya kotak Search (TC-AC-CS-305 tidak menyebut); spec mengetik Search dengan asumsi kotak itu ada. (5) TC-AC-CS-612 tidak menyebut nama Client baru pada Dinamis; spec memakai Client seed `Toko Resubmit Suspended+{runId}-056` dan `Toko Resubmit Expired+{runId}-056` (padanan Pre-setup #138 dan #139).
