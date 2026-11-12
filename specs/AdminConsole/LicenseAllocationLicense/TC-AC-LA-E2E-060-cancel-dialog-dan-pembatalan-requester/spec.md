---
id: TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester
title: "Cancel Allocation: Dialog D-03, Go Back, Klik Ganda, dan Cancel oleh Requester"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-217
  - TC-AC-LA-218
  - TC-AC-LA-228
  - TC-AC-LA-219
  - TC-AC-LA-220
coverage:
  web: automated
---

# Cancel Allocation: Dialog D-03, Go Back, Klik Ganda, dan Cancel oleh Requester

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current). Ganti akun ke Fajar Nugroho dilakukan eksplisit pada langkah 50 dan 51; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (anggota approver pool, pengamat notifikasi) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #46 bersama):
  - `{idD03}`, `{idBatal}`, `{idGanda}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idPending}`: alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (bentuk Pre-setup #46).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong (Balance, Reserved, Available), jumlah entri Allocation Log record, Current Quota term Pending (baseline sebelum seed `{idPending}` dicatat di hook `before`), dan notifikasi in-app.
- State global: tidak ada yang diubah selain saldo kantong akibat Cancel; saldo dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Dialog konfirmasi D-03 dan Go Back

1. Ketik Search `{idD03}`, tekan Enter
2. Catat jumlah entri Allocation Log `{idD03}` sebagai baseline
3. Klik row action `Cancel Allocation` pada baris `Waiting for Approval` milik sendiri
4. Verifikasi dialog D-03 dengan Title `Cancel License Allocation Confirmation`, Body baris bullet `• {idD03}` lalu `Are you sure you want to cancel it?`, serta tombol `[Cancel Request]` (severity danger) dan `[Go Back]`
5. Klik area backdrop
6. Verifikasi klik backdrop tidak menutup dialog
7. Klik `[Go Back]`
8. Verifikasi tidak ada toast
9. Verifikasi dialog tertutup
10. Verifikasi Status `{idD03}` tetap `Waiting for Approval`
11. Verifikasi jumlah entri Allocation Log `{idD03}` sama dengan baseline (tidak ada log baru)

### Klik ganda Cancel Request

12. Ganti isi kotak search dengan `{idGanda}`, tekan Enter
13. Klik row action `Cancel Allocation`
14. Klik ganda cepat `[Cancel Request]`
15. Verifikasi hanya satu request diproses: Reserved kantong turun sekali sebesar `$150.00`
16. Klik tab `History`
17. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
18. Ketik Search `{idGanda}`, tekan Enter
19. Klik row action `Allocation Log`
20. Verifikasi Allocation Log memuat tepat satu entri Cancel `Allocation canceled by Dewi A`
21. Tutup modal Allocation Log

### Cancel Pending oleh requester

22. Klik tab `Current`
23. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
24. Ketik Search `{idPending}`, tekan Enter
25. Klik row action `Cancel Allocation` pada baris Pending milik sendiri
26. Klik `[Cancel Request]`
27. Verifikasi toast sukses: "Success, license allocation has been canceled."
28. Verifikasi Status `{idPending}` menjadi `Canceled`
29. Verifikasi Reserve `$3,650.00` dilepas
30. Verifikasi Balance kantong tidak berubah (tanpa refund)
31. Klik `[+ Allocation]`
32. Pilih Client `Toko Serba Ada`
33. Pilih Target `SUBS-20260819-00001`
34. Pilih Type `Concurrent User`
35. Verifikasi Current Quota term Pending kembali ke nilai baseline tanpa tambahan `+10` dari alokasi itu
36. Klik `[×]`
37. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
38. Klik `[Leave]`

### Cancel Waiting for Approval oleh requester

39. Ganti isi kotak search dengan `{idBatal}`, tekan Enter
40. Klik row action `Cancel Allocation` pada baris `Waiting for Approval` milik sendiri
41. Klik `[Cancel Request]`
42. Verifikasi toast sukses: "Success, license allocation has been canceled."
43. Klik tab `History`
44. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
45. Ketik Search `{idBatal}`, tekan Enter
46. Verifikasi baris `{idBatal}` pindah ke tab History dengan Status `Canceled`
47. Verifikasi Reserved kantong turun `$150.00`
48. Verifikasi Available kantong pulih sebesar `$150.00`
49. Verifikasi Balance kantong tidak berubah (dana tidak pernah di-Capture)

### Notifikasi approver pool

50. Ganti akun: Logout dari Dewi Anggraini
51. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
52. Buka daftar notifikasi in-app
53. Verifikasi notifikasi `License allocation canceled` dengan Body `{idBatal} · Concurrent User · PT Sejahtera`

## Notes

- Alasan di atas sekitar 35 langkah: kelima TC satu topik (Cancel Allocation oleh requester Dewi Anggraini), kelas harness fungsional yang sama, tiap blok memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-AC-LA-220 memakai form Allocate hanya untuk membaca Current Quota.
- Urutan blok berbeda dari urutan TC (217, 218, 228, 220, lalu 219 terakhir): TC-AC-LA-219 butir d membutuhkan pengamat notifikasi Fajar Nugroho sehingga blok itu ditaruh terakhir agar ganti akun hanya sekali (S-05, S-07).
- Langkah penghubung (S-03, R-16): langkah 17, 23, 44 (mengosongkan kotak search lewat `✕` dan Enter sesudah pindah tab sebelum Search berikutnya; isi kotak setelah pindah tab tidak diandaikan), langkah 1, 12, 18, 24, 39, dan 45 (Search untuk menemukan baris seed), langkah 16, 22, dan 43 (pindah tab), langkah 21 (menutup modal Allocation Log), langkah 36 sampai 38 (menutup form Allocate dirty sesuai S-08), langkah 50 sampai 52 (ganti akun dan membuka notifikasi).
- P-1: langkah 2 dan 11 memakai `Verifikasi` berbaseline untuk "tidak ada log" TC-AC-LA-218 butir a karena spec absence tidak memuat TC ini (S-05); record `Waiting for Approval` dengan Reserve dibangun seeding backend sebelum aksi.
- Temuan untuk QA:
  - TC-AC-LA-218 butir a dan b ("tidak ada log", "tidak ada toast") adalah asersi absence tanpa menyebut surface log; spec memakai jumlah entri Allocation Log record dengan baseline dan anchor Status baris (langkah 10).
  - TC-AC-LA-219 butir c dan TC-AC-LA-220 butir b/c serta TC-AC-LA-228 butir a menyebut saldo kantong dan ledger term tanpa menyebut halaman atau cara membacanya; spec memakai kemampuan baca state BE yang disediakan tim FE/BE.
  - TC-AC-LA-219 butir d tidak menyebut akun penerima notifikasi dari approver pool; spec memakai Fajar Nugroho (Pre-setup #10) yang disebut pada Precondition TC.
  - TC-AC-LA-220 langkah 3 ("Buka form Allocate dan lihat Current Quota term Pending") tidak menyebut Client, Target, dan Type yang dipilih serta nilai Current Quota yang diharapkan; spec memakai Toko Serba Ada, `SUBS-20260819-00001`, Type `Concurrent User`, dan membandingkan dengan baseline hook `before`.
  - TC-AC-LA-228 tidak menyebut cara mengamati "Release sekali ($150.00)" dan "satu entri log Cancel"; spec memakai saldo kantong dan Allocation Log record di tab History.
