---
id: TC-AC-ACHS-E2E-008-banner-waiting-for-approval-stock-detail
title: "Banner Waiting for Approval Stock Detail: Teks, Link, dan Scope per Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-37
  - TC-AC-ACHS-38
  - TC-AC-ACHS-39
  - TC-AC-ACHS-40
  - TC-AC-ACHS-41
coverage:
  web: automated
---

# Banner Waiting for Approval Stock Detail: Teks, Link, dan Scope per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`), anggota approver pool. Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun eksplisit (langkah 25 dan 30):
  - Read Only `{Fixture.hardwareStock.account.p03.readOnly.email}` (Pre-setup No 3).
  - Distributor, role Manage hardware stock, toggle Local Registration nonaktif, `{Fixture.hardwareStock.account.p12.distributorSumberJaya.email}` (Pre-setup No 12).
  - Password kedua akun memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE (belum terdaftar; lihat Temuan untuk QA).
- Data Pre-setup (hanya dibaca): SKU `{Fixture.hardwareStock.p16.a[4].sku}` dengan 1 Subject Register Duplicate pending (unit `{Fixture.hardwareStock.p17.e[28].deviceName}`, milik Distributor Pre-setup No 12) dan SKU `{Fixture.hardwareStock.p16.a[1].sku}` dengan 2 Subject Register Duplicate pending (Pre-setup No 19, Tabel C) (Pre-setup No 17, 19, 21, Tabel C). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p03.readOnly.email}` | No 3 | email akun Pre-setup No 3 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p03.readOnly.email` |
  | `{Fixture.hardwareStock.account.p12.distributorSumberJaya.email}` | No 12 | email akun Pre-setup No 12 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p12.distributorSumberJaya.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[4].deviceName}` | No 16, Tabel A baris 4 | Device Name SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].deviceName` |
  | `{Fixture.hardwareStock.p16.a[1].sku}` | No 16, 19, Tabel A baris 1 | kode SKU Handheld Reader Short Range (50 Total Registered: 34 Available, 16 In Use) | `Fixture.hardwareStock.p16.a[1].sku` |
  | `{Fixture.hardwareStock.p17.e[28].deviceName}` | No 17, Tabel E baris N = 28 | Device Name unit Waiting for Approval SKU Long Range (N = 28; Current Power `—`) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | `{Fixture.hardwareStock.p17.e[10].serialNumber}` | No 17, Tabel E baris N = 10 | Serial Number unit Available SKU Long Range dengan N terkecil (N = 10) | `Fixture.hardwareStock.p17.e[10].serialNumber` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun aktor pertama (lihat suite.md). Flag halaman Stock List dan Approvals Hardware Stock untuk akun Read Only dan akun Distributor disetel true di hook `before` spec ini dan dipulihkan di hook `after`; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-37: Teks tunggal dan jamak mengikuti jumlah Subject pending

1. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
2. Verifikasi banner "1 unit is waiting for approval."
3. Klik segmen breadcrumb `Stock`
4. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[1].sku}`, klik row action `Detail`
5. Verifikasi banner "2 units are waiting for approval."

### TC-AC-ACHS-38: Link Review in Approvals membuka Tab Active dengan filter SKU terisi

6. Klik segmen breadcrumb `Stock`
7. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
8. Verifikasi banner memuat link `Review in Approvals`
9. Klik link `Review in Approvals` di banner
10. Verifikasi Approvals > Hardware Stock Tab Active terbuka di halaman yang sama
11. Verifikasi filter Device Name (SKU) terisi Device Name `{Fixture.hardwareStock.p16.a[4].deviceName}` dan SKU `{Fixture.hardwareStock.p16.a[4].sku}`
12. Verifikasi sedikitnya satu baris tampil
13. Verifikasi setiap baris Tab Active memiliki Device Name (SKU) `{Fixture.hardwareStock.p16.a[4].deviceName} ({Fixture.hardwareStock.p16.a[4].sku})`

### TC-AC-ACHS-41: Banner tidak terpengaruh Search dan Filter, tidak bisa ditutup, tidak ada di Tab In Use

14. Klik menu Hardware > Stock di sidebar
15. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
16. Ketik Search Serial Number `{Fixture.hardwareStock.p17.e[10].serialNumber}`, tekan Enter
17. Klik icon Filter, pilih Status `Available`, klik `[Apply]`
18. Cari tombol tutup pada banner
19. Verifikasi banner tetap tampil dengan teks "1 unit is waiting for approval." saat Search dan Filter aktif
20. Verifikasi banner tidak punya tombol tutup
21. Verifikasi Summary bar tetap `25 | 18 | 7`
22. Klik Tab `In Use`
23. Verifikasi toolbar Tab In Use `Search | Filter | Download` tampil
24. Verifikasi Tab In Use tidak menampilkan banner

### TC-AC-ACHS-39: Banner untuk aktor non-approver hanya teks tanpa link

25. Logout, lalu login sebagai Read Only (Pre-setup No 3)
26. Klik menu Hardware > Stock di sidebar
27. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
28. Verifikasi banner "1 unit is waiting for approval." tampil sebagai teks pesan (Alert Message Only)
29. Verifikasi banner tanpa link `Review in Approvals`

### TC-AC-ACHS-40: Banner aktor Distributor hanya menghitung batch registrasinya sendiri

30. Logout, lalu login sebagai Distributor (Pre-setup No 12)
31. Klik menu Hardware > Stock di sidebar
32. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
33. Verifikasi banner "1 unit is waiting for approval."
34. Verifikasi banner tanpa link `Review in Approvals`
35. Verifikasi Tab Available menampilkan baris `{Fixture.hardwareStock.p17.e[28].deviceName}` dengan Status `Waiting for Approval`
36. Verifikasi Tab Available hanya menampilkan unit milik Distributor Pre-setup No 12 dengan info `Showing 1–1 of 1 entries`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-37, 38, 39, 40, 41). Tidak ada TC hanya-BE di spec ini.
- Spec memuat Step ganti akun eksplisit (langkah 25 dan 30). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras karena tiap akun membuka Stock Detail sendiri; keempat TC adalah verifikasi baca murni pada banner yang sama (bagian 3 konvensi, pemisah beda akun butir b). Urutan TC pada spec: TC-37, 38, 41 (Total Control), TC-39 (Read Only), TC-40 (Distributor) agar ganti akun minimal.
- Spec di atas smell 35 langkah (36 langkah). Alasan: seluruh blok adalah verifikasi banner yang sama pada Stock Detail RFD40 dan TC52, kelima TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Step ganti akun tidak menambah kelas harness.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 dan 6 (kembali ke Stock List lewat breadcrumb), langkah 14, 26, dan 31 (membuka Stock List lewat sidebar yang juga mereset Search dan Filter).
- Langkah 12 adalah pembanding sebelum asersi universal "setiap baris" pada langkah 13 (bagian 8b butir 2); Expected TC-38 tidak memuatnya.
- Temuan untuk QA:
  - Tidak ada literal Pre-setup: spec merujuk lewat tabel Parameter Pre-setup sehingga tidak memerlukan pengecualian S-12. Email akun aktor dirujuk lewat kunci `account.*` pada tabel Parameter Pre-setup (kredensial login).
  - TC-38 judul menyebut "hanya untuk approver pool" tetapi Expected hanya memuat aktor Total Control; aktor non-approver diuji di TC-39 (Read Only) dan TC-40 (Distributor).
  - TC-40 Expected b ("hanya menampilkan unit milik Distributor Pre-setup No 12") tidak menyebut jumlah baris; spec mengasersi satu baris `{Fixture.hardwareStock.p17.e[28].deviceName}` dan info `Showing 1–1 of 1 entries` berdasarkan Pre-setup No 12 (satu-satunya unit Distributor itu pada `{Fixture.hardwareStock.p16.a[4].sku}` adalah `{Fixture.hardwareStock.p17.e[28].deviceName}`).
  - TC-41 langkah 5 ("Cari tombol tutup pada banner") tidak punya langkah aksi yang dapat diamati selain pengamatan; spec memakai langkah amati lalu `Verifikasi` tidak adanya tombol tutup.
  - Nama env password untuk akun Read Only dan Distributor tidak didefinisikan di TC, PRD, atau konvensi; nama `AC_<ROLE>_PASSWORD` diminta dari tim FE.
  - Perbandingan kata kunci Search terhadap substring TC (S-12): Search `000010` (TC-41) dan nilai penuh Serial Number `SN-ZEBRA-RFD40-000010`: hasil sama (satu unit N = 10; `000010` tidak cocok dengan Serial Number lain pada SKU itu). Tidak ada perbedaan hasil.
