---
id: TC-AC-ACHA-E2E-055-defense-in-depth-permintaan-langsung-otorisasi
title: "Defense-in-Depth: Permintaan Langsung Ditolak oleh Otorisasi (Non-Creator, Read Only, Tanpa Capability, Scope READ, Self-Approve, Non-Approver, dan Group Lain)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-429
  - TC-AC-ACHA-430
  - TC-AC-ACHA-431
  - TC-AC-ACHA-432
  - TC-AC-ACHA-433
  - TC-AC-ACHA-434
  - TC-AC-ACHA-440
  - TC-AC-ACHA-489
coverage:
  web: automated
---

# Defense-in-Depth: Permintaan Langsung Ditolak oleh Otorisasi (Non-Creator, Read Only, Tanpa Capability, Scope READ, Self-Approve, Non-Approver, dan Group Lain)

## Prerequisites

- Mode: FE+BE (seluruh langkah permintaan langsung lewat klien HTTP dan sesi API aktor; tidak ada langkah UI selain hook).
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture). Tiap aktor dipakai lewat sesi API-nya sendiri (bukan login UI), sehingga tidak ada langkah ganti akun UI:

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo (aktor hook `before`) | TC-AC-ACHA-429, 430 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `readOnlyDistributor` | #34 | Read Only Distributor | TC-AC-ACHA-431 | `Spectra.env.AC_DA_RO_DIST_PASSWORD` |
| `noCapabilityDistributor` | #41 | Role tanpa capability Manage allocation | TC-AC-ACHA-432 | `Spectra.env.AC_DA_NOCAP_DIST_PASSWORD` |
| `totalControlPartner1` | #43 | Maya Putri (CV Mitra Solusi) | TC-AC-ACHA-433 | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| `memberApprover` | #42 | Lina Marlina (MB_APR) | TC-AC-ACHA-434 | `Spectra.env.AC_DA_MB_APR_PASSWORD` |
| `defaultUserDistributor` | #28 | Default User Distributor | TC-AC-ACHA-440 | `Spectra.env.AC_DA_DU_PASSWORD` |
| `memberOffDistributor` | #33 | Citra Anggraini | TC-AC-ACHA-489 | `Spectra.env.AC_DA_MB_OFF_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | Pembuat transaksi target (fixture) | `Spectra.env.AC_DA_MB_ON_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan role Citra Anggraini di Group Jakarta.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- K-1 (konvensi bagian 2): TC kelas a dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan dokumen TC backend (tidak ada untuk modul ini).
- Kemampuan teknis: klien HTTP lewat sesi API tiap aktor untuk permintaan langsung (Create, Edit, Cancel, Resubmit, Approve, Reject, baca Allocation Log, baca daftar alokasi); asersi hanya respons server (status dan isi) dan state data lewat fixture baca (bagian 8b butir 1); fixture baca (disediakan tim FE/BE) untuk status, Quantity, Reserved, dan jumlah transaksi; fixture hak role (disediakan tim FE/BE) untuk mencabut dan memulihkan role Manage allocation Citra Anggraini di Group Jakarta.
- Data Pre-setup: #3 PT Global Distribusi (group target Group Jakarta), #4 CV Mitra Solusi, #7 Client PT Sejahtera Logistik, #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`), #48 Seed 30 alokasi (target TC-AC-ACHA-433: `HALC-20260901-00001`, Seed List #1 milik PT Global Distribusi yang tidak terlihat oleh Partner CV Mitra Solusi; dibaca saja, tidak diubah).
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49, #52, #65, #71): transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Notes `Batch uji`, Reserve $250.00) untuk TC-AC-ACHA-429, 431, 440; transaksi Canceled milik MB_ON untuk TC-AC-ACHA-430; transaksi Waiting for Approval milik MB_APR (Total Cost $250.00, Reserve $250.00) untuk TC-AC-ACHA-434; transaksi Waiting for Approval (BLE Gateway, Quantity 10, Reserve $20.00) dan transaksi Canceled (NFC, Quantity 10) milik Citra Anggraini sebelum role Group Jakarta dicabut untuk TC-AC-ACHA-489. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`.
- Baseline (S-12): sebelum tiap blok dicatat lewat fixture baca status, Quantity, Reserved transaksi target, jumlah transaksi entitas pengirim, dan saldo kantong PT Global Distribusi; asersi "tidak berubah" membandingkan dengan catatan itu.
- State global: role Citra Anggraini dicabut dan dipulihkan (TC-AC-ACHA-489) di langkah 66 dan di hook `after` (tetap jalan walau spec gagal di tengah). Efek pada Pre-setup bersama (S-06): Last Updated role dan group serta audit trail perubahan hak Citra Anggraini ikut berubah dan bertambah permanen walau nilainya dipulihkan lewat fixture yang disediakan tim FE/BE. Suite berjalan serial (`parallel: false`).
- Klausa "tidak ada entri log baru" pada TC-AC-ACHA-429, 430, 431, 440, 489 dijalankan di spec 049 (`absence-pencatatan-log-aksi-ditolak`); spec ini mengasersi status respons dan state data.

