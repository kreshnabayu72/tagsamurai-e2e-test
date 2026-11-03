---
id: TC-AC-DN-E2E-144-changelog-setup-column-pin-reset-tutup
title: "Modal Changelog Setup Column: Pin Old Value/New Value/Modified By, Pin Ke-4, Reset to Default, dan Tutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-464
  - TC-AC-DN-465
  - TC-AC-DN-466
  - TC-AC-DN-467
coverage:
  web: automated
---

# Modal Changelog Setup Column: Pin Old Value/New Value/Modified By, Pin Ke-4, Reset to Default, dan Tutup

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

- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global yang diubah: konfigurasi kolom Changelog (dan kolom List bila disebut) tersimpan per user di browser. Hook `after` spec ini menghapus preferensi kolom di browser (bagian 4), bukan `[Reset to Default]`; kemampuan itu disediakan tim FE.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List
2. Klik ikon `⋯` pada header kolom terakhir
3. Klik item `Setup Column...` di bagian bawah overlay

### TC-AC-DN-464: Pin dan unpin kolom Old Value, New Value, dan Modified By

4. Klik ikon Pin pada baris Old Value
5. Verifikasi preview menampilkan kolom Old Value beku
6. Klik ikon Pin pada baris Old Value lagi
7. Verifikasi preview menampilkan kolom Old Value kembali normal
8. Klik ikon Pin pada baris New Value
9. Verifikasi preview menampilkan kolom New Value beku
10. Klik ikon Pin pada baris New Value lagi
11. Verifikasi preview menampilkan kolom New Value kembali normal
12. Klik ikon Pin pada baris Modified By
13. Verifikasi preview menampilkan kolom Modified By beku
14. Klik ikon Pin pada baris Modified By lagi
15. Verifikasi preview menampilkan kolom Modified By kembali normal

### TC-AC-DN-465: Pin keempat dibatasi maksimum tiga kolom

16. Klik ikon Pin pada baris Date, Action, dan Device Name
17. Arahkan kursor ke ikon Pin pada baris Field
18. Verifikasi ikon Pin pada baris Field tidak dapat diklik dan kolom Field tidak menjadi beku
19. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
20. Klik ikon Pin pada baris Date lagi (unpin)
21. Verifikasi ikon Pin pada baris Field kembali aktif

### TC-AC-DN-466: Reset to Default mengembalikan susunan kolom ke default setelah Save

22. Hilangkan centang kolom Date dan seret kolom Modified By ke posisi paling atas daftar
23. Klik `[Reset to Default]`
24. Verifikasi preview menampilkan tujuh kolom dengan urutan default
25. Klik `[Save]`
26. Verifikasi tabel setelah Save menampilkan tujuh kolom berurutan: Date, Action, Device Name, Field, Old Value, New Value, Modified By
27. Muat ulang halaman dengan F5
28. Klik ikon Changelog di toolbar List
29. Verifikasi tabel setelah F5 menampilkan tujuh kolom berurutan: Date, Action, Device Name, Field, Old Value, New Value, Modified By

### TC-AC-DN-467: Menutup popup Setup Column lewat (X) atau Esc membuang perubahan

30. Klik ikon `⋯` pada header kolom terakhir
31. Klik item `Setup Column...` di bagian bawah overlay
32. Hilangkan centang kolom Date
33. Klik ikon close `(X)` pada popup Setup Column
34. Verifikasi tabel tetap menampilkan kolom Date setelah ditutup lewat `(X)`
35. Klik ikon `⋯` pada header kolom terakhir
36. Klik item `Setup Column...` di bagian bawah overlay
37. Hilangkan centang kolom Action
38. Tekan `Esc`
39. Verifikasi tabel tetap menampilkan kolom Action setelah ditutup lewat `Esc`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bagian 4); `[Reset to Default]` hanya dipakai bila TC mengujinya.
- Popup Setup Column TC-AC-DN-465 ditinggalkan dengan dua kolom masih di-pin; `[Reset to Default]` pada TC-AC-DN-466 memulihkannya (langkah penghubung S-03). Tidak ada asersi baris tabel sehingga pembatas Filter Date tidak dipakai.
- Ukuran spec (39 langkah, di atas smell 35 langkah): satu topik (Setup Column modal Changelog), satu kelas harness, popup Setup Column yang sama dibuka berulang (kasus pin dan tutup memakai satu pembukaan bila state tidak berbeda); tiap blok TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
