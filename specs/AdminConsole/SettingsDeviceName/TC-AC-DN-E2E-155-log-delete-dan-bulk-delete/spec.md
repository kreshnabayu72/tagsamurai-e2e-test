---
id: TC-AC-DN-E2E-155-log-delete-dan-bulk-delete
title: "Pencatatan Delete dan Bulk Delete: Entri Hanya untuk Item yang Terhapus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-496
  - TC-AC-DN-499
  - TC-AC-DN-500
coverage:
  web: automated
---

# Pencatatan Delete dan Bulk Delete: Entri Hanya untuk Item yang Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20; #21 Selection Limit entitas uji bernilai awal 1000 (tidak diubah).
- Data Dinamis (milik spec, dibuat lewat API di hook `before`; D1, D2, B1, B2 terhapus oleh aksi, hook `after` menghapus sisanya):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | D1 | `Cable Tester {runId}-155` | `Unit` | `Accessory` | tanpa SKU, tanpa unit BYO | TC-AC-DN-496 |
  | D2 | `Cable Hapus {runId}-155` | `Unit` | `Accessory` | tanpa SKU, tanpa unit BYO | TC-AC-DN-499 |
  | B1 | `Bulk Alfa {runId}-155` | `Unit` | `Accessory` | tanpa SKU, tanpa unit BYO | TC-AC-DN-500 |
  | B2 | `Bulk Beta {runId}-155` | `Unit` | `Antenna` | tanpa SKU, tanpa unit BYO | TC-AC-DN-500 |
  | B3 | `Bulk Bersku {runId}-155` | `Unit` | `Tag` | memiliki satu SKU (seed) sehingga Delete diblok | TC-AC-DN-500 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah entri Changelog ber-Action `Delete` sebagai baseline Bd0 (kemampuan baca)
2. TC-AC-DN-496: Delete mencatat entri Field Device Name
3. Ketik Search `Cable Tester {runId}-155`, tekan Enter
4. Klik ikon row action `⋯` pada baris `Cable Tester {runId}-155`, lalu klik `Delete`
5. Klik `[Delete]` pada dialog "Delete Device Name"
6. Verifikasi toast sukses "Success, device name has been deleted."
7. Klik ikon Changelog di toolbar
8. Verifikasi popup `Changelog: Device Name` tampil
9. Ketik Search `Cable Tester {runId}-155`, tekan Enter
10. Verifikasi baris Changelog: Action `Delete`, Device Name `Cable Tester {runId}-155`, Field `Device Name`, Old Value `Cable Tester {runId}-155`, New Value `—`, Modified By `Budi S`
11. Klik ikon close `(X)` pada popup Changelog
12. Buka menu `Activity Log`, lalu klik tab `User Action`
13. Verifikasi halaman `Activity Log > User Action` tampil
14. Ketik Search `Cable Tester {runId}-155`, tekan Enter
15. Verifikasi entri Activity Log: Action `Delete`, Object `Device Name`, Name `Cable Tester {runId}-155`, Field `Device Name`, Old Value `Cable Tester {runId}-155`, New Value `—`, Modified By `Budi S`
16. TC-AC-DN-499: Delete menghasilkan tepat satu entri tanpa duplikat
17. Buka halaman `Settings > Device > Device Name`
18. Ketik Search `Cable Hapus {runId}-155`, tekan Enter
19. Klik ikon row action `⋯` pada baris `Cable Hapus {runId}-155`, lalu klik `Delete`
20. Klik `[Delete]` pada dialog "Delete Device Name"
21. Verifikasi toast sukses "Success, device name has been deleted."
22. Klik ikon Changelog di toolbar
23. Verifikasi popup `Changelog: Device Name` tampil
24. Klik ikon Filter, centang `Delete` pada field `Action`, lalu klik `[Apply]`
25. Ketik Search `Cable Hapus {runId}-155`, tekan Enter
26. Verifikasi entri Delete untuk `Cable Hapus {runId}-155` berjumlah tepat 1 baris: Field `Device Name`, Old Value `Cable Hapus {runId}-155`, New Value `—`
27. Klik `(←)` pada kotak Search
28. Verifikasi total entri Action `Delete` menjadi Bd0 + 2 (satu dari TC-AC-DN-496 dan satu dari TC-AC-DN-499)
29. Klik ikon close `(X)` pada popup Changelog
30. TC-AC-DN-500: Bulk Delete mencatat entri hanya untuk item yang terhapus
31. Buka halaman `Settings > Device > Device Name`
32. Ketik Search `{runId}-155`, tekan Enter
33. Centang baris `Bulk Alfa {runId}-155`, `Bulk Beta {runId}-155`, dan `Bulk Bersku {runId}-155`
34. Verifikasi bar Bulk Action tampil dengan 3 terpilih
35. Klik tombol `Bulk Action`, lalu pilih `Delete`
36. Verifikasi dialog "Delete Device Names": kelompok "The following will be deleted:" berisi bullet `Bulk Alfa {runId}-155` dan `Bulk Beta {runId}-155`; kelompok `Skipped: has SKUs` berisi bullet `Bulk Bersku {runId}-155`; tombol `[Cancel]` dan `[Continue]`
37. Klik `[Continue]`
38. Verifikasi toast sukses sebagian "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
39. Klik ikon Changelog di toolbar
40. Verifikasi popup `Changelog: Device Name` tampil
41. Klik ikon Filter, centang `Delete` pada field `Action`, lalu klik `[Apply]`
42. Verifikasi total entri Action `Delete` menjadi Bd0 + 4 (dua baris baru, satu per Device Name yang terhapus, ditambah dua baris dari TC-AC-DN-496 dan TC-AC-DN-499)
43. Ketik Search `Bulk Alfa {runId}-155`, tekan Enter
44. Verifikasi baris baru `Bulk Alfa {runId}-155`: Field `Device Name`, Old Value `Bulk Alfa {runId}-155`, New Value `—`
45. Ganti isi kotak Search dengan `Bulk Beta {runId}-155`, tekan Enter
46. Verifikasi baris baru `Bulk Beta {runId}-155`: Field `Device Name`, Old Value `Bulk Beta {runId}-155`, New Value `—`
47. Klik `(←)` pada kotak Search
48. Verifikasi hanya dua baris Delete yang bertambah pada blok ini (selisih tepat 2), sehingga tidak ada baris Delete untuk `Bulk Bersku {runId}-155` yang di-skip

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): baseline Bd0 dicatat sebelum aksi pertama (S-12); Search menemukan record spec; filter Action `Delete` pada Changelog.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (48 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- P-1: pada TC-AC-DN-500 butir f ('tidak ada baris Delete untuk item yang di-skip') ditulis sebagai asersi jumlah (selisih tepat 2) di spec ini karena state berat Bulk Delete campuran dibangun oleh aksi TC itu sendiri; spec absence 157 sampai 160 tidak memuat aksi Bulk Delete.
- Temuan untuk QA:
  - TC-AC-DN-499 dan 500 memakai total absolut entri Delete (2 dan 3); spec memakai selisih terhadap baseline Bd0 (S-12). Post Condition tanpa langkah observasi tidak diasersi (S-01).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
