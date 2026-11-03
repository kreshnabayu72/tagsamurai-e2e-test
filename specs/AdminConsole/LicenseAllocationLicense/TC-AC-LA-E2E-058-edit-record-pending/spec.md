---
id: TC-AC-LA-E2E-058-edit-record-pending
title: "Edit Allocation Pending dengan Require Approval ON: Kembali ke Waiting for Approval, D-04, dan Requester Bypass"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-211
  - TC-AC-LA-212
  - TC-AC-LA-214
coverage:
  web: automated
---

# Edit Allocation Pending dengan Require Approval ON: Kembali ke Waiting for Approval, D-04, dan Requester Bypass

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current). Ganti akun ke Hadi Setiawan dilakukan eksplisit pada langkah 23 dan 24; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Hadi Setiawan | #9 | Group Manager dengan Manage allocation, Distributor PT Maju Bersama | `gmAllocLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_GM_ALLOC_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), Gudang Cimahi Retail (Pre-setup #32; term Pending FAMS Professional), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Konfigurasi: Require Approval for Allocation ON pada group Client uji (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 dan #63 bersama): alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10, Cost $3,650.00 di-Reserve: `{idP1}` dan `{idP2}` pada term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini (bentuk Pre-setup #46); `{idP3}` pada term Pending FAMS Professional Gudang Cimahi Retail, requester Hadi Setiawan sebagai Group Manager bypass (bentuk Pre-setup #63).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, kemampuan membaca saldo kantong (Reserved, Available), ledger term, batas SLA alokasi, serta notifikasi approver pool.
- State global: toggle Require Approval ON dipulihkan ke nilai awal di hook `after`; saldo kantong dikembalikan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Pending (toggle ON): D-04 lalu kembali ke Waiting for Approval

1. Ketik Search `{idP1}`, tekan Enter
2. Klik row action `Edit` pada baris Pending milik sendiri
3. Ubah Additional Quantity dari `10` menjadi `20`
4. Klik `[Save]`
5. Verifikasi dialog D-04 dengan Title `Send for Approval Again Confirmation`, Body bullet `• {idP1}` lalu `This allocation will be sent for approval again.` dan `Are you sure you want to send it?`, serta tombol `[Send]` dan `[Go Back]`
6. Klik `[Send]`
7. Verifikasi toast sukses: "Success, license allocation has been updated."
8. Verifikasi Status kembali `Waiting for Approval`
9. Verifikasi batas SLA alokasi dihitung baru dari saat `[Send]`
10. Verifikasi Reserve kantong disesuaikan menjadi `$7,300.00` dengan harga snapshot transaksi pertama
11. Verifikasi entri ledger term yang belum efektif dibatalkan atomik bersama penyesuaian Reserve
12. Verifikasi notifikasi `Waiting for your approval` terkirim ke approver pool

### Go Back pada D-04

13. Ganti isi kotak search dengan `{idP2}`, tekan Enter
14. Klik row action `Edit` pada baris Pending milik sendiri
15. Ubah Additional Quantity dari `10` menjadi `20`
16. Klik `[Save]`
17. Klik `[Go Back]` pada dialog D-04
18. Verifikasi dialog D-04 tertutup dan Form Edit tetap terbuka dengan Additional Quantity `20`
19. Klik `[✕]`
20. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
21. Klik `[Leave]`
22. Verifikasi data tersimpan belum berubah: Status baris `{idP2}` tetap `Pending`

### Edit Pending oleh requester bypass Group Manager

23. Ganti akun: Logout dari Dewi Anggraini
24. Login sebagai Hadi Setiawan (`gmAllocLic`, password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`)
25. Buka Allocation > License Allocation pada tab Current
26. Ketik Search `{idP3}`, tekan Enter
27. Klik row action `Edit` pada baris Pending milik sendiri
28. Ubah Additional Quantity dari `10` menjadi `15`
29. Klik `[Save]`
30. Verifikasi Cost pada List `{idP3}` berubah menjadi `$5,475.00`
31. Verifikasi tidak ada dialog D-04
32. Verifikasi Status tetap `Pending`
33. Verifikasi Reserve kantong disesuaikan dari `$3,650.00` menjadi `$5,475.00` (15 × $365 × 365 hari ÷ 365) dan ledger tetap pada term yang sama

## Notes

- Langkah penghubung (S-03, R-16): langkah 1, 13, dan 26 (Search untuk menemukan baris seed), langkah 19 sampai 21 (menutup form dirty sesuai S-08), langkah 23 sampai 25 (ganti akun dan membuka halaman).
- Langkah 30 mendahului langkah 31 dan 32 supaya perubahan Cost yang tampil menjadi anchor bahwa penyimpanan selesai sebelum asersi ketiadaan dialog D-04 (8b butir 2 dan 11). Urutan butir Expected TC-AC-LA-214 (a sebelum b) berubah karena alasan itu.
- Spec ini sengaja hanya memuat edit Pending dengan toggle ON; edit Pending dengan toggle OFF ada di spec 071.
- Temuan untuk QA:
  - TC-AC-LA-211 butir b dan e (SLA baru, notifikasi `Waiting for your approval` ke approver pool) dan butir d (ledger term dibatalkan atomik) tidak menyebut cara mengamati atau akun penerima notifikasi; langkah 9, 11, dan 12 memakai kemampuan baca state BE dan notifikasi yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-AC-LA-211 butir c dan TC-AC-LA-214 butir b menyebut Reserve kantong tanpa menyebut halaman atau cara membacanya; langkah 10 dan 33 memakai kemampuan baca saldo kantong dari tim FE/BE.
  - TC-AC-LA-212 butir b ("Data tersimpan belum berubah (status tetap `Pending`)") tidak punya langkah observasi di LK; langkah 19 sampai 22 mengamatinya lewat menutup form lalu membaca Status baris.
  - TC-AC-LA-214 memakai Pre-setup #9 (Group Manager + Manage allocation) sebagai aktor dan Pre-setup #63 sebagai record; TC tidak menyebut cara membuka List sebagai akun ini, spec membukanya lewat langkah 25.
