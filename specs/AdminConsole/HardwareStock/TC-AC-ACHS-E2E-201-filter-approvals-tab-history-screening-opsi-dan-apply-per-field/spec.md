---
id: TC-AC-ACHS-E2E-201-filter-approvals-tab-history-screening-opsi-dan-apply-per-field
title: "Filter Approvals > Hardware Stock Tab History: Screening, Opsi, dan Apply per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-425
  - TC-AC-ACHS-426
  - TC-AC-ACHS-427
  - TC-AC-ACHS-428
coverage:
  web: automated
---

# Filter Approvals > Hardware Stock Tab History: Screening, Opsi, dan Apply per Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini. Nilai populasi menentukan asersi. Footer dengan 12 entri pada ukuran halaman 10 membaca `Showing 1–10 of 12 entries`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama singkat akun Total Control Principal #1 | #1 | Total Control Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | Nama singkat akun Default User Principal #2 | #2 | Default User Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p02.defaultUser.shortName` |
  | Nama singkat akun Additional Approver dengan capability Create #6 | #6 | Additional Approver dengan capability Create; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p06.additionalApproverCreate.shortName` |
  | Type baris #n (n = 1 sampai 12) | #22 Tabel D | Activation Collision pada #1, #3, #6, #8, #10, #12; Register Duplicate pada #2, #4, #5, #7, #9, #11 | `Fixture.hardwareStock.p22.d[n].type` |
  | Device Name (SKU) baris #n (n = 1 sampai 12) | #22 Tabel D | Device Name diikuti kode SKU dalam kurung; #8 adalah Subject BYO tanpa SKU (berakhiran `(—)`, Category `—`) | `Fixture.hardwareStock.p22.d[n].deviceName` |
  | Category baris #n (n = 1 sampai 12) | #22 Tabel D | Short Range pada #1, #2, #6, #7, #9, #11; Long Range pada #4, #5, #10; Smart Fixed Reader pada #3, #12; `—` pada #8 | `Fixture.hardwareStock.p22.d[n].category` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Approval baris #n (n = 1 sampai 12) | #22 Tabel D | Canceled pada #1, #8; Approved pada #2, #5, #6, #7, #11, #12; Rejected pada #3, #4, #9, #10 | `Fixture.hardwareStock.p22.d[n].approval` |
  | Approver baris #n (n = 1 sampai 12) | #22 Tabel D | `—` pada #1 dan #8 (Canceled); `System` pada #7; nama singkat akun Pre-setup #1 pada #2, #3, #9, #11, akun #2 pada #4, #5, #12, akun #6 pada #6, #10 | `Fixture.hardwareStock.p22.d[n].approver` |
  | Requested At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Requested At tiap baris, format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p22.d[n].requestedAt` |
  | Resolved At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Resolved At tiap baris, menurun menurut n (Resolved At terbaru lebih dulu) | `Fixture.hardwareStock.p22.d[n].resolvedAt` |
  | Keyword pencarian internal dropdown Device Name (SKU) | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[3].deviceName`: tiga huruf pertama nama Device; cocok dengan opsi #3 dan #12 (keduanya Fixed Reader) | `Fixture.hardwareStock.derived.deviceNameFixedPrefix` |
- Format tanggal dan jam General Settings: bawaan yang tampil pada Pre-setup (nilai tanggal dibaca dari fixture Pre-setup); spec tidak mengubahnya.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Opsi (langkah 18 sampai 21):

| No | Field | Placeholder | Opsi |
|---|---|---|---|
| 1 | Type | `All types` | `Activation Collision`, `Register Duplicate` (2 opsi) |
| 2 | Device Name (SKU) | `All device names` | 6 opsi DISTINCT `Device Name (SKU)` dari Tabel D, urutan A-Z, yaitu opsi baris #8 (berakhiran `(—)`, tanpa SKU), #12, #3, #6, #4, #1 (6 opsi) |
| 3 | Category | `All categories` | `Handheld Reader - Long Range`, `Handheld Reader - Short Range`, `Smart Fixed Reader` (3 opsi) |
| 4 | Requested By | `All requesters` | 10 opsi DISTINCT `<nama entitas> (<tier>)` dari Tabel D, urutan A-Z, yaitu opsi baris #8, #1, #7, #2, #9, #5, #6, #10, #4, #3 (#11 dan #12 memakai opsi yang sama dengan #4 dan #8) (10 opsi) |
| 5 | Approval | `All approvals` | `Approved`, `Canceled`, `Rejected` (3 opsi) |
| 6 | Approver | `All users` | `Fixture.hardwareStock.account.p02.defaultUser.shortName`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.shortName`, `Fixture.hardwareStock.account.p01.totalControl.shortName`, `System` (4 opsi) |

- Parameter Apply (langkah 31 sampai 36):

| No | Field | Nilai | Hasil |
|---|---|---|---|
| 1 | Type | `Register Duplicate` | 6 baris: #2, #4, #5, #7, #9, #11 |
| 2 | Device Name (SKU) | opsi baris #8 | 1 baris: #8 |
| 3 | Category | `Smart Fixed Reader` | 2 baris: #3, #12 |
| 4 | Requested By | opsi baris #9 | 1 baris: #9 |
| 5 | Approval | `Rejected` | 4 baris: #3, #4, #9, #10 |
| 6 | Approver | `Fixture.hardwareStock.account.p01.totalControl.shortName` | 4 baris: #2, #3, #9, #11 |

- Parameter Tanggal (langkah 38 sampai 43):

| No | Field | Rentang (Start ≠ End) | Hasil |
|---|---|---|---|
| 1 | Requested At | Start = tanggal Requested At #8, End = tanggal Requested At #5 | 4 baris: #5, #6, #7, #8 |
| 2 | Resolved At | Start = tanggal Resolved At #4, End = tanggal Resolved At #2 | 3 baris: #2, #3, #4 |

## Test Steps

### TC-AC-ACHS-425: Screening Filter Panel

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`
3. Hover icon Filter
4. Verifikasi tooltip `Filter`
5. Klik icon Filter
6. Verifikasi ikon Filter menjadi gelap saat panel terbuka
7. Verifikasi field pertama: Type (multi-select searchable, placeholder `All types`)
8. Verifikasi field kedua: Device Name (SKU) (multi-select searchable, placeholder `All device names`)
9. Verifikasi field ketiga: Category (multi-select searchable, placeholder `All categories`)
10. Verifikasi field keempat: Requested By (multi-select searchable, placeholder `All requesters`)
11. Verifikasi field kelima: Approval (multi-select searchable, placeholder `All approvals`)
12. Verifikasi field keenam: Approver (multi-select searchable, placeholder `All users`)
13. Verifikasi field ketujuh: Requested At (date range picker, placeholder `Select date`)
14. Verifikasi field kedelapan: Resolved At (date range picker, placeholder `Select date`)
15. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
16. Verifikasi tidak ada field Photo maupun identifier teks

