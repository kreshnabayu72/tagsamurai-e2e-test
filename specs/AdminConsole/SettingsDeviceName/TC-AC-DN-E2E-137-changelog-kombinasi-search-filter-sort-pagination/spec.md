---
id: TC-AC-DN-E2E-137-changelog-kombinasi-search-filter-sort-pagination
title: "Modal Changelog: Kombinasi Search, Filter, Sort, dan Pagination serta Empty State Pulih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-443
  - TC-AC-DN-444
coverage:
  web: automated
---

# Modal Changelog: Kombinasi Search, Filter, Sort, dan Pagination serta Empty State Pulih

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

- Isolasi riwayat seed: Filter Date `01/09/26` sampai `15/09/26` dipasang bersama Filter Modified By dalam satu `[Apply]` sebagai pembatas (S-12, S-14).
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon Filter di toolbar popup

### TC-AC-DN-443: Kombinasi Search, Filter, Sort, dan Pagination aktif bersamaan

3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
4. Klik field `Modified By`, centang pelaku Maya Putri, lalu tutup dropdown
5. Klik `[Apply]`
6. Klik ikon Search, ketik Search `tag`, tekan Enter
7. Klik header kolom Device Name satu kali
8. Ubah page size menjadi 25 lewat Overlay Page Size
9. Verifikasi tabel menampilkan 3 baris milik `Maya P` yang mengandung `tag`
10. Verifikasi urutan: dua baris Edit `NFC Tag` (Field `Category` 07/09/26 14:05 dan Field `Measurement` 08/09/26 15:40; urutan kedua baris tidak diasumsikan), lalu Create `Tag Reel`
11. Verifikasi Filter Modified By `Maya Putri` tetap aktif
12. Verifikasi Search `tag` tetap aktif
13. Verifikasi sort ascending kolom Device Name tetap aktif
14. Verifikasi page size 25 tetap aktif

### TC-AC-DN-444: Empty state akibat Search dan Filter pulih setelah salah satu dilepas

15. Ganti isi kotak search dengan `tester`, tekan Enter
16. Verifikasi empty state tampil dengan Title "No results found" dan Description "Try adjusting your search or filter."
17. Verifikasi kombinasi Filter `Maya P` dan Search `tester` tidak menghasilkan baris data
18. Klik ikon `(✕)` pada kotak Search, lalu tekan Enter pada input kosong
19. Verifikasi tabel menampilkan 5 baris `Maya P`
20. Verifikasi Filter Modified By `Maya Putri` tetap aktif

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembatas Filter Date adalah langkah penghubung (S-03). Empty state hasil Search pada TC-AC-DN-444 (`No results found`) adalah anchor positif yang sah untuk asersi tidak ada baris; baris `Maya P` pada TC-AC-DN-443 menjadi pembanding.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
