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
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current). Ganti akun ke Hadi Setiawan dilakukan eksplisit pada langkah 25 dan 26; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Hadi Setiawan | #9 | Group Manager dengan Manage allocation, Distributor PT Maju Bersama | `gmAllocLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_GM_ALLOC_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), Gudang Cimahi Retail (Pre-setup #32; term Pending FAMS Professional), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Konfigurasi: Require Approval for Allocation ON pada group Client uji (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 dan #63 bersama): alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10, Cost $3,650.00 di-Reserve: `{idP1}` dan `{idP2}` pada term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini (bentuk Pre-setup #46); `{idP3}` pada term Pending FAMS Professional Gudang Cimahi Retail, requester Hadi Setiawan sebagai Group Manager bypass (bentuk Pre-setup #63).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, kemampuan membaca saldo kantong (Reserved, Available), menampilkan kolom Cost pada List lewat Setup Column (pemulihan preferensi kolom di hook `after`), ledger term, batas SLA alokasi, serta notifikasi approver pool.
- State global: toggle Require Approval ON dipulihkan ke nilai awal di hook `after`; saldo kantong dikembalikan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Pending (toggle ON): D-04 lalu kembali ke Waiting for Approval

1. Ketik Search `{idP1}`, tekan Enter
2. Klik row action `Edit` pada baris Pending milik sendiri
3. Ubah Additional Quantity dari `10` menjadi `20`
4. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
5. Klik `[Save]`
6. Verifikasi dialog D-04 dengan Title `Send for Approval Again Confirmation`, Body bullet `• {idP1}` lalu `This allocation will be sent for approval again.` dan `Are you sure you want to send it?`, serta tombol `[Send]` dan `[Go Back]`
7. Klik `[Send]`
8. Verifikasi toast sukses: "Success, license allocation has been updated."
9. Verifikasi Status kembali `Waiting for Approval`
10. Verifikasi batas SLA alokasi dihitung baru dari saat `[Send]`
11. Verifikasi Reserved kantong naik `$3,650.00` terhadap baseline langkah 4 (Reserve alokasi `{idP1}` disesuaikan menjadi `$7,300.00` dengan harga snapshot transaksi pertama)
12. Verifikasi entri ledger term yang belum efektif dibatalkan atomik bersama penyesuaian Reserve
13. Verifikasi notifikasi `Waiting for your approval` terkirim ke approver pool

### Go Back pada D-04

14. Ganti isi kotak search dengan `{idP2}`, tekan Enter
15. Klik row action `Edit` pada baris Pending milik sendiri
16. Ubah Additional Quantity dari `10` menjadi `20`
17. Klik `[Save]`
18. Klik `[Go Back]` pada dialog D-04
19. Verifikasi dialog D-04 tertutup
20. Verifikasi Form Edit tetap terbuka dengan Additional Quantity `20`
21. Klik `[×]`
22. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
23. Klik `[Leave]`
24. Verifikasi data tersimpan belum berubah: Status baris `{idP2}` tetap `Pending`

### Edit Pending oleh requester bypass Group Manager

25. Ganti akun: Logout dari Dewi Anggraini
26. Login sebagai Hadi Setiawan (`gmAllocLic`, password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`)
27. Buka Allocation > License Allocation pada tab Current
28. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
29. Ketik Search `{idP3}`, tekan Enter
30. Klik row action `Edit` pada baris Pending milik sendiri
31. Ubah Additional Quantity dari `10` menjadi `15`
32. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
33. Klik `[Save]`
34. Verifikasi Cost pada List `{idP3}` berubah menjadi `$5,475.00`
35. Verifikasi tidak ada dialog D-04
36. Verifikasi Status tetap `Pending`
37. Verifikasi Reserved kantong naik `$1,825.00` terhadap baseline langkah 32 (Reserve alokasi `{idP3}` disesuaikan dari `$3,650.00` menjadi `$5,475.00`; 15 × $365 × 365 hari ÷ 365)
38. Verifikasi ledger tetap pada term yang sama

## Notes

- Alasan di atas sekitar 35 langkah: ketiga blok satu topik (Edit alokasi berstatus lisensi `Pending`), kelas harness fungsional yang sama, tiap blok memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihan langkah berasal dari langkah penghubung (baseline saldo, Setup Column, ganti akun) dan pemecahan `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, R-16): langkah 28 (menampilkan kolom Cost lewat Setup Column sesudah ganti akun, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 4 dan 32 (baseline saldo kantong), langkah 1, 14, dan 29 (Search untuk menemukan baris seed), langkah 21 sampai 23 (menutup form dirty sesuai S-08), langkah 25 sampai 27 (ganti akun dan membuka halaman).
- Langkah 34 mendahului langkah 35 dan 36 supaya perubahan Cost yang tampil menjadi anchor bahwa penyimpanan selesai sebelum asersi ketiadaan dialog D-04 (8b butir 2 dan 11). Urutan butir Expected TC-AC-LA-214 (a sebelum b) berubah karena alasan itu.
- Spec ini sengaja hanya memuat edit Pending dengan toggle ON; edit Pending dengan toggle OFF ada di spec 071.
- Temuan untuk QA:
  - TC-AC-LA-211 butir c dan TC-AC-LA-214 butir b menulis nilai Reserve kantong absolut ("disesuaikan menjadi $7,300.00") seolah satu reservasi di kantong; kantong yang sama menahan Reserve beberapa alokasi seed sehingga spec mengasersi selisih Reserved kantong terhadap baseline sebelum Save (Reserve alokasi disebut dalam kurung).
  - TC-AC-LA-211 butir b dan e (SLA baru, notifikasi `Waiting for your approval` ke approver pool) dan butir d (ledger term dibatalkan atomik) tidak menyebut cara mengamati atau akun penerima notifikasi; langkah 10, 12, dan 13 memakai kemampuan baca state BE dan notifikasi yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-AC-LA-211 butir c dan TC-AC-LA-214 butir b menyebut Reserve kantong tanpa menyebut halaman atau cara membacanya; langkah 11 dan 37 memakai kemampuan baca saldo kantong dari tim FE/BE.
  - TC-AC-LA-212 butir b ("Data tersimpan belum berubah (status tetap `Pending`)") tidak punya langkah observasi di LK; langkah 21 sampai 24 mengamatinya lewat menutup form lalu membaca Status baris.
  - TC-AC-LA-214 memakai Pre-setup #9 (Group Manager + Manage allocation) sebagai aktor dan Pre-setup #63 sebagai record; TC tidak menyebut cara membuka List sebagai akun ini, spec membukanya lewat langkah 27.
