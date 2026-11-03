---
id: TC-AC-ACHS-E2E-104-resilience-baca-error-load-try-again
title: "Resilience Baca: Error Load dan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-20
  - TC-AC-ACHS-49
  - TC-AC-ACHS-55
  - TC-AC-ACHS-522
  - TC-AC-ACHS-588
coverage:
  web: automated
---

# Resilience Baca: Error Load dan Try Again

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada respons baca; asersi data termuat berasal dari backend nyata).
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` untuk memaksa respons HTTP 500 pada request daftar Stock List, daftar unit Stock Detail, daftar Subject Approvals, daftar Event Log, dan detail sesi Event Log, lalu melepas intercept segera setelah asersi tiap blok (S-09); hook `after` melepas intercept yang tersisa. Tidak ada endpoint yang ditulis di spec.
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `{Fixture.hardwareStock.p16.a[4].sku}` dengan 12 sesi Event Log (Pre-setup #17, #18, #20, Tabel B), sesi `Add Stock` `{Fixture.hardwareStock.p20.b[4].date}` (Success 13, Waiting for Approval 2); Approvals Tab Active dan Tab History (Pre-setup #21, #22). Tidak ada data yang diubah.

- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p20.b[4].date}` | No 20, Tabel B baris 4 | Date sesi Event Log `Add Stock` (Success 13, Waiting for Approval 2, Modified By akun No 1) | `Fixture.hardwareStock.p20.b[4].date` |

## Test Steps

### TC-AC-ACHS-20: Stock List gagal dimuat

1. Pasang intercept respons daftar Stock List dengan status 500
2. Klik sidebar Hardware > Stock
3. Verifikasi area tabel menampilkan teks `Unable to load this data.` dan tombol `[Try Again]`
4. Verifikasi bukan empty state `No hardware stock yet`
5. Lepas intercept, lalu klik `[Try Again]`
6. Verifikasi tabel memuat baris data

### TC-AC-ACHS-49: Stock Detail gagal dimuat pada kedua tab

7. Klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[4].sku}`
8. Pasang intercept respons daftar unit dengan status 500
9. Muat ulang halaman (F5)
10. Verifikasi Tab Available menampilkan `Unable to load this data.` dan tombol `[Try Again]`
11. Verifikasi Tab Available bukan empty state
12. Klik Tab `In Use`
13. Verifikasi Tab In Use menampilkan `Unable to load this data.` dan tombol `[Try Again]`
14. Verifikasi Tab In Use bukan empty state
15. Lepas intercept

### TC-AC-ACHS-522: Popup Event Log gagal dimuat

16. Pasang intercept respons daftar Event Log dengan status 500
17. Klik Tab `Available`
18. Klik icon `[Event Log]`
19. Verifikasi popup menampilkan `Unable to load this data.` dan tombol `[Try Again]`
20. Lepas intercept, lalu klik `[Try Again]`
21. Verifikasi tabel Event Log termuat

### TC-AC-ACHS-588: Popup Detail Event Log gagal dimuat

22. Pasang intercept respons detail sesi Event Log dengan status 500
23. Klik `Detail` pada sesi `Add Stock` (`{Fixture.hardwareStock.p20.b[4].date}`)
24. Verifikasi popup Detail menampilkan teks `Unable to load this data.` dan tombol `[Try Again]`
25. Verifikasi bukan empty state `No details to show`
26. Lepas intercept, lalu klik `[Try Again]`
27. Verifikasi section `Added` termuat
28. Verifikasi section `Waiting for Approval` termuat
29. Tutup popup Detail dan popup Event Log

### TC-AC-ACHS-55: Approvals gagal dimuat pada kedua tab

30. Pasang intercept respons daftar Subject Approvals dengan status 500
31. Buka Approvals > Hardware Stock
32. Verifikasi Tab Active menampilkan `Unable to load this data.` dan tombol `[Try Again]`
33. Klik Tab `History`
34. Verifikasi Tab History menampilkan `Unable to load this data.` dan tombol `[Try Again]`
35. Lepas intercept

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-20, 49, 55, 522, 588). Tidak ada TC hanya-BE di spec ini. Spec kelas b (kegagalan server yang dipaksa); semua blok berdiri sendiri dan memakai intercept dan asersi sendiri.
- Urutan menyimpang dari TC: blok popup (TC-522, TC-588) dikelompokkan setelah TC-49 pada halaman Stock Detail yang sama dan TC-55 (Approvals) di akhir untuk menghemat navigasi.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 8, 16, 22, 30 (memasang intercept), 15, 35 (melepas intercept), 2, 7, 12, 17, 18, 23, 31, 33 (navigasi dan pindah tab), 9 (memuat ulang halaman supaya request daftar unit diminta ulang setelah intercept terpasang), 29 (menutup popup).
- Asersi `bukan empty state` (langkah 4, 11, 14, 25) mengikuti Expected TC; pembandingnya adalah teks error yang tampil pada langkah sebelumnya (anchor positif).
- Temuan untuk QA:
  - TC-49 dan TC-55 tidak menyebut pemulihan setelah intercept dilepas; spec hanya melepas intercept.
  - TC-49 menyebut intercept dipasang sebelum klik `Detail`; spec memasangnya setelah halaman Detail terbuka lalu memuat ulang halaman (langkah 9), yang menghasilkan kondisi sama.
