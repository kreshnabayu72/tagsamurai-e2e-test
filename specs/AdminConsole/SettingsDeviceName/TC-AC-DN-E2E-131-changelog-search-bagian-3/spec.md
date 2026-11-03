---
id: TC-AC-DN-E2E-131-changelog-search-bagian-3
title: "Modal Changelog Search: Tanggal Tidak Dicocokkan, Tanpa Hasil, Reset Halaman, dan Kolom Tersembunyi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-416
  - TC-AC-DN-417
  - TC-AC-DN-418
  - TC-AC-DN-419
coverage:
  web: automated
---

# Modal Changelog Search: Tanggal Tidak Dicocokkan, Tanpa Hasil, Reset Halaman, dan Kolom Tersembunyi

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
2. Klik ikon Filter di toolbar popup
3. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
4. Klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel
6. Verifikasi baris Create `Tag Reel` `15/09/26 10:10` tampil pada halaman 1 sebagai pembanding

### TC-AC-DN-416: Search tidak mencocokkan nilai tanggal pada kolom Date

7. Klik ikon Search, ketik Search `15/09/26`, tekan Enter
8. Verifikasi tabel tidak menampilkan baris data (kolom Date hanya dapat disaring lewat Filter Panel)

### TC-AC-DN-417: Search tanpa hasil

9. Ganti isi kotak search dengan `zzzz`, tekan Enter
10. Verifikasi tabel tidak menampilkan baris data
11. Verifikasi empty state popup Changelog dengan Title `No results found` dan Description `Try adjusting your search or filter.`
12. Verifikasi tampilan bukan teks `No changes recorded yet.`
13. Verifikasi tampilan bukan error-load

### TC-AC-DN-418: Search saat di halaman 2 mengembalikan ke halaman 1

14. Klik ikon panah `(←)` di kiri toolbar
15. Klik tombol halaman 2 pada pagination
16. Klik ikon Search, ketik Search `tester`, tekan Enter
17. Verifikasi hasil Search tampil pada halaman 1
18. Verifikasi indikator halaman aktif menunjukkan halaman 1
19. Klik ikon panah `(←)` di kiri toolbar

### TC-AC-DN-419: Search tidak mencocokkan kolom yang disembunyikan

20. Klik ikon `⋯` pada header kolom terakhir
21. Hilangkan centang kolom Modified By
22. Klik ikon Search, ketik Search `maya`, tekan Enter
23. Verifikasi kata kunci `maya` tidak menemukan baris (tabel tidak menampilkan baris data, empty state hasil Search `No results found` tampil)
24. Klik ikon panah `(←)` di kiri toolbar
25. Klik ikon `⋯` pada header kolom terakhir lalu centang kembali kolom Modified By
26. Klik ikon Search, ketik Search `maya`, tekan Enter
27. Verifikasi kata kunci `maya` menampilkan 5 baris dengan Modified By `Maya P`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Langkah Verifikasi baris Create `Tag Reel` sebelum Search adalah pembanding sedikitnya satu baris untuk asersi tidak ada baris (bagian 8b butir 2); empty state `No results found` pada hasil Search adalah anchor positif yang sah dan ditulis dalam klausa yang sama dengan Expected TC.
- Visibilitas kolom Modified By dipulihkan di dalam TC-AC-DN-419 dan preferensi kolom dihapus di hook `after`.
- Temuan untuk QA:
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
