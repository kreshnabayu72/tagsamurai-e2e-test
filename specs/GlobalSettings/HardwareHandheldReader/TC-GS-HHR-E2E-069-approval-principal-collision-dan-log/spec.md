---
id: TC-GS-HHR-E2E-069-approval-principal-collision-dan-log
title: "Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-371
  - TC-GS-HHR-372
  - TC-GS-HHR-385
  - TC-GS-HHR-386
  - TC-GS-HHR-387
  - TC-GS-HHR-388
  - TC-GS-HHR-389
coverage:
  web: automated
---

# Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, Principal memutuskan approval saat sesi Client terbuka; dua tenant pada TC-GS-HHR-386). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `principal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |
| C | Total Control (Client C) | Email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net`; nilai `{namaClient}` tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | | `Spectra.env.GS_CLIENTC_TC_PASSWORD` |

- Nama env var Sesi C baru dan belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Password tidak ditulis di spec atau fixture.
- Login Sesi A dilakukan di hook `before`; Sesi P dan Sesi C dibuka dengan langkah ganti akun eksplisit (langkah 1 dan 2) karena hasilnya diasersi. Hook `after` menutup Sesi P dan Sesi C, lalu mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE): DD-05 (`Chainway C72 - 1`, Long Range, Source Self-Purchased, `Waiting for Approval`, permintaan collision di Admin Console > Approvals untuk `SN-HHR-00105`); kartu `Long Range` `5 of 6`, `1 remaining` pada keadaan awal. Client C: reader `SN-HHR-00301` aktif dan dipakai (Self-Purchased, tenant lain).
- Kemampuan teknis (disediakan tim FE/BE):
  - Konteks browser kedua dan ketiga (Sesi P dan Sesi C).
  - Pemulihan Seed Reader A dan permintaan Approvals DD-05 ke keadaan Tabel Data Uji TC antar blok (fixture BE; DD-05 menjadi Available, terhapus, atau permintaannya dibatalkan oleh tiap blok).
  - Pembacaan jumlah entri System Log akun Principal pada surface Global Settings (TC-GS-HHR-371 butir c tidak menyebut cara mengaksesnya; lihat Temuan untuk QA).
- Baseline: jumlah entri Changelog Handheld Reader Client A, Changelog dan Activity Log Client C, serta Activity Log dan System Log akun Principal dicatat sebelum keputusan Principal tiap blok (S-12).
- State global yang diubah: DD-05 dan stok `SN-HHR-00105` di Admin Console. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi P) dan login sebagai Principal Bambang Hartono
2. Ganti akun: buka konteks browser ketiga (Sesi C) dan login sebagai Total Control Client C

### Blok 1 - Approve collision DD-05: TC-GS-HHR-389, TC-GS-HHR-385, TC-GS-HHR-371, TC-GS-HHR-386

3. Pulihkan Seed Reader A dan permintaan Approvals DD-05
4. Sesi C: buka Global Settings > Hardware > Handheld Reader, catat jumlah entri Changelog dan jumlah entri Activity Log Client C sebagai baseline
5. Sesi C: ketik Search `SN-HHR-00301`, tekan Enter, catat `Status` reader sebagai Status awal
6. Sesi A: muat ulang Handheld Reader, klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, tutup Modal Changelog
7. Sesi P: catat jumlah entri Activity Log dan System Log akun Principal di Admin Console, dan jumlah entri System Log akun Principal di surface Global Settings sebagai baseline
8. Sesi A: biarkan daftar Handheld Reader terbuka tanpa refresh
9. Sesi P: buka Admin Console > Approvals dan klik Approve pada permintaan DD-05 (`SN-HHR-00105`)
10. Tunggu aksi selesai
11. Sesi A: amati daftar yang sedang terbuka tanpa refresh
12. Verifikasi baris DD-05 tetap menampilkan `Status` `Waiting for Approval`
13. Verifikasi daftar tidak berubah tanpa push realtime dan tanpa muat ulang otomatis
14. Sesi A: muat ulang halaman Handheld Reader
15. Verifikasi baris DD-05 `Status` `Available`
16. Verifikasi badge `Status` baris DD-05 bergaya `severity="success"` (identitas `Active` di Admin Console tampil sebagai `Available`)
17. Sesi A: buka Overlay row action DD-05
18. Verifikasi Overlay row action DD-05 memuat `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Delete`
19. Tutup Overlay row action DD-05 dengan `Esc`
20. Verifikasi kartu `Long Range` tetap `5 of 6` dan `1 remaining`
21. Sesi A: klik ikon Changelog
22. Verifikasi jumlah entri Changelog bertambah satu dari baseline
23. Verifikasi entri Changelog baru: `Edit` | `Chainway C72 - 1` | `Status` | `Waiting for Approval` | `Available` | `Principal`
24. Sesi A: tutup Modal Changelog
25. Sesi P: buka Activity Log di Admin Console
26. Verifikasi Activity Log akun Principal memuat entri baru: `Approve Request` | `Handheld Reader` | `Chainway C72 - 1` | `Status` | `Waiting for Approval` | `Available` | `Principal`
27. Sesi P: buka System Log di Admin Console
28. Verifikasi System Log akun Principal di Admin Console memuat entri yang sama dengan Action `Edit`
29. Verifikasi jumlah entri System Log akun Principal di surface Global Settings sama dengan baseline (tidak ada entri di surface Global Settings)
30. Sesi C: muat ulang Handheld Reader, ketik Search `SN-HHR-00301`, tekan Enter
31. Verifikasi reader `SN-HHR-00301` `Status` tetap `Available` sama dengan Status awal (tidak berubah)
32. Sesi C: bersihkan Search dengan klik `(←)` pada kotak Search, klik ikon Changelog
33. Verifikasi sedikitnya satu entri Changelog Client C tampil
34. Verifikasi jumlah entri Changelog Client C sama dengan baseline (tidak ada entri baru dari keputusan ini)
35. Sesi C: tutup Modal Changelog, buka Activity Log Client C
36. Verifikasi jumlah entri Activity Log Client C sama dengan baseline (tidak ada entri baru dari keputusan ini)

### Blok 2 - Reject collision DD-05: TC-GS-HHR-387, TC-GS-HHR-372

37. Pulihkan Seed Reader A dan permintaan Approvals DD-05
38. Sesi A: muat ulang Handheld Reader, klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, tutup Modal Changelog
39. Sesi P: catat jumlah entri Activity Log dan System Log akun Principal di Admin Console sebagai baseline, catat `Status` stok `SN-HHR-00105` di Admin Console sebagai Status awal
40. Sesi P: buka Admin Console > Approvals dan klik Reject pada permintaan DD-05 (`SN-HHR-00105`)
41. Tunggu aksi selesai
42. Sesi A: muat ulang halaman Handheld Reader
43. Verifikasi baris DD-05 tidak ada di tabel (anchor: baris Seed Reader A lain tampil)
44. Verifikasi kartu `Long Range` menjadi `4 of 6` dan `2 remaining`
45. Sesi P: buka Hardware Stock, ketik Search `SN-HHR-00105`, tekan Enter
46. Verifikasi `Status` stok `SN-HHR-00105` di Admin Console sama dengan Status awal (tidak berubah)
47. Verifikasi identitas perangkat `SN-HHR-00105` berstatus `Rejected` dipertahankan di Admin Console untuk jejak audit
48. Verifikasi tidak ada reader berstatus `Rejected` di daftar Handheld Reader Global Settings
49. Sesi A: klik ikon Changelog
50. Verifikasi jumlah entri Changelog bertambah satu dari baseline
51. Verifikasi entri Changelog baru: `Delete` | `Chainway C72 - 1` | `Device Name` | `Chainway C72 - 1` | `—` | `Principal`
52. Sesi A: tutup Modal Changelog
53. Sesi P: buka Activity Log di Admin Console
54. Verifikasi Activity Log akun Principal memuat entri baru: `Reject Request` | `Handheld Reader` | `Chainway C72 - 1` | `Device Name` | `Chainway C72 - 1` | `—` | `Principal`
55. Sesi P: buka System Log di Admin Console
56. Verifikasi System Log akun Principal di Admin Console memuat entri yang sama dengan Action `Delete`
57. Verifikasi jumlah entri System Log akun Principal di surface Global Settings sama dengan baseline (tidak ada entri di surface Global Settings)

### Blok 3 - Cancel Request DD-05 oleh Client: TC-GS-HHR-388

58. Pulihkan Seed Reader A dan permintaan Approvals DD-05
59. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request`
60. Sesi A: klik `[Cancel Request]` pada dialog
61. Tunggu aksi selesai
62. Sesi P: buka Admin Console > Approvals, buka Tab Active Approvals > Hardware Stock, ketik Search `SN-HHR-00105`, tekan Enter
63. Verifikasi permintaan collision untuk `SN-HHR-00105` tidak muncul di Tab Active Approvals > Hardware Stock (empty state `No results found`)
64. Sesi P: klik Tab History, ketik Search `SN-HHR-00105`, tekan Enter
65. Verifikasi Tab History memuat permintaan `SN-HHR-00105` dengan `Decision` `Canceled`
66. Verifikasi `Decided By` permintaan tersebut `—`
67. Sesi P: buka Changelog Hardware Stock
68. Verifikasi Changelog Hardware Stock memuat entri `Device Activation Canceled` dengan Old Value `Waiting for Approval` dan New Value `Canceled`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 5c dan 7b). TC-GS-HHR-371, 372, 385 sampai 389 berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhannya ditulis di Prerequisites.
- Urutan blok: keputusan yang mempertahankan DD-05 (Approve) lebih dulu, lalu yang menghapus DD-05 (Reject, Cancel Request) (prinsip 3 butir 5). TC-GS-HHR-389 diletakkan di awal Blok 1 karena asersinya harus terjadi sebelum refresh; langkah Approve yang sama dipakai bersama TC-GS-HHR-385, TC-GS-HHR-371, dan TC-GS-HHR-386 (satu keputusan, banyak surface), dan ini dicatat di sini sebagai penggabungan.
- Spec melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (multi-konteks dengan Principal sebagai pemutus approval) dan topik yang sama; tiap blok berdiri sendiri karena Seed Reader A dan permintaan Approvals dipulihkan di awal blok (langkah 3, 37, 58), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Bagian pencatatan log di blok 1 dan 2 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom).
- Absence "tidak ada entri di surface Global Settings" (TC-GS-HHR-371 butir c dan TC-GS-HHR-372 butir c) dan "tidak ada entri baru Client C" (TC-GS-HHR-386) ditulis di spec ini dengan baseline jumlah entri (S-12) dan butir P-1 konvensi bagian 3: kondisi berat (keputusan Principal baru saja dibangun di spec yang sama) membuat memindahkannya ke spec absence kehilangan konteks. Penggabungan dengan spec absence (spec 065) tidak dilakukan karena spec itu tidak memuat keputusan Principal.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan, mencatat baseline, muat ulang, menutup Overlay dan Modal Changelog, bersihkan Search, berpindah tab. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi.
- Temuan untuk QA:
  - Email dan nilai `{namaClient}` untuk Total Control Client C tidak tertulis di Pre-setup TC; password memakai env var baru yang belum terdaftar.
  - TC-GS-HHR-371 butir c ("tidak ada entri di surface Global Settings") tidak menyebut surface mana yang dimaksud dan apakah akun Principal dapat membuka System Log pada surface Global Settings; spec memakai jumlah entri sebelum dan sesudah dengan kemampuan baca yang disediakan tim FE.
  - TC-GS-HHR-387 butir c ("Status stok Admin Console tidak berubah") tidak menyebut nilai awal; spec mencatat Status stok sebelum keputusan sebagai baseline.
  - TC-GS-HHR-387 butir d ("identitas perangkat berstatus `Rejected` dipertahankan di Admin Console") tidak menyebut lokasi tampilannya; spec membukanya di Hardware Stock.
  - TC-GS-HHR-385 butir a menyebut badge `severity="success"` tanpa menyebut cara membacanya di UI; spec mengasersi gaya badge hijau/sukses sesuai TC.
  - TC-GS-HHR-388 butir b menyebut Tab History tanpa menyebut menu tempatnya; spec memakai Admin Console > Approvals.
  - TC-GS-HHR-386 precondition d hanya menyebut `SN-HHR-00301` aktif tanpa Device Name; spec mencarinya lewat Search `SN-HHR-00301` (asumsi Search mencakup `Serial Number`, tidak dinyatakan di bagian ini).