### TC-AC-ACHS-426: Screening isi opsi dropdown Filter kelas multi

17. Untuk setiap baris tabel Parameter Opsi (6 baris), lakukan langkah 18 sampai 21
18. Buka dropdown field baris tersebut
19. Verifikasi opsi sesuai kolom Opsi baris tersebut dan bersumber DISTINCT dari baris tabel
20. Verifikasi kotak pencarian internal ada
21. Tutup dropdown field baris tersebut
22. Buka dropdown Device Name (SKU)
23. Ketik `Fixture.hardwareStock.derived.deviceNameFixedPrefix` pada kotak pencarian internal
24. Verifikasi daftar menyempit hanya memuat opsi yang mengandung `Fixture.hardwareStock.derived.deviceNameFixedPrefix`: opsi baris #12 dan opsi baris #3
25. Ganti isi kotak pencarian internal dengan `Fixture.hardwareStock.derived.deviceNameFixedPrefix` huruf kecil
26. Verifikasi daftar opsi identik dengan hasil pada langkah 24 (case-insensitive)
27. Ganti isi kotak pencarian internal dengan `zzqx-tidak-ada`
28. Verifikasi teks `No results found`
29. Tutup dropdown Device Name (SKU)

### TC-AC-ACHS-427: Filter kelas multi, Apply per field

30. Untuk setiap baris tabel Parameter Apply (6 baris), lakukan langkah 31 sampai 36
31. Isi field baris tersebut dengan nilai baris tersebut
32. Klik `[Apply]`
33. Verifikasi tabel sesuai kolom Hasil baris tersebut
34. Klik `[Clear Field]`
35. Klik `[Apply]`
36. Verifikasi tabel kembali ke seluruh baris: footer `Showing 1–10 of 12 entries`

### TC-AC-ACHS-428: Filter kelas date, Apply per field

37. Untuk setiap baris tabel Parameter Tanggal (2 baris), lakukan langkah 38 sampai 43
38. Isi field baris tersebut dengan rentang baris tersebut
39. Klik `[Apply]`
40. Verifikasi tabel sesuai kolom Hasil baris tersebut
41. Klik `[Clear Field]`
42. Klik `[Apply]`
43. Verifikasi tabel kembali ke seluruh baris: footer `Showing 1–10 of 12 entries`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-425 sampai 428). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 21 dan 29 (menutup dropdown sebelum field berikutnya, S-09), Filter Panel tetap terbuka sesudah `[Apply]` (ditunjukkan TC-AC-ACHS-436, panel ditutup dengan klik icon Filter), sehingga iterasi berikutnya tidak membuka ulang panel. Langkah 25 sampai 28 mengamati pencarian internal dropdown pada satu field (Device Name (SKU), opsi paling banyak yang mengandung kata bersama).
- Spec ini di atas 35 langkah dengan ekspansi blok ulang (langkah 18 sampai 21 enam kali, 31 sampai 36 enam kali, 38 sampai 43 dua kali). Alasan: semua blok memakai satu Filter Panel dan satu dataset read-only (Tab History), tiap iterasi berdiri sendiri dan diakhiri `[Clear Field]` dan `[Apply]`, dan topik Filter satu dataset digabung sesuai prinsip 1.
- Konfirmasi (#8): kata kunci dropdown diturunkan dari tiga huruf pertama nama Device #3 (sesuai TC-426 langkah 7, "3 huruf pertama salah satu opsi"), bukan nilai kolom penuh; pada 6 opsi distinct Tabel D opsi yang memuatnya (substring, case-insensitive) hanya opsi #3 dan #12, sesuai langkah 24. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-426 langkah 7 ("Ketik 3 huruf pertama salah satu opsi") tidak menyebut field; spec memakai Device Name (SKU) dengan `Fixture.hardwareStock.derived.deviceNameFixedPrefix`. Expected n (keyword tanpa kecocokan menampilkan `No results found`) tidak punya langkah di TC; spec menambah keyword `zzqx-tidak-ada` (S-03).
  - TC-427 Expected a sampai f memakai nilai dropdown yang bergantung pada populasi Pre-setup #22; spec merujuknya lewat nomor baris Tabel D (`#n`) dan opsi baris itu.
  - TC-428 tidak menyebut cara memilih rentang di date range picker; spec menulis "isi field dengan rentang" tanpa mengarang interaksi picker.
  - Pre-setup TC memberi tanggal Resolved At dalam format tanggal General Settings yang tampil; hasil bergantung pada zona waktu General Settings yang tidak diubah spec.
