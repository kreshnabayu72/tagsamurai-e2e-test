---
id: TC-AC-ACHS-E2E-103-download-sukses-semua-surface-tanpa-toast
title: "Download Sukses Semua Surface Tanpa Toast"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-581
coverage:
  web: automated
---

# Download Sukses Semua Surface Tanpa Toast

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `{Fixture.hardwareStock.p16.a[4].sku}` (Pre-setup #17, #18, #20); Approvals Tab Active dan Tab History (Pre-setup #21, #22). Tidak ada data yang diubah.

- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |

- Kemampuan teknis (disediakan tim FE): mendeteksi berkas yang terunduh dan toast yang tampil.
- Surface yang diuji (parameter langkah 1 sampai 5):

| Surface | Cara membuka | Penutup |
|---|---|---|
| Stock List | Halaman awal Hardware > Stock (dibuka hook `beforeEach`) | - |
| Tab Available | Klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[4].sku}`, Tab `Available` aktif | - |
| Tab In Use | Klik Tab `In Use` | - |
| Popup Event Log | Klik Tab `Available`, lalu klik icon `[Event Log]` di toolbar | Klik `[X]` pada popup Event Log |
| Approvals Tab Active | Buka Approvals > Hardware Stock, Tab `Active` aktif | - |
| Approvals Tab History | Klik Tab `History` | - |

## Test Steps

Untuk setiap surface pada tabel Prerequisites (keenam surface berurutan dari atas ke bawah), lakukan langkah 1 sampai 5:

1. Buka surface sesuai kolom Cara membuka (Stock List tidak perlu dibuka karena sudah dibuka hook)
2. Klik icon Download, pilih `Download as CSV`
3. Verifikasi tidak ada toast sukses (T-14)
4. Verifikasi berkas CSV terunduh
5. Lakukan aksi kolom Penutup surface itu (surface berpenutup `-` tidak punya popup terbuka dan langkah ini tidak melakukan apa pun)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-581). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 5 diulang enam kali (satu per surface), ekspansi 30 langkah, di bawah sekitar 35 langkah. Tab Available, Tab In Use, dan popup Event Log memakai SKU yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 5. Langkah 5 menutup popup Event Log dengan `[X]` (kolom Penutup tabel surface) sebelum surface berikutnya dibuka; surface lain berpenutup `-`.
- Asersi absence toast (langkah 3) diletakkan segera setelah pemicu (langkah 2) dan sebelum `Verifikasi` artefak (langkah 4), sesuai butir 8b nomor 11; pemicu menjadi anchor positif yang buktinya menyusul pada langkah 4.
- Hanya nama berkas, header, dan jumlah baris yang boleh diasersi di spec fungsional; isi sel dan BOM adalah kelas f dan tidak diasersi di sini.
- Temuan untuk QA:
  - TC-581 menyebut "berkas terunduh" tanpa nama berkas; nama berkas diasersi di spec Download tiap surface, bukan di spec ini.
