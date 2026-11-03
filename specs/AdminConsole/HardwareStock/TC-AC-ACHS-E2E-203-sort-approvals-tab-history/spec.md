---
id: TC-AC-ACHS-E2E-203-sort-approvals-tab-history
title: "Sort Approvals > Hardware Stock Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-439
  - TC-AC-ACHS-440
  - TC-AC-ACHS-441
  - TC-AC-ACHS-442
  - TC-AC-ACHS-443
  - TC-AC-ACHS-444
  - TC-AC-ACHS-445
coverage:
  web: automated
---

# Sort Approvals > Hardware Stock Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini. Setiap kolom yang disortir memiliki sedikitnya dua nilai distinct pada data ini. Nilai populasi menentukan urutan asersi.
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
  | Existing Record baris #n (n = 1 sampai 12) | #22 Tabel D | memuat kata `Registrant` pada #2, #4, #5, #7, #9, #11; memuat `Active (Client: ...)` pada baris lain | `Fixture.hardwareStock.p22.d[n].existingRecord` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Approval baris #n (n = 1 sampai 12) | #22 Tabel D | Canceled pada #1, #8; Approved pada #2, #5, #6, #7, #11, #12; Rejected pada #3, #4, #9, #10 | `Fixture.hardwareStock.p22.d[n].approval` |
  | Approver baris #n (n = 1 sampai 12) | #22 Tabel D | `—` pada #1 dan #8 (Canceled); `System` pada #7; nama singkat akun Pre-setup #1 pada #2, #3, #9, #11, akun #2 pada #4, #5, #12, akun #6 pada #6, #10 | `Fixture.hardwareStock.p22.d[n].approver` |
  | Requested At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Requested At tiap baris, format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p22.d[n].requestedAt` |
  | Resolved At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Resolved At tiap baris, menurun menurut n (Resolved At terbaru lebih dulu) | `Fixture.hardwareStock.p22.d[n].resolvedAt` |
  | Keyword Search nama Client | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[10].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; muncul pada Existing Record atau Requested By tepat tiga baris #1, #8, #10 | `Fixture.hardwareStock.derived.clientCoreNameHistory` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Sort (langkah 12 sampai 17). Kolom Hasil memuat Matched Identifier tiga baris teratas; urutan default (netral) tiga teratas selalu #1, #2, #3:

| No | TC | Kolom | Ascending (klik 1) | Descending (klik 2) |
|---|---|---|---|---|
| 1 | 439 | Type | #1, #3, #6 | #2, #4, #5 |
| 2 | 439 | Approval | #2, #5, #6 | #3, #4, #9 |
| 3 | 440 | Device Name (SKU) | #8, #12, #3 | #1, #2, #11 |
| 4 | 440 | Category | #4, #5, #10 | #8, #3, #12 |
| 5 | 440 | Matched Identifier | #3, #12, #5 | #2, #1, #10 |
| 6 | 440 | Existing Record | #10, #6, #3 | #9, #11, #5 |
| 7 | 440 | Requested By | #8, #12, #1 | #3, #4, #11 |
| 8 | 441 | Approver | #4, #5, #12 | #1, #8, #7 |
| 9 | 442 | Requested At | #12, #11, #10 | #1, #2, #3 |
| 10 | 442 | Resolved At | #12, #11, #10 | #1, #2, #3 |

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`

### TC-AC-ACHS-443: Sort default Resolved At Newest First

3. Verifikasi urutan default tanpa menyentuh header sort, lima teratas: #1, #2, #3, #4, #5
4. Klik header Resolved At tiga kali sampai netral
5. Verifikasi urutan sama dengan default: lima teratas #1, #2, #3, #4, #5

### TC-AC-ACHS-444: Guard kolom non-sortable, Actions tanpa ikon sort

6. Verifikasi kolom Actions tidak punya ikon sort
7. Klik header kolom Actions `(⋯)`
8. Verifikasi urutan baris tidak berubah: lima teratas #1, #2, #3, #4, #5
9. Verifikasi overlay `Column Visibility` terbuka
10. Tutup overlay dengan `Esc`

### TC-AC-ACHS-439, TC-AC-ACHS-440, TC-AC-ACHS-441, TC-AC-ACHS-442: Siklus 3-state per kolom

11. Untuk setiap baris tabel Parameter Sort (10 baris), lakukan langkah 12 sampai 17
12. Klik header kolom baris tersebut (klik 1)
13. Verifikasi indikator Ascending (`↑`) dan tiga baris teratas sesuai kolom Ascending baris tersebut
14. Klik header kolom yang sama lagi (klik 2)
15. Verifikasi indikator Descending (`↓`) dan tiga baris teratas sesuai kolom Descending baris tersebut
16. Klik header kolom yang sama lagi (klik 3)
17. Verifikasi indikator netral dan urutan default: tiga teratas #1, #2, #3

### TC-AC-ACHS-445: Sort tidak mereset Search dan Filter saat ganti kolom

18. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
19. Klik header kolom Resolved At (Ascending)
20. Klik header kolom Type (Ascending)
21. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameHistory` tetap terisi
22. Verifikasi tabel hanya berisi hasil search, 3 baris: #1, #8, #10
23. Verifikasi indikator Resolved At kembali netral
24. Verifikasi indikator Type Ascending
25. Klik header kolom Type dua kali sampai netral
26. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-439 sampai 445). Tidak ada TC hanya-BE di spec ini.
- Urutan mengikuti prinsip 2 konvensi (screening di awal): TC-443 (urutan default tanpa menyentuh header) dan TC-444 (guard Actions) ditaruh sebelum siklus sort kolom, karena urutan default harus diamati sebelum header disentuh.
- Langkah penghubung (bukan dari langkah TC): langkah 10 (menutup overlay), langkah 25 dan 26 (mengembalikan sort dan Search ke keadaan awal, S-09). Siklus klik 3 pada tiap kolom (langkah 16) mengembalikan sort ke netral sehingga baris berikutnya bermula dari urutan default.
- Spec ini di atas 35 langkah dengan ekspansi blok ulang (langkah 12 sampai 17 sepuluh kali). Alasan: seluruh blok memakai satu tabel dan satu dataset read-only, tiap iterasi berdiri sendiri (kolom berbeda dengan siklus lengkap) dan diakhiri netral.
- Konfirmasi (#8): nama inti Client sama dengan substring yang ditulis TC-445 (bukan nilai kolom penuh); hasil pada Tabel D: tiga baris #1, #8, #10. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-443 langkah 4 ("klik berulang hingga netral") tidak menyebut jumlah klik; spec memakai tiga klik sesuai siklus 3-state.
  - TC-445 tidak menyebut kapan Type menjadi Ascending relatif sort Resolved At; spec mengikuti Expected c (Resolved At netral, Type Ascending) sebagai perilaku sort satu kolom aktif.
  - Hasil sort menyebut tiga baris teratas saja; tie-break antar baris bernilai sama bergantung pada urutan sekunder yang tidak ditulis TC.
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
