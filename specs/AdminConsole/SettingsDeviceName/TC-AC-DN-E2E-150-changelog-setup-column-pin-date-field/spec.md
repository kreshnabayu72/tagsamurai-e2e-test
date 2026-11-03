---
id: TC-AC-DN-E2E-150-changelog-setup-column-pin-date-field
title: "Modal Changelog Setup Column: Pin dan Unpin Kolom Date, Action, Device Name, Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-463
coverage:
  web: automated
---

# Modal Changelog Setup Column: Pin dan Unpin Kolom Date, Action, Device Name, Field

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
- State global yang diubah: konfigurasi kolom Changelog (dan kolom List bila disebut) tersimpan per user di browser. Hook `after` spec ini menghapus preferensi kolom di browser (bagian 4), bukan `[Reset to Default]`; kemampuan itu disediakan tim FE.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon `⋯` pada header kolom terakhir
3. Klik item `Setup Column...` di bagian bawah overlay

### TC-AC-DN-463: Pin dan unpin kolom Date, Action, Device Name, dan Field

4. Klik ikon Pin pada baris Date
5. Verifikasi preview menampilkan kolom Date beku
6. Klik ikon Pin pada baris Date lagi
7. Verifikasi preview menampilkan kolom Date kembali normal
8. Klik ikon Pin pada baris Action
9. Verifikasi preview menampilkan kolom Action beku
10. Klik ikon Pin pada baris Action lagi
11. Verifikasi preview menampilkan kolom Action kembali normal
12. Klik ikon Pin pada baris Device Name
13. Verifikasi preview menampilkan kolom Device Name beku
14. Klik ikon Pin pada baris Device Name lagi
15. Verifikasi preview menampilkan kolom Device Name kembali normal
16. Klik ikon Pin pada baris Field
17. Verifikasi preview menampilkan kolom Field beku
18. Klik ikon Pin pada baris Field lagi
19. Verifikasi preview menampilkan kolom Field kembali normal
20. Klik ikon Pin pada baris Date, klik `[Save]`
21. Gulir tabel secara horizontal
22. Verifikasi kolom Date tetap beku di kiri saat tabel digulir horizontal setelah Save
23. Muat ulang halaman dengan F5
24. Klik ikon Changelog di toolbar List
25. Gulir tabel secara horizontal
26. Verifikasi kolom Date tetap beku di kiri saat tabel digulir horizontal setelah F5

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bagian 4); `[Reset to Default]` hanya dipakai bila TC mengujinya.
- Pin kolom Old Value, New Value, dan Modified By (TC-AC-DN-464) ada di spec 144.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
