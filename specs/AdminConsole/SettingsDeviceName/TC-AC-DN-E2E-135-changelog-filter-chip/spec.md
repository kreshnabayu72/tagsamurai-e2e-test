---
id: TC-AC-DN-E2E-135-changelog-filter-chip
title: "Modal Changelog Filter: Pencarian Opsi, Hapus Chip, Uncheck Opsi, dan +N more"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-433
  - TC-AC-DN-434
  - TC-AC-DN-435
  - TC-AC-DN-436
  - TC-AC-DN-437
coverage:
  web: automated
---

# Modal Changelog Filter: Pencarian Opsi, Hapus Chip, Uncheck Opsi, dan +N more

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

- Isolasi riwayat seed: hanya TC-AC-DN-436 memakai baris tabel, dibatasi Filter Date `01/09/26` sampai `15/09/26` (S-12, S-14).
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup

### TC-AC-DN-433: Pencarian di dalam dropdown mempersempit opsi

3. Klik field `Device Name`
4. Verifikasi opsi `Cable Tester` tampil pada dropdown sebelum pencarian opsi
5. Ketik `tag` pada kotak pencarian di dalam dropdown
6. Verifikasi daftar opsi memuat `NFC Tag` dan `Tag Reel`
7. Verifikasi opsi `Cable Tester` tidak tampil lagi pada daftar yang menyempit
8. Verifikasi tabel Changelog belum berubah dan tetap 10 baris pada halaman 1
9. Kosongkan kotak pencarian di dalam dropdown dan tutup dropdown

### TC-AC-DN-434: Hapus chip lewat ikon (X) meng-uncheck opsi

10. Klik field `Device Name`, centang `Cable Tester` dan `Tag Reel`, lalu tutup dropdown
11. Klik ikon `(X)` pada chip `Tag Reel`
12. Verifikasi chip `Tag Reel` hilang
13. Verifikasi chip `Cable Tester` tetap tampil
14. Klik field `Device Name`
15. Verifikasi checkbox `Tag Reel` tidak tercentang
16. Verifikasi checkbox `Cable Tester` tercentang

### TC-AC-DN-435: Uncheck opsi di dalam dropdown menghapus chip

17. Centang `Tag Reel` pada dropdown yang masih terbuka
18. Hilangkan centang `Cable Tester` pada dropdown yang masih terbuka
19. Verifikasi chip `Cable Tester` hilang dari field
20. Verifikasi chip `Tag Reel` tetap tampil
21. Tutup dropdown

### TC-AC-DN-436: Hasil tabel mengikuti opsi yang tersisa setelah chip dihapus dan Apply

22. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
23. Klik field `Device Name`, centang `Cable Tester`, lalu tutup dropdown
24. Klik `[Apply]`
25. Klik ikon `(X)` pada chip `Tag Reel`
26. Klik `[Apply]`
27. Verifikasi tabel menampilkan 4 baris `Cable Tester`

### TC-AC-DN-437: Chip yang tidak muat diringkas menjadi +N more

28. Klik `[Clear Field]`
29. Klik field `Device Name`, centang `Cable Tester`, `NFC Tag`, `Retired Gateway`, `Gate Antenna`, dan `Tag Reel`
30. Verifikasi chip yang tidak muat diringkas dalam satu chip `+N more` sehingga jumlah chip tampil ditambah N sama dengan 5
31. Verifikasi field tidak melebar keluar panel
32. Verifikasi field tidak digulir horizontal

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah memasang Filter Date, `[Clear Field]`, dan menutup dropdown adalah langkah penghubung (S-03). Langkah mencentang `Tag Reel` dan `Cable Tester` kembali pada TC-AC-DN-435 membentuk precondition TC (dua chip) dan tidak diasersi.
- Pada TC-AC-DN-433 jumlah tepat 2 opsi tidak diasersi karena nama Device Name lain yang memuat `tag` dapat muncul dari entri spec lain (S-12); spec mengasersi bahwa kedua opsi seed tampil dan opsi `Cable Tester` hilang.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
