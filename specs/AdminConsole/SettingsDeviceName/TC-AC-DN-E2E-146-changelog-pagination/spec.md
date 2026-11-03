---
id: TC-AC-DN-E2E-146-changelog-pagination
title: "Modal Changelog Pagination: Default 10, Page Size 25, Input Nomor, dan Nomor Tidak Valid"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-472
  - TC-AC-DN-473
  - TC-AC-DN-474
  - TC-AC-DN-475
coverage:
  web: automated
---

# Modal Changelog Pagination: Default 10, Page Size 25, Input Nomor, dan Nomor Tidak Valid

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal, rujukan `Fixture.settings-device-name.akunTotalControl`; fixture belum ada, disediakan tim FE), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data Pre-setup (dibaca saja, tidak diubah): #16 Device Name inti; #19 Riwayat Changelog Uji (11 entri, tabel di bawah, pelaku `Budi S` = Budi Santoso dan `Maya P` = Maya Putri, nama lengkap pelaku seed #2 `Maya Putri`); #20 General Settings entitas uji (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).

  | No | Date | Action | Device Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|---|
  | 1 | 01/09/26 08:30 | Create | Cable Tester | Device Name | — | Cable Tester | Budi S |
  | 2 | 02/09/26 09:10 | Create | NFC Tag | Device Name | — | NFC Tag | Budi S |
  | 3 | 03/09/26 10:00 | Create | Retired Gateway | Device Name | — | Retired Gateway | Maya P |
  | 4 | 05/09/26 13:15 | Edit | Gate Antenna | Device Name | Gate Antena | Gate Antenna | Maya P |
  | 5 | 06/09/26 09:30 | Edit | Cable Tester | Category | TAG > NFC > Tag | TAG > NFC > Accessory | Budi S |
  | 6 | 07/09/26 14:05 | Edit | NFC Tag | Category | TAG > NFC > Accessory | TAG > NFC > Tag | Maya P |
  | 7 | 08/09/26 15:40 | Edit | NFC Tag | Measurement | Box | Unit | Maya P |
  | 8 | 09/09/26 08:00 | Edit | Cable Tester | Measurement | Unit | Meter | Budi S |
  | 9 | 10/09/26 12:25 | Edit | Cable Tester | Measurement | Meter | Unit | Budi S |
  | 10 | 12/09/26 17:45 | Delete | Retired Gateway | Device Name | Retired Gateway | — | Budi S |
  | 11 | 15/09/26 10:10 | Create | Tag Reel | Device Name | — | Tag Reel | Maya P |

- Isolasi riwayat seed (S-12, S-14): Changelog adalah audit trail permanen yang tumbuh karena spec lain menulis entri bertanggal waktu nyata (lebih baru dari 15/09/26). Asersi isi, jumlah, dan urutan atas riwayat seed dibatasi dengan Filter Date `01/09/26` sampai `15/09/26` sehingga hanya 11 entri seed yang terlihat; jumlah total seluruh entri tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup
3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
4. Klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel

### TC-AC-DN-472: Pagination default 10 data per halaman

6. Verifikasi halaman 1 menampilkan 10 baris
7. Klik tombol halaman 2 pada pagination
8. Verifikasi halaman 2 menampilkan 1 baris dari 11 entri seed dalam pembatas Filter Date

### TC-AC-DN-473: Mengganti page size ke 25

9. Klik Overlay Page Size
10. Verifikasi Overlay Page Size menawarkan opsi 10, 25, 50, dan 100
11. Pilih 25
12. Verifikasi tabel menampilkan 11 baris pada halaman 1
13. Verifikasi indikator halaman kembali ke halaman 1
14. Klik Overlay Page Size lalu pilih 10

### TC-AC-DN-474: Input nomor halaman langsung membawa ke halaman tujuan

15. Ketik 2 pada input nomor halaman, tekan Enter
16. Verifikasi halaman 2 aktif
17. Verifikasi halaman 2 menampilkan 1 baris

### TC-AC-DN-475: Nomor halaman tidak valid diabaikan

18. Klik tombol halaman 1 pada pagination
19. Ketik 0 pada input nomor halaman, tekan Enter
20. Verifikasi input 0 diabaikan dan tabel tetap berada di halaman 1
21. Ketik 3 pada input nomor halaman, tekan Enter
22. Verifikasi input 3 (melebihi halaman terakhir) diabaikan dan tabel tetap berada di halaman 1
23. Ketik abc pada input nomor halaman, tekan Enter
24. Verifikasi input abc diabaikan dan tabel tetap berada di halaman 1

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Angka 11 entri pada TC-AC-DN-472, TC-AC-DN-473, dan TC-AC-DN-474 benar hanya dalam pembatas Filter Date riwayat seed (S-12). Langkah memilih page size 10 kembali sebelum TC-AC-DN-474 memulihkan state TC-AC-DN-473 (S-09).
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
