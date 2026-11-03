---
id: TC-AC-DN-E2E-138-changelog-reset-halaman-kolom-tersembunyi-dan-opsi-baru
title: "Modal Changelog: Reset Halaman saat Apply, Filter Kolom Tersembunyi, dan Opsi Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-445
  - TC-AC-DN-446
  - TC-AC-DN-447
coverage:
  web: automated
---

# Modal Changelog: Reset Halaman saat Apply, Filter Kolom Tersembunyi, dan Opsi Baru

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

- Data Dinamis (milik spec): Device Name `Dock Station {runId}-138` (Measurement `Unit`, Category `TAG > NFC > Accessory`) dibuat lewat form pada TC-AC-DN-447 dan dihapus di hook `after` lewat API (kemampuan seeding disediakan tim FE/BE); penghapusan menambah entri Delete pada Changelog, sedangkan opsi nama bersuffix unik tetap ada di dropdown karena audit trail permanen.
- Isolasi riwayat seed: TC-AC-DN-446 dibatasi Filter Date `01/09/26` sampai `15/09/26`; TC-AC-DN-445 dan TC-AC-DN-447 tidak mengasersi isi baris seed (S-12, S-14).
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global yang diubah: konfigurasi kolom Changelog (dan kolom List bila disebut) tersimpan per user di browser. Hook `after` spec ini menghapus preferensi kolom di browser (bagian 4), bukan `[Reset to Default]`; kemampuan itu disediakan tim FE.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik ikon Changelog di toolbar List

### TC-AC-DN-445: Apply Filter saat di halaman 2 mengembalikan ke halaman 1

2. Klik tombol halaman 2 pada pagination
3. Klik ikon Filter di toolbar popup
4. Klik field `Action`, centang `Create`, lalu tutup dropdown
5. Klik `[Apply]`
6. Verifikasi hasil Filter (baris Action `Create`) tampil pada halaman 1
7. Verifikasi indikator halaman aktif menunjukkan halaman 1

### TC-AC-DN-446: Filter pada kolom yang disembunyikan tetap tersedia

8. Klik `[Clear Field]`, lalu klik `[Apply]`
9. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
10. Klik field `Modified By`, centang pelaku Maya Putri, lalu tutup dropdown
11. Klik `[Apply]`
12. Klik ikon `⋯` pada header kolom terakhir lalu hilangkan centang kolom Modified By
13. Klik ikon Filter untuk menutup lalu membuka Filter Panel kembali
14. Verifikasi field `Modified By` tetap ada di Filter Panel dengan chip pelaku Maya Putri
15. Verifikasi tabel tetap menampilkan 5 baris hasil Filter
16. Klik ikon `⋯` pada header kolom terakhir lalu centang kembali kolom Modified By

### TC-AC-DN-447: Device Name baru muncul sebagai opsi filter setelah dibuat

17. Klik ikon close `(X)` pada popup
18. Klik `+ Device Name`
19. Ketik `Dock Station {runId}-138` pada field Device Name
20. Pilih `Unit` pada field Measurement
21. Pada field Category, expand `TAG` lalu `NFC`, pilih leaf `Accessory` pada TreeSelect
22. Klik `[Submit]`
23. Verifikasi toast sukses `Success, device name has been created.`
24. Verifikasi popup form tertutup
25. Klik ikon Changelog di toolbar List
26. Klik ikon Filter di toolbar popup
27. Klik field `Device Name`
28. Verifikasi opsi `Dock Station {runId}-138` tampil pada dropdown Device Name tanpa memuat ulang halaman

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Visibilitas kolom Modified By dipulihkan di dalam TC-AC-DN-446; preferensi kolom dihapus di hook `after`. Langkah menutup popup sebelum `+ Device Name` adalah langkah penghubung (S-03).
- TC-AC-DN-445: hasil Filter diasersi sebagai baris Action `Create` pada halaman 1 tanpa pembatas karena yang diuji adalah posisi halaman.
- Temuan untuk QA:
  - TC-AC-DN-447 menciptakan Device Name `Dock Station` tanpa suffix; spec memakai nama bersuffix `{runId}-138` (S-12).
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
