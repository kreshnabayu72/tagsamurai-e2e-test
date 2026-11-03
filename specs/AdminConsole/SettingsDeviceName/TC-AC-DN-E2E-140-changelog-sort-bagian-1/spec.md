---
id: TC-AC-DN-E2E-140-changelog-sort-bagian-1
title: "Modal Changelog Sort: Date, Kolom Teks, dan Nilai Kosong Old/New Value"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-450
  - TC-AC-DN-451
  - TC-AC-DN-452
  - TC-AC-DN-453
coverage:
  web: automated
---

# Modal Changelog Sort: Date, Kolom Teks, dan Nilai Kosong Old/New Value

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

### TC-AC-DN-450: Siklus sort tiga state kolom Date

6. Klik header kolom Date satu kali
7. Verifikasi indikator `↑` aktif
8. Verifikasi baris pertama adalah Create `Cable Tester` `01/09/26 08:30` (Oldest First)
9. Klik header kolom Date kedua kali
10. Verifikasi indikator `↓` aktif
11. Verifikasi baris pertama adalah Create `Tag Reel` `15/09/26 10:10` (Newest First)
12. Klik header kolom Date ketiga kali
13. Verifikasi indikator sort hilang
14. Verifikasi urutan kembali ke default Date terbaru di atas dengan baris pertama Create `Tag Reel` `15/09/26 10:10`

### TC-AC-DN-451: Siklus sort tiga state kolom teks Action, Device Name, dan Field

15. Klik header kolom Action satu kali
16. Verifikasi Action ascending: 10 baris halaman 1 terdiri dari 4 baris `Create`, 1 baris `Delete`, lalu 5 baris `Edit`
17. Klik header kolom Action kedua kali
18. Verifikasi Action descending: 6 baris `Edit`, lalu 1 baris `Delete`, lalu 3 baris `Create`
19. Klik header kolom Action ketiga kali
20. Verifikasi sort Action netral dan urutan kembali ke default Date terbaru di atas
21. Klik header kolom Device Name satu kali
22. Verifikasi Device Name ascending: 4 baris `Cable Tester` terlebih dahulu
23. Klik header kolom Device Name kedua kali
24. Verifikasi Device Name descending: 1 baris `Tag Reel` terlebih dahulu lalu 2 baris `Retired Gateway`
25. Klik header kolom Field satu kali
26. Verifikasi Field ascending: 2 baris `Category` terlebih dahulu
27. Klik header kolom Field kedua kali
28. Verifikasi Field descending: 3 baris `Measurement` terlebih dahulu lalu 6 baris `Device Name` dan 1 baris `Category`

### TC-AC-DN-452: Sort Old Value menempatkan nilai kosong di akhir saat ascending dan di awal saat descending

29. Klik header kolom Old Value satu kali
30. Verifikasi Old Value ascending: nilai terisi berurutan `Box`, `Gate Antena`, `Meter`, `Retired Gateway`, `TAG > NFC > Accessory`, `TAG > NFC > Tag`, lalu `Unit`, kemudian 3 baris dengan Old Value kosong (Create) menempati sisa halaman 1
31. Klik header kolom Old Value kedua kali
32. Verifikasi Old Value descending: 4 baris Create dengan Old Value kosong paling atas, lalu `Unit`, `TAG > NFC > Tag`, `TAG > NFC > Accessory`, `Retired Gateway`, `Meter`, dan `Gate Antena`

### TC-AC-DN-453: Sort New Value menempatkan nilai kosong di awal saat descending

33. Klik header kolom New Value satu kali
34. Verifikasi New Value ascending: nilai terisi dimulai `Cable Tester`, `Gate Antenna`, `Meter`, `NFC Tag`, `Retired Gateway`
35. Klik header kolom New Value kedua kali
36. Verifikasi New Value descending: 1 baris Delete dengan New Value kosong paling atas, lalu `Unit` dua baris

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Ukuran spec (36 langkah, di atas smell 35 langkah): satu topik (sort modal Changelog), satu dataset (riwayat seed), satu kelas harness; tiap blok TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Asersi sort memakai kelompok nilai (mis. 4 baris Create lebih dulu) dan bukan urutan antar-baris yang nilainya sama, karena TC tidak menetapkan urutan sekunder.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
