---
id: TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field
title: "Log per field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-104
  - TC-GS-GSET-105
  - TC-GS-GSET-106
  - TC-GS-GSET-107
  - TC-GS-GSET-108
coverage:
  web: automated
---

# Log per field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis; kelima Save mengubah record itu (Currency Code `USD`, Time Zone `UTC`, Date Format `M/d/yy`, Time Format `hh:mm a`, Session Idle Timeout `1 hour`), masing-masing satu field berbeda tanpa pemulihan record di antara blok, sehingga hanya field yang diuji tiap blok dijamin bernilai baseline dan Old Value baris log field itu adalah nilai baseline.
- Label opsi yang dibaca dari dropdown (tidak ditulis literal karena ditentukan programmer, NC-09 dan NC-10): label opsi Currency Code `USD` dicatat sebagai `{labelUSD}` saat opsi dipilih (langkah 3). Label opsi Time Zone mengikuti PRD §4.3a: `Asia/Jakarta` = `(UTC+07:00) Bangkok, Hanoi, Jakarta`; `UTC` = `(UTC+00:00) UTC, Reykjavik, Accra` (alias "Time Zone Lain" pada TC dipetakan ke `UTC`). Label Currency Code `IDR` = `Rp - Indonesian Rupiah`.
- Baseline log (S-12): jumlah total entri Modal Changelog dicatat sebagai `{nCL0}` dan jumlah total entri Activity Log (Search `General Settings`, sehingga hanya entri Object `General Settings`) dicatat sebagai `{nAL0}` pada langkah 1 dan 2, sebelum Save pertama. Kolom Name Activity Log `—`; Modified By `Budi S` (nama aktor singkat).
- Tabel "Save per field" (dipakai langkah 14 sampai 25; Currency Code diuji tersendiri pada langkah 3 sampai 13 karena menampilkan dialog Change Currency):

  | Urutan | TC | Field | Pilihan | Old Value | New Value | Total Changelog | Total Activity Log |
  |---|---|---|---|---|---|---|---|
  | 1 | TC-GS-GSET-105 | `Time Zone` | opsi `(UTC+00:00) UTC, Reykjavik, Accra` | `(UTC+07:00) Bangkok, Hanoi, Jakarta` | `(UTC+00:00) UTC, Reykjavik, Accra` | `{nCL0}` + 2 | `{nAL0}` + 2 |
  | 2 | TC-GS-GSET-106 | `Date Format` | `M/d/yy` | `dd/MM/yy` | `M/d/yy` | `{nCL0}` + 3 | `{nAL0}` + 3 |
  | 3 | TC-GS-GSET-107 | `Time Format` | `hh:mm a` | `HH:mm` | `hh:mm a` | `{nCL0}` + 4 | `{nAL0}` + 4 |
  | 4 | TC-GS-GSET-108 | `Session Idle Timeout` | `1 hour` | `30 minutes` | `1 hour` | `{nCL0}` + 5 | `{nAL0}` + 5 |

- Kemampuan teknis: membaca jumlah total entri (total data pada Pagination) Modal Changelog dan Activity Log; Search Activity Log.
- State global yang diubah: seluruh field record General Settings Client A (lima Save). Pemulihan ke baseline dilakukan hook `beforeEach` dan `after` suite lewat PUT API. Entri Changelog dan Activity Log bersifat audit trail permanen dan tidak dihapus. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### Baseline log

1. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL0}`, lalu tutup modal
2. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter, catat jumlah total entri sebagai `{nAL0}`, lalu buka Global Settings > General Settings

### TC-GS-GSET-104: Save Currency Code tercatat di Changelog dan Activity Log

3. Pilih Currency Code `USD` dan catat teks label opsinya sebagai `{labelUSD}`
4. Klik `[Save]`, lalu klik `[Change Currency]` pada dialog Change Currency
5. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
6. Buka Modal Changelog
7. Verifikasi jumlah total entri Changelog `{nCL0}` + 1 (tepat 1 baris baru, tidak ada baris untuk field yang tidak berubah)
8. Verifikasi baris teratas Changelog: Action `Edit`, Field `Currency Code`, Old Value `Rp - Indonesian Rupiah`, New Value `{labelUSD}`, Modified By `Budi S`
9. Tutup Modal Changelog
10. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
11. Verifikasi jumlah total entri Activity Log `{nAL0}` + 1 (tepat 1 baris baru)
12. Verifikasi baris teratas Activity Log: Action `Edit`, Object `General Settings`, Name `—`, Field `Currency Code`, Old Value `Rp - Indonesian Rupiah`, New Value `{labelUSD}`, Modified By `Budi S`
13. Buka Global Settings > General Settings

### TC-GS-GSET-105, TC-GS-GSET-106, TC-GS-GSET-107, TC-GS-GSET-108: Save Time Zone, Date Format, Time Format, dan Session Idle Timeout tercatat

14. Untuk setiap baris tabel "Save per field" (urutan 1 sampai 4), lakukan langkah 15 sampai 25 dengan nilai kolom baris itu
15. Pilih nilai kolom Pilihan pada Select kolom Field
16. Klik `[Save]`
17. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
18. Buka Modal Changelog
19. Verifikasi jumlah total entri Changelog sama dengan kolom Total Changelog (tepat 1 baris baru, tidak ada baris untuk field yang tidak berubah)
20. Verifikasi baris teratas Changelog: Action `Edit`, Field sesuai kolom Field, Old Value sesuai kolom Old Value, New Value sesuai kolom New Value, Modified By `Budi S`
21. Tutup Modal Changelog
22. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
23. Verifikasi jumlah total entri Activity Log sama dengan kolom Total Activity Log (tepat 1 baris baru)
24. Verifikasi baris teratas Activity Log: Action `Edit`, Object `General Settings`, Name `—`, Field sesuai kolom Field, Old Value sesuai kolom Old Value, New Value sesuai kolom New Value, Modified By `Budi S`
25. Buka Global Settings > General Settings

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-104 sampai TC-GS-GSET-108). Mode: FE+BE. Kelas: pencatatan log (presence) pada layar yang sama dengan fungsi Save; tidak berkelas harness.
- Langkah berulang: langkah 15 sampai 25 diulang empat kali (baris tabel Prerequisites, bagian 8b butir 7). Perkiraan langkah ekspansi 14 + 11 x 4 = 58, dengan 40 di antaranya blok baca-log berpola (langkah 6 sampai 13 dan 18 sampai 25: buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung ke batas sekitar 35 langkah (prinsip 13, bagian smell); sisanya 18 langkah. Kelima blok berdiri sendiri dan satu kelas.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 6, 9, 10, 13, 18, 21, 22, 25 (membuka dan menutup surface log serta kembali ke halaman); langkah 5 dan 17 (tunggu Save selesai sebelum membuka surface lain). Search `General Settings` pada Activity Log membatasi hitungan ke entri Object `General Settings` (hanya kolom Date yang dikecualikan dari Search, NC-16).
- Asersi "tepat 1 baris baru" memakai selisih jumlah total terhadap baseline (S-12), bukan angka absolut; "tidak ada baris untuk field yang tidak berubah" dibuktikan oleh selisih tepat 1 bersama `Verifikasi` Field baris teratas.
- Urutan Save mengikuti TC (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout). Penyimpangan sengaja: tidak ada pemulihan record ke baseline di antara blok. Tiap Save mengubah field yang berbeda dari Save sebelumnya, sehingga hanya field yang diuji tiap blok dijamin bernilai baseline; field lain sudah berubah oleh Save sebelumnya.
- Dipisah dari spec 042 karena gabungan langkahnya melewati batas ukuran (58 + 41 = 99 langkah dengan ekspansi; 41 langkah setelah blok baca-log berpola dikecualikan, di atas batas sekitar 35).
- Dependensi TC (TC-GS-GSET-38, 33, 34, 35, 36) adalah aksi Save yang sama dengan langkah spec ini; langkahnya ditulis utuh (S-04), tanpa rujukan.
- Temuan untuk QA:
  - TC-GS-GSET-104 dan TC-GS-GSET-105 memakai alias `teks label opsi USD` dan `teks label opsi Time Zone Lain` karena label ditentukan programmer (NC-09, NC-10). Spec membaca label USD dari dropdown dan memetakan "Time Zone Lain" ke `UTC` dengan label PRD §4.3a; QA perlu menetapkan opsi yang dimaksud bila bukan `UTC`.
  - Precondition c TC-GS-GSET-105 sampai TC-GS-GSET-108 ("Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`") mensyaratkan seluruh record pada baseline. Precondition itu tidak dapat terpenuhi untuk keempat TC dalam satu spec tanpa pemulihan record di antara blok (sejak TC-GS-GSET-105 Currency Code sudah `USD`, sejak TC-GS-GSET-106 Time Zone juga sudah `UTC`, dan seterusnya); spec hanya menjamin baseline untuk field yang diuji tiap blok.
  - Kolom Modified By Activity Log pada TC ditulis `[nama aktor singkat]`; spec memakai `Budi S` sesuai kolom Modified By pada Tabel Pre-setup.
