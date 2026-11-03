---
id: TC-AC-ACHS-E2E-223-sort-popup-event-log
title: "Sort Popup Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-487
  - TC-AC-ACHS-488
  - TC-AC-ACHS-489
  - TC-AC-ACHS-490
  - TC-AC-ACHS-491
  - TC-AC-ACHS-492
  - TC-AC-ACHS-493
coverage:
  web: automated
---

# Sort Popup Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki tepat 12 sesi Event Log; baris dikenali lewat kolom Date. Setiap kolom yang disortir memiliki sedikitnya dua nilai distinct. Event Log adalah audit trail permanen; urutan dan total 12 sesi ditetapkan Pre-setup dan berlaku sebelum spec lain menambah sesi pada SKU ini (suite.md menjalankan spec yang mengubah baseline sesudah spec baca). Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
  | Activity baris #n (n = 1 sampai 12) | #20 Tabel B | Delete Stock pada #1, #5, #9; Add Stock pada baris lain (9 baris) | `Fixture.hardwareStock.p20.b[n].activity` |
  | Success baris #n (n = 1 sampai 12) | #20 Tabel B | jumlah unit berhasil tiap sesi | `Fixture.hardwareStock.p20.b[n].success` |
  | Waiting for Approval baris #n (n = 1 sampai 12) | #20 Tabel B | jumlah unit Waiting for Approval tiap sesi; `—` pada baris Delete Stock (#1, #5, #9) | `Fixture.hardwareStock.p20.b[n].waitingForApproval` |
  | Modified By baris #n (n = 1 sampai 12) | #20 Tabel B | nama singkat user: akun Pre-setup #1 pada #1, #4, #7, #10; user Distributor Pre-setup #11 pada #2, #5, #8, #11; user Distributor Pre-setup #10 pada #3, #6, #9, #12 | `Fixture.hardwareStock.p20.b[n].modifiedBy` |
- Format tanggal dan jam General Settings: bawaan yang tampil pada Pre-setup; spec tidak mengubahnya.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Sort (langkah 13 sampai 18). Kolom memuat nilai kolom Date tiga baris teratas; urutan default (netral) tiga teratas selalu #1, #2, #3:

| No | TC | Kolom | Ascending (klik 1) | Descending (klik 2) |
|---|---|---|---|---|
| 1 | 487 | Date | #12, #11, #10 | #1, #2, #3 |
| 2 | 488 | Activity | #2, #3, #4 | #1, #5, #9 |
| 3 | 489 | Success | #1, #5, #9 | #2, #3, #4 |
| 4 | 489 | Waiting for Approval | #3, #6, #12 | #1, #5, #9 |
| 5 | 490 | Modified By | #3, #6, #9 | #1, #4, #7 |

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-491: Sort default Date Newest First

4. Verifikasi urutan default tanpa menyentuh header sort, lima teratas: #1, #2, #3, #4, #5
5. Klik header Success tiga kali sampai netral
6. Verifikasi urutan sama dengan default: lima teratas #1, #2, #3, #4, #5

### TC-AC-ACHS-492: Guard kolom non-sortable, Actions tanpa ikon sort

7. Verifikasi kolom Actions tidak punya ikon sort
8. Klik header kolom Actions `(⋯)`
9. Verifikasi urutan baris tidak berubah: lima teratas #1, #2, #3, #4, #5
10. Verifikasi overlay `Column Visibility` terbuka
11. Tutup overlay dengan `Esc`

### TC-AC-ACHS-487, TC-AC-ACHS-488, TC-AC-ACHS-489, TC-AC-ACHS-490: Siklus 3-state per kolom

12. Untuk setiap baris tabel Parameter Sort (5 baris), lakukan langkah 13 sampai 18
13. Klik header kolom baris tersebut (klik 1)
14. Verifikasi indikator Ascending (`↑`) dan tiga baris teratas sesuai kolom Ascending baris tersebut
15. Klik header kolom yang sama lagi (klik 2)
16. Verifikasi indikator Descending (`↓`) dan tiga baris teratas sesuai kolom Descending baris tersebut
17. Klik header kolom yang sama lagi (klik 3)
18. Verifikasi indikator netral dan urutan default: tiga teratas #1, #2, #3

### TC-AC-ACHS-493: Sort tidak mereset Search dan Filter saat ganti kolom

19. Ketik Search `Delete`, tekan Enter
20. Klik header kolom Success (Ascending)
21. Klik header kolom Date (Ascending)
22. Verifikasi keyword `Delete` tetap terisi
23. Verifikasi tabel hanya berisi hasil search, 3 baris: #1, #5, #9
24. Verifikasi indikator Success kembali netral
25. Verifikasi indikator Date Ascending
26. Klik header kolom Date dua kali sampai netral
27. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-487 sampai 493). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Urutan mengikuti prinsip 2 konvensi: TC-491 (urutan default tanpa menyentuh header) dan TC-492 (guard Actions) ditaruh sebelum siklus sort kolom karena urutan default harus diamati sebelum header disentuh.
- Langkah penghubung (bukan dari langkah TC): langkah 11 (menutup overlay), langkah 26 dan 27 (mengembalikan sort dan Search, S-09). Siklus klik 3 pada tiap kolom (langkah 17) mengembalikan sort ke netral.
- Spec ini di atas 35 langkah dengan ekspansi blok ulang (langkah 13 sampai 18 lima kali). Alasan: seluruh blok memakai satu tabel dan satu dataset read-only, tiap iterasi berdiri sendiri dan diakhiri netral.
- Temuan untuk QA:
  - TC-491 langkah 6 ("klik berulang hingga netral") tidak menyebut jumlah klik; spec memakai tiga klik sesuai siklus 3-state.
  - TC-493 menyebut hasil dalam urutan default padahal sort Date Ascending aktif; spec hanya mengasersi himpunan 3 baris.
  - Tie-break antar baris bernilai sama (Activity, Success, Modified By) bergantung pada urutan sekunder yang tidak ditulis TC.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Total 12 sesi hanya berlaku sebelum spec lain menambah sesi pada SKU ini (audit trail permanen, lihat suite.md). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
