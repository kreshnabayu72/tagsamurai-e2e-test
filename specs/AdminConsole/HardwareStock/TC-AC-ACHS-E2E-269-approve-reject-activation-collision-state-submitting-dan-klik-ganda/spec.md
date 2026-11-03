---
id: TC-AC-ACHS-E2E-269-approve-reject-activation-collision-state-submitting-dan-klik-ganda
title: "Approve dan Reject Activation Collision, State Submitting, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-183
  - TC-AC-ACHS-184
  - TC-AC-ACHS-591
  - TC-AC-ACHS-604
coverage:
  web: automated
---

# Approve dan Reject Activation Collision, State Submitting, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; penahanan respons lewat intercept parsial di atas backend nyata).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup hanya dibaca: SKU `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[5].sku` (Pre-setup #16) dan daftar Client Pre-setup #23. Subject Pre-setup #21 tidak diputuskan oleh spec ini (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-269`): empat Subject Activation Collision pending beserta unit rujukan (Existing Record Active) di-seed hook `before` lewat fixture BE (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD) dan hook `after` menghapus semuanya (idempotent). Efek pada Pre-setup: hitungan unit In Use SKU `{skuShort}`, `{skuEda}`, `{skuBle}` dan isi Approvals Tab Active dan Tab History berubah selama spec berjalan; data milik spec dihapus hook `after`, sedangkan Last Updated SKU tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `skuShort` | #16, #19 (Tabel A baris ke-1) | SKU Handheld Reader Range Type Short Range, Total Registered 50 (34 Available, 16 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[1].sku` |
| `skuEda` | #16 (Tabel A baris ke-2) | SKU Handheld Reader Range Type Short Range, Total Registered 12 (12 Available, 0 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[2].sku` |
| `skuBle` | #16, #27 (Tabel A baris ke-5) | SKU BLE Gateway dengan 5 unit (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
| `snAc183` | milik spec | Matched Identifier Subject Activation Collision pending pada `skuShort` (unit Existing Record Active milik Client ke-1 Pre-setup #23, requester Client ke-2) untuk TC-183 | `SN-AC183-{runId}-269` |
| `snAc184` | milik spec | Matched Identifier Subject Activation Collision pending untuk Fixed Reader tanpa SKU (Existing Record Active, requester Client ke-6 Pre-setup #23) untuk TC-184 | `SN-AC184-{runId}-269` |
| `snAc591` | milik spec | Matched Identifier Subject Activation Collision pending pada `skuBle` (requester Client ke-4 Pre-setup #23) untuk TC-591 | `SN-AC591-{runId}-269` |
| `snAc604` | milik spec | Matched Identifier Subject Activation Collision pending pada `skuEda` (Existing Record Active Client ke-2, requester Client ke-1 Pre-setup #23) untuk TC-604 | `SN-AC604-{runId}-269` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |

- Kemampuan teknis (disediakan tim FE): intercept dan penahanan respons HTTP keputusan Approval; pada TC-591 ditahan selama 3 detik (nilai 3 detik berasal dari Data Uji TC-591, bukan aturan PRD) lalu dilepas, pada TC-604 ditahan sampai dilepas manual pada langkah 55 (pemicu state sementara, bukan kegagalan yang dipaksakan). Seed Subject dan unit milik spec serta pembersihannya di `after` disediakan tim FE/BE.
- Waktu: tidak ada pergeseran jam.

## Test Steps

### TC-AC-ACHS-183: Approve Activation Collision

1. Klik row action `Detail` pada SKU `{skuShort}`
2. Klik Tab `In Use`
3. Catat jumlah entri pada footer tabel sebagai nilai awal
4. Ketik Search `{snAc183}`, tekan Enter
5. Catat Client unit `{snAc183}` sebagai nilai awal
6. Buka Approvals > Hardware Stock
7. Klik Tab `Active`
8. Ketik Search `{snAc183}`, tekan Enter
9. Klik row action `Review` pada Subject dengan Matched Identifier `{snAc183}`
10. Pilih radio `Approve`
11. Klik `[Submit]`
12. Verifikasi toast sukses `Success, activation has been approved.`
13. Klik Tab `History`
14. Ketik Search `{snAc183}`, tekan Enter
15. Verifikasi Subject `{snAc183}` pindah ke Tab History dengan Approval `Approved`
16. Buka Hardware > Stock, klik row action `Detail` pada SKU `{skuShort}`, lalu klik Tab `In Use`
17. Verifikasi Tab In Use tidak berubah: jumlah entri sama dengan langkah 3
18. Ketik Search `{snAc183}`, tekan Enter
19. Verifikasi Client unit `{snAc183}` tetap seperti langkah 5

### TC-AC-ACHS-184: Reject Activation Collision

20. Buka Approvals > Hardware Stock
21. Klik Tab `Active`
22. Ketik Search `{snAc184}`, tekan Enter
23. Klik row action `Review` pada Subject dengan Matched Identifier `{snAc184}`
24. Pilih radio `Reject`
25. Isi Approval Note `Perangkat sudah aktif di Client lain`
26. Klik `[Submit]`
27. Verifikasi toast sukses `Success, activation has been rejected.`
28. Klik Tab `History`
29. Ketik Search `{snAc184}`, tekan Enter
30. Verifikasi Subject `{snAc184}` pindah ke Tab History dengan Approval `Rejected`

### TC-AC-ACHS-591: State Submitting pada Dialog Detail Approval

31. Klik Tab `Active`
32. Ketik Search `{snAc591}`, tekan Enter
33. Klik row action `Review` pada Subject dengan Matched Identifier `{snAc591}`
34. Pasang penahanan respons keputusan Approval selama 3 detik
35. Pilih radio `Approve`
36. Klik `[Submit]`
37. Verifikasi `[Submit]` menampilkan spinner
38. Verifikasi `[Submit]` disabled
39. Verifikasi radio `Approve | Reject`, textarea Approval Note, dan `[Cancel]` dinonaktifkan selama request berjalan
40. Lepas penahanan respons
41. Verifikasi toast sukses `Success, activation has been approved.`
42. Verifikasi dialog tertutup
43. Klik Tab `History`
44. Ketik Search `{snAc591}`, tekan Enter
45. Verifikasi Subject `{snAc591}` pindah ke Tab History

### TC-AC-ACHS-604: Klik ganda cepat pada [Submit]

46. Tunggu toast lama hilang otomatis, lalu klik Tab `Active`
47. Ketik Search `{snAc604}`, tekan Enter
48. Klik row action `Review` pada Subject dengan Matched Identifier `{snAc604}`
49. Pilih radio `Approve`
50. Pasang penahanan respons keputusan Approval
51. Klik `[Submit]` dua kali cepat
52. Verifikasi setelah klik pertama `[Submit]` menampilkan spinner
53. Verifikasi setelah klik pertama `[Submit]` disabled
54. Verifikasi kontrol dialog dinonaktifkan
55. Lepas penahanan respons
56. Verifikasi hanya satu toast sukses `Success, activation has been approved.` tampil
57. Verifikasi tidak ada dialog D-05 maupun error dari klik kedua
58. Klik Tab `History`
59. Ketik Search `{snAc604}`, tekan Enter
60. Verifikasi Tab History memuat tepat satu baris Subject itu dengan Approval `Approved`
61. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-183, 184, 591, 604). Tidak ada TC hanya-BE di spec ini.
- Search memakai Matched Identifier penuh milik spec (bersuffix unik, hanya satu baris yang memuatnya); tidak ada perbedaan dengan sel tabel.
- Penahanan respons pada TC-591 dan TC-604 hanya untuk mengamati state Submitting, bukan kegagalan yang dipaksakan, sehingga bukan kelas b (bagian 3 prinsip 13b). Intercept TC-591 dilepas pada langkah 40 dan intercept TC-604 pada langkah 55, segera setelah asersi state sementara (S-09, butir 8b nomor 5); langkah 50 (pasang) dan 55 (lepas) pada TC-604 adalah langkah penghubung yang membuat spinner, disabled, dan kontrol nonaktif teramati. Asersi toast ditulis sesudah penahanan dilepas (butir 8b nomor 11).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 6, 7, 13, 16, 20, 21, 28, 31, 43, 46, 58 (navigasi dan membuka dialog; langkah 7, 21, 31, 46 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 3 dan 5 (baseline), 4, 8, 14, 18, 22, 29, 32, 44, 47, 59 (Search untuk menemukan baris target, R-16), 61 (mengosongkan Search lewat `(←)`).
- Spec ini 61 langkah, lebih dari sekitar 35 langkah. Alasan: empat TC satu topik aksi Approve dan Reject Activation Collision; tiap blok memakai Subject milik spec sendiri dan berdiri sendiri.
- Post Condition TC-183 (status identitas perangkat Active di Global Settings, notifikasi Approved ke Client tanpa rincian Client lain, Activity Log `Device Activation Approved`), TC-184 (identitas Rejected, notifikasi Rejected ke Client, Activity Log `Device Activation Rejected`), TC-591 (identitas Active), dan TC-604 (satu entri Activity Log) tidak punya langkah observasi di TC dan tidak diasersi; Activity Log diuji di spec 276.
- Temuan untuk QA:
  - TC-183 Expected butir c menyebut "Client unit tetap yang tertaut saat aktivasi" tanpa nilai; spec membandingkan terhadap nilai awal yang dicatat.
  - Subject Activation Collision Fixed Reader (TC-184) dan Subject lain memakai Device Name `Fixture.hardwareStock.p16.a[3].deviceName (—)` tanpa SKU; dialog TC-184 tidak diasersi header-nya.
  - TC-604 tidak menyebut penahanan respons; spec menambah langkah 50 dan 55 sebagai langkah penghubung supaya asersi state sementara (butir a) teramati tepat waktu.
  - Seed Subject Activation Collision dan unit rujukan milik spec serta pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