## Test Steps

### Baseline

1. Catat saldo dan Reserved kantong PT Global Distribusi serta jumlah transaksi entitas pengirim PT Global Distribusi lewat fixture baca sebagai baseline blok

### TC-AC-ACHA-429: Edit dan Cancel oleh non-creator via permintaan langsung ditolak

2. Catat status, Quantity, dan Reserved transaksi Waiting for Approval milik MB_ON (target blok TC-AC-ACHA-429) lewat fixture baca sebagai baseline
3. Kirim permintaan Edit langsung (sesi API `Hendra Wibowo`, Quantity `120`) untuk transaksi milik MB_ON
4. Kirim permintaan Cancel langsung untuk transaksi yang sama
5. Verifikasi kedua permintaan ditolak HTTP 403
6. Baca status, Quantity, dan Reserved transaksi lewat fixture baca
7. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 2
8. Verifikasi Quantity tetap 100 sesuai baseline langkah 2
9. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 2

### TC-AC-ACHA-430: Resubmit oleh non-creator via permintaan langsung ditolak

10. Catat jumlah transaksi entitas pengirim dan saldo kantong lewat fixture baca sebagai baseline
11. Kirim permintaan Resubmit langsung (sesi API `Hendra Wibowo`) untuk transaksi Canceled milik MB_ON
12. Verifikasi permintaan ditolak HTTP 403
13. Baca jumlah transaksi dan saldo kantong lewat fixture baca
14. Verifikasi tidak ada transaksi baru dibanding baseline langkah 10
15. Verifikasi saldo kantong tidak berubah dibanding baseline langkah 10

### TC-AC-ACHA-431: Read Only tidak dapat menulis via permintaan langsung

16. Catat status, Quantity, dan Reserved transaksi Waiting for Approval milik MB_ON (target blok TC-AC-ACHA-431), jumlah transaksi, dan saldo kantong lewat fixture baca sebagai baseline
17. Kirim permintaan Create langsung (sesi API Read Only Distributor) dengan Category `BLE`, Client `PT Sejahtera Logistik`, dan Quantity `5`
18. Kirim permintaan Edit langsung untuk transaksi milik MB_ON
19. Kirim permintaan Cancel langsung untuk transaksi milik MB_ON
20. Verifikasi ketiga permintaan ditolak HTTP 403 oleh middleware
21. Baca status, Quantity, Reserved, jumlah transaksi, dan saldo kantong lewat fixture baca
22. Verifikasi tidak ada transaksi baru dibanding baseline langkah 16
23. Verifikasi saldo kantong tidak berubah dibanding baseline langkah 16
24. Verifikasi Reserve kantong tidak berubah dibanding baseline langkah 16
25. Verifikasi transaksi target tidak berubah (status, Quantity, Reserved) dibanding baseline langkah 16

