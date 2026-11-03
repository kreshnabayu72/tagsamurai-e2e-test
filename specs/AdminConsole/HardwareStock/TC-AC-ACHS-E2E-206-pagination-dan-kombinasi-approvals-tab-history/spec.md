---
id: TC-AC-ACHS-E2E-206-pagination-dan-kombinasi-approvals-tab-history
title: "Pagination dan Kombinasi Empat Kontrol Approvals > Hardware Stock Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-455
  - TC-AC-ACHS-456
  - TC-AC-ACHS-457
  - TC-AC-ACHS-458
  - TC-AC-ACHS-459
coverage:
  web: automated
---

# Pagination dan Kombinasi Empat Kontrol Approvals > Hardware Stock Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini. Total 12 entri menghasilkan 2 halaman pada ukuran halaman 10.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Type baris #n (n = 1 sampai 12) | #22 Tabel D | Activation Collision pada #1, #3, #6, #8, #10, #12; Register Duplicate pada #2, #4, #5, #7, #9, #11 | `Fixture.hardwareStock.p22.d[n].type` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Keyword Search nama Client | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[10].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; muncul pada Existing Record atau Requested By tepat tiga baris #1, #8, #10 | `Fixture.hardwareStock.derived.clientCoreNameHistory` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- State global: tidak ada yang diubah; sort, filter, dan ukuran halaman dipulihkan pada langkah 27 dan 45 sampai 48. Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`

### TC-AC-ACHS-455: Default 10 baris, opsi 10/25/50/100, info jumlah

3. Verifikasi tabel menampilkan default 10 baris per halaman
4. Verifikasi info `Showing 1–10 of 12 entries`
5. Buka dropdown rows per page
6. Verifikasi opsi rows per page: 10, 25, 50, 100 (tanpa opsi All)
7. Tutup dropdown rows per page dengan `Esc`

### TC-AC-ACHS-456: Next/Prev, input nomor halaman, ganti page size kembali ke halaman 1

8. Klik `Next`
9. Verifikasi halaman 2 terbuka: `Showing 11–12 of 12 entries`
10. Isi input halaman `1`, tekan Enter
11. Verifikasi kembali ke halaman 1: `Showing 1–10 of 12 entries`
12. Klik `Next`
13. Pilih rows per page 25
14. Verifikasi mengganti page size kembali ke halaman 1: `Showing 1–12 of 12 entries`
15. Pilih rows per page 10

### TC-AC-ACHS-457: Input nomor halaman tidak valid diabaikan

16. Isi input halaman `0`, tekan Enter
17. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of 12 entries`
18. Isi input halaman `6` (melebihi halaman terakhir), tekan Enter
19. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of 12 entries`
20. Isi input halaman `abc`, tekan Enter
21. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of 12 entries`

### TC-AC-ACHS-458: Search kembali ke halaman 1, ganti sort tetap di halaman sekarang

22. Klik `Next`
23. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
24. Verifikasi halaman kembali ke 1: `Showing 1–3 of 3 entries`
25. Klik header kolom Type sekali
26. Verifikasi nomor halaman tidak berubah: tetap halaman 1, `Showing 1–3 of 3 entries`
27. Klik header kolom Type dua kali sampai netral

### TC-AC-ACHS-459: Kombinasi empat kontrol Search + Filter + Sort + Pagination, recovery dari 0 hasil

28. Ganti isi kotak search dengan `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
29. Klik icon Filter
30. Isi Type = `Activation Collision`, klik `[Apply]`
31. Klik header kolom Resolved At sekali (Ascending)
32. Pilih rows per page 25
33. Verifikasi Search berlaku: keyword `Fixture.hardwareStock.derived.clientCoreNameHistory` tetap terisi
34. Verifikasi Filter berlaku: badge titik tampil pada ikon Filter
35. Verifikasi Sort berlaku: indikator Ascending pada Resolved At
36. Verifikasi Pagination berlaku: rows per page 25
37. Verifikasi tabel menampilkan 3 baris: #1, #8, #10
38. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
39. Verifikasi kombinasi tanpa hasil menampilkan `No results found`
40. Kosongkan isi kotak search, tekan Enter
41. Verifikasi baris sesuai Filter, 6 baris: #1, #3, #6, #8, #10, #12
42. Verifikasi Sort masih aktif: indikator Ascending pada Resolved At
43. Verifikasi page size masih aktif: rows per page 25
44. Verifikasi Filter masih aktif: badge titik tampil pada ikon Filter
45. Klik `[Clear Field]`, lalu klik `[Apply]`
46. Klik header kolom Resolved At dua kali sampai netral
47. Pilih rows per page 10
48. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-455 sampai 459). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 7 (menutup dropdown), langkah 15 (mengembalikan ukuran halaman 10), langkah 22 (membuka halaman 2 sebagai precondition TC-458), langkah 27 dan 45 sampai 48 (memulihkan sort, filter, ukuran halaman, dan kotak Search, S-09). Langkah 28 mengganti isi kotak Search yang masih berisi `Fixture.hardwareStock.derived.clientCoreNameHistory` dari TC-458; langkah 48 menutup kotak Search.
- Spec ini di atas 35 langkah (48 langkah nominal). Alasan: lima TC memakai satu footer pagination dan satu dataset read-only (Tab History), tiap TC berdiri sendiri karena sort, filter, dan ukuran halaman dipulihkan di antaranya, dan topik Pagination satu dataset digabung sesuai prinsip 1.
- Konfirmasi (#8): nama inti Client sama dengan substring yang ditulis TC-458 dan TC-459 (bukan nilai kolom penuh); hasil pada Tabel D: tiga baris #1, #8, #10. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-458 langkah 3 dan 5 ("Kembali ke halaman 2 jika ada") bersifat bersyarat; Search `Fixture.hardwareStock.derived.clientCoreNameHistory` menghasilkan 3 baris sehingga halaman 2 tidak ada. Spec mengamati sort di halaman 1 (tetap halaman 1) dan tidak menulis langkah bersyarat. Judul TC menyebut Apply Filter kembali ke halaman 1 tetapi langkah dan Expected hanya memuat Search.
  - TC-456 langkah 5 ("klik Next jika ada halaman berikutnya") bersifat bersyarat dan pada ukuran halaman 25 tidak ada halaman berikutnya; spec menjalankan Next pada ukuran halaman 10 (langkah 12) lalu mengganti ukuran halaman ke 25 untuk mengamati kembali ke halaman 1. Langkah 6 TC ("pada halaman 2 ganti rows per page ke 10") tidak dapat dijalankan sesudah ukuran 25; spec memakai urutan yang bermakna.
  - TC-459 tidak menyebut Filter, Sort, dan page size yang dipakai; spec memilih Type = `Activation Collision`, sort Resolved At Ascending, dan 25 baris per halaman. Baris hasil pemulihan (6 baris) berasal dari Expected TC-436.
  - Nilai `6` pada TC-457 mengasumsikan 2 halaman (12 entri, 10 baris per halaman).
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
