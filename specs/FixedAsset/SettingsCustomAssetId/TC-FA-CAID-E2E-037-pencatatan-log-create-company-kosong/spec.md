---
id: TC-FA-CAID-E2E-037-pencatatan-log-create-company-kosong
title: "Pencatatan Log Create pada Company Kosong: Save Pertama dan Toggle Pertama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-233
  - TC-FA-CAID-234
  - TC-FA-CAID-235
coverage:
  web: automated
---

# Pencatatan Log Create pada Company Kosong: Save Pertama dan Toggle Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `Company Kosong` (Pre-setup No 12). Email akun disediakan tim FE/BE (Pre-setup No 12); password `Spectra.env.FA_KOSONG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: `Company Kosong` tanpa konfigurasi tersimpan dan tanpa aset; log Custom Asset ID tidak dihapus, sehingga asersi log memakai baseline jumlah entri (S-12) (No 12). General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: seed reset `Company Kosong` ke keadaan tanpa konfigurasi dan aset sebelum tiap TC, log tidak dihapus (disediakan tim FE/BE); sesi API aktor (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi `Company Kosong` terbentuk pada tiap TC. Hook `after` mengembalikan Company ke keadaan tanpa konfigurasi dan aset lewat seed reset. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-233: Log Create pada Save pertama

1. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log, dan Activity Log
2. Klik `[Save]` tanpa mengubah nilai apa pun
3. Tunggu aksi selesai: tombol `[Save]` kembali disabled
4. Buka Modal Changelog: Custom Asset ID
5. Verifikasi Changelog bertambah tiga baris Create dibanding baseline
6. Verifikasi baris Action `Create`, Field `Status`, Old Value `—`, New Value `Active`
7. Verifikasi baris Action `Create`, Field `Separator`, Old Value `—`, New Value `Slash`
8. Verifikasi baris Action `Create`, Field `Segments Formula`, Old Value `—`, New Value `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)`
9. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
10. Verifikasi System Log bertambah tiga baris dibanding baseline dengan Field `Status`, `Separator`, dan `Segments Formula` serta nilai Old/New yang sama dengan Changelog
11. Verifikasi ketiga baris System Log memuat Object `Custom Asset ID` dan Name `—`
12. Buka Fixed Asset > Activity Log > tab User Action
13. Verifikasi Activity Log bertambah tiga baris dibanding baseline dengan Field `Status`, `Separator`, dan `Segments Formula` serta nilai Old/New yang sama dengan Changelog
14. Verifikasi ketiga baris Activity Log memuat Object `Custom Asset ID` dan Name `—`
15. Verifikasi ketiga baris Activity Log memuat Modified By `Sarah J`

### TC-FA-CAID-234: Log Create pada Toggle pertama

16. Atur `Company Kosong` ke keadaan tanpa konfigurasi dan aset (seed reset; log tidak dihapus), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
17. Geser Master Switch ke OFF
18. Klik `[Disable]`
19. Tunggu aksi selesai: dialog konfirmasi tertutup dan Master Switch berada pada posisi OFF
20. Buka Modal Changelog: Custom Asset ID
21. Verifikasi Changelog bertambah tiga baris Create dibanding baseline
22. Verifikasi baris Action `Create`, Field `Status`, Old Value `—`, New Value `Inactive`
23. Verifikasi baris Action `Create`, Field `Separator`, Old Value `—`, New Value `Slash`
24. Verifikasi baris Action `Create`, Field `Segments Formula`, Old Value `—`, New Value `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)`
25. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
26. Verifikasi System Log bertambah tiga baris dibanding baseline dengan Field, Old Value, dan New Value yang sama dengan Changelog
27. Verifikasi ketiga baris System Log memuat Object `Custom Asset ID` dan Name `—`
28. Buka Fixed Asset > Activity Log > tab User Action
29. Verifikasi Activity Log bertambah tiga baris dibanding baseline dengan Field, Old Value, dan New Value yang sama dengan Changelog
30. Verifikasi ketiga baris Activity Log memuat Object `Custom Asset ID` dan Name `—`
31. Verifikasi ketiga baris Activity Log memuat Modified By `Sarah J`

### TC-FA-CAID-235: Log Create dengan Initial Company terisi

32. Atur `Company Kosong` ke keadaan tanpa konfigurasi dan aset (seed reset; log tidak dihapus), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
33. Centang `Initial Company` dan ketik `ABC`
34. Klik `[Save]`
35. Tunggu aksi selesai: tombol `[Save]` kembali disabled
36. Buka Modal Changelog: Custom Asset ID
37. Verifikasi Changelog bertambah satu baris dibanding baseline (langkah 32)
38. Verifikasi baris Action `Create`, Field `Segments Formula`, Old Value `—`, New Value `Initial Company (Active: ABC), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)`
39. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
40. Verifikasi System Log bertambah satu baris dibanding baseline (langkah 32)
41. Verifikasi baris Action `Create`, Field `Segments Formula`, Old Value `—`, New Value `Initial Company (Active: ABC), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` yang sama dengan Changelog
42. Buka Fixed Asset > Activity Log > tab User Action
43. Verifikasi Activity Log bertambah satu baris dibanding baseline (langkah 32)
44. Verifikasi baris Action `Create`, Field `Segments Formula`, Old Value `—`, New Value `Initial Company (Active: ABC), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` yang sama dengan Changelog

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 44 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik dan satu kelas harness (pencatatan log Create pada Company Kosong); blok baca-log berpola (buka surface, lalu `Verifikasi` kolom log) tidak dihitung menurut bagian 3 prinsip 13, sehingga langkah di luar blok itu hanya sebelas (langkah 1 sampai 3, 16 sampai 19, dan 32 sampai 35).
- Langkah penghubung: langkah 1, 16, dan 32 (baseline jumlah entri, S-12; langkah 16 dan 32 sekaligus seed reset dan membuka halaman), langkah 3, 19, dan 35 (tunggu aksi selesai sebelum membuka Modal Changelog, bagian 8b butir 8), membuka Modal Changelog, System Log, dan Activity Log.
- Seed reset `Company Kosong` hanya mengembalikan konfigurasi dan aset; log tidak dihapus (audit trail permanen). Asersi jumlah memakai selisih terhadap baseline (S-12), tidak memakai keadaan log kosong. TC-FA-CAID-235 memakai baseline langkah 32 pada langkah 37, 40, dan 43; baris `Segments Formula` ber-New Value `ABC` diasersi sesudah selisih satu baris, karena baris dari run lama tetap ada di log permanen dan tidak boleh meloloskan asersi tanpa Save run ini.
- Pembagian TC lintas spec: TC-FA-CAID-236 sampai 238 ada di spec 038, TC-FA-CAID-239 sampai 242 di spec 039, TC-FA-CAID-243 sampai 245 di spec 040.
- Temuan untuk QA:
  - TC-FA-CAID-233 sampai 235 menyebut pengguna Sarah Johnson (Modified By `Sarah J`) pada `Company Kosong`, sedangkan Pre-setup No 12 hanya menyebut Total Control `Company Kosong` tanpa nama pengguna; identitas dan email akun ditulis "disediakan tim FE/BE".
  - TC-FA-CAID-233 Expected a menyebut "tiga baris Create" di Changelog tanpa urutan baris; spec mengasersi tiap baris per Field.
  - Post Condition TC-FA-CAID-233 sampai 235 tidak diasersi karena TC tidak memberi langkah observasinya.
