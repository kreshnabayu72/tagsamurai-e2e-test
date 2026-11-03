---
id: TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor
title: "Defense-in-Depth: Validasi Server atas Submit Request Langsung (Distributor)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-443
  - TC-AC-LA-446
  - TC-AC-LA-447
  - TC-AC-LA-448
  - TC-AC-LA-449
  - TC-AC-LA-456
coverage:
  web: automated
---

# Defense-in-Depth: Validasi Server atas Submit Request Langsung (Distributor)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Abadi Jaya (#25, dipegang Partner CV Karya Mandiri), Warung Gratis (#26, hanya FAMS Free Active), Toko Percobaan (#27, hanya FAMS Trial Active), PT Sejahtera (#19) dengan term FAMS `SUBS-20260101-A1B2C`, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation OFF (#39).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): satu alokasi `Completed` milik Distributor lain di luar jaringan Distributor PT Maju Bersama, Allocation ID-nya dibaca dari hasil seeding dan dipakai TC-AC-LA-456 (Distributor dan akun pemiliknya disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit dan request membuka Allocation Log langsung ke server memakai sesi API `Dewi Anggraini` (login API tidak dihitung sebagai sesi web, `suite.md`), serta membaca jumlah alokasi berdasarkan Client target lewat fixture BE (tanpa mengarang endpoint, S-13).
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah alokasi untuk Client PT Abadi Jaya, Warung Gratis, Toko Percobaan, dan PT Sejahtera lewat fixture BE sebagai baseline

### TC-AC-LA-443: Submit alokasi ke Client di luar scope WRITE Distributor ditolak

2. Kirim request submit langsung untuk Client `PT Abadi Jaya` memakai sesi API `Dewi Anggraini`
3. Verifikasi respons server menolak request (di luar scope WRITE exact match)
4. Verifikasi tidak ada record dibuat (jumlah alokasi PT Abadi Jaya sama dengan baseline)

### TC-AC-LA-446: Target Free ditolak server

5. Kirim request submit langsung dengan Target Subscription Free Client `Warung Gratis`
6. Verifikasi respons server menolak dengan pesan `Only Paid subscriptions can be allocated. Free plan uses its fixed plan cap.`
7. Verifikasi alokasi tidak dibuat (jumlah alokasi Warung Gratis sama dengan baseline)

### TC-AC-LA-447: Target Trial ditolak server

8. Kirim request submit langsung dengan Target Subscription Trial Client `Toko Percobaan`
9. Verifikasi respons server menolak dengan pesan `Only Paid subscriptions can be allocated. Free plan uses its fixed plan cap.`
10. Verifikasi tidak ada record dibuat (jumlah alokasi Toko Percobaan sama dengan baseline)

### TC-AC-LA-448: Type tidak cocok Product Target ditolak server

11. Kirim request submit langsung dengan Type `Log Source` pada Target FAMS `SUBS-20260101-A1B2C` Client `PT Sejahtera`
12. Verifikasi respons server menolak dengan pesan `This license type is not available for the selected subscription.`
13. Verifikasi tidak ada record dibuat (jumlah alokasi PT Sejahtera sama dengan baseline)

### TC-AC-LA-449: Target Client-wide tanpa Subscription Paid Active ditolak server

14. Kirim request submit langsung Asset Control Station dengan Target `Client-wide` untuk Client Free `Warung Gratis`
15. Verifikasi respons server menolak dengan pesan `Asset Control Station requires at least one active paid subscription.`
16. Verifikasi tidak ada record dibuat (jumlah alokasi Warung Gratis sama dengan baseline)

### TC-AC-LA-456: Akses Allocation ID lintas tenant ditolak

17. Kirim request membuka Allocation Log langsung dengan Allocation ID milik Distributor lain
18. Verifikasi respons server menolak dengan tepat salah satu: `403 Forbidden` atau `404 Not Found`, dan bukan 2xx
19. Verifikasi respons tidak memuat data alokasi itu (Allocation ID, Client, Product, Quantity, Cost, riwayat Log)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend.
- Langkah penghubung (S-03): langkah 1 (baseline jumlah alokasi, S-12). Asersi hanya respons server dan state data lewat fixture BE (8b butir 1); perilaku FE untuk respons yang sama tidak diasersi.
- Asersi absence "tidak ada record" (langkah 4, 7, 10, 13, 16) berbaseline (langkah 1) dan beranchor respons server yang sudah diasersi.
- Temuan untuk QA:
  - TC-AC-LA-443, 446, 447, 448, 449, 456 tidak menyebut status HTTP penolakan kecuali TC-AC-LA-456 (`403` atau `404`); spec mengasersi penolakan dan pesan sesuai TC.
  - TC-AC-LA-449 Langkah 1 menyebut Type Station untuk Client Free tanpa menyebut Quantity; spec memakai payload yang disediakan tim FE.
  - TC-AC-LA-456 menyebut "Allocation ID milik Distributor lain" tanpa data Pre-setup; alokasi tersebut disediakan tim FE. Gap Spec G22 (403 atau 404 belum ditetapkan) dicatat di TC.
  - TC-AC-LA-448 Langkah 1 menyebut "Target FAMS" tanpa ID Subscription; spec memakai `SUBS-20260101-A1B2C`.
