---
id: TC-AC-DN-E2E-128-changelog-hover-modified-by-dan-buka-kembali
title: "Modal Changelog: Hover Modified By dan Dibuka Kembali Mereset State"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-402
  - TC-AC-DN-405
coverage:
  web: automated
---

# Modal Changelog: Hover Modified By dan Dibuka Kembali Mereset State

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

### TC-AC-DN-402: Hover Modified By menampilkan nama lengkap pelaku

6. Arahkan kursor ke sel Modified By `Maya P` pada baris Create `Tag Reel`
7. Verifikasi tooltip untuk `Maya P` `Maya Putri`
8. Arahkan kursor ke sel Modified By `Budi S` pada baris Delete `Retired Gateway`
9. Verifikasi tooltip untuk `Budi S` `Budi Santoso`

### TC-AC-DN-405: Popup dibuka kembali mengembalikan Search, Filter, Sort, dan Pagination ke default

10. Klik ikon Filter di toolbar popup
11. Klik field `Action`, centang `Edit`, lalu klik `[Apply]`
12. Klik ikon Search, ketik Search `tester`, tekan Enter
13. Klik header kolom Date satu kali
14. Ubah page size menjadi 25 lewat Overlay Page Size
15. Klik ikon close `(X)` pada popup
16. Klik ikon Changelog di toolbar List
17. Verifikasi kolom pencarian kembali ke ikon Search dan tidak ada kata kunci aktif
18. Verifikasi ikon Filter tanpa badge titik
19. Klik ikon Filter di toolbar popup
20. Verifikasi field `Action` kosong dengan placeholder `All actions`
21. Verifikasi tidak ada indikator sort pada header kolom mana pun
22. Verifikasi Overlay Page Size menunjukkan 10
23. Verifikasi indikator halaman aktif menunjukkan halaman 1
24. Verifikasi tabel menampilkan 10 baris pada halaman 1
25. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
26. Klik `[Apply]`
27. Verifikasi urutan kembali ke default Date terbaru di atas dan baris pertama adalah Create `Tag Reel` `15/09/26 10:10`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Pada TC-AC-DN-405 Filter Action `Edit` dan Search `tester` dijalankan di atas pembatas Filter Date sehingga hasil antara 6 dan 3 baris deterministik; setelah popup dibuka kembali pembatas hilang sehingga Expected e (baris pertama `15/09/26 10:10`) diasersi setelah pembatas diterapkan ulang. Angka `11 entri` pada Expected e tidak diasersi (S-12).
- Temuan untuk QA:
  - TC-AC-DN-405 Expected e menyebut `10 baris halaman 1 dari 11 entri`; total entri Changelog adalah audit trail yang tumbuh sehingga hanya 10 baris halaman 1 yang diasersi.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
