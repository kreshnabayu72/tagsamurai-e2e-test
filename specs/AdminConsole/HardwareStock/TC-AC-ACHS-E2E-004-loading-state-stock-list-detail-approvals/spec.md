---
id: TC-AC-ACHS-E2E-004-loading-state-stock-list-detail-approvals
title: "Loading State Stock List, Stock Detail, dan Approvals"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-19
  - TC-AC-ACHS-50
  - TC-AC-ACHS-590
coverage:
  web: automated
---

# Loading State Stock List, Stock Detail, dan Approvals

## Prerequisites

- Mode: FE+BE (backend nyata; response ditahan sebagian lewat intercept sehingga state server tetap nyata).
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris (No 16), unit SKU `{Fixture.hardwareStock.p16.a[4].sku}` (No 17, 18), Approvals Tab Active 12 Subject dan Tab History 12 Subject (No 21, 22). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): intercept yang menahan response HTTP daftar Stock List, daftar unit Stock Detail, dan daftar Subject Approvals selama 3 detik, lalu melepas tahanan. Durasi 3 detik adalah nilai data uji TC (bukan aturan PRD); intercept dilepas segera setelah tiap blok (S-09).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini; jumlah baris Katalog SKU (30) dan Approvals (12 Active, 12 History) pada langkah 5, 16, 17, 20, 21 diturunkan dari No 16, 21, dan 22):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-19: Stock List menampilkan Loading component

1. Pasang intercept yang menahan response daftar Stock List selama 3 detik
2. Klik menu Hardware > Stock di sidebar
3. Verifikasi area tabel menampilkan Loading component sampai data tiba
4. Verifikasi setelah response tiba tabel menampilkan baris
5. Verifikasi setelah response tiba tabel menampilkan pagination
6. Lepas intercept daftar Stock List

### TC-AC-ACHS-50: Stock Detail menampilkan Loading component pada kedua tab

7. Pasang intercept yang menahan response daftar unit selama 3 detik
8. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
9. Verifikasi Tab Available menampilkan Loading component sebelum data tiba
10. Klik Tab `In Use`
11. Verifikasi Tab In Use menampilkan Loading component sebelum data tiba
12. Lepas intercept daftar unit

### TC-AC-ACHS-590: Approvals menampilkan Loading component pada Tab Active dan Tab History

13. Pasang intercept yang menahan response daftar Subject selama 3 detik
14. Klik menu Approvals > Hardware Stock di sidebar
15. Verifikasi area tabel Tab Active menampilkan Loading component sampai data tiba
16. Verifikasi setelah response tiba Tab Active menampilkan 10 baris
17. Verifikasi setelah response tiba Tab Active menampilkan info `Showing 1–10 of 12 entries`
18. Klik Tab `History`
19. Verifikasi area tabel Tab History menampilkan Loading component sampai data tiba
20. Verifikasi setelah response tiba Tab History menampilkan 10 baris
21. Verifikasi setelah response tiba Tab History menampilkan info `Showing 1–10 of 12 entries`
22. Lepas intercept daftar Subject

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-19, 50, 590). Tidak ada TC hanya-BE di spec ini.
- Menahan response untuk mengamati state Loading bukan kelas fault injection (b); tidak ada kegagalan atau timeout yang dipaksakan, sehingga spec tetap fungsional.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6, 12, dan 22 (melepas intercept segera setelah asersi Loading, S-09).
- Temuan untuk QA:
  - TC-50 tidak menyebut apakah penahanan response berlaku untuk kedua tab; spec mengasumsikan response daftar unit Tab In Use juga ditahan selama 3 detik setelah klik Tab `In Use`.
  - TC-590 mengasumsikan response daftar Subject Tab History diminta saat Tab `History` diklik (bukan dimuat bersamaan dengan Tab Active); bila dimuat bersamaan, Loading Tab History tidak teramati.
  - Tidak ada literal Pre-setup: spec merujuk SKU lewat `{Fixture.hardwareStock.p16.a[4].sku}` sehingga tidak memerlukan pengecualian S-12.
  - Durasi tahanan 3 detik adalah nilai data uji TC yang ditandai untuk konfirmasi PRD; spec memakainya sebagai pilihan spec.
