---
id: TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone
title: "PUT simbol, no-op, 422 A"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-131
  - TC-GS-GSET-132
  - TC-GS-GSET-133
  - TC-GS-GSET-134
  - TC-GS-GSET-135
  - TC-GS-GSET-136
  - TC-GS-GSET-137
coverage:
  web: automated
---

# PUT simbol, no-op, 422 A

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login UI di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Klien HTTP (disediakan tim FE) yang mengirim request langsung ke server, tanpa melewati browser, untuk `PUT` dan `GET /v2/enterprise-management/general-settings` (`API/openapi.yaml`), memakai token sesi akun Total Control di atas yang diperoleh lewat login API (penangkapan token disediakan tim FE). Request langsung hanya diasersi pada respons server dan state data (bagian 8b butir 1); tampilan UI hanya dipakai untuk membaca state tersimpan dan log, bukan reaksi atas request.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis. Payload valid: `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30` (sama dengan nilai tersimpan). "Kosong" berarti string kosong `""`. Properti `currencySymbol` `XX` dan `placement` `suffix` pada TC-GS-GSET-131 dikirim sebagai properti tambahan di luar skema `PutGeneralSettingsBody`.
- Label simbol: simbol opsi Currency Code `USD` (Pre-setup No 12) dibaca dari label opsi `[Symbol] - [Currency Name]` pada dropdown dan dicatat sebagai `{simbolUSD}` pada langkah 26 (label ditentukan programmer, NC-10).
- Baseline log (S-12): `{nCL0}` (total entri Modal Changelog) dan `{nAL0}` (total entri Activity Log dengan Search `General Settings`) dicatat pada langkah 1 dan 2, sebelum request pertama.
- Tabel "PUT ditolak" (dipakai langkah 12 sampai 16):

  | Urutan | TC | Field | Nilai | Pesan kesalahan |
  |---|---|---|---|---|
  | 1 | TC-GS-GSET-133 | `currencyCode` | `""` | `Currency Code must not be empty` |
  | 2 | TC-GS-GSET-134 | `currencyCode` | `ZZZ` | `Invalid currency code` |
  | 3 | TC-GS-GSET-135 | `timezone` | `""` | `Time Zone must not be empty` |
  | 4 | TC-GS-GSET-136 | `timezone` | `Mars/Olympus` | `Invalid time zone` |
  | 5 | TC-GS-GSET-137 | `timezone` | `Europe/London` | `Invalid time zone` |

- Kemampuan teknis: (a) membaca jumlah total entri (total data pada Pagination) Modal Changelog dan Activity Log; (b) sesi API Total Control untuk PUT dan GET endpoint di atas; (c) memulihkan record Client A ke baseline Pre-setup No 10 lewat PUT yang sama pada langkah 30.
- State global yang diubah: Currency Code record General Settings Client A (TC-GS-GSET-131, `USD`), dipulihkan pada langkah 30 serta hook `beforeEach` dan `after` suite. Request lain tidak mengubah state. Entri log bersifat audit trail permanen dan tidak dihapus. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### Baseline log

1. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL0}`, lalu tutup modal
2. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter, catat jumlah total entri sebagai `{nAL0}`, lalu buka Global Settings > General Settings

### TC-GS-GSET-132: PUT langsung dengan payload identik adalah no-op sukses

3. Kirim PUT `/v2/enterprise-management/general-settings` dengan payload identik dengan nilai tersimpan
4. Verifikasi respons `200`
5. Buka Modal Changelog
6. Verifikasi jumlah total entri Changelog sama dengan `{nCL0}` (0 baris baru)
7. Tutup Modal Changelog
8. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
9. Verifikasi jumlah total entri Activity Log sama dengan `{nAL0}` (0 baris baru)
10. Buka Global Settings > General Settings

### TC-GS-GSET-133, TC-GS-GSET-134, TC-GS-GSET-135, TC-GS-GSET-136, TC-GS-GSET-137: PUT dengan Currency Code atau Time Zone tidak valid ditolak

11. Untuk setiap baris tabel "PUT ditolak" (urutan 1 sampai 5), lakukan langkah 12 sampai 16 dengan nilai baris itu
12. Kirim PUT dengan payload valid kecuali field kolom Field bernilai kolom Nilai
13. Verifikasi respons `422`
14. Verifikasi pesan kesalahan sesuai kolom Pesan kesalahan
15. Kirim GET `/v2/enterprise-management/general-settings`
16. Verifikasi nilai tersimpan tidak berubah (`currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`)
17. Buka Modal Changelog
18. Verifikasi jumlah total entri Changelog sama dengan `{nCL0}` (tidak ada baris log baru dari kelima request yang ditolak)
19. Tutup Modal Changelog
20. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
21. Verifikasi jumlah total entri Activity Log sama dengan `{nAL0}` (tidak ada baris log baru dari kelima request yang ditolak)
22. Buka Global Settings > General Settings

### TC-GS-GSET-131: Nilai simbol dari client diabaikan, simbol di-derive dari Currency Code

23. Kirim PUT dengan `currencyCode` `USD`, `currencySymbol` `XX`, `placement` `suffix`, dan field lain sama dengan nilai tersimpan
24. Verifikasi respons `200`
25. Muat ulang halaman (F5)
26. Buka dropdown Currency Code, catat simbol pada label opsi `USD` sebagai `{simbolUSD}`, lalu tutup dropdown tanpa mengubah pilihan
27. Verifikasi Preview Currency menampilkan `{simbolUSD} 5.000,00` (simbol dari `USD`, penempatan tidak berubah)
28. Verifikasi Preview Currency tidak memuat `XX`
29. Verifikasi Select Currency Code menampilkan opsi `USD` (Currency Code `USD` tersimpan)
30. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API, lalu muat ulang halaman (F5)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-131 sampai TC-GS-GSET-137). Mode: FE+BE. Kelas: defense-in-depth (direct API tampering, prinsip 13 butir a).
- Ukuran: langkah berulang 12 sampai 16 diulang lima kali (bagian 8b butir 7); ekspansi 30 + 4 x 5 = 50 langkah nominal. Blok baca-log berpola (langkah 5 sampai 9 dan 17 sampai 22) berjumlah 11 langkah dan blok baseline langkah 1 dan 2 tidak dihitung ke batas sekitar 35 langkah; sisanya 37 langkah, sedikit di atas batas. Alasan pertahanan: semua blok satu kelas (defense-in-depth), berdiri sendiri (kegagalan satu request tidak membuat request lain kehilangan makna), dan lima request ditolak memakai langkah identik per baris tabel sehingga memisahkannya hanya menggandakan login, hook, dan baseline log.
- Dipisah dari spec 050 karena gabungan langkahnya jauh melewati batas ukuran (50 + 49 = 99 langkah dengan ekspansi; 37 + 41 = 78 langkah setelah blok baseline dan baca-log berpola dikecualikan, batas sekitar 35).
- Urutan berbeda dari TC (TC-GS-GSET-131, 132, lalu 133 sampai 137): TC-GS-GSET-132 dan TC-GS-GSET-133 sampai 137 tidak mengubah state dan dijalankan lebih dulu, TC-GS-GSET-131 (satu-satunya yang menyimpan nilai) paling akhir (prinsip 3 butir 3; aksi yang mengubah state di akhir). Precondition baseline Pre-setup No 10 tetap terpenuhi pada tiap TC.
- Asersi "tidak ada baris log baru" (TC-GS-GSET-132 dan TC-GS-GSET-133 sampai 137) adalah asersi jumlah berbaseline (S-12; prinsip 13 butir g, paragraf akhir), bukan kelas g; anchor positif adalah jumlah awal yang dicatat pada langkah 1 dan 2 serta respons yang dikirim pada langkah 3 dan 12. Untuk lima request yang ditolak, jumlah dibandingkan sekali setelah kelima request (langkah 18 dan 21) terhadap baseline sebelum request pertama, sehingga mencakup tiap request.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, 5, 7, 8, 10, 12, 15, 17, 19, 20, 22, 23, 25, 26, dan 30 (membuka dan menutup surface log, mengirim request, dan memulihkan baseline); langkah 26 hanya membaca label opsi tanpa mengubah pilihan.
- Langkah 24 adalah `Verifikasi` tambahan di luar Expected TC (anchor bahwa request TC-GS-GSET-131 diterima dengan properti tambahan diabaikan, `API/openapi.yaml` deskripsi `currencySymbol`).
- Dependensi TC-GS-GSET-131 sampai TC-GS-GSET-137 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-131 menyebut properti `placement` `suffix`, yang tidak ada di `PutGeneralSettingsBody` pada `API/openapi.yaml` (hanya `currencyCode`, `timezone`, `dateFormat`, `timeFormat`, `sessionIdleTimeout`). Spec mengirimnya sebagai properti tambahan sesuai TC; penempatan simbol di Preview tidak punya padanan field di API.
  - TC-GS-GSET-133 sampai TC-GS-GSET-137 menyebut field kosong tanpa bentuk nilainya (string kosong, null, atau properti hilang); spec memakai string kosong `""`, kecuali Session Idle Timeout pada spec 050 yang memakai `null` sesuai TC-GS-GSET-142.
  - TC-GS-GSET-137 mengandalkan keputusan NC-05 (hanya opsi kurasi diterima server); `API/low-level-design.md` menyebut semua IANA valid, sehingga hasil `422` untuk `Europe/London` bergantung pada implementasi mengikuti PRD.
