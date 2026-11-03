---
id: TC-AC-DN-E2E-136-changelog-filter-clear-tutup-dan-kombinasi
title: "Modal Changelog Filter: Clear Field, Tutup Tanpa Apply, Indikator Titik, dan Kombinasi dengan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-438
  - TC-AC-DN-439
  - TC-AC-DN-440
  - TC-AC-DN-441
  - TC-AC-DN-442
coverage:
  web: automated
---

# Modal Changelog Filter: Clear Field, Tutup Tanpa Apply, Indikator Titik, dan Kombinasi dengan Search

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

- Isolasi riwayat seed: baris tabel pada TC-AC-DN-441, TC-AC-DN-442, dan TC-AC-DN-438 dibatasi Filter Date `01/09/26` sampai `15/09/26` (S-12, S-14); TC-AC-DN-439 dan TC-AC-DN-440 tidak mengasersi isi baris.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup

### TC-AC-DN-439: Menutup Filter Panel tanpa Apply membuang perubahan

3. Klik field `Action`, centang `Delete`, lalu tutup dropdown
4. Klik ikon Filter untuk menutup panel
5. Klik ikon Filter untuk membuka panel kembali
6. Verifikasi tabel tetap menampilkan 10 baris halaman 1 tanpa penyaringan
7. Verifikasi field `Action` pada panel kembali kosong dengan placeholder `All actions`

### TC-AC-DN-440: Ikon Filter menampilkan indikator titik selama filter ter-Apply

8. Klik field `Action`, centang `Delete`, lalu tutup dropdown
9. Klik `[Apply]`
10. Verifikasi ikon Filter menampilkan badge titik tanpa angka saat panel terbuka
11. Klik ikon Filter untuk menutup panel
12. Verifikasi ikon Filter menampilkan badge titik tanpa angka saat panel tertutup
13. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
14. Verifikasi badge titik pada ikon Filter hilang setelah filter dilepas

### TC-AC-DN-441: Search lalu Filter menghasilkan irisan yang sama

15. Klik ikon Search, ketik Search `tester`, tekan Enter
16. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
17. Klik field `Action`, centang `Edit`, lalu tutup dropdown
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan 3 baris Edit `Cable Tester`
20. Verifikasi kata kunci Search `tester` tidak dihapus oleh Filter dan tetap tampil di kotak pencarian

### TC-AC-DN-442: Filter lalu Search menghasilkan irisan yang sama

21. Klik ikon panah `(←)` di kiri toolbar
22. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
23. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
24. Klik field `Action`, centang `Edit`, lalu tutup dropdown
25. Klik `[Apply]`
26. Klik ikon Search, ketik Search `tester`, tekan Enter
27. Verifikasi tabel menampilkan 3 baris Edit `Cable Tester`
28. Verifikasi kriteria Filter `Edit` tetap aktif (chip `Edit` pada field `Action`)

### TC-AC-DN-438: Clear Field dan Apply melepas Filter tanpa mereset Search dan Sort

29. Klik `[Clear Field]`, lalu klik `[Apply]`
30. Klik ikon panah `(←)` di kiri toolbar
31. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
32. Klik field `Modified By`, centang pelaku Maya Putri, lalu tutup dropdown
33. Klik `[Apply]`
34. Klik ikon Search, ketik Search `tag`, tekan Enter
35. Klik header kolom Device Name satu kali
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Verifikasi kolom Modified By pada Filter Panel kosong dan filter terlepas
38. Verifikasi kata kunci Search `tag` tetap aktif
39. Verifikasi sort ascending kolom Device Name tetap aktif
40. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
41. Klik `[Apply]`
42. Verifikasi tabel menampilkan 5 baris yang mengandung `tag` milik `Maya P` maupun `Budi S`, terurut Device Name ascending (`Cable Tester`, tiga baris `NFC Tag`, lalu `Tag Reel`)

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-AC-DN-439 dan TC-AC-DN-440 lebih dulu karena membutuhkan panel tanpa filter; TC-AC-DN-438 terakhir karena berakhir dengan Search, Sort, dan Filter aktif. Popup menyimpan state hanya selama terbuka, sehingga tidak ada pemulihan tambahan.
- Pada TC-AC-DN-438 `[Clear Field]` melepas pembatas Filter Date ikut; Date diterapkan ulang sebelum asersi hasil tabel (langkah penghubung, S-03) karena audit trail tumbuh.
- Pada TC-AC-DN-439 tabel tidak diasersi memuat baris seed tertentu karena audit trail tumbuh; yang diasersi hanya 10 baris halaman 1 dan field Action kembali kosong.
- Ukuran spec (42 langkah, di atas smell 35 langkah): satu topik (Filter Panel modal Changelog), satu dataset, satu kelas harness; Filter Panel yang sama dipakai berulang dan tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna).
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
