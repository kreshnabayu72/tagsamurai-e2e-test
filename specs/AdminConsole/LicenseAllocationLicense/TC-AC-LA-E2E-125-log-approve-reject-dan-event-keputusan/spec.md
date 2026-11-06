---
id: TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan
title: "Log Approve dan Reject: System Log, Activity Log, Allocation Log, dan Bukan Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-393
  - TC-AC-LA-394
  - TC-AC-LA-411
  - TC-AC-LA-402
  - TC-AC-LA-403
coverage:
  web: automated
---

# Log Approve dan Reject: System Log, Activity Log, Allocation Log, dan Bukan Changelog

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Spec dimulai dari Approvals > License Allocation sebagai langkah pertama. Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38), data Changelog seed (Pre-setup #54: 25 entri) sebagai pembanding.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 bersama): empat alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41): `{idA}` (Approve), `{idR}` (Reject), `{idN}` (Approve dengan Approval Note), `{idM}` (Approve tanpa Approval Note).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; kemampuan membaca jumlah entri Changelog modul (`{nChangelog}`) dan jumlah entri Allocation Log `{idA}` (`{nLogA}`) setelah seeding dan sebelum keputusan pertama, dicatat di hook `before`.
- State global: tidak ada yang diubah selain saldo kantong #33 akibat Approve dan Reject; saldo dipulihkan oleh pembersihan record di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Keputusan Approve dan Reject dari Approvals

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi `{idA}`
3. Pilih Approve
4. Klik Submit
5. Klik `[Review]` pada alokasi `{idR}`
6. Pilih Reject
7. Isi Rejection Reason `Kuota tidak sesuai`
8. Klik Submit
9. Klik `[Review]` pada alokasi `{idN}`
10. Pilih Approve
11. Isi Approval Note `OK`
12. Klik Submit
13. Klik `[Review]` pada alokasi `{idM}`
14. Pilih Approve tanpa Approval Note
15. Klik Submit
16. Tunggu aksi selesai (tombol Submit aktif kembali atau baris keputusan hilang dari Tab Active)
17. Buka Allocation > License Allocation (tab Current)

### Changelog tidak bertambah (TC-AC-LA-393 butir a, TC-AC-LA-394 butir a, TC-AC-LA-411 butir b)

18. Klik ikon `Changelog` pada List
19. Verifikasi modal Changelog menampilkan sedikitnya satu baris entri
20. Verifikasi jumlah entri Changelog modul sama dengan `{nChangelog}` (tidak ada baris baru untuk Approve maupun Reject)
21. Tutup modal Changelog

### System Log approver dan Activity Log (TC-AC-LA-393 butir b dan c, TC-AC-LA-394 butir b dan c, TC-AC-LA-411 butir c)

22. Buka Detail User `Fajar Nugroho` > tab System Log
23. Ketik Search `{idA}`, tekan Enter
24. Verifikasi System Log memuat entri Action `Approve`, Object `License Allocation`, Name `{idA}`, Field `Status`, Old `Waiting for Approval`, New `Active`
25. Ganti isi kotak search dengan `{idR}`, tekan Enter
26. Verifikasi System Log memuat entri Action `Reject`, Status `Waiting for Approval` ke `Rejected`
27. Buka Activity Log Admin Console
28. Ketik Search `{idA}`, tekan Enter
29. Verifikasi Activity Log memuat entri Action `Approve`, Field `Status`, Old `Waiting for Approval`, New `Active`, Modified By `Fajar N`
30. Verifikasi Activity Log entitas PT Maju Bersama memuat tepat satu entri Approve oleh `Fajar N` untuk `{idA}`, tanpa entri ganda
31. Ganti isi kotak search dengan `{idR}`, tekan Enter
32. Verifikasi Activity Log memuat entri Action `Reject`, Status `Waiting for Approval` ke `Rejected`, Modified By `Fajar N`
33. Buka Allocation > License Allocation (tab Current)

### Allocation Log Approve (TC-AC-LA-411 butir a, TC-AC-LA-402)

34. Ketik Search `{idA}`, tekan Enter
35. Klik row action `Allocation Log` pada baris `{idA}`
36. Verifikasi Allocation Log `{idA}` bertambah satu entri `Allocation approved by Fajar N` terhadap `{nLogA}`
37. Tutup modal Allocation Log
38. Ganti isi kotak search dengan `{idN}`, tekan Enter
39. Klik row action `Allocation Log` pada baris `{idN}`
40. Verifikasi entri berjudul `Allocation approved by Fajar N` dengan Description `Approval Note: OK`
41. Verifikasi entri memuat Date & Time sesuai General Settings
42. Verifikasi baris judul berupa teks biasa, bukan badge
43. Tutup modal Allocation Log
44. Ganti isi kotak search dengan `{idM}`, tekan Enter
45. Klik row action `Allocation Log` pada baris `{idM}`
46. Verifikasi entri berjudul `Allocation approved by Fajar N` tanpa baris Description
47. Verifikasi entri memuat Date & Time sesuai General Settings
48. Verifikasi baris judul berupa teks biasa, bukan badge
49. Tutup modal Allocation Log

### Allocation Log Reject (TC-AC-LA-403)

50. Klik tab `History`
51. Ketik Search `{idR}`, tekan Enter
52. Klik row action `Allocation Log` pada baris `{idR}`
53. Verifikasi entri berjudul `Allocation rejected by Fajar N` dengan Description `Rejection Reason: Kuota tidak sesuai`
54. Verifikasi entri memuat Date & Time sesuai General Settings
55. Verifikasi baris judul berupa teks biasa, bukan badge
56. Tutup modal Allocation Log

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (pencatatan keputusan Approve dan Reject oleh Fajar Nugroho), satu kelas harness fungsional, empat keputusan memakai record seed sendiri sehingga berdiri sendiri. Satu rangkaian keputusan (langkah 1 sampai 15) dibaca di tiga surface log dan tiga modal Allocation Log; blok baca-log berpola tidak dihitung pada ambang smell, sehingga langkah aksi hanya 17.
- Penggabungan: TC-AC-LA-393 dan TC-AC-LA-411 memakai record `{idA}` yang sama, dan TC-AC-LA-394 dan TC-AC-LA-403 memakai record `{idR}` yang sama, sehingga tiap keputusan dijalankan sekali. Asersi "Changelog tidak bertambah" TC-AC-LA-393 butir a, TC-AC-LA-394 butir a, dan TC-AC-LA-411 butir b ditulis sekali sebagai selisih agregat Changelog modul terhadap `{nChangelog}` setelah keempat keputusan (langkah 20) dengan anchor langkah 19 (8b.2, S-12).
- Asersi "Changelog tidak bertambah" adalah scope exclusion dengan anchor positif atas surface yang sama (prinsip 13g) dan bukan kelas g murni; rujukan ke spec absence tidak ada.
- Langkah penghubung (S-03, R-16): langkah 1 dan 17 dan 33 (navigasi), langkah 16 (tunggu aksi selesai, 8b.8), langkah 21, 37, 43, 49, dan 56 (menutup modal), langkah 23, 25, 28, 31, 34, 38, 44, dan 51 (Search entri atau baris berdasarkan Allocation ID), langkah 50 (pindah tab History).
- Pembagian TC lintas spec: Approve oleh approver dari entitas berbeda dengan Plan Owner (TC-AC-LA-517) ada di spec 138.
- Temuan untuk QA:
  - TC-AC-LA-393, 394, dan 411 tidak menyebut cara menemukan entri di System Log, Activity Log, dan Changelog; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-393 butir a dan TC-AC-LA-394 butir a ("tidak ada baris baru") tidak menyebut baseline; spec memakai jumlah entri Changelog modul sebelum dan sesudah, dicatat lewat kemampuan baca yang disediakan tim FE/BE.
  - TC-AC-LA-411 butir a ("Allocation Log bertambah") tidak menyebut baseline; spec memakai jumlah entri sebelum dan sesudah.
  - TC-AC-LA-411 butir c menyebut Activity Log "entitas PT Maju Bersama" sedangkan Fajar Nugroho adalah staf Plan Owner PT Maju Bersama; spec membuka Activity Log dari akun Fajar Nugroho.
  - TC-AC-LA-402 Langkah 3 tidak menyebut tab untuk mencari kedua alokasi sesudah Approve; spec mencari di tab Current (status `Active`).