### TC-AC-ACHA-432: Role tanpa capability ditolak pada permintaan langsung

26. Catat jumlah transaksi entitas pengirim lewat fixture baca sebagai baseline
27. Kirim permintaan baca daftar alokasi langsung (sesi API role tanpa capability Manage allocation Distributor)
28. Kirim permintaan Create langsung dengan Category `BLE`, Client `PT Sejahtera Logistik`, dan Quantity `5`
29. Verifikasi kedua permintaan ditolak HTTP 403
30. Verifikasi tidak ada data alokasi yang dikembalikan oleh permintaan baca daftar
31. Baca jumlah transaksi entitas pengirim lewat fixture baca
32. Verifikasi tidak ada transaksi baru dibanding baseline langkah 26

### TC-AC-ACHA-433: Allocation Log di luar scope READ tidak dapat dibaca langsung

33. Kirim permintaan baca Allocation Log langsung (sesi API `Maya Putri`, Total Control Partner CV Mitra Solusi) untuk transaksi `HALC-20260901-00001` milik PT Global Distribusi (Seed List #1) yang tidak terlihat oleh Partner CV Mitra Solusi
34. Verifikasi permintaan ditolak server
35. Verifikasi respons tidak mengembalikan data log transaksi di luar scope READ

### TC-AC-ACHA-434: Self-approve via permintaan langsung ditolak

36. Catat status dan Reserved transaksi Waiting for Approval milik MB_APR (Pre-setup #42, pembuat sekaligus Additional Approver) lewat fixture baca sebagai baseline
37. Kirim permintaan Approve langsung (sesi API `Lina Marlina`) untuk transaksi buatan akun ini
38. Kirim permintaan Reject langsung dengan Rejection Reason `Uji` untuk transaksi yang sama
39. Verifikasi kedua permintaan ditolak HTTP 403 (pembuat tidak boleh menyetujui atau menolak transaksinya sendiri)
40. Baca status dan Reserved transaksi lewat fixture baca
41. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 36
42. Verifikasi Reserved tidak berubah dibanding baseline langkah 36

### TC-AC-ACHA-440: Approve dan Reject oleh non-approver via permintaan langsung ditolak

43. Catat status dan Reserved transaksi Waiting for Approval milik MB_ON (target blok TC-AC-ACHA-440) lewat fixture baca sebagai baseline
44. Kirim permintaan Approve langsung (sesi API Default User Distributor) untuk transaksi milik MB_ON
45. Kirim permintaan Reject langsung dengan Rejection Reason `Uji` untuk transaksi yang sama
46. Verifikasi kedua permintaan ditolak HTTP 403 pada tahap pertama evaluasi izin (aktor bukan anggota approver pool)
47. Baca status dan Reserved transaksi lewat fixture baca
48. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 43
49. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 43

### TC-AC-ACHA-489: Aktor yang hanya memiliki Manage allocation di group lain ditolak untuk Create, Edit, Cancel, dan Resubmit

50. Cabut role Manage allocation Citra Anggraini di Group Jakarta lewat fixture hak role (disediakan tim FE/BE) sehingga hanya tersisa role Manage allocation (Create, Read, Update) di Group Surabaya
51. Catat status, Quantity, dan Reserved transaksi Waiting for Approval `target Citra`, status transaksi Canceled `target Citra`, jumlah transaksi, dan saldo kantong lewat fixture baca sebagai baseline
52. Kirim permintaan Create langsung (sesi API `Citra Anggraini`) dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `5`
53. Kirim permintaan Edit langsung (Quantity `20`) untuk transaksi Waiting for Approval milik akun ini
54. Kirim permintaan Cancel langsung untuk transaksi yang sama
55. Kirim permintaan Resubmit langsung untuk transaksi Canceled milik akun ini
56. Verifikasi keempat permintaan ditolak HTTP 403 oleh middleware karena Manage allocation akun ini tidak ada pada group target (Group Jakarta, group entitas pengirim PT Global Distribusi); role di Group Surabaya tidak memengaruhi hasil
57. Baca jumlah transaksi, status, Quantity, Reserved, dan saldo kantong lewat fixture baca
58. Verifikasi permintaan Create tidak membuat transaksi `Completed` tanpa persetujuan dibanding baseline langkah 51
59. Verifikasi permintaan Create tidak membuat transaksi `Waiting for Approval` baru dibanding baseline langkah 51
60. Verifikasi tidak ada Reserve atau Capture akibat permintaan Create (Reserved tidak berubah dibanding baseline langkah 51)
61. Verifikasi saldo kantong tetap $20,000.00 sesuai baseline langkah 51
62. Verifikasi transaksi Waiting for Approval tetap Quantity `10` sesuai baseline langkah 51
63. Verifikasi transaksi Waiting for Approval tetap Reserved $20.00 sesuai baseline langkah 51
64. Verifikasi transaksi Canceled tetap `Canceled` sesuai baseline langkah 51
65. Verifikasi tidak ada transaksi baru hasil Resubmit dibanding baseline langkah 51
66. Pulihkan role Manage allocation Citra Anggraini di Group Jakarta lewat fixture hak role (disediakan tim FE/BE)

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 8). Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan dokumen TC backend (tidak ada untuk modul ini); BE mencatatnya pada tingkat endpoint.
- Seluruh langkah adalah permintaan langsung ke server: tidak ada langkah UI sehingga tidak ada ganti akun UI (S-07); tiap aktor memakai sesi API sendiri. Perilaku FE untuk respons yang sama diasersi di spec jalur form (bagian 8b butir 1).
- Pembagian TC lintas spec: klausa "tidak ada entri log baru" (Activity Log, System Log, Allocation Log) pada TC-AC-ACHA-429, 430, 431, 440, dan 489 dijalankan di spec 049 (`absence-pencatatan-log-aksi-ditolak`) dengan permintaan nyata, aktor, dan baseline sendiri (S-05); spec ini mengasersi status respons dan state data. TC-AC-ACHA-432, 433, dan 434 tidak memuat klausa log.
- Langkah penghubung (S-03): langkah baseline (1 sampai 51) dan langkah baca ulang lewat fixture baca (kemampuan "disediakan tim FE/BE", S-11, S-13); langkah mencabut dan memulihkan role Citra Anggraini (S-09, R-08). Langkah 1 dicatat sebagai baseline umum blok.
- Pengecualian S-12 nama literal (Lampiran A butir A-11): Rejection Reason `Uji` dan Notes `Batch uji` ditulis persis seperti TC.
- Ukuran spec: 66 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (a, defense-in-depth otorisasi) dan berdiri sendiri dengan transaksi, aktor, dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah baseline dan baca ulang state lewat fixture baca menambah langkah tanpa interaksi UI.
- Temuan untuk QA:
  - TC-AC-ACHA-433 tidak menyebut kode penolakan (403 atau 404) dan tidak menyebut surface log yang dimaksud; spec hanya mengasersi "ditolak" dan tidak ada data log yang dikembalikan.
  - TC-AC-ACHA-432 tidak menyebut kode penolakan untuk permintaan baca; Expected menyebut HTTP 403 untuk keduanya.
  - TC-AC-ACHA-440 menyebut "tahap pertama evaluasi izin" tanpa kriteria teramati; spec hanya mengasersi HTTP 403.
  - TC-AC-ACHA-489 a menyebut ketentuan "Reserved $20.00" pada precondition b yang bergantung pada transaksi Pre-setup #71; spec memakai salinan fixture dengan Reserve $20.00.
  - Post Condition TC-AC-ACHA-429 sampai 434, 440, dan 489 ("-") tidak ada.
