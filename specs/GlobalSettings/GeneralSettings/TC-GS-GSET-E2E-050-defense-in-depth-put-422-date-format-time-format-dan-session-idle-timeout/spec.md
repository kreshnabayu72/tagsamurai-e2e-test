---
id: TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout
title: "PUT 422 B"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-138
  - TC-GS-GSET-139
  - TC-GS-GSET-140
  - TC-GS-GSET-141
  - TC-GS-GSET-142
  - TC-GS-GSET-143
coverage:
  web: automated
---

# PUT 422 B

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login UI di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Klien HTTP (disediakan tim FE) yang mengirim request langsung ke server, tanpa melewati browser, untuk `PUT` dan `GET /v2/enterprise-management/general-settings` (`API/openapi.yaml`), memakai token sesi akun Total Control di atas yang diperoleh lewat login API (penangkapan token disediakan tim FE). Request langsung hanya diasersi pada respons server dan state data (bagian 8b butir 1); tampilan UI hanya dipakai untuk membaca jumlah baris log, bukan reaksi atas request.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis dan tidak mengubah state (semua request ditolak). Payload valid: `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30` (sama dengan nilai tersimpan). "Kosong" berarti string kosong `""`; Session Idle Timeout kosong berarti `null` (TC-GS-GSET-142).
- Baseline log (S-12): `{nCL0}` (total entri Modal Changelog) dan `{nAL0}` (total entri Activity Log dengan Search `General Settings`) dicatat pada langkah 1 dan 2, sebelum request pertama.
- Tabel "PUT ditolak" (dipakai langkah 4 sampai 8):

  | Urutan | TC | Field | Nilai | Pesan kesalahan |
  |---|---|---|---|---|
  | 1 | TC-GS-GSET-138 | `dateFormat` | `""` | `Date Format must not be empty` |
  | 2 | TC-GS-GSET-139 | `dateFormat` | `YYYY-MM-DD` | `Invalid date format` |
  | 3 | TC-GS-GSET-140 | `timeFormat` | `""` | `Time Format must not be empty` |
  | 4 | TC-GS-GSET-141 | `timeFormat` | `h:mm a` | `Invalid time format` |
  | 5 | TC-GS-GSET-142 | `sessionIdleTimeout` | `null` | `Session Idle Timeout must not be empty` |
  | 6 | TC-GS-GSET-143 | `sessionIdleTimeout` | `45` | `Invalid session idle timeout value` |
  | 7 | TC-GS-GSET-143 | `sessionIdleTimeout` | `0` | `Invalid session idle timeout value` |
  | 8 | TC-GS-GSET-143 | `sessionIdleTimeout` | `"Never"` | `Invalid session idle timeout value` |

- Kemampuan teknis: (a) membaca jumlah total entri (total data pada Pagination) Modal Changelog dan Activity Log; (b) sesi API Total Control untuk PUT dan GET endpoint di atas.
- Tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### Baseline log

1. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL0}`, lalu tutup modal
2. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter, catat jumlah total entri sebagai `{nAL0}`, lalu buka Global Settings > General Settings

### TC-GS-GSET-138 sampai TC-GS-GSET-143: PUT dengan Date Format, Time Format, atau Session Idle Timeout tidak valid ditolak

3. Untuk setiap baris tabel "PUT ditolak" (urutan 1 sampai 8), lakukan langkah 4 sampai 8 dengan nilai baris itu
4. Kirim PUT `/v2/enterprise-management/general-settings` dengan payload valid kecuali field kolom Field bernilai kolom Nilai
5. Verifikasi respons `422`
6. Verifikasi pesan kesalahan sesuai kolom Pesan kesalahan
7. Kirim GET `/v2/enterprise-management/general-settings`
8. Verifikasi nilai tersimpan tidak berubah (`currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`)
9. Buka Modal Changelog
10. Verifikasi jumlah total entri Changelog sama dengan `{nCL0}` (tidak ada baris log baru dari kedelapan request yang ditolak)
11. Tutup Modal Changelog
12. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
13. Verifikasi jumlah total entri Activity Log sama dengan `{nAL0}` (tidak ada baris log baru dari kedelapan request yang ditolak)
14. Buka Global Settings > General Settings

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-138 sampai TC-GS-GSET-143). Mode: FE+BE. Kelas: defense-in-depth (direct API tampering, prinsip 13 butir a).
- Ukuran: langkah berulang 4 sampai 8 diulang delapan kali (bagian 8b butir 7); ekspansi 2 + 1 + 5 x 8 + 6 = 49 langkah. Blok baseline (langkah 1 dan 2) dan blok baca-log berpola (langkah 9 sampai 14) berjumlah 8 langkah dan tidak dihitung ke batas sekitar 35 langkah; sisanya 41 langkah. Alasan pertahanan: semua blok satu kelas (defense-in-depth), berdiri sendiri (kegagalan satu request tidak membuat request lain kehilangan makna), dan setiap request memakai langkah identik per baris tabel; memisahkannya hanya menggandakan login, hook, dan baseline log.
- Dipisah dari spec 049 karena gabungan langkahnya jauh melewati batas ukuran (49 + 50 = 99 langkah dengan ekspansi; 41 + 37 = 78 langkah setelah blok baseline dan baca-log berpola dikecualikan, batas sekitar 35).
- Tiga nilai TC-GS-GSET-143 (`45`, lalu `0`, lalu `"Never"`) menjadi tiga baris tabel (urutan 6 sampai 8) dengan langkah yang sama dan pesan yang sama sesuai Expected TC.
- Asersi "tidak ada baris log baru" adalah asersi jumlah berbaseline (S-12; prinsip 13 butir g, paragraf akhir), bukan kelas g. Anchor positif adalah jumlah awal yang dicatat pada langkah 1 dan 2. Jumlah dibandingkan sekali setelah kedelapan request (langkah 10 dan 13) terhadap baseline sebelum request pertama, sehingga mencakup tiap request.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, 4, 7, 9, 11, 12, dan 14 (membuka dan menutup surface log serta mengirim request); langkah 7 membaca state data lewat GET (bagian 8b butir 1).
- Dependensi TC-GS-GSET-138 sampai TC-GS-GSET-143 adalah "-" pada TC. Urutan TC dipertahankan.
- Temuan untuk QA:
  - TC-GS-GSET-138, 140, dan 142 menyebut field "kosong"/"null" tanpa bentuk nilai yang pasti untuk Date Format dan Time Format (string kosong atau properti hilang); spec memakai string kosong `""`.
  - TC-GS-GSET-143 menulis satu baris Expected untuk tiga nilai (`45`, `0`, `"Never"`) dengan satu pesan; spec memeriksa pesan yang sama untuk tiap nilai. `API/openapi.yaml` memuat enum numerik `[15, 30, 60, 120, 240, 480]` sehingga `"Never"` (string) bisa saja ditolak dengan pesan tipe data berbeda; urutan `error[]` multi-kesalahan diuji di `tc-general-settings-backend.md`.
