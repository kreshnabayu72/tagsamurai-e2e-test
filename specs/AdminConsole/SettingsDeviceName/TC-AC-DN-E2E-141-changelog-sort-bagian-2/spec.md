---
id: TC-AC-DN-E2E-141-changelog-sort-bagian-2
title: "Modal Changelog Sort: Modified By, Pindah Kolom, Tanpa Ikon pada Column Visibility, dan Halaman 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-454
  - TC-AC-DN-455
  - TC-AC-DN-456
  - TC-AC-DN-457
coverage:
  web: automated
---

# Modal Changelog Sort: Modified By, Pindah Kolom, Tanpa Ikon pada Column Visibility, dan Halaman 2

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

### TC-AC-DN-454: Sort Modified By mengikuti nama lengkap pelaku

6. Klik header kolom Modified By satu kali
7. Verifikasi Modified By ascending: 6 baris `Budi S` terlebih dahulu lalu 4 baris `Maya P` pada halaman 1 (Budi Santoso lebih awal dari Maya Putri)
8. Klik header kolom Modified By kedua kali
9. Verifikasi Modified By descending: 5 baris `Maya P` terlebih dahulu lalu 5 baris `Budi S`

### TC-AC-DN-455: Berpindah kolom sort mereset kolom sebelumnya

10. Klik header kolom Action satu kali
11. Klik header kolom Field satu kali
12. Verifikasi indikator sort kolom Action menjadi netral
13. Verifikasi kolom Field aktif ascending dan baris pertama adalah baris Field `Category`

### TC-AC-DN-456: Header kolom Column Visibility tidak memiliki ikon sort

14. Verifikasi header kolom terakhir `⋯` tidak menampilkan ikon sort
15. Klik header kolom terakhir
16. Verifikasi overlay Column Visibility terbuka
17. Verifikasi urutan baris tidak berubah dan baris pertama tetap Field `Category` sesuai sort Field ascending
18. Klik header kolom terakhir untuk menutup overlay Column Visibility

### TC-AC-DN-457: Mengubah sort di halaman 2 tetap berada di halaman 2

19. Klik tombol halaman 2 pada pagination
20. Klik header kolom Action satu kali
21. Verifikasi nomor halaman aktif tetap 2
22. Verifikasi isi halaman 2 mengikuti urutan Action ascending dan baris tunggal pada halaman 2 berAction `Edit`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Sort Field pada TC-AC-DN-455 dibiarkan aktif untuk asersi TC-AC-DN-456; popup menyimpan sort hanya selama terbuka.
- Temuan untuk QA:
  - TC-AC-DN-457 Expected 'isi halaman 2 mengikuti urutan Action ascending' diasersi lewat baris terakhir pada urutan ascending (Action `Edit`), karena halaman 2 riwayat seed berisi satu baris (S-14).
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
